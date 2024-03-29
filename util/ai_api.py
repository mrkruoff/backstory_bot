import openai
import logging


class GptApiHandler():
    def __init__(self, key):
        self.secret = key
        self.base_string = "Create a{} backstory for a character with the following details \n" \
                           " gender: {} \n race: {} \n class: {} \n name: {}"
        self.optional_base_string = self.base_string + "\n optional details: {}"

    def initialize_api(self):
        openai.api_key = self.secret

    def call_api (self, gender, race, char_class, name, optional=None, modifier=None):
        modifierString = f" {modifier}" if modifier else ""
        if not optional:
            prompt = self.base_string.format(modifierString, gender, race, char_class, name)
        else:
            prompt = self.optional_base_string.format(modifierString, gender, race, char_class, name, optional)
        logging.info(prompt)
        response = openai.Completion.create(model="text-davinci-002", prompt=prompt, temperature=0.7, max_tokens=500)
        return response


