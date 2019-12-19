import boto3
import unittest
from unittest.mock import Mock, patch
import json
from getUserData.file_download import file_download_lambda

context = Mock()
event = {
    'pathParameters': {
        'messageID': 123
    }
}


class TestFileDownloadLambda(unittest.TestCase):
    # @patch('file-download-lambda.json')
    @patch('boto3.resource')
    def test_get_item_from_db(self, mock_dynamo):
        mock_table = Mock()
        mock_dynamo.Table.return_value = mock_table

        file_download_lambda(event, context)

        mock_table.get_item.assert_called_once_with(Key={'Message_Id': 123})






