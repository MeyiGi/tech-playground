-- 1. COUNTRY
CREATE TABLE Country (
    country_id NUMBER PRIMARY KEY,
    name VARCHAR2(100) UNIQUE NOT NULL,
    international_ranking NUMBER NOT NULL,
    budget NUMBER(15,2) NOT NULL
);

-- 2. LEAGUE
CREATE TABLE League (
    league_id NUMBER PRIMARY KEY,
    name VARCHAR2(100) NOT NULL,
    ranking NUMBER NOT NULL,
    country_id NUMBER NOT NULL,
    
    CONSTRAINT fk_league_country
        FOREIGN KEY (country_id)
        REFERENCES Country(country_id),
        
    CONSTRAINT unique_league_per_country
        UNIQUE (name, country_id)
);

-- 3. TEAM
CREATE TABLE Team (
    team_id NUMBER PRIMARY KEY,
    name VARCHAR2(100) NOT NULL,
    ranking NUMBER NOT NULL,
    league_id NUMBER NOT NULL,
    
    CONSTRAINT fk_team_league
        FOREIGN KEY (league_id)
        REFERENCES League(league_id)
);

-- 4. STUDENT
CREATE TABLE Student (
    member_id NUMBER PRIMARY KEY,
    name VARCHAR2(100) NOT NULL,
    birthday DATE NOT NULL,
    gender VARCHAR2(10) NOT NULL,
    team_id NUMBER NOT NULL,
    
    CONSTRAINT fk_student_team
        FOREIGN KEY (team_id)
        REFERENCES Team(team_id)
);

-- 5. SOFTWARE DEVELOPER
CREATE TABLE SoftwareDeveloper (
    member_id NUMBER PRIMARY KEY,
    programming_language VARCHAR2(100) NOT NULL,
    
    CONSTRAINT fk_dev_student
        FOREIGN KEY (member_id)
        REFERENCES Student(member_id)
);

-- 6. SOFTWARE TESTER
CREATE TABLE SoftwareTester (
    member_id NUMBER PRIMARY KEY,
    main_testing_tool VARCHAR2(100) NOT NULL,
    
    CONSTRAINT fk_tester_student
        FOREIGN KEY (member_id)
        REFERENCES Student(member_id)
);

-- 7. DATABASE EXPERT
CREATE TABLE DatabaseExpert (
    member_id NUMBER PRIMARY KEY,
    dbms_name VARCHAR2(100) NOT NULL,
    
    CONSTRAINT fk_db_student
        FOREIGN KEY (member_id)
        REFERENCES Student(member_id)
);

-- 8. ORGANIZATION
CREATE TABLE Organization (
    abbreviation VARCHAR2(20) PRIMARY KEY,
    name VARCHAR2(150) NOT NULL,
    type VARCHAR2(100) NOT NULL
);

-- 9. SPONSORSHIP
CREATE TABLE Sponsorship (
    team_id NUMBER NOT NULL,
    abbreviation VARCHAR2(20) NOT NULL,
    donation_amount NUMBER(12,2) NOT NULL,
    
    PRIMARY KEY (team_id, abbreviation),
    
    CONSTRAINT fk_sponsor_team
        FOREIGN KEY (team_id)
        REFERENCES Team(team_id),
        
    CONSTRAINT fk_sponsor_org
        FOREIGN KEY (abbreviation)
        REFERENCES Organization(abbreviation)
);

INSERT INTO Country VALUES (1, 'USA', 1, 5000000000);
INSERT INTO Country VALUES (2, 'Germany', 2, 3000000000);
INSERT INTO League VALUES (1, 'University League', 1, 1);
INSERT INTO League VALUES (2, 'High School League', 2, 1);
INSERT INTO League VALUES (3, 'University League', 1, 2);
INSERT INTO Team VALUES (1, 'CodeMasters', 1, 1);
INSERT INTO Team VALUES (2, 'BugHunters', 2, 2);
INSERT INTO Team VALUES (3, 'DBWarriors', 1, 3);
INSERT INTO Student VALUES (101, 'John Smith', DATE '2002-05-10', 'Male', 1);
INSERT INTO Student VALUES (102, 'Alice Brown', DATE '2001-08-15', 'Female', 1);
INSERT INTO Student VALUES (103, 'Mark Lee', DATE '2003-03-20', 'Male', 2);
INSERT INTO Student VALUES (104, 'Sara White', DATE '2002-11-05', 'Female', 3);
INSERT INTO SoftwareDeveloper VALUES (101, 'Java');
INSERT INTO SoftwareDeveloper VALUES (103, 'Python');
INSERT INTO SoftwareTester VALUES (102, 'Selenium');
INSERT INTO DatabaseExpert VALUES (104, 'Oracle');
INSERT INTO Organization VALUES ('IEEE', 'Institute of Electrical and Electronics Engineers', 'Technical');
INSERT INTO Organization VALUES ('ACM', 'Association for Computing Machinery', 'Technical');
INSERT INTO Organization VALUES ('IEEE', 'Institute of Electrical and Electronics Engineers', 'Technical');
INSERT INTO Organization VALUES ('ACM', 'Association for Computing Machinery', 'Technical');
INSERT INTO Sponsorship VALUES (1, 'IEEE', 50000);
INSERT INTO Sponsorship VALUES (1, 'ACM', 30000);
INSERT INTO Sponsorship VALUES (3, 'ACM', 45000);
COMMIT;

SELECT * FROM Country;
SELECT * FROM League;
SELECT * FROM Team;
SELECT * FROM Student;
SELECT * FROM Sponsorship;
SELECT 
    t.team_id,
    t.name AS team_name,
    l.name AS league_name,
    c.name AS country_name,
    t.ranking
FROM Team t
JOIN League l ON t.league_id = l.league_id
JOIN Country c ON l.country_id = c.country_id
ORDER BY c.name, t.ranking;
