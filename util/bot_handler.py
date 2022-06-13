from discord.ext import commands

class Bot_Handler():
    def __init__(self, token):
        self.token = token
        self.bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"))

    def start_discord_bot(self):
        self.bot.run(self.token)

    def get_bot(self):
        return self.bot
