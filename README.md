
# Project Title 
Family Tree 
## Description 
family tree app allow users to display thier family tree , filter thier family tree , add relatives to them and allow registeration for new users 

## DataBase & Schema DEsign
- for database and schema desgin 
- Drawseql https://drawsql.app/teams/development-9/diagrams/family-tree

## Request & Response Cycle
- E2E test 
- request & response with different testcases 
- Documented Postman Collection https://api.postman.com/collections/6749950-6fedf54e-02ba-42b9-a8c4-d515102190cf?access_key=PMAT-01GY5JQEGQ9QQJFVZYVBDRR5B3
- you can load it directly in postman app by up link 
- collection include documentation for API E2E test 

## Operate Locally
- create python virtalenv with 
  - `pipenv shell`
- install depandancies 
  - `pipenv install -r requirements.txt` 

- go to app directory 
   - `cd family_tree`
- detect migrations 
   - `python manage.py makemigrations`
- apply migrations
   - `python manage.py migrate`

- to create superuser
  - `python manage.py createsuperuser`
  - them go with prompots

- run development test & start api requests 
   - you can change port & host as per your own needs
   - `python manage.py runserver 0.0.0.0:8000`

## Dockerization
- throw dockerfile we can create docker image for project family_tree and them create new containers from this image 
- to build and create image for project 

  - `docker image build -t family_tree:1`

- create docker container from docker image
  - {IMAGE_ID} change from enviroment to enviroment replace {IMAGE_ID} as per your system 

  - `docker run -d --name family_tree_container -p 8000:8000 {IMAGE_ID}`

- now you can consume urls from you localhost using port 8000

### Service Urls 
|HTTP METHOD| Service UR| Description| 
|--|--|--|
| POST  |`/member/`  | Register New User|
| GET | `/member/` | Authenticated User can display thier family tree and filter by `username`|
| POST | `/member/add/relatives/`| Authenticated User can add relatives to his family tree| 
| POST | `/api/token/` | User can login with `username` and `password` and obtain new access token|
| POST | `api/token/refresh/` | get new access token by refersh token| 
| GET |`/redoc/`| read api documentation|
| GET | `/swagger/` | read doc & simulate request , response|

### Build Project 

- python version `3.10`
- Django version `4.2` 
- DRF version `3.14`

### Prerequestes

- machine with python run time enviroment 
- docker engine installed 
- python package index `pip`

