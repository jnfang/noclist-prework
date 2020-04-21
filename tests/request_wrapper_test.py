import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from noclist.request_wrapper import RequestWrapper
import unittest
from requests import exceptions
from mock import patch
from unittest.mock import Mock

class RequestWrapperTest(unittest.TestCase):
    def test_twice_retry(self):
        response_mock = Mock()
        response_mock.status_code = 200
        response_mock.json.return_value = ["123456"]
        with patch('noclist.request_wrapper.requests.get', side_effect=[exceptions.Timeout, response_mock]) as get_patch:
            rw = RequestWrapper()
            result = rw.get_with_retry("/auth")
            self.assertEqual(result.json.return_value, response_mock.json.return_value)
            self.assertEqual(get_patch.call_count, 2)
    
    def test_max_attempts(self):
        response_mock = Mock()
        response_mock.status_code = 200
        response_mock.json.return_value = ["123456"]
        with patch('noclist.request_wrapper.requests.get', side_effect=[exceptions.Timeout, exceptions.ConnectionError, response_mock]) as get_patch:
            rw = RequestWrapper()
            rw.get_with_retry("/auth")
            self.assertEqual(get_patch.call_count, 3)

    def test_failure_after_retries(self):
        with patch('noclist.request_wrapper.requests.get', side_effect=[exceptions.Timeout, exceptions.ConnectionError,  exceptions.HTTPError]) as get_patch:
            with self.assertRaises(SystemExit) as sysexit: 
                rw = RequestWrapper()
                rw.get_with_retry("/auth")
                self.assertEqual(sysexit.exception.code, 1)
                self.assertEqual(get_patch.call_count, 3)

if __name__ == '__main__':
    unittest.main()