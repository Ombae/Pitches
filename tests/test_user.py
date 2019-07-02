import unittest
from app.models import User,Pitch,Review,Role
from app import db

class UserModelTest(unittest.TestCase):

    def setUp(self):
        self.new_user = User(password = 'banana')

    def test_password_setter(self):
        self.assertTrue(self.new_user.password_hash is not None)

    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password

    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('banana'))

class ReviewTest(unittest.TestCase):
    def setUp(self):
        # self.user_seth = User(id=1,username = 'seth',password = 'SethOmbae1', email = 'ombaejr@gmail.com',bio="Time is an abstract")
        self.new_review = Review(id=5,review='Review for pitches',date="2019-02-7" )

    def tearDown(self):
        Review.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_review.id,5)
        self.assertEquals(self.new_review.review,'Review for pitches')
        self.assertEquals(self.new_review.date,"2018-09-5")
        # self.assertEquals(self.new_review.user,self.user_seth)

    def test_save_review(self):
        self.new_review.save_review()
        self.assertTrue(len(Review.query.all())>0)
