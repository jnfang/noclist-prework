import request_wrapper

class AuthnResource():
    AUTH_ENDPOINT = "/auth"
    TOKEN_KEY = "Badsec-Authentication-Token"
    
    def __init__(self):
        self.session = request_wrapper.RequestWrapper()

    def get_token(self):
        auth_result = self.session.get_with_retry(self.AUTH_ENDPOINT)
        return auth_result.headers[self.TOKEN_KEY]
