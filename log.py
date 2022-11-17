import hikari
import lightbulb

from secret import TOKEN

# Initialising the bot.

bot = lightbulb.BotApp( token=TOKEN,
                        intents=hikari.Intents.ALL_MESSAGES,
                        prefix="!",
                      )

import sqlite3
import datetime

# Initialize SQLite3

try:
    sqliteConnection = sqlite3.connect('SQLite_Python.db')
    cursor = sqliteConnection.cursor()
    print("Database created and Successfully Connected to SQLite")

    sqlite_select_Query = "select sqlite_version();"
    cursor.execute(sqlite_select_Query)
    record = cursor.fetchall()
    print("SQLite Database Version is: ", record)
    cursor.close()

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)

try:
    sqlite_create_table_query = '''
                                CREATE TABLE SqwixMessageLog 
                                (
                                GuildID INTEGER NOT NULL,
                                ChannelID INTEGER NOT NULL,
                                UserID INTEGER NOT NULL,
                                Message TEXT NOT NULL,
                                Date TEXT
                                );
                                '''

    cursor = sqliteConnection.cursor()
    print("Successfully Connected to SQLite")
    cursor.execute(sqlite_create_table_query)
    sqliteConnection.commit()
    print("SQLite table created")

    cursor.close()

except sqlite3.Error as error:
    print("Error while creating a sqlite table", error)

finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("sqlite connection is closed")


@bot.listen(hikari.MessageCreateEvent)   
async def CreateLog(event):
    GuildID = event.guild_id
    ChannelID = event.channel_id
    UserID = event.author_id
    Message = str(event.content)
    Date = datetime.datetime.now()

    try:
        sqliteConnection = sqlite3.connect('SQLite_Python.db')
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")

        sqlite_insert_with_param = '''
                            INSERT INTO SqwixMessageLog
                            (GuildID, ChannelID, UserID, Message, Date) 
                            VALUES 
                            (?,?,?,?,?)
                            '''

        data_tuple = (GuildID, ChannelID, UserID, Message, Date)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqliteConnection.commit()   

        print("Record inserted successfully into SqwixMessageLog table ", cursor.rowcount)
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)

    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

bot.run()

# INCLUDE SHOW LOG 
