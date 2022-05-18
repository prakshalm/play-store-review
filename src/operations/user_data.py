import pandas as pd
import re
from operations.helper import *
from operations.import_modules import *

def getUserName(userMessage:str):
    userMessage=userMessage.split(" ")
    userName=None   
    for data in userMessage:
        returned_value=re.search(r"https://www.google.com/search\?q=%22",data,re.IGNORECASE)
        if returned_value:
            userName=returned_value.string
            userName=userName.replace("https://www.google.com/search?q=%22","")
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
    
def get_cx_data(user_to_search:str,threshold=1):
    if threshold<=2:
        print('Searching For CX')
        user_info_df=get_data_cmdb(
        f"""
        WITH q AS (
            SELECT '{user_to_search}' AS given_name
        )
        SELECT
            DISTINCT ON (o.user_id)
            o.user_id,u.user_name,u.user_phone,o.processing_at
        FROM orders o join tbl_user u on u.user_id=o.user_id, q
        WHERE soundex(u.user_name) = soundex(given_name)
        AND levenshtein(lower(u.user_name),lower(given_name)) <= {threshold} and o.created_at > now() - interval '10 days';
        """
        )
        if user_info_df.shape[0]>=1:
            print(user_info_df)
            user_info_df=pd.DataFrame(removeDuplicates(user_info_df.values.tolist()))
            user_info_df.rename(columns = {0:'Name',1:'user_id',2:'phone_number',3:'processing_at'}, inplace = True)
            user_info_df=user_info_df.sort_values(by=['processing_at']).head(11)
            user_info_df= user_info_df.drop("processing_at",axis=1)
            user_info_df.reset_index(drop=True, inplace=True)
            print(user_info_df)
            return user_info_df
        else:
            print(user_info_df)
            res=get_cx_data(user_to_search,threshold+1)
            return res
        
    elif(len(user_to_search)>1):
        user_to_search=user_to_search.split(" ")
        print('''Searching CX's First Name''')
        user_info_df=get_data_cmdb(
        f"""
        WITH q AS (
            SELECT '{user_to_search[0]}' AS given_name
        )
        SELECT
            DISTINCT ON (o.user_id)
            o.user_id,u.user_name,u.user_phone,o.processing_at
        FROM orders o join tbl_user u on u.user_id=o.user_id, q
        WHERE soundex(u.user_name) = soundex(given_name)
        AND levenshtein(lower(u.user_name),lower(given_name)) <= 1 and o.created_at > now() - interval '10 days';
        """
        )
        if user_info_df.shape[0]>=1:
            user_info_df=pd.DataFrame(removeDuplicates(user_info_df.values.tolist()))
            user_info_df.rename(columns = {0:'Name',1:'user_id',2:'phone_number',3:'processing_at'}, inplace = True)
            user_info_df=user_info_df.sort_values(by=['processing_at']).head(11)
            user_info_df= user_info_df.drop("processing_at",axis=1)
            user_info_df.reset_index(drop=True, inplace=True)
            print(user_info_df)
            return user_info_df
        else:
            return "No User Found"
    else:
        return "No user Found"

# FOR CL
def get_cl_data(user_to_search:str,threshold=1):
    if threshold<=2:
        print('Searching For CL')
        user_info_df=get_data_cmdb(
        f"""
        WITH q AS (
            SELECT '{user_to_search}' AS given_name
        )
        SELECT
            DISTINCT ON (o.user_id)
            o.user_id, tl.name, tl.phone_number, o.processing_at
        FROM orders o join team_leaders tl on tl.id = o.team_leader, q
        WHERE soundex(tl.name) = soundex(given_name)
        AND levenshtein(lower(tl.name),lower(given_name)) <= {threshold} and o.created_at > now() - interval '10 days';
        """
        )
        if user_info_df.shape[0]>=1:
            print(user_info_df)
            user_info_df=pd.DataFrame(removeDuplicates(user_info_df.values.tolist()))
            user_info_df.rename(columns = {0:'Name',1:'user_id',2:'phone_number',3:'processing_at'}, inplace = True)
            user_info_df=user_info_df.sort_values(by=['processing_at']).head(11)
            user_info_df= user_info_df.drop("processing_at",axis=1)
            user_info_df.reset_index(drop=True, inplace=True)
            print(user_info_df)
            return user_info_df
        else:
            print(user_info_df)
            res=get_cx_data(user_to_search,threshold+1)
            return res
        
    elif(len(user_to_search)>1):
        user_to_search=user_to_search.split(" ")
        print('''Searching CL's First Name''')
        user_info_df=get_data_cmdb(
        f"""
        WITH q AS (
            SELECT '{user_to_search[0]}' AS given_name
        )
        SELECT
            DISTINCT ON (o.user_id)
            o.user_id, tl.name, tl.phone_number, o.processing_at
        FROM orders o join team_leaders tl on tl.id = o.team_leader, q
        WHERE soundex(tl.name) = soundex(given_name)
        AND levenshtein(lower(tl.name),lower(given_name)) <= 1 and o.created_at > now() - interval '10 days';
        """
        )
        if user_info_df.shape[0]>=1:
            user_info_df=pd.DataFrame(removeDuplicates(user_info_df.values.tolist()))
            user_info_df.rename(columns = {0:'Name',1:'user_id',2:'phone_number',3:'processing_at'}, inplace = True)
            user_info_df=user_info_df.sort_values(by=['processing_at']).head(11)
            user_info_df= user_info_df.drop("processing_at",axis=1)
            user_info_df.reset_index(drop=True, inplace=True)
            print(user_info_df)
            return user_info_df
        else:
            return "No User Found"
    else:
        return "No user Found"
