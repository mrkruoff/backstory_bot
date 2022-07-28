import util.ai_api
import util.bot_handler
import os
import logging

logging.basicConfig(filename='bot.log', level=logging.INFO)

def start_bot():
    api_handler = util.ai_api.GptApiHandler(os.getenv("GPTKEY"))
    api_handler.initialize_api()
    bot_handler = util.bot_handler.Bot_Handler(os.getenv("DISCORDTOKEN"))
    return api_handler, bot_handler


if __name__ == "__main__":
    api_handler, discord_handler = start_bot()
    bot = discord_handler.get_bot()

    @bot.command(name='backstory', help='Creates a backstory for a character.  Specify Gender, race, class, name, optional details. ie: '
                                        ' Male, Half-Orc, Paladin, Clem, "From Neverwinter", happy')
    async def create_backstory(ctx, gender, race, clss, name, optional=None, modifier=None):
        logging.info(f"request from {ctx.author.name}.  With variables {gender}, {race}, {clss}, "
                     f"{name}, {optional}, {modifier}")
        answer = api_handler.call_api(gender, race, clss, name, optional=optional, modifier=modifier)
        await ctx.channel.send(answer.choices[0].text)

    discord_handler.start_discord_bot()

