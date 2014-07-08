from django.db import models
from django.contrib.auth.models import User


class Currency(models.Model):
    name = models.CharField(max_length=10)

    class Meta:
        verbose_name = ('Currency')
        verbose_name_plural = ('Currencys')

    def __unicode__(self):
        pass


class Account(models.Model):
    user = models.ForeignKey(User)
    currency = models.ForeignKey(Currency)
    amount = models.IntegerField()

    class Meta:
        verbose_name = ('Account')
        verbose_name_plural = ('Accounts')

    def __unicode__(self):
        pass

    def withdraw(self, amount, target):
        assert self.amount >= amount
        assert self.currency.name == target.currency.name
        self.amount -= amount
        target.amount += amount
