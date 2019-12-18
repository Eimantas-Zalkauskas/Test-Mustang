import unittest
from unittest.mock import Mock, patch
import boto3
import json
from getUserData import met_data_lambda
from nose.tools import assert_is_not_none, assert_is_none, assert_true, assert_false


#
# class FileValidation(unittest.TestCase):
#
#     def test_file_event_is_true(self):
#         mock_event = event['Messages'][0]
#         assert_true(met_data_lambda.get_message_from_queue(mock_event, context))
#
#     def test_file_event_is_none(self):
#         mock_event = event['Messages'][0]
#         assert_is_none(mock_event, False)
#
#
# class DataVerification(unittest.TestCase):
#
#     mock_db = Mock(boto3.resource('dynamodb'))
#     mock_table = Mock(mock_db.Table('Met_Test'))
#     mock_json = Mock(json)
#
#     def test_db_is_not_none(self):
#         DataVerification.mock_table.return_value = True
#         assert_true(DataVerification.mock_table)
#
#     def test_db_is_not_present(self):
#         DataVerification.mock_table.return_value = False
#         assert_false(DataVerification.mock_table)
#
#     @patch('queue.dynamodb.table')
#     def test_items_adding_to_table(self, mock_table):
#         mock_table.return_value.put_item(Item=1)
#         response = met_data_lambda.get_message_from_queue(event, context)
#
#         assert_is_not_none(mock_table)
#
#     @patch('queue.json.loads')
#     def test_json_loads_obj_body(self, mock_loads):
#         mock_loads.return_value.loads = Mock(mock_loads.body)
#         response = met_data_lambda.get_message_from_queue(event, context)
#
#         assert_is_not_none(response.body)









