from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.helpers.hasmethod import hasmethod
from hamcrest import close_to
import time


class TimeCloseTo(BaseMatcher):

    def __init__(self, expected, diff):
        self.expected = expected
        self.diff = diff

    def _matches(self, item):
        if not hasmethod(item, 'timetuple'):
            return False
        return abs(time.mktime(item.timetuple()) - time.mktime(self.expected.timetuple())) < self.diff

    def describe_to(self, description):
        description.append_text('diff is less than ').append_text(self.diff).append_text(' second')


def time_close_to(expected, seconds=1):
    return TimeCloseTo(expected, seconds)
