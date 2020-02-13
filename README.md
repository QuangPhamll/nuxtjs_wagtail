# Base site - full stack
A initial environment of full-stack web app with wagtail postgres for backend and nuxtjs vue for frontend, run with docker-compose
## Build with:
```
- django: v.3.0.3
- wagtail: v.2.8
- postgres: 11
- nuxjs: v.2.11.0
- docker
```
## Run app:
```
docker-compose build
```
```
docker-compose up
```
backend cms:
```
http://localhost:7999/admin
user: admin
password: changeme
```
frontend:
```
http://localhost:8000
```
## Run command inside container:
- Backend example: `docker-compose run backend python manage.py`

- Fontend example: `docker-compose run --no-deps frontend npm -v`

- Access database: 
    - `docker exec -it  nuxtjs_wagtail_db_1 /bin/bash` : nuxtjs_wagtail_db_1 is container name
    - then `psql -U postgres` - postgres is user defined in `DATABASES` of `backend/backend/settings/base.py`
