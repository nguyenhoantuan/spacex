-- Slide 24
SELECT DISTINCT Launch_Site FROM SPACEXTABLE ORDER BY Launch_Site;

-- Slide 25
SELECT Date,Booster_Version,Launch_Site,PAYLOAD_MASS__KG_ FROM SPACEXTABLE WHERE Launch_Site LIKE 'CCA%' ORDER BY Date LIMIT 5;

-- Slide 26
SELECT SUM(PAYLOAD_MASS__KG_) AS NASA_payload_kg FROM SPACEXTABLE WHERE Customer LIKE '%NASA%';

-- Slide 27
SELECT AVG(PAYLOAD_MASS__KG_) AS mean_payload_kg FROM SPACEXTABLE WHERE Booster_Version LIKE 'F9 v1.1%';

-- Slide 28
SELECT MIN(Date) AS first_ground_landing FROM SPACEXTABLE WHERE Landing_Outcome='Success (ground pad)';

-- Slide 29
SELECT DISTINCT Booster_Version FROM SPACEXTABLE WHERE Landing_Outcome='Success (drone ship)' AND PAYLOAD_MASS__KG_>4000 AND PAYLOAD_MASS__KG_<6000;

-- Slide 30
SELECT Mission_Outcome,COUNT(*) AS count FROM SPACEXTABLE GROUP BY Mission_Outcome ORDER BY count DESC;

-- Slide 31
SELECT Booster_Version,PAYLOAD_MASS__KG_ FROM SPACEXTABLE WHERE PAYLOAD_MASS__KG_=(SELECT MAX(PAYLOAD_MASS__KG_) FROM SPACEXTABLE);

-- Slide 32
SELECT Date,Booster_Version,Launch_Site,Landing_Outcome FROM SPACEXTABLE WHERE strftime('%Y',Date)='2015' AND Landing_Outcome='Failure (drone ship)';

-- Slide 33
SELECT Landing_Outcome,COUNT(*) AS count FROM SPACEXTABLE WHERE Date BETWEEN '2010-06-04' AND '2017-03-20' GROUP BY Landing_Outcome ORDER BY count DESC;