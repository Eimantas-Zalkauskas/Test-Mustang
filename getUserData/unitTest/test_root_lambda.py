import unittest
from unittest.mock import Mock, patch
from getUserData.root_lambda import api_root_lambda


context = Mock()
event = {
    'pathParameters': 'Message_Id'
}


class TestRootLambda(unittest.TestCase):
    @patch('boto3.resource')
    def test_dynamo_scan_return_not_none(self, mock_dynamo):
        mock_table = Mock()
        mock_table.scan.return_value = {
            'Items': ['Message_Id'],
            'LastEvaluatedKey': 'Message'
        }
        mock_dynamo.Table.return_value = mock_table
        self.assertIsNotNone(mock_table)

    @patch('boto3.resource')
    def test_dynamo_scan_return_none(self, mock_dynamo):
        mock_table = Mock()
        mock_table.scan.return_value = {}
        mock_dynamo.Table.return_value = mock_table

        expected_result = {'Items': ['Message_Id'],
                           'LastEvaluatedKey': 'Message'}
        self.assertNotEqual(expected_result, mock_table)


if __name__ == '__main__':
    unittest.main()
