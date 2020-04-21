import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from noclist import users_resource
import unittest

class UsersResourceTest(unittest.TestCase):
    def test_checksum_hash(self):
        users = users_resource.UsersResource()
        result = users.get_checksum_header("12345")
        expected = {users.CHECKSUM_KEY: "c20acb14a3d3339b9e92daebb173e41379f9f2fad4aa6a6326a696bd90c67419"}
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()