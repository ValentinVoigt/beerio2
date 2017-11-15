import unittest
import transaction
import factory
import random

from pyramid import testing

from beerio2.models.meta import Base
from beerio2 import models

class BaseTest(unittest.TestCase):

    def setUp(self):
        self.config = testing.setUp(settings={
            'sqlalchemy.url': 'sqlite:///:memory:'
        })
        self.config.include('.models')
        settings = self.config.get_settings()

        self.engine = models.get_engine(settings)
        session_factory = models.get_session_factory(self.engine)
        self.session = models.get_tm_session(session_factory, transaction.manager)

        self.init_database()

    def init_database(self):
        ## Create all tables
        Base.metadata.create_all(self.engine)

        ## Add session to factory_boy's Factorys
        models.UserFactory._meta.sqlalchemy_session = self.session

        ## Add test data to database

        # users
        users = [models.UserFactory(room=room) for room in range(1, 16)]
        self.session.add_all(users)
        self.session.add_all(models.UserFactory.create_batch(size=5, active=False))

        # receipts
        for user in users[:10]:
            user.add_receipt(models.ReceiptFactory(amount_guarantee=50))
            user.add_receipt(models.ReceiptFactory(amount_balance=random.randint(1, 20)*5))

    def tearDown(self):
        testing.tearDown()
        transaction.abort()
        Base.metadata.drop_all(self.engine)
