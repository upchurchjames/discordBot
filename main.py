import discord
import os
from dotenv import load_dotenv
from discord.ext import tasks


class MyClient(discord.Client):
    async def setup_hook(self) -> None:
        # start the task to run in the background
        self.my_background_task.start()

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author.id == 446069741396688906:
            await message.add_reaction("✅")

        if message.author.id == 951643914471874560:
            await message.add_reaction("🐢")

        # if message.author.id == 951502733783998534:
        #     await message.add_reaction("🤠")

        # if message.content.find("thank you") != -1 or message.content.find("thanks") != -1:
        #     if message.mentions.
        #     message.reply("Happy to help! : )")

    @tasks.loop(seconds=60)  # task runs every 60 seconds
    async def my_background_task(self):
        print("Task started!")
        await self.send_message()
        print("Task finished!")

        # channel = self.get_channel(1234567)  # channel ID goes here
        # self.counter += 1
        # await channel.send(self.counter)


    @my_background_task.before_loop
    async def before_my_task(self):
        await self.wait_until_ready()  # wait until the bot logs in

    async def send_message(self):
        channel = self.get_channel(951338686681845790)
        myid = '<@446069741396688906>'

        await channel.send(' %s, you\'re a fat fuck ' % myid)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')

    intents = discord.Intents.default()
    intents.message_content = True

    client = MyClient(intents=intents)
    client.run(TOKEN)
