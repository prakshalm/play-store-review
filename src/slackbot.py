from slack_sdk import WebClient
import os
import logging
from slack_sdk.errors import SlackApiError
from pathlib import Path
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from operations.user_data import get_cx_data,getUserName,get_cl_data
import json
'''setting tokens for the bot and environment for app'''

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
client=WebClient(token=os.environ['SLACK_TOKEN'])
logger = logging.getLogger(__name__)
slack_app=App(
    token=os.environ['SLACK_TOKEN'],
    signing_secret=os.environ['SIGNING_SECRET']
)
BOT_ID=client.api_call("auth.test")['user_id']

@slack_app.event("message")
def userDetails(payload):
    try:
        if 'subtype' in payload:
            user_id=payload['user']
            userName_link=payload['attachment'][0]['fields'][0]['value']
            app_name=payload['attachment'][0]['fallback']
            channel_id=payload['channel']
            ts=payload['ts']
            with open('paylod_data.json', 'a') as json_file:
                json_file.write('\n')
                json.dump(payload, json_file,indent=4,separators=(',',': '))
                
            if BOT_ID!=user_id:
                if 'thread_ts' not in payload:
                    app_name=app_name.split(" ")
                    user_name=getUserName(userName_link)
                    if user_name!="No user_name detected":
                        if app_name[0]!='CityMall':
                            user_details=get_cl_data(user_name)

                        else:
                            user_details=get_cx_data(user_name)

                        client.chat_postMessage(
                            channel=channel_id,
                            text=f"User can be:\n{user_details}",
                            thread_ts=ts
                        )
                    else:
                        print("User_name Couldnt be detected")
                    
            
    except SlackApiError as e:
        logger.error("Error creating conversation: {}".format(e))

            
if __name__== "__main__":
    SocketModeHandler(slack_app, os.environ["SLACK_APP_TOKEN"]).start()
