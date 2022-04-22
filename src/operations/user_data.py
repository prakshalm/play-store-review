
import pandas as pd
import numpy as np
from thefuzz import fuzz

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
    
    df=pd.read_csv('data_cx.csv',skiprows=1)
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
    return user_info_df

def get_cl_data(user_to_search:str):
    
    df=pd.read_csv('data_cl.csv',skiprows=1)
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
    return user_info_df
