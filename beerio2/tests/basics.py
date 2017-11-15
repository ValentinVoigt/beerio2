from pyramid import testing
from webob.multidict import MultiDict

from . import BaseTest
from beerio2.models import User

class TestBasicDatabaseInvariants(BaseTest):

    def test_users(self):
        active_users = self.session.query(User).filter(User.active).count()
        inactive_users = self.session.query(User).filter(~User.active).count()

        assert active_users <= 15
        assert inactive_users > 0

    def test_money(self):
        for user in self.session.query(User).all():
            balance_receipts = sum([r.amount_balance for r in user.receipts])
            sell_prices = sum([s.price for s in user.sells])
            guarantee_receipts = sum([r.amount_guarantee for r in user.receipts])

            assert user.balance == balance_receipts - sell_prices
            assert user.guarantee == guarantee_receipts 

    def test_form_fail(self):
        from ..views.default import my_view
        request = testing.DummyRequest(dbsession=self.session, post=MultiDict())
        info = my_view(request)
        assert not info['form'].validate()

    def test_form_okay(self):
        from ..views.default import my_view
        request = testing.DummyRequest(
            dbsession=self.session,
            post=MultiDict([
                ('name', 'Asdf'),
                ('company', ''),
                ('volume_ml', '500'),
            ]),
        )
        info = my_view(request)
        assert info['form'].validate()
        assert info['form'].data['volume_ml'] == 500
