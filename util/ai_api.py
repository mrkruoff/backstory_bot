import creds.secrets
import openai


class GptApiHandler():
    def __init__(self, key=None):
        self.secret = creds.secrets.key if not key else key
        self.base_string = "Create a backstory for a character with the following details \n" \
                           " gender: {} \n race: {} \n class: {} \n name: {}"
        self.optional_base_string = self.base_string + "\n optional details: {}"

    def initialize_api(self):
        openai.api_key = self.secret

    def call_api (self, gender, race, char_class, name, optional=None):
        if not optional:
            prompt = self.base_string.format(gender, race, char_class, name)
        else:
            prompt = self.optional_base_string.format(gender, race, char_class, name, optional)
        print(prompt)
        response = openai.Completion.create(model="text-davinci-002", prompt=prompt, temperature=0.7, max_tokens=500)
        return response


