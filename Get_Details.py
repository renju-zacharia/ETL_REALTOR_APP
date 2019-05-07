from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
import pandas as pd
import requests
from sqlalchemy import create_engine
import os
import pymysql
pymysql.install_as_MySQLdb()

def extract_data(town):

    pwd = os.environ['MYSQL_PWD']

    rds_connection_string = f"root:{pwd}@127.0.0.1/realtor_db"
    engine = create_engine(f'mysql://{rds_connection_string}') 
    TOWN = town
    elem_df = pd.read_sql_query('SELECT CATEGORY, SCHOOL_RANKING, SCHOOL_NAME ,OVERALL_GRADE,STUDENT_TEACHER_RATIO,SCHOOL_URL FROM REALTOR_DB.SCHOOLS WHERE TOWN = ' + '"' + TOWN + '"' + 'AND CATEGORY = ' + '"E"' + 'ORDER BY SCHOOL_RANKING LIMIT 1' , con=engine).head()
    middle_df = pd.read_sql_query('SELECT CATEGORY, SCHOOL_RANKING, SCHOOL_NAME ,OVERALL_GRADE,STUDENT_TEACHER_RATIO,SCHOOL_URL FROM REALTOR_DB.SCHOOLS WHERE TOWN = ' + '"' + TOWN + '"' + 'AND CATEGORY = ' + '"M"' + 'ORDER BY SCHOOL_RANKING LIMIT 1' , con=engine).head()
    high_df = pd.read_sql_query('SELECT CATEGORY, SCHOOL_RANKING, SCHOOL_NAME ,OVERALL_GRADE,STUDENT_TEACHER_RATIO,SCHOOL_URL FROM REALTOR_DB.SCHOOLS WHERE TOWN = ' + '"' + TOWN + '"' + 'AND CATEGORY = ' + '"H"' + 'ORDER BY SCHOOL_RANKING LIMIT 1' , con=engine).head()
    response_list = []

    listing_df = pd.read_sql_query('SELECT LAT, LNG, MEDIAN_PRICE, URL FROM REALTOR_DB.ZILLOW_LISTING WHERE CITY = ' + '"' + TOWN + '"' + 'AND STATE_CD = ' + '"NJ"' + 'ORDER BY MEDIAN_PRICE DESC LIMIT 5' , con=engine)
    listing_list = []    

    for index, row in listing_df.iterrows():
        listing_dict={}
        if (str(row['MEDIAN_PRICE']) != 'nan'):
            try:                
                listing_dict['LAT'] = 'LATITUDE : ' + str(row['LAT'])
                listing_dict['LNG'] = 'LONGITUDE : ' + str(row['LNG'])
                listing_dict['MEDIAN_PRICE'] = 'MEDIAN PRICE : ' + str(row['MEDIAN_PRICE'])
                listing_dict['LISTING_URL'] = str(row['URL'])                
                listing_list.append(listing_dict)
            except:    
                print("Error ")
 
    for index, row in elem_df.iterrows():
        elem_dict={}
        if (str(row['SCHOOL_NAME']) != 'nan'):
            try:                
                elem_dict['SCHOOL_RANKING'] = 'ELEMENTARY SCHOOL RANKING : ' + str(row['SCHOOL_RANKING'])
                elem_dict['SCHOOL_NAME'] = 'ELEMENTARY SCHOOL NAME : ' + str(row['SCHOOL_NAME'])
                elem_dict['SCHOOL_GRADE'] = 'ELEMENTARY SCHOOL OVERALL GRADE : ' + str(row['OVERALL_GRADE'])
                elem_dict['SCHOOL_RATIO'] = 'ELEMENTARY SCHOOL STUDENT TEACHER RATIO : ' + str(row['STUDENT_TEACHER_RATIO'])
                elem_dict['SCHOOL_URL'] = str(row['SCHOOL_URL'])
                response_list.append(elem_dict)
            except:    
                print("Error ")

    for index, row in middle_df.iterrows():
        middle_dict = {}
        if (str(row['SCHOOL_NAME']) != 'nan'):
            try:
                middle_dict['SCHOOL_RANKING'] = 'MIDDLE SCHOOL RANKING : ' + str(row['SCHOOL_RANKING'])
                middle_dict['SCHOOL_NAME'] = 'MIDDLE SCHOOL_NAME : ' + str(row['SCHOOL_NAME'])
                middle_dict['SCHOOL_GRADE'] = 'MIDDLE SCHOOL OVERALL GRADE : ' + str(row['SCHOOL_NAME'])
                middle_dict['SCHOOL_RATIO'] = 'MIDDLE SCHOOL STUDENT TEACHER RATIO : ' + str(row['SCHOOL_NAME'])
                middle_dict['SCHOOL_URL'] = str(row['SCHOOL_URL'])
                response_list.append(middle_dict)
            except:    
                print("Error ")      

    for index, row in high_df.iterrows():
        high_dict = {}
        if (str(row['SCHOOL_NAME']) != 'nan'):
            try:
                high_dict['SCHOOL_RANKING'] = 'HIGH SCHOOL RANKING : ' + str(row['SCHOOL_RANKING'])
                high_dict['SCHOOL_NAME'] = 'HIGH SCHOOL NAME : ' + str(row['SCHOOL_NAME'])
                high_dict['SCHOOL_GRADE'] = 'HIGH SCHOOL OVERALL GRADE : ' + str(row['SCHOOL_NAME'])
                high_dict['SCHOOL_RATIO'] = 'HIGH SCHOOL STUDENT TEACHER RATIO : ' + str(row['SCHOOL_NAME'])
                high_dict['SCHOOL_URL'] = str(row['SCHOOL_URL'])

                response_list.append(high_dict)
            except:    
                print("Error ")   

    return(response_list, listing_list)

if __name__ == "__main__":

    extract_data(town)
   





