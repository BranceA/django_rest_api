USE djangorestapi_db;
TRUNCATE person_api_person;
INSERT INTO people(age, date_joined, date_updated, name) 
values(30, '2021-05-10', '2021-05-15', 'Bob Doe'),
(45, '2021-05-02', '2021-05-15', 'Sally Doe'),
(7, '2021-08-10', '2021-11-10', 'Billy Doe'), 
(22, '2020-02-10', '2021-12-25', 'Bertha Doe');
