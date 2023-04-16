FROM python:3.9-slim-buster

# set work directory
ENV APP_HOME /app
WORKDIR $APP_HOME

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt .
RUN pip install --quiet -r requirements.txt

# copy project
COPY . .

# port
ENV PORT 8080

# run web service with gunicorn
CMD exec gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 8 --timeout 0 simple_inventory.wsgi:application
