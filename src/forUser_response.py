import random
import string
from slack_sdk import WebClient
import os
from slack_sdk.errors import SlackApiError
from pathlib import Path
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from operations.user_data import get_cx_data,getUserName,get_cl_data
import re
from operations.logging import logger

# def getUserName(userMessage:str):
#     userMessage=userMessage.split(" ")
#     for data in userMessage:
#         returned_value=re.search(r"<https://www.google.com/search\?q=%22",data,re.IGNORECASE)
#         if returned_value:
#             userName=returned_value.string
#             userName=userName.replace("<https://www.google.com/search?q=%22","")
#             userName=userName.replace("+"," ")
#             userName=userName.replace("%22","")
#             userName=userName.replace("|"," ")
#             if '-' and '_' in userName:
#                 userName=userName.replace("_","") 
#                 userName=userName.replace("-"," ") 
#             else:
#                 userName=userName.replace("_"," ") 
#                 userName=userName.replace("-"," ")  
#             userName = ''.join([i for i in userName if not i.isdigit()]) # removing digits from the retreived name
#             userName=userName.split(" ")
#             userName=str(userName[0]+" "+userName[1])
#             print(userName)
#     if userName:        
#         return userName
#     else:
#         return "No user_name detected"
    
'''setting tokens for the bot and environment for app'''

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
client=WebClient(token=os.environ['SLACK_TOKEN'])
slack_app=App(
    token=os.environ['SLACK_TOKEN'],
    signing_secret=os.environ['SIGNING_SECRET']
)
BOT_ID=client.api_call("auth.test")['user_id']

@slack_app.event("message")
def userDetails(payload):
    try:
        channel_id=payload['channel']
        user_id=payload['user']
        user_message=payload['text']
        ts=payload['ts']
        if (BOT_ID != user_id):
            if 'thread_ts' not in payload:
                user_name=getUserName(user_message)
                if user_message != "No User Name found":
                    app_name=user_message.split(" ")
                    if app_name[1]=='Customer': 
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
    SocketModeHandler(slack_app, os.environ["SLACK_APP_TOKEN"]).start()
