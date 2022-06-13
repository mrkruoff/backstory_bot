import util.ai_api
import util.bot_handler
from creds.secrets import discordToken



def start_bot():
    api_handler = util.ai_api.GptApiHandler()
    api_handler.initialize_api()
    bot_handler = util.bot_handler.Bot_Handler(discordToken)
    return api_handler, bot_handler


if __name__ == "__main__":
    api_handler, discord_handler = start_bot()
    bot = discord_handler.get_bot()

    @bot.command(name='backstory', help='Creates a backstory for a character.  Specify Gender, race, class, name, optional details. ie: '
                                        ' Male, Half-Orc, Paladin, Clem, "From Neverwinter"')
    async def create_backstory(ctx, gender, race, clss, name, opt=None):
        answer = api_handler.call_api(gender, race, clss, name, optional=opt)
        await ctx.channel.send(answer.choices[0].text)

    discord_handler.start_discord_bot()

