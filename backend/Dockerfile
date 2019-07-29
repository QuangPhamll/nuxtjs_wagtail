# Use an official Python runtime as a parent image
FROM python:3.7
LABEL maintainer="quang.pham.fr@gmail.com"

# Set environment varibles
ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENV dev

COPY ./requirements.txt /code/requirements.txt
RUN pip install --upgrade pip
# Install any needed packages specified in requirements.txt
RUN pip install -r /code/requirements.txt
RUN pip install gunicorn

# Copy the current directory contents into the container at /backend/
COPY . /backend/
# Set the working directory to /backend/
WORKDIR /backend/

#RUN python manage.py migrate
RUN chmod +x wait-for-it.sh

RUN useradd wagtail
RUN chown -R wagtail /backend
USER wagtail

EXPOSE 7999
#CMD exec gunicorn backend.wsgi:application --bind 0.0.0.0:7999 --workers 3
