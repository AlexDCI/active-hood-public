# active_hood

1. Create a virtual environment and activate it
2. Run pip install -r requirements.txt (from where this file is located)
3. Create .env where manage.py is located
4. Add this variables into .env by replacing sample with your datd without quaotation marks!!!! (you need to creat a db in postgres)

SECRET_KEY=sample

SECRET_KEY=sample

DB_NAME=sample
DB_USER=sample
DB_PASS=sample

EMAIL_USER= #your email
EMAIL_HOST_PASSWORD= #password to your email

5. python manage.py makemigrations
6. python manage.py migrate
7. Add .env and your virtual environment into .gitignore - DO NOT PUSH IT


To enable sign in with Google account on the website:

Step 1: Create a Project on Google Cloud Console
Go to Google Cloud Console:
Open Google Cloud Console.

Create a New Project:

Click on the project drop-down and select New Project.
Enter a project name and click Create.
Step 2: Configure OAuth Consent Screen
Navigate to OAuth Consent Screen:

In the Cloud Console, go to APIs & Services > OAuth consent screen.
Choose External and click Create.
Configure the Consent Screen:

Fill in the required fields such as App name, User support email, and Developer contact information.
Click Save and Continue.
Step 3: Create OAuth 2.0 Client IDs
Enable APIs:

Navigate to APIs & Services > Library.
Search for Google+ API or Google People API and click Enable.
Create Credentials:

Go to APIs & Services > Credentials.
Click Create Credentials and select OAuth 2.0 Client ID.
Configure OAuth Client:

Choose Web application.
Enter a name for the client.
Under Authorized redirect URIs, add the URI where your application will handle OAuth 2.0 responses: http://127.0.0.1:8000/oauth/complete/google-oauth2/
Click Create.
Download OAuth Credentials:

After creation, you will see a Client ID and Client Secret. Note these down or download the JSON file.


To be able to send emails to restore password:
Enable Less Secure Apps (Not Recommended)
Enabling less secure apps is not recommended because it makes your account less secure. However, for testing purposes, you can enable it:

Go to your Google Account settings at https://myaccount.google.com/.
Click on Security in the left-hand menu.
Scroll down to Less secure app access and click Turn on access.
Toggle the switch to turn on access for less secure apps.


TO BE ABLE TO USE THESE FEATURES YOU NEED TO CHANGE THIS CONSTANT TO YOUR OWN 

# social auth configs for google #This data will be from your project in the Google Consol. Later you can plce these  constants in .env
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '' # change here
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '' # change here
SOCIAL_AUTH_GOOGLE_OAUTH2_REDIRECT_URI = '' # change here


# email configs
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = config('EMAIL_USER') # in .env file
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD') # in .env file
