import imp
import hikari
import lightbulb
from secret import TOKEN

bot = lightbulb.BotApp( token=TOKEN,
                        intents=hikari.Intents.ALL_MESSAGES,
                        prefix="!",
                      )



bot.run()