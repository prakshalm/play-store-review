
import logging
import pandas as pd
import numpy as np
from thefuzz import fuzz
import re
logger = logging.getLogger(__name__)

def getUserName(userMessage:str):
    userMessage=userMessage.split(" ")
    for data in userMessage:
        returned_value=re.search(r"<https://www.google.com/search\?q=%22",data,re.IGNORECASE)
        if returned_value:
            userName=returned_value.string
            userName=userName.replace("<https://www.google.com/search?q=%22","")
            userName=userName.replace("+"," ")         
            userName=userName.split('|')
            userName=re.sub('[^A-Za-z ]+', '',userName[0])
            print(userName)

    if userName:        
        return userName
    else:
        return "No user_name detected"
    

def removeDuplicates(lst):
    '''
    Removes Duplicate values and appends the user_id of the entries having same phone number
    '''
    seen = []
    Output = []
    for a, b, c, d in lst:
        if [a,b,c] not in seen:
            seen.append([a,b,c])
            Output.append([a, b, c, d])

    seen = []
    removed_Duplicate = []
    for a, b, c, d in Output:
        if c not in seen:
            seen.append(c)
            removed_Duplicate.append([a, b, c, d])
        else:
            index=seen.index(c)
            removed_Duplicate[index][1]=str(removed_Duplicate[index][1])+','+str(b)
            
    return removed_Duplicate


# FOR CX
def get_cx_data(user_to_search:str,threshold=95):
    if threshold>=80:
        logger.info('Searching in cx.csv')
        df=pd.read_csv('./operations/data_cx.csv',skiprows=1)
        length=df.shape[0]
        user_info=list()
        for i in range(length):
            if(fuzz.ratio(str(df['user_name'][i]).lower(),user_to_search.lower())>threshold):
                user_info.append((df['user_name'][i],df['user_id'][i],df['user_phone'][i],df['processing_at'][i]))
        user_info=removeDuplicates(user_info)
        user_info_df=pd.DataFrame(user_info)
        user_info_df.rename(columns = {0:'Name',1:'user_id',2:'phone_number',3:'Processing At'}, inplace = True)
        if user_info_df.shape[0]>=1:
            user_info_df=user_info_df.sort_values(by=['Processing At']).head(11)
            user_info_df.drop("Processing At",axis=1,inplace=True)
            user_info_df.reset_index(drop=True, inplace=True)
            logger.info('Searched in cx.csv')
            print(user_info_df)
            return user_info_df
        else:
            print(user_info_df)
            res=get_cx_data(user_to_search,threshold-5)
            return res
    else:
        return "No user Found"


# FOR CL
def get_cl_data(user_to_search:str,threshold=95):
    if(threshold>=80):
        logger.info('Searching in cl.csv')
        df=pd.read_csv('./operations/data_cl.csv',skiprows=1)
        length=df.shape[0]
        user_info=list()
        for i in range(length):
            if(fuzz.ratio(str(df['name'][i]).lower(),user_to_search.lower())>threshold):
                user_info.append((df['name'][i],df['user_id'][i],df['phone_number'][i],df['processing_at'][i]))
        user_info=removeDuplicates(user_info)
        user_info_df=pd.DataFrame(user_info)
        user_info_df.rename(columns = {0:'Name',1:'user_id',2:'phone_number',3:'Processing At'}, inplace = True)
        if user_info_df.shape[0]>=1:
            user_info_df=user_info_df.sort_values(by=['Processing At']).head(11)
            user_info_df= user_info_df.drop("Processing At",axis=1)
            user_info_df.reset_index(drop=True, inplace=True)
            logger.info('Searched in cl.csv')
            print(user_info_df)
            return user_info_df
        else:
            print(user_info_df)
            res=get_cl_data(user_to_search,threshold-5)
            return res
    else:
        return "No user Found"