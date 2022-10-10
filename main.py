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
        

# Bot makes a Dad Joke: Hi X, I am Sqwix.

@bot.listen(hikari.MessageCreateEvent)
async def dadjoke(event):
    if event.is_human:
        name = event.content
        if name.lower().startswith("i am"):
            await event.message.respond(f"Hi {name[5:]}, I am Sqwix.")
        elif name.lower().startswith("i m"):
            await event.message.respond(f"Hi {name[4:]}, I am Sqwix.")
        elif name.lower().startswith("i'm"):
            await event.message.respond(f"Hi {name[4:]}, I am Sqwix.")
        elif name.lower().startswith("im"):
            await event.message.respond(f"Hi {name[3:]}, I am Sqwix.")
        elif name.lower().startswith("am"):
            await event.message.respond(f"Hi {name[3:]}, I am Sqwix.")
        elif name.lower().startswith("m"):
            await event.message.respond(f"Hi {name[2:]}, I am Sqwix.")
        else:
            pass


#Running the bot.
bot.run()