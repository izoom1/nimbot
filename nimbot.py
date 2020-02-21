import os

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='nim')
async def play_nim(ctx):
    await ctx.send("Still working on it, kiddo.")

bot.run(token)

import pandas as pd
@bot.command(name='weatherman')
async def weather(ctx):
url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/weatherdata/forecast?aggregateHours=24&shortColumnNames=false&sendAsDatasource=false&allowAsynch=false&contentType=csv&unitGroup=us&key=DDBCK6MYKAUWQ5K6SYJ7APGYL&locations=north%20bergen%2C%20new%20jersey"
weather_data = pd.read_csv(url)
    await ctx.send(weather_data.pivot_table(values=["Minimum Temperature", "Maximum Temperature", "Chance Precipitation (%)", "Conditions"], index="Date time", fill_value=0))

bot.run(token)