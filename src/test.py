# import re
# import pandas as pd
# import numpy
# from thefuzz import fuzz
# import sys

# #LEADER APP
# # userMessage="""Google Play, City Mall Live

# # ★☆☆☆☆ English
# # फ्रॉड फाउंडेशन की जगह
# # _by_ <https://www.google.com/search?q=%22ShivBharat-__-Yadav00220%22|ShivBharat Yadav> _for v1.30.9 () -_  · <https://watch.appfollow.io/apps/my-first-workspace/reviews/56176?review_id=917686285&amp;utm_medium=slack&amp;utm_source=reviews&amp;utm_campaign=reply&amp;autologin=236483:95e0da652c4a6fdbd206204d31e3bf36474201424133dfa0b75749973c93f0e6:1650551048&amp;t=r|Reply> · <https://appfollow.io/gp/10556/review/917686285?s=global4&amp;utm_medium=slack&amp;utm_source=reviews&amp;utm_campaign=permalink|Permalink> · <https://appfollow.io/gp/10556/review/917686285?s=global4&amp;action=translate&amp;utm_medium=slack&amp;utm_source=reviews&amp;utm_campaign=translate|Translate> · <https://watch.appfollow.io/apps/my-first-workspace/reviews/56176?review_id=917686285&amp;utm_medium=slack&amp;utm_source=reviews&amp;utm_campaign=add_tag&amp;autologin=236483:95e0da652c4a6fdbd206204d31e3bf36474201424133dfa0b75749973c93f0e6:1650551048&amp;t=r|Add tag>"""

# # userMessage=userMessage.split(" ")
# # for data in userMessage:
# #     returned_value=re.search(r"<https://www\.google\.com/search\?q=%22",data,re.IGNORECASE)
# #     if returned_value:
# #         userName=returned_value.string
# #         print(userName)
        
# #         #removing unnecessary symbols from the userName
# #         userName=userName.replace("<https://www.google.com/search?q=%22","")
# #         userName=userName.replace("+"," ")
# #         userName=userName.replace("%22","")
# #         userName=userName.replace("|"," ")
# #         userName=userName.replace("_","")
# #         userName=userName.replace("-","")
# #         userName = ''.join([i for i in userName if not i.isdigit()])    #removing digits from the userName
# #         userName=userName.split(" ")
# #         print(userName)
# #         userName=str(userName[0]+" "+userName[1])
# #         print(userName)
        
        

# import pandas as pd
# import numpy as np
# from thefuzz import fuzz
# import re
# from tabulate import tabulate

# from slackbot import userDetails

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
    

# def removeDuplicates(lst):
      
#     seen = []
#     Output = []
#     for a, b, c, d in lst:
#         if [a,b,c] not in seen:
#             seen.append([a,b,c])
#             Output.append([a, b, c, d])

#     seen = []
#     removed_Duplicate = []
#     for a, b, c, d in Output:
#         if c not in seen:
#             seen.append(c)
#             removed_Duplicate.append([a, b, c, d])
#         else:
#             index=seen.index(c)
#             removed_Duplicate[index][1]=str(removed_Duplicate[index][1])+','+str(b)
            
#     return removed_Duplicate


# # FOR CX
# def get_cx_data(user_to_search:str,threshold=85):
#     if threshold>=80:
#         print('Searching in cx.csv')
#         df=pd.read_csv('./operations/data_cx.csv',skiprows=1)
#         length=df.shape[0]
#         user_info=list()
#         for i in range(length):
#             if(fuzz.ratio(str(df['user_name'][i]).lower(),user_to_search.lower())>threshold):
#                 user_info.append((df['user_name'][i],df['user_id'][i],df['user_phone'][i],df['processing_at'][i]))
#         user_info=removeDuplicates(user_info)
#         user_info_df=pd.DataFrame(user_info)
#         user_info_df.rename(columns = {0:'Name',1:'user_id',2:'phone_number',3:'Processing At'}, inplace = True)
#         if user_info_df.shape[0]>=1:
#             user_info_df=user_info_df.sort_values(by=['Processing At']).head(11)
#             user_info_df.drop("Processing At",axis=1,inplace=True)
#             print('Searched in cx.csv')
#             print(user_info_df)
#             return user_info_df
#         else:
#             print(user_info_df)
#             get_cx_data(user_to_search,threshold-5)
#     else:
#         return "No user Found"


# # FOR CL
# def get_cl_data(user_to_search:str,threshold=85):
#     if threshold>=80:
#         print('Searching in cl.csv')
#         df=pd.read_csv('./operations/data_cl.csv',skiprows=1)
#         length=df.shape[0]
#         user_info=list()
#         for i in range(length):
#             if(fuzz.ratio(str(df['name'][i]).lower(),user_to_search.lower())>threshold):
#                 user_info.append((df['name'][i],df['user_id'][i],df['phone_number'][i],df['processing_at'][i]))
#         user_info=removeDuplicates(user_info)
#         user_info_df=pd.DataFrame(user_info)
#         user_info_df.rename(columns = {0:'Name',1:'user_id',2:'phone_number',3:'Processing At'}, inplace = True)
#         if user_info_df.shape[0]>=1:
#             user_info_df=user_info_df.sort_values(by=['Processing At']).head(11)
#             user_info_df= user_info_df.drop("Processing At",axis=1)
#             print('Searched in cx.csv')
#             print(user_info_df)
#             return user_info_df
#         else:
#             print(user_info_df)
#             get_cl_data(user_to_search,threshold-5)
#     else:
#         return "No user Found"
    
    

        
# if __name__=="__main__":
#     data=getUserName('<https://www.google.com/search?q=%22ShivBharat-_Yadav00220%22|ShivBharat Yadav>')
#     print(data)


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
        channel_id=payload['channel']
        user_id=payload['user']
        user_message=payload['text']
        ts=payload['ts']
        if (BOT_ID != user_id):
            if 'thread_ts' not in payload:
                user_name=getUserName(user_message)
                if user_message != "No User Name found":
                    print(user_name)
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
