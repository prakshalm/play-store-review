from thefuzz import fuzz
from slack_sdk import WebClient
import os
import logging
from slack_sdk.errors import SlackApiError
from pathlib import Path
from dotenv import load_dotenv
from slackeventsapi import SlackEventAdapter

'''setting tokens for the bot and environment for app'''

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
client=WebClient(token=os.environ['SLACK_TOKEN'])
logger = logging.getLogger(__name__)

slack_event_adapter=SlackEventAdapter(os.environ['SIGNING_SECRET'],"/slack/events",app)
BOT_ID=client.api_call("auth.test")['user_id']

