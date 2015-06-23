# -*- coding: utf-8 -*-
from __future__ import absolute_import
import pytest
from django_dynamic_fixture import G
from monitoring.models import Url, CheckResult
from hamcrest import assert_that, equal_to, has_properties, close_to
from django.utils import timezone
import datetime

from .matchers import time_close_to


@pytest.fixture
def url():
    return G(Url, url="http://site.ru/")


@pytest.fixture
def check(url):
    return G(CheckResult, status=200, content="test content", url=url)


@pytest.mark.django_db
@pytest.mark.parametrize('status_code, text, expected_count', (
    (200, "test content", 1),
    (201, "test content", 2),
    (200, "test content2", 2),
))
def test_not_create_if_exists(url, check, mocker, status_code, text, expected_count):
    date = timezone.now() - datetime.timedelta(minutes=30)
    check.__class__.objects.all().update(updated_on=date, created_on=date)
    patched = mocker.patch('monitoring.models.requests.get')
    answer = patched.return_value
    answer.status_code = status_code
    answer.text = text
    url.check_url()
    assert_that(url.checks.count(), equal_to(expected_count))
    last = url.checks.order_by("updated_on").last()
    assert_that(last, has_properties(
        content=text,
        status=status_code,
        updated_on=time_close_to(timezone.now(), 1)
    ))


@pytest.mark.django_db
def test_process_exception(url, check, mocker):
    patched = mocker.patch('monitoring.models.requests.get')
    patched.side_effect = Exception(u"привет")
    url.check_url()
    assert_that(url.checks.count(), equal_to(2))
    assert_that(url.checks.order_by("updated_on").last().error, equal_to(u"привет"))
