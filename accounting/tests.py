from django.test import TestCase
from django_any import any_model
from accounting.models import Account
# Create your tests here.


class TestAccountTransaction(TestCase):
    #fixtures = ['userx.xml', 'account.xml']

    def setUp(self):
        self.account1 = any_model(Account, amount=25)
        self.account2 = any_model(Account, amount=0,
                                  currency__name=self.account1.currency.name)

    def test_transaction_succed(self):
        # user=
        self.account1.withdraw(10, self.account2)
        self.assertEquals(self.account1.amount, 15)
        self.assertEquals(self.account2.amount, 10)

    def test_transaction_whith_enough_money_fails(self):
        self.assertRaises(
            AssertionError, self.account1.withdraw, 100, self.account2)
