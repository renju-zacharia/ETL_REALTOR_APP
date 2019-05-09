{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Rutgers 2019 Data Engineering and Visualization ETL Project \n",
    "\n",
    "## Quick Summary \n",
    "\n",
    "We provide an ETL pipeline that enables parents or realtors helping parents with school age children, who are looking to identify good public-school districts and are sensitive to high home prices. This ETL pipeline allows for analysis of median home prices and school ranking and come up with an optimal township / city school based on a predefined median house price combination. Based on the median house price range, a list of highest ranked schools, are provided across NJ."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Steps to run the pipeline: \n",
    "\n",
    "First, ensure the following are in place at the same level as ‘Niche_Scraper.py’\n",
    "\t‘Resources’  directory \n",
    "\t‘states.csv’ within the ‘Resources’ Directory \n",
    "\tCreate_DB.sql is in the same directory ‘Niche_Scraper.py’\n",
    "\t‘load_schools_data.sql’ in the same directory as ‘Niche_Scraper.py’\n",
    "\t‘chromedriver.exe’ in the same directory as ‘Niche_Scraper.py’\n",
    "\t\n",
    "\t\n",
    "Install all the required pip installs / python libraries using ‘requirements.txt’ \n",
    "\n",
    "\t\n",
    "\n",
    "Then proceed through following steps\n",
    "\n",
    "1. In the terminal,  export MYSQL_PWD=\"TYPE YOUR PASSWORD HERE\";\n",
    "\n",
    "2.  Run the following python scripts in sequence \n",
    "\n",
    "o\tpython zillow_all_states.py\n",
    "\n",
    "o\tpython Niche_Scraper.py\n",
    "\n",
    "3. Final sql to find top ranked High Schools with Listings for Median Household prices between $300,000  and  $500,000.\n",
    "\n",
    "1.\tOpen MYSQL Workbench, and run the following SQL \n",
    "\n",
    "\n",
    "SELECT LISTING.*, SCHOOL.*\n",
    "FROM REALTOR_DB.ZILLOW_LISTING LISTING\n",
    "INNER JOIN REALTOR_DB.SCHOOL_INFO  SCHOOL\n",
    "ON SCHOOL.TOWN = LISTING.CITY\n",
    "AND LISTING.STATE_CD = 'NJ'\n",
    "AND CATEGORY_DESCRIPTION = 'HIGH'\n",
    "AND MEDIAN_PRICE > 299999\n",
    "AND MEDIAN_PRICE < 500001\n",
    "ORDER BY SCHOOL_RANKING;\n",
    "\n",
    "\n",
    "4. Make sure templates directory has \n",
    "\tindex.html and \n",
    "\tcss.style.\n",
    "\n",
    "  Make sure \n",
    "o\tGet_Details.py and \n",
    "o\tapp.py are both in same level as templates \n",
    "o\tKick off app.py \n",
    "\n",
    "\tby running below -\n",
    "\n",
    "•\tpython app.py\n",
    "\n",
    "5. Go to chrome and visit http://127.0.0.1:5000/\n",
    "        \n",
    "  Type in your favorite NJ town to find the schools and listings.\n",
    "     ex: SUMMIT, UNION, MILLBURN, EDISON\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Narrative / Motivation\n",
    "\n",
    "Important considerations for families with school age children, when purchasing a house especially when they relocate, is the affordability of the house and the quality of education in the school districts. Even though good information exits online, about school districts and their ranking, rarely is this information along with available housing easily available across the state in a standardized and consistent manner to do comparative analysis.\n",
    "\n",
    "We are helping parents or Realtors (serving parents) to help make decisions to find suitable city/town/district to settle by identifying a list of top ranked public schools at the Elementary/ Middle, High School level, based on their housing affordability.\n",
    "\n",
    "Our Use Case is to help parents with school age children, who are looking to relocate their homes into areas where they can get the best schools, with suitable housing costs."
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Final Schema / Data Model \n",
    "\n",
    "<img src=\"Images/Data_Model.png\">\n",
    "\n",
    "\n",
    "Data Model looks at two tables listing_info and school_info. A join at the 'TOWN' AND 'STATE' allows for building a relationship between the housing and school and related information. \n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "\n",
    "\n",
    "## Data Sources\n",
    "\n",
    "Two data sources were extracted. \n",
    "\n",
    "1.\tNiche.com - School ranking information from ‘Niche.com’ was scraped along with location (city, district…) and  other related information using Niche_Scraper.py.\n",
    "\tThis script will create 2 csv files – \t\n",
    "o\tniche_school_info_all.csv & \n",
    "o\tniche_school_info_all_nj.csv \t into Resources folder.\n",
    "\n",
    "2.\tZillow.com – Housing information was extracted to identify available homes for sale  at the city  level. \n",
    "\n",
    "The above data sets reflect the best of content available in the marketplace for identifying the ranking of public schools at a state level (Niche.com) and Zillow.com provides the best and most comprehensive and up to date data of available homes for sales at an aggregated level,   and hence were sourced.\n",
    "\n",
    "Assumptions:\n",
    "•\tParents with school age children have a fairly good idea about the homes prices (range) they are able to afford.\n",
    "•\tParents with school age children are looking for either a ‘Public’ elementary or middle or high school\n",
    "•\tAll other factors, size of homes, age of homes, other factors – distance to work (if applicable) are all assumed to not have as significant impact as the first two (home price and school ranking)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Transformation Step\n",
    "\n",
    "Raw data was scraped from the Niche.com and was transformed significantly, which involved below steps - \n",
    "\n",
    "1. Cleansing using Python \n",
    "\n",
    "Grouped the education level of schools across three categories - E = Elementary, M = Middle School and H = High School.\n",
    "Filtered out  all ‘Private School’s’ and ‘online’ schools from the data set.\n",
    "Removed removed for other states and retained only NJ\n",
    "For records that did not have District and State available, it was derived by parsing the url.\n",
    "\n",
    "2. Cleansing Using SQL\n",
    "\n",
    "Grading was standardized – we removed the ‘Overall Niche’ Grade \n",
    "e.g.  Before - A Overall Niche Grade\n",
    "      After  - A \n",
    "\n",
    "Removed ‘Students’ from the ‘Overall Number of student fields’\n",
    "e.g. Before - 500 overall number of students\n",
    "     After  - 500\n",
    "\n",
    "3. Add a new column - Rank which was based on the order in which schools are listed. \n",
    "The rank was reset to 1 for each school type ( Elementary / Middle / High )\n",
    "\n",
    "Using a Join to match Schools to Median Housing Price Information.\n",
    "Assigned Rank based on the sequence of listing.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# BONUS - To be updated \n",
    "\n",
    "## APP Development \n",
    "\n",
    "A web application was created to allow for searches using available home median home price range and category of schools (Elementary, Middle and/or High School). The report lists out the best ranked schcools/districts meeting the requirements.\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Team: \t\n",
    "Mark Reilly, Renju Zacharia, Sanjeev Mankar, Abdul Razak"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
