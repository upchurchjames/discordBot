from discord.ext import commands, tasks
import datetime

# If no tzinfo is given then UTC is assumed.
times = [
    datetime.time(hour=23, minute=35, second=45)
]


class MyCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.my_task.start()

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        print(f'Logged on as {self.bot.user}!')

    @commands.Cog.listener()
    async def on_message(self, message):
        print("Message received!")
        if message.author.id == 446069741396688906:
            await message.add_reaction("✅")

        if message.author.id == 951643914471874560:
            await message.add_reaction("🐢")

    def cog_unload(self):
        self.my_task.cancel()

    @tasks.loop(time=times)
    async def my_task(self):
        print("Hello")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(MyCog(bot))