import creds.secrets
import openai


class GptApiHandler():
    def __init__(self, key=None):
        self.secret = creds.secrets.key if not key else key
        self.base_string = "Create a backstory for a {} {} named {}.{}"

    def initialize_api(self):
        openai.api_key = self.secret

    def call_api (self, race, char_class, name, optional=None):
        prompt = self.base_string.format(race, char_class, name, optional)
        response = openai.Completion.create(model="text-davinci-002", prompt=prompt, temperature=0.7, max_tokens=256)
        return response


