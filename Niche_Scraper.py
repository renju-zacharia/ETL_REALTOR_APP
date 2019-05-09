from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
import pandas as pd
import requests
from sqlalchemy import create_engine
import os
import pymysql
pymysql.install_as_MySQLdb()

def scrape():

    executable_path = {"executable_path": "chromedriver"}
    browser = Browser("chrome", **executable_path, headless=True)

    base_url_h = "https://www.niche.com/k12/search/best-public-high-schools/s/new-jersey/?page="
    base_url_m = "https://www.niche.com/k12/search/best-public-middle-schools/s/new-jersey/?page="
    base_url_e = "https://www.niche.com/k12/search/best-public-elementary-schools/s/new-jersey/?page="

    types = [ 
              {"school_cat": "E", "base_url":base_url_e, "num_pages":64},
              {"school_cat": "M", "base_url":base_url_m, "num_pages":31},
              {"school_cat": "H", "base_url":base_url_h, "num_pages":20}
            ]

    school_info = []

    for x in types:    
    
        school_ranking = 1

        for page_num in range(1,x['num_pages']):   
            url = x['base_url']+str(page_num)
            browser.visit(url)
            time.sleep(1)
            html = browser.html
            soup = bs(html, "html.parser") 
        
            all_search_results = soup.find_all(class_="search-results__list__item")

            for search_results in all_search_results:
            
                school_dict = {}
        
                try:
                
                    school_dict['school_cat'] = x['school_cat']
                        
                    school_url = search_results.find(class_="search-result__link")['href']
                    school_dict['school_url'] = school_url
                    
                    school_dict['school_town'] = school_url.split('/')[-2].split('school-')[1].replace("-nj","")
                    
                    school_info.append(school_dict)
                
                    school_name = search_results.find(class_="search-result__title").text
                    school_dict['school_name'] = school_name
                
                    taglines = search_results.find_all(class_="search-result-tagline__item")
                
                    if len(taglines) == 3:
                        school_district  = taglines[0].text.split(',')[0]
                        school_state = taglines[0].text.split(',')[1]
                        school_grp   = taglines[1].text
                    elif len(taglines) == 4:
                        school_type  = taglines[0].text  
                        school_district  = taglines[1].text.split(',')[0]
                        school_state = taglines[1].text.split(',')[1]
                        school_grp   = taglines[2].text
                    elif len(taglines) == 2:
                        school_district  = taglines[0].text.split(',')[0]
                        school_state = taglines[0].text.split(',')[1]
                        school_grp   = taglines[1].text    
                    
                    school_dict['school_type']  = school_type
                    school_dict['school_district']  = school_district
                    school_dict['school_state'] = school_state
                    school_dict['school_grp']   = school_grp
                
                    factlists = search_results.find_all(class_="search-result-fact-list__item")

                    school_grade = factlists[0].text
                    school_pop = factlists[1].text
                    school_ratio = factlists[2].text

                    school_dict['school_grade'] = school_grade
                    school_dict['school_pop'] = school_pop
                    school_dict['school_ratio'] = school_ratio
                
                    school_dict['school_ranking'] = school_ranking
                
                    school_ranking = school_ranking + 1
                
                    school_badge = search_results.find(class_="search-result-badge").text
                    school_dict['school_badge'] = school_badge

                except:
                    temp = 0
                
                school_info.append(school_dict)  

    return (school_info)       
    
def cleanse_write_csv(school_info):
    
    my_df = pd.DataFrame(school_info).drop_duplicates()

    for index, row in my_df.iterrows():
        if (str(row['school_town']) == 'nan'):
            try:
                my_df.loc[my_df['school_url'] == row['school_url'] ,'school_state' ] = str(row['school_url']).split('/')[-2].split('-')[-1]
                my_df.loc[my_df['school_url'] == row['school_url'] ,'school_district' ] = str(row['school_url']).split('/')[-2].split('-')[-1]
            except:
                print("Error ")

    public_df = my_df.loc[ ( my_df['school_type'].str.strip() != 'Private School' ) &  ( my_df['school_type'].str.strip() != 'Online School' ) ]
    nj_df = public_df.loc[ ( public_df['school_state'].str.strip() == 'NJ' ) | ( public_df['school_state'].str.strip() == 'nj' )]

    public_df.to_csv('Resources/niche_school_info_all.csv')
    nj_df.to_csv('Resources/niche_school_info_all_nj.csv')

    return(nj_df)

def read_csv():
    nj_read_df = pd.read_csv('Resources/niche_school_info_all_nj.csv')

    nj_clean_df = nj_read_df.loc[ :,  ['school_badge', 'school_cat', 'school_district',
        'school_grade', 'school_grp', 'school_name', 'school_pop',
        'school_ranking', 'school_ratio', 'school_state', 'school_town',
        'school_type', 'school_url'] ]

    return (nj_clean_df)

def load_file(nj_clean_df):
    
    pwd = os.environ['MYSQL_PWD']

    #os.system('mysql -u root < ./Create_DB.sql')
    
    rds_connection_string = f"root:{pwd}@127.0.0.1/realtor_db"
    engine = create_engine(f'mysql://{rds_connection_string}')

    nj_clean_df.to_sql(name='schools_stg', con=engine, if_exists='replace', index=False)

def load_final():
    os.system('mysql -u root -D realtor_db < ./load_schools_data.sql')
    
if __name__ == "__main__":

    try:
        os.system('mkdir Resources')
    except:
        print("Resources folder exists..proceeding")

    school_info = scrape()

    nj_df = cleanse_write_csv(school_info)

    nj_clean_df = read_csv()

    load_file(nj_clean_df)

    load_final()
   





