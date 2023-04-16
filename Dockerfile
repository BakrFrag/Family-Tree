FROM python:3.10-alpine3.15
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev jpeg-dev zlib-dev 
WORKDIR /app 
RUN python3 -m venv venv
RUN source venv/bin/activate
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
RUN find . -path "*/migrations/__pycache__/*"  -delete
EXPOSE 8000
WORKDIR /app/family_tree
RUN python manage.py makemigrations 
RUN python manage.py migrate
ENTRYPOINT python manage.py runserver 0.0.0.0:8000