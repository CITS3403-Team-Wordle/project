# project
This is the file of the application

# Intro for CITS3403 Teams!

##manually test database connection
1. change dir to app/
2. do command:  source venv/bin/activate
3. do command:  python3 manage.py db init       # initiate the database

4. if wish to test the connect with database, do command:
    python3 manage.py shell     # run app in shell
    from __init__ import db     # import connection db
    from models import User     # test table User, structure is introduced in models.py
    
    u1 = User(name='name', passwd='passwd', email='email', uid=1)   #create User object
    db.session.add(u1)
    db.session.commit()         # commit the change of adding u1
5. then we can check the database see if the u1 is added, quit python3 shell and do:
    sqlite dev_data.sqlite      # open dev_data.sqlite
    .mode box
    .width 20                   #optionally set the form of output
    select * from User;         # output all from table User


