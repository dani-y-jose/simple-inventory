# Example django app
This repo is an example of a django app that can be tested using docker containers and deployed 
to google cloud.

## Local development
Clone this repo
```bash
git clone https://github.com/dani-y-jose/django-cloudrun.git
cd django-cloudrun
```
In order to develop locally the only thing you need is a python virtualenv.
```bash
virtualenv venv
source bin/activate
```
### 1. Install dependencies:
```bash
pip install -r requirements-dev.txt
```

### 2. Create .env file
.env file defines some parameters for running the server. The most basic one
should contain the following contents (you can copy or rename .env.local file too):

```bash
DEBUG=1
SECRET_KEY=secret
```
### 3. Initialize DB
You need to run migrations and add a superuser in order to get access to admin
page
#### Linux/MacOS:
```bash
python manage.py migrate
python manage.py runscript create_dev_users
```
Once completed, you can access admin page with creds user: admin, pass: admin.
> Note: do not run this script against prod database, this is only for local development.

### 4. Start server
In order to run local server, we need to set some enviroment variables:

### 5. Connect local server to dev database
If you want to run a local django server connected to the development
postgres database hosted in the cloud, you only need to add the 
corresponding variables to .env file.
The correct values can be found in the `django-settings` secret on Google
Cloud Secret Manager. Replace the values and run the service again.
#### Linux/MacOS:
```bash
python manage.py runserver
```

And then just go to `http://localhost:8000/example` to see the example app.

## Local development with docker
...