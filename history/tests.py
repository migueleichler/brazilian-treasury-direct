from unittest import TestCase
from unittest.mock import patch

from main import get_older_suspensions


class TestGetSuspensions(TestCase):

    @patch('main.get_older_suspensions.requests.get')
    def test_status_code_ok(self, mock_get):
        mock_get.return_value.ok = True

        self.assertTrue()
