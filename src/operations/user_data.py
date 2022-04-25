
import pandas as pd
import numpy as np
from thefuzz import fuzz
import re

from src.slackbot import user_details

def getUserName(userMessage:str):
    userMessage=userMessage.split(" ")
    print(userMessage)
    for data in userMessage:
        returned_value=re.search(r"<https://www.google.com/search\?q=%22",data,re.IGNORECASE)
        if returned_value:
            userName=returned_value.string
            userName=userName.replace("<https://www.google.com/search?q=%22","")
            userName=userName.replace("+"," ")
            userName=userName.replace("%22","")
            userName=userName.replace("|"," ")
            userName=userName.split(" ")
            userName=userName.replace("_"," ") 
            userName=userName.replace("-"," ")
            userName = ''.join([i for i in userName if not i.isdigit()])
            userName=str(userName[0]+" "+userName[1])
            print(userName)
            return userName
    return "No User Found"
    

def removeDuplicates(lst):
      
    return list(set([i for i in lst]))

def removeDuplicatesPhone(lst):
    seen = []
    Output = []
    for a, b, c in lst:
        if not c in seen:
            seen.append(c)
            Output.append([a, b, c])
        else:
            index=seen.index(c)
            Output[index][1]=str(Output[index][1])+','+str(b)
            
    return Output

def get_cx_data(user_to_search:str):
    
    df=pd.read_csv('./operations/data_cx.csv',skiprows=1)
    length=df.shape[0]
    df_name=df['user_name']
    user_info=list()
    for i in range(length):
        if(fuzz.ratio(str(df_name[i]).lower(),user_to_search.lower())>80):
            user_info.append((df_name[i],df['user_id'][i],df['user_phone'][i]))
    user_info=removeDuplicates(user_info)
    user_info=removeDuplicatesPhone(user_info)
    user_info_df=pd.DataFrame(user_info)
    user_info_df.rename(columns = {0:'Name',1:'user_id',2:'phone_number'}, inplace = True)
    return user_info_df.to_string()

def get_cl_data(user_to_search:str):
    
    df=pd.read_csv('./operations/data_cl.csv',skiprows=1)
    length=df.shape[0]
    df_name=df['name']
    user_info=list()
    for i in range(length):
        if(fuzz.ratio(str(df_name[i]).lower(),user_to_search.lower())>80):
            user_info.append((df_name[i],df['user_id'][i],df['phone_number'][i]))
    user_info=removeDuplicates(user_info)
    user_info=removeDuplicatesPhone(user_info)
    user_info_df=pd.DataFrame(user_info)
    user_info_df.rename(columns = {0:'Name',1:'user_id',2:'phone_number'}, inplace = True)
    return user_info_df.to_string()