import util.ai_api
import os



def start_bot():
    api_handler = util.ai_api.GptApiHandler()
    api_handler.initialize_api()
    answer = api_handler.call_api("Half-Orc", "Paladin", "Clemance", "")
    print(answer.choices[0].text)

if __name__ == "__main__":
    start_bot()