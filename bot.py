""" Import Lighthouse """
from lighthouse import bot
import slack

# Import the duallog package to set up simultaneous
# logging to screen and console.
import duallog

# Import the logging package to generate log messages.
import logging

# Set up dual logging and tell duallog where to store the logfiles.
duallog.setup("logs")

# Bot will run and wait on 1 second intervals.
# This will parse and run commands based on
# parsing of messages received from message
listener = bot.Bot()


@slack.RTMClient.run_on(event="message")
def wait_for_event(**event):
    """
    entry point for commands from slack.
    reads from slack and handles splitting of arguments.
    submission of commands transitions to mcp for handling
    """
    logging.debug("Event received")
    data = event["data"]

    if "subtype" in data and data["subtype"] == "message_changed":
        logging.debug("Alteration of messages are not handled")

        return

    if "text" in data and listener.bot_id in data["text"]:
        listener.event.handle_event(
            data["user"],
            data["text"].split(listener.bot_id)[1].strip().lower(),
            data["channel"],
        )


# listen for commands
listener.rtm_slack_client.start()
