# -*- coding: utf-8 -*-
from django.db import models
import requests


class Url(models.Model):
    url = models.URLField(unique=True)

    class Meta:
        verbose_name = "Url"
        verbose_name_plural = "Urls"

    def __str__(self):
        return self.url

    def check_url(self):
        result = CheckResult(url=self)
        try:
            response = requests.get(self.url)
            result.status = response.status_code
            result.content = response.text
        except Exception as e:
            result.error = e
        result.save()

    def get_last_check(self):
        return self.checks.order_by('created_on').last()

    @property
    def last_status(self):
        last_check = self.get_last_check()
        if last_check is not None:
            return last_check.status

    @property
    def last_check_date(self):
        last_check = self.get_last_check()
        if last_check is not None:
            return last_check.created_on


class CheckResult(models.Model):
    url = models.ForeignKey(Url, related_name='checks')
    status = models.IntegerField(u'HTTP Status', null=True)
    content = models.TextField(u'Content', null=True)
    error = models.TextField(u'Error', null=True, default=None)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "CheckResult"
        verbose_name_plural = "CheckResults"

    def __str__(self):
        return "Check %s %s" % (self.pk, self.url)
