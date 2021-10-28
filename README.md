# LightCastle Technical Evaluation

Serialize the given csv file into the given format.

## Platform
Python v3.8
Windows OS/Debian based Linux OS

Dependencies can be found in `requirements.txt`

# HOW TO RUN

1. Install Python 3.8 from https://www.python.org/downloads/release/python-3812/.
2. Clone the git repo and change the working directory to it's root (The Git Repo's root).
3. Install the dependencies by executing the command `pip install -r requirements.txt` in the terminal.
4. Migrate the models to the database, it's a file-based sqlite database by executing the command `python manage.py migrate`.
5. Create a superuser to login to the system by executing the command `python manage.py createsuperuser` and fillup the form accordingly. Please remember the password.
6. Start the Web Server by executing the command `python manage.py runserver`.
7. Download Postman for Testing the API from https://www.postman.com/downloads/.
8. Run the API Documentation to see the results. Link: https://documenter.getpostman.com/view/12416836/UV5f6tDi

