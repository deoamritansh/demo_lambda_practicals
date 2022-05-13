# importing necessary files
from demo_lambda.src import demo_lambda
from demo_lambda.src.demo_lambda import lambda_handler
import unittest

from unittest.mock import patch, MagicMock


class Test_Lambda_Handler(unittest.TestCase):

    def test_lambda_handler_successful(self):
        self.event = {'Address': 'Gurgaon'}
        with patch.object(demo_lambda, 'create_dynamoDB', return_value='Success'):
            response = lambda_handler(self.event)
            assert response == 'Success'

    def test_lambda_handler_unsuccessful(self):
        self.event = {'Address': ' '}
        with patch.object(demo_lambda, 'create_dynamoDB', return_value='Fail'):
            response = lambda_handler(self.event)
            assert response != 'Success'


if __name__ == '__main__':
    unittest.main()
















