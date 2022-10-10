"""
Author: Kushagra Mittal (kshgr@kshgr.tech)
Initial Commit: 10th October, 2022

Project Name: Sqwix
Project Description: Sqwix is a multi functional Discord bot, created to be an all in
                     one server management tool.

Last Update: 10th October, 2022
"""


# Importing required libraries

import hikari
import lightbulb
# Importing bot-token from an air-gapped file.
from secret import TOKEN

bot = lightbulb.BotApp( token=TOKEN,
                        intents=hikari.Intents.ALL_MESSAGES,
                        prefix="!",
                      )



bot.run()