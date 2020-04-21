import json
import hashlib
import authn_resource
import request_wrapper

class UsersResource():
    USERS_ENDPOINT = "/users"
    CHECKSUM_KEY = "X-Request-Checksum"
    
    def __init__(self):
        self.session = request_wrapper.RequestWrapper()
        self.auth_token = authn_resource.AuthnResource().get_token()
    
    def get_checksum_header(self, auth_token):
        checksum = hashlib.sha256(bytearray((auth_token + self.USERS_ENDPOINT).encode())).hexdigest()
        return {self.CHECKSUM_KEY: checksum}
    
    def get_users(self):
        users_result = self.session.get_with_retry(self.USERS_ENDPOINT, headers = self.get_checksum_header(self.auth_token))
        users = users_result.text.splitlines()
        return json.dumps(users)
