from app import create_app, db
import unittest
import json
import os


class TestAPP(unittest.TestCase):
    def setUp(self):
        self.app = create_app(os.environ.get('FLASK_CONFIG') or 'default')
        self.app.config["WTF_CSRF_ENABLED"] = False
        self.app.testing = True
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

    def test_signup(self):
        params = {"Username": "test", "Password": "123", "Password_confirm": "123", "Email": "123@gamil.com"}
        res = self.client.post('/signup', data=json.dumps(params), content_type='application/json')
        self.assertEqual(res.status_code, 200)
        self.assertIn('error',  res.json)
        self.assertEqual(res.json['error'],
                         'Field must be between 6 and 30 characters long.\nField must be between 8 '
                         'and 30 characters long.\n')

        params = {"Username": "!!!!!!!!", "Password": "1234567890", "Password_confirm": "1234567890", "Email": "1234567890@gamil.com"}
        res = self.client.post('/signup', data=json.dumps(params), content_type='application/json')
        self.assertEqual(res.status_code, 200)
        self.assertIn('error',  res.json)
        self.assertEqual(res.json['error'],
                         'Username must have only letters, numbers or underscores.\n')

        params = {"Username": "abcdefghjk", "Password": "1234567890", "Password_confirm": "12390", "Email": ""}
        res = self.client.post('/signup', data=json.dumps(params), content_type='application/json')
        self.assertEqual(res.status_code, 200)
        self.assertIn('error',  res.json)
        self.assertEqual(res.json['error'],
                         'Passwords must match.\nEmail is required.\n')

        params = {"Username": "abcdefghjk", "Password": "1234567890", "Password_confirm": "1234567890", "Email": "1234567890@gamil.com"}
        res = self.client.post('/signup', data=json.dumps(params), content_type='application/json')
        self.assertEqual(res.status_code, 200)
        self.assertIn('success',  res.json)
        self.assertEqual(res.json['success'], 'signed in')

        params = {"Username": "abcdefghjk", "Password": "1234567890", "Password_confirm": "1234567890", "Email": "1234567890@gamil.com"}
        res = self.client.post('/signup', data=json.dumps(params), content_type='application/json')
        self.assertEqual(res.status_code, 200)
        self.assertIn('error',  res.json)
        self.assertEqual(res.json['error'], 'Username already exists.\nEmail already exists.\n')

    def test_sign(self):
        # This previous signup has been registered

        params = {"Username": "qwertyu", "Password": "1234567890", "Password_confirm": "1234567890", "Email": "qwertyu@gamil.com"}
        res = self.client.post('/signup', data=json.dumps(params), content_type='application/json')
        self.assertEqual(res.status_code, 200)
        self.assertIn('success',  res.json)
        self.assertEqual(res.json['success'], 'signed in')

        params = {"Email": "qwertyu@gamil.com", "Password": "1234567890", "Remember_me": ""}
        res = self.client.post('/login', data=json.dumps(params), content_type='application/json')
        self.assertEqual(res.status_code, 200)
        self.assertIn('success', res.json)
        self.assertEqual(res.json['success'], 'logged in')

        params = {"Email": "qwertyu@gamil.com", "Password": "abc", "Remember_me": ""}
        res = self.client.post('/login', data=json.dumps(params), content_type='application/json')
        self.assertEqual(res.status_code, 200)
        self.assertIn('error', res.json)
        self.assertEqual(res.json['error'], 'bad user')

        params = {"Email": "12345678", "Password": "1234567890", "Remember_me": ""}
        res = self.client.post('/login', data=json.dumps(params), content_type='application/json')
        self.assertEqual(res.status_code, 200)
        self.assertIn('error', res.json)
        self.assertEqual(res.json['error'], 'bad user')

    def test_logout(self):
        # This previous signup has been registered

        params = {"Username": "a123456789", "Password": "1234567890", "Password_confirm": "1234567890", "Email": "a123456789@gamil.com"}
        res = self.client.post('/signup', data=json.dumps(params), content_type='application/json')
        self.assertEqual(res.status_code, 200)
        self.assertIn('success',  res.json)
        self.assertEqual(res.json['success'], 'signed in')

        params = {"Email": "a123456789@gamil.com", "Password": "1234567890", "Remember_me": ""}
        res = self.client.post('/login', data=json.dumps(params), content_type='application/json')
        self.assertEqual(res.status_code, 200)
        self.assertIn('success', res.json)
        self.assertEqual(res.json['success'], 'logged in')
        self.assertEqual(len(self.client.cookie_jar), 1)

        res = self.client.get('/logout')
        self.assertIn('success', res.json)
        self.assertEqual(res.json['success'], 'logged out')
        self.assertEqual(len(self.client.cookie_jar), 0)



    def tearDown(self):
        with self.app.app_context():
            db.drop_all()


