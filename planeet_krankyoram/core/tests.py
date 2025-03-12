from django.test import TestCase
from .models import AppsLib
from django.core.exceptions import ValidationError


class AppsLibValidatorTests(TestCase):

    def setUp(self):

        AppsLib.objects.create(app_name='core', display_name='valid_url', url='/test_123/test/', show=True)

        invalid_chars = '~!@#$%^&*()-+={}[]:;|<>?,.'
        test_cases_invalid = [f'/test{c}/' for c in invalid_chars] + ['test/', '/test']
        for i, url in enumerate(test_cases_invalid):
            AppsLib.objects.create(app_name='core', display_name=f'invalid_url_{i+1}', url=url, show=True)

    def test_url_validation(self):
        valid_app = AppsLib.objects.get(display_name='valid_url')
        valid_app.full_clean()
        self.assertEquals(valid_app.url, '/test_123/test/')

        invalid_apps = AppsLib.objects.filter(display_name__contains='invalid')
        for invalid_app in invalid_apps:
            self.assertRaises(ValidationError, invalid_app.full_clean)









