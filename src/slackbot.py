from slack_sdk import WebClient
import os
import logging
from slack_sdk.errors import SlackApiError
from pathlib import Path
from dotenv import load_dotenv
from slackeventsapi import SlackEventAdapter
from flask import Flask
from operations.user_data import get_cl_data,get_cx_data,getUserName

'''setting tokens for the bot and environment for app'''

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
client=WebClient(token=os.environ['SLACK_TOKEN'])
logger = logging.getLogger(__name__)
app=Flask(__name__)
slack_event_adapter=SlackEventAdapter(os.environ['SIGNING_SECRET'],"/slack/events",app)
BOT_ID=client.api_call("auth.test")['user_id']


'''Replying to the message as a thread with user_details'''
@slack_event_adapter.on("message")
def user_details(payload):
    try:
        event=payload.get('event',{})
        channel_id=event['channel']
        user_id=event['user']
        user_message=event['text']
        ts=event['ts']
        if (BOT_ID != user_id):
            if 'thread_ts' not in event:
                user_name=getUserName(user_message)
                if user_message != "No User Name found":
                    print(user_name)
                    app_name=user_message.split(" ")
                    if app_name==app_name[1]: 
                        user_data=get_cl_data(user_name)    
                    else:
                        user_data=get_cx_data(user_name)    
                        
                    client.chat_postMessage(
                        channel=channel_id,
                        thread_ts=ts,
                        text=f"User can be:\n{user_data}"
                    )   
                else:
                    client.chat_postMessage(
                        channel=channel_id,
                        thread_ts=ts,
                        text=f"{user_data}"
                    )
        
    except SlackApiError as e:
        logger.error("Error creating conversation: {}".format(e))
        
    
if __name__== "__main__":
    app.run(debug=True,port=5002)