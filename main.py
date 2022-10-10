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


# Register the command to the bot
@bot.command
# Use the command decorator to convert the function into a command
@lightbulb.command("ping", "Returns the Latency for our Bot.")
# Define the command type(s) that this command implements
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
# Define the command's callback. The callback should take a single argument which will be
# an instance of a subclass of lightbulb.context.Context when passed in
async def ping(ctx: lightbulb.Context):
    # Send a message to the channel the command was used in
    await ctx.respond(f"Pong! Latency: {bot.heartbeat_latency*1000:.2f}ms")




#Running the bot.
bot.run()