"""
Author: Kushagra Mittal (kshgr@kshgr.tech)
Initial Commit: 10th October, 2022

Project Name: Sqwix
Project Description: Sqwix is a multi functional Discord bot, created to be an all in
                     one server management tool.

Last Update: 10th October, 2022
"""


# Importing required libraries.
import hikari
import lightbulb

# Importing bot-token from an air-gapped file.
from secret import TOKEN

#Initialising the bot.
bot = lightbulb.BotApp( token=TOKEN,
                        intents=hikari.Intents.ALL_MESSAGES,
                        prefix="!",
                      )


# Command - Ping
@bot.command
@lightbulb.command("ping", "Returns the Latency for our Bot.")
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def ping(ctx: lightbulb.Context):
    await ctx.respond(f"Pong! Latency: {bot.heartbeat_latency*1000:.2f}ms")
        

@bot.listen(hikari.MessageCreateEvent)
async def log(event):
    print(event.content)


#Running the bot.
bot.run()