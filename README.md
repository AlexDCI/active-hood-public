# active_hood

1. Create a virtual environment and activate it
2. Run pip install -r requirements.txt (from where this file is located)
3. Create .env where manage.py is located
4. Add this variables into .env by replacing sample with your datd without quaotation marks!!!! (you need to creat a db in postgres)

SECRET_KEY=sample

DB_NAME=sample
DB_USER=sample
DB_PASS=sample

5. python manage.py makemigrations
6. python manage.py migrate
7. Add .env and your virtual environment into .gitignore - DO NOT PUSH IT
