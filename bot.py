""" Import Lighthouse """
from lighthouse import bot

# Bot will run and wait on 1 second intervals.
# This will parse and run commands based on
# parsing of messages received from message
listener = bot.Bot()

# Listen for commands
listener.listen()
