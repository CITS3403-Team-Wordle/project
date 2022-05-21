import unittest

from flask import current_app
from app import create_app, db

from app/models import User

import sqlite3
import os

# database name
#db_name = "test.db"


class SqliteTests(unittest.TestCase):
    def setUp(self):
        self.app = create_app('test')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()


    def test_One_Plus_One(self):
        return self.assertEqual(1,1)

'''
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()


    def create_table(self):
        self.cursor.execute("""DROP TABLE IF EXISTS "User";""")
        self.cursor.execute("""CREATE TABLE "User" (
                  "name" String,
                  "passwd" String,
                  "email" String,
                  "uid" Integer
                );""")

        self.cursor.execute("""DROP TABLE IF EXISTS "alembic_version";""")
        self.cursor.execute("""CREATE TABLE "alembic_version" (
                  "version_num" VARCHAR(32) NOT NULL,
                  CONSTRAINT "alembic_version_pkc" PRIMARY KEY ("version_num")
                );""")
        self.conn.commit()
        
'''

'''

    def test_insert(self):
        self.create_table()

        # test insert
        self.cursor.execute("""INSERT INTO User VALUES('test_name', 'test_passwd', 'test_eamil', 12345)""")
        self.assertEqual(1, self.cursor.rowcount)

        self.cursor.execute("""INSERT INTO alembic_version VALUES('version_0.0.1')""")
        self.assertEqual(1, self.cursor.rowcount)

    def test_query(self):
        self.create_table()

        # test search
        self.cursor.execute("""INSERT INTO User VALUES('test_name', 'test_passwd', 'test_eamil', 12345)""")
        self.cursor.execute("""SELECT * FROM User""")
        rows = self.cursor.fetchall()
        self.assertEqual(1, len(rows))
        self.assertEqual(('test_name', 'test_passwd', 'test_eamil', 12345), rows[0])

        self.cursor.execute("""INSERT INTO alembic_version VALUES('version_0.0.1')""")
        self.cursor.execute("""SELECT * FROM alembic_version""")
        rows = self.cursor.fetchall()
        self.assertEqual(1, len(rows))
        self.assertEqual(('version_0.0.1', ), rows[0])

    def test_update(self):
        self.create_table()

        # test modification
        self.cursor.execute("""INSERT INTO User VALUES('test_name', 'test_passwd', 'test_eamil', 12345)""")
        self.cursor.execute("""SELECT * FROM User""")
        rows = self.cursor.fetchall()
        self.assertEqual(('test_name', 'test_passwd', 'test_eamil', 12345), rows[0])
        self.cursor.execute("""UPDATE User SET passwd='update_passwd' WHERE name='test_name'""")
        self.cursor.execute("""SELECT * FROM User""")
        rows = self.cursor.fetchall()
        self.assertEqual(('test_name', 'update_passwd', 'test_eamil', 12345), rows[0])

        self.cursor.execute("""INSERT INTO alembic_version VALUES('version_0.0.1')""")
        self.cursor.execute("""SELECT * FROM alembic_version""")
        rows = self.cursor.fetchall()
        self.assertEqual(('version_0.0.1', ), rows[0])
        self.cursor.execute("""UPDATE alembic_version SET version_num='version_0.0.2' WHERE version_num='version_0.0.1'""")
        self.cursor.execute("""SELECT * FROM alembic_version""")
        rows = self.cursor.fetchall()
        self.assertEqual(('version_0.0.2', ), rows[0])

    def test_delete(self):
        self.create_table()

        self.cursor.execute("""INSERT INTO User VALUES('test_name', 'test_passwd', 'test_eamil', 12345)""")
        self.cursor.execute("""SELECT * FROM User""")
        rows = self.cursor.fetchall()
        self.assertEqual(1, len(rows))
        self.cursor.execute("""DELETE FROM User""")
        self.assertEqual(1, self.cursor.rowcount)
        self.cursor.execute("""SELECT * FROM User""")
        rows = self.cursor.fetchall()
        self.assertEqual(0, len(rows))

        self.cursor.execute("""INSERT INTO alembic_version VALUES('version_0.0.1')""")
        self.cursor.execute("""SELECT * FROM alembic_version""")
        rows = self.cursor.fetchall()
        self.assertEqual(1, len(rows))
        self.cursor.execute("""DELETE FROM alembic_version""")
        self.assertEqual(1, self.cursor.rowcount)
        self.cursor.execute("""SELECT * FROM alembic_version""")
        rows = self.cursor.fetchall()
        self.assertEqual(0, len(rows))
        '''
        
