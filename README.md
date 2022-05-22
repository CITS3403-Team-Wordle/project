# CITS3403 project

TYPING CHAMPION practice your speed-tying everyday!

The goal of Typing Champion is to provide a oppertunity to pracitce typing skill with daliy puzzles everyday! 

Typing Champion conatains various categlories of articles, which is extremely helpful to improve reading, typing and spellings. It always provides 60 seconds but with totally different experiences. Will you exceed yourself? Prove it just within 1 minute.

## Starting!

### Requriement
- Unix or Mac OS.
- Python 3.8 or newer
- Heroku server
    - (For Mac) brew tap heroku/brew && brew install heroku

### Installing
Install Python 3.8 or newer
Install Python dependencies
    - python3 -m pip install -r requirements.txt
Install sqlite3

### Running

- change directory to *project* (or *project-main*)

- initiate virtual enrivronment:
    - `source venv/bin/activate`

- for **Development** app:

    set flask configuration
    - `export FLASK_CONFIG='development'`

    run server
    - `python3 manage.py runserver`

- for **Deployment** app:

    set flask configuration
    - `export FLASK_CONFIG='deploy`

    run server
    - `python3 manage.py deploy`

### Testing App

Run unittest:
```
python3 manage.py test
```

### More commands

#### Developing in Python Shell

Run `python3 manage.py shell`

#### Migrate Database

Run `python3 manage.py db init`, also `python3 manage.py migrate`, also `python3 manage.py upgrade` and others

#### Other commands
Run `python3 manage.py` to see more commands

### NOTICE

if compiling error occurs such as **Flask-Script: from flask.\_compat import text_type ModuleNotFoundError: No module named 'flask._compat'**

#### Solution:

find the file location (usually showing a few lines above the Error message)

find: **flask_script/__init__.py**

Manually change:

Where

`from .\_compat import text_type` on original flask-script file

to

`from flask_script._compat import text_type`
