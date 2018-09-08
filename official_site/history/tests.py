from unittest import TestCase
from unittest.mock import patch

from main import get_older_suspensions


class TestGetSuspensions(TestCase):

    @patch('history.main.requests.get')
    def test_status_code_ok(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.content = """
            <a class="next" href="http://www.tesouro.fazenda.gov.br/avisos/next/">
              Próximo
            </a>
        """

        self.assertEqual(
            get_older_suspensions(),
            "http://www.tesouro.fazenda.gov.br/avisos/next/"
        )
