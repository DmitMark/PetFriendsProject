import json
class Base_pf_response:
    def __init__(self, response):
        self.response = response
        self.response_json = ""
        try:
            self.response_json = response.json()
        except json.decoder.JSONDecodeError:
            self.response_json = response.text
        self.response_status = response.status_code

    def assert_status_code(self, status_code):
        assert self.response_status == status_code

    def validate(self, schema):
        schema.model_validate(self.response_json)
        return self