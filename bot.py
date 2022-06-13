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

    @bot.command(name='backstory', help='Creates a backstory for a character.  Specify race, class, name. ie: '
                                        'Half-Orc, Paladin, Clem')
    async def create_backstory(ctx, race, clss, name):
        answer = api_handler.call_api(race, clss, name)
        await ctx.channel.send(answer.choices[0].text)

    discord_handler.start_discord_bot()

