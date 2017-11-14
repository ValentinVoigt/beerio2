import unittest
import transaction
import factory

from datetime import datetime
from beverages import models
from pyramid import testing
from webob.multidict import MultiDict

class UserFactory(factory.Factory):

    class Meta:
        model = models.User

    created_at = factory.LazyFunction(datetime.now)
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('email')
    balance = 0
    guarantee = 0
    active = True

class BaseTest(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp(settings={
            'sqlalchemy.url': 'sqlite:///:memory:'
        })
        self.config.include('.models')
        settings = self.config.get_settings()

        from .models import (
            get_engine,
            get_session_factory,
            get_tm_session,
            )

        self.engine = get_engine(settings)
        session_factory = get_session_factory(self.engine)

        self.session = get_tm_session(session_factory, transaction.manager)

    def init_database(self):
        from .models.meta import Base
        Base.metadata.create_all(self.engine)

    def tearDown(self):
        from .models.meta import Base

        testing.tearDown()
        transaction.abort()
        Base.metadata.drop_all(self.engine)


class TestMyViewSuccessCondition(BaseTest):

    def setUp(self):
        super(TestMyViewSuccessCondition, self).setUp()
        self.init_database()
        self.add_fixtures()

    def add_fixtures(self):
        self.session.add(UserFactory())

    def test_sql(self):
        all_users = self.session.query(models.User).all()
        assert len(all_users) == 1

    def test_form_fail(self):
        from .views.default import my_view
        request = testing.DummyRequest(dbsession=self.session, post=MultiDict())
        info = my_view(request)
        self.assertFalse(info['form'].validate())

    def test_form_okay(self):
        from .views.default import my_view
        request = testing.DummyRequest(
            dbsession=self.session,
            post=MultiDict([
                ('name', 'Asdf'),
                ('company', ''),
                ('volume_ml', '500'),
            ]),
        )
        info = my_view(request)
        self.assertTrue(info['form'].validate())
        self.assertEqual(info['form'].data['volume_ml'], 500)
