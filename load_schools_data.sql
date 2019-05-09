# Create schools table if it does exist.
CREATE TABLE IF NOT EXISTS SCHOOLS (
  SCHOOL_ID INT NOT NULL AUTO_INCREMENT,
  SCHOOL_NAME text,
  SCHOOL_TYPE text,
  TOWN text,
  STATE text,
  SCHOOL_DISTRICT text,
  OVERALL_GRADE text,
  SCHOOL_RANKING bigint(21) unsigned DEFAULT NULL,
  SCHOOL_BADGE text,
  CATEGORY text,
  SCHOOL_GROUP text,
  SCHOOL_POPULATION text,
  STUDENT_TEACHER_RATIO text,
  SCHOOL_URL text,
  AUDIT_DATE datetime,
  PRIMARY KEY ( SCHOOL_ID ) 
) ENGINE=InnoDB DEFAULT CHARSET=latin1
;

CREATE TABLE IF NOT EXISTS `school_category` (
  `CATEGORY_CD` char(1) NOT NULL,
  `CATEGORY_DESCRIPTION` text,
  PRIMARY KEY (`CATEGORY_CD`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

#CREATE THE VIEW ON SCHOOL JOIN ON CATEGORY TO BRING IN DESCRIPTION
CREATE OR REPLACE VIEW SCHOOL_INFO
AS
(
SELECT 

SCHOOL_ID,
SCHOOL_NAME,
SCHOOL_TYPE,
TOWN,
STATE,
SCHOOL_DISTRICT,
OVERALL_GRADE,
SCHOOL_RANKING,
SCHOOL_CATEGORY.CATEGORY_DESCRIPTION,
SCHOOL_GROUP,
SCHOOL_POPULATION,
STUDENT_TEACHER_RATIO,
SCHOOL_URL,
AUDIT_DATE

FROM SCHOOLS

INNER JOIN SCHOOL_CATEGORY
ON SCHOOLS.CATEGORY = SCHOOL_CATEGORY.CATEGORY_CD
)
;

#Insert lookup values for category table. The sql can be run multiple times and would load only first time.
INSERT INTO school_category 
select 
'E' CATEGORY_CD, 
'ELEMENTARY'  CATEGORY_DESCRIPTION
WHERE 'E' NOT IN 
( select category_cd from school_category WHERE CATEGORY_CD = 'E' ) 
;

INSERT INTO school_category 
select 
'M' AS CATEGORY_CD, 
'MIDDLE' AS CATEGORY_DESCRIPTION
WHERE 'M' NOT IN 
( select category_cd from school_category ) 
;

INSERT INTO school_category 
select 
'H' AS CATEGORY_CD,
'HIGH' AS CATEGORY_DESCRIPTION
WHERE 'H' NOT IN 
( select category_cd from school_category ) 
;

# Cleanup bad data where school name is not found.
DELETE FROM SCHOOLS_STG
WHERE SCHOOL_NAME IS NULL
;

# Insert new records from Stage to Target, Insert only New records based on 4 key columns.
INSERT INTO SCHOOLS
(
SCHOOL_NAME,
SCHOOL_TYPE,
TOWN,
STATE,
SCHOOL_DISTRICT,
OVERALL_GRADE,
SCHOOL_RANKING,
SCHOOL_BADGE,
CATEGORY,
SCHOOL_GROUP,
SCHOOL_POPULATION,
STUDENT_TEACHER_RATIO,
SCHOOL_URL,
AUDIT_DATE
)

SELECT   
   
(TRIM(school_name))  AS SCHOOL_NAME,     
UPPER(TRIM(school_type)) AS SCHOOL_TYPE,     
UPPER(TRIM(school_town)) AS TOWN,     
UPPER(TRIM(school_state)) AS STATE,     
UPPER(school_district) AS SCHOOL_DISTRICT,     
TRIM(REPLACE (school_grade, 'Overall Niche Grade', '' )) AS OVERALL_GRADE,     
cast(  (TRIM(coalesce(school_ranking , 0 ) ))  as unsigned ) AS SCHOOL_RANKING,     
UPPER(TRIM(school_badge) ) AS SCHOOL_BADGE,     
TRIM(school_cat) AS CATEGORY, 
TRIM(school_grp) AS SCHOOL_GROUP,     
TRIM(REPLACE ( school_pop , 'Students' , '' )) AS SCHOOL_POPULATION,     
TRIM(REPLACE( school_ratio , 'Student-Teacher Ratio', '')) AS STUDENT_TEACHER_RATIO,     
TRIM(school_url) AS SCHOOL_URL ,
now()       

FROM schools_stg  STG 

WHERE NOT EXISTS
   ( SELECT 1 
     FROM SCHOOLS TGT 
     WHERE TGT.SCHOOL_NAME = TRIM(STG.SCHOOL_NAME)
     AND TGT.TOWN = TRIM(STG.SCHOOL_TOWN)
     AND TGT.STATE = TRIM(STG.SCHOOL_STATE)
     AND TGT.CATEGORY = TRIM(STG.SCHOOL_CAT)
    ) 
;	

# Update only changes - the records are matched based on 4 key columns.
UPDATE SCHOOLS tgt , 
       SCHOOLS_STG stg

SET tgt.SCHOOL_RANKING    = cast(  (TRIM(coalesce(STG.school_ranking , 0 ) ))  as unsigned ),
    tgt.SCHOOL_POPULATION = TRIM(REPLACE ( STG.school_pop , 'Students' , '' )),	
    tgt.STUDENT_TEACHER_RATIO = TRIM(REPLACE( STG.school_ratio , 'Student-Teacher Ratio', '')),
    tgt.SCHOOL_URL = TRIM(STG.SCHOOL_URL),
	tgt.AUDIT_DATE = now()
    
WHERE   UPPER(TRIM(TGT.SCHOOL_NAME)) = UPPER(TRIM(STG.SCHOOL_NAME))
  AND UPPER(TRIM(TGT.TOWN))  = UPPER(TRIM(STG.SCHOOL_TOWN))
  AND UPPER(TRIM(TGT.STATE)) = UPPER(TRIM(STG.SCHOOL_STATE))
  AND UPPER(TRIM(TGT.CATEGORY )) = UPPER(TRIM(STG.SCHOOL_CAT))
  AND 
         (
            tgt.SCHOOL_RANKING    <> cast(  (TRIM(coalesce(STG.school_ranking , 0 ) ))  as unsigned )
         OR tgt.SCHOOL_POPULATION <> TRIM(REPLACE ( STG.school_pop , 'Students' , '' ))	
         OR tgt.STUDENT_TEACHER_RATIO <> TRIM(REPLACE( STG.school_ratio , 'Student-Teacher Ratio', ''))
         OR tgt.SCHOOL_URL <> TRIM(STG.SCHOOL_URL)
         )
;



 

