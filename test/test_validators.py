# Python
from datetime import datetime, timedelta

# Django
from django.test import TestCase

from django_carpet.validators import date_time_validation
from django_carpet.exceptions import InputError


class ValidaotrsTest(TestCase):

    def test_date_time_validators(self):
        now = datetime.now()
        valid_iso = now.isoformat()
        min_iso = (datetime.now() + timedelta(days=10)).isoformat()

        # Testing the date time validation when the value is None
        try:
            date_time_validation(None, "dateTime")
            self.fail("exception was not raised")
        except InputError as e:
            self.assertEqual(e.obj, 'dateTime')
        except Exception as e:
            self.fail(e)


        # Testing the date time validation when the value is not an ISO format date time
        try:
            date_time_validation('abc', "dateTime")
            self.fail("exception was not raised")
        except InputError as e:
            self.assertEqual(e.obj, 'dateTime')
        except Exception as e:
            self.fail(e)

        # Testing the date time validation when the value is a valid but before min date
        try:
            date_time_validation(valid_iso, "dateTime", False, min_iso)
            self.fail("exception was not raised")
        except InputError as e:
            self.assertEqual(e.obj, 'dateTime')
        except Exception as e:
            self.fail(e)

        # Testing the date time validation when the value is None and empty is allowed
        self.assertIsNone(date_time_validation(None, 'dateTime', True))

        # Testing the date time validation when the value is an empty string and empty is allowed
        self.assertIsNone(date_time_validation("", 'dateTime', True))
        
        # Testing the date time validation when the value is valid without min date
        self.assertEqual(
            date_time_validation(valid_iso, 'dateTime'),
            now
        )

        # Testing the date time validation when the value is valid with a min date
        self.assertEqual(
            date_time_validation(valid_iso, 'dateTime', False, (datetime.now() - timedelta(days=10))),
            now
        )
        