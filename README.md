"# django_apiCall" 


https://praw.readthedocs.io/en/latest/getting_started/authentication.html#code-flow

TO START
- Please start the project with making virtual environment
    python -m venv venv
    venv\scripts\activate
    pip install -r requirements.txt

- To run the reddit app go into the app and run the commands.   Activate venv
    python manage.py runserver
    
- To connect to the Database please insert your databse info in  setting.py and call the following . Activate venv
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver


- Working flow of the reddit app

RUN DJANGO SERVER   ---->   GET REDIRECTED TO APP PERMISSIONS OF REDIT   ---->    GET REDIRECTED BY TO APP HOME PAGE WITH APP TOKEN AND REFRESH TOKEN

NOTE:-

YOUR DEVELOPER CREDENTIALS TO BE INSERTED INTO ---- reddit/reddit/reditCreds.py
