#Create database realtor_db if it does not exist
Create Database IF NOT EXISTS realtor_db;

CREATE TABLE IF NOT EXISTS realtor_db.zillow_listing (
   id varchar(25),
   median_price varchar(50),
   lat varchar(25),
   lng varchar(25),
   city varchar(100),
   url varchar(255),
   state_cd varchar(10) 
);

DELETE FROM realtor_db.zillow_listing; 

CREATE OR REPLACE VIEW realtor_db.LISTINGS_INFO
AS
(
SELECT 

id as ID,
median_price AS MEDIAN_PRICE,
lat AS LAT,
lng AS LNG,
city AS TOWN,
url AS URL,
state_cd AS STATE

FROM realtor_db.zillow_listing
);
