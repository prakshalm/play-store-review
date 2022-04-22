#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3.9
import sys
sys.path.append('/home/ubuntu/prakshal_mehra')
from helper import *
from import_modules import *
from datetime import datetime
import csv

def get_userData():
    df_cx=get_data_cmdb(
        """
        select 
        o.user_id, u.user_name, u.user_phone, o.order_status
        from orders o join tbl_user u on u.user_id = o.user_id 
        where o.processing_at > now() - interval '1 days';
        """
       
    )
    print("Writing data in data_cx.csv")
    time=list()
    current_time=str(datetime.now())
    time.append(current_time)
    
    with open('data_cx.csv','w') as f:
        writer = csv.writer(f)
        writer.writerow(time)
        f.close()
    df_cx.to_csv('data_cx.csv', mode='a', index=False, header=True)
        
    df_cl=get_data_cmdb(
        """
        select
        o.user_id, tl.name, tl.phone_number, o.order_status 
        from orders o join team_leaders tl on tl.id = o.team_leader 
        where o.processing_at > now() - interval '1 days';
        """
    )
    print("Writing data in data_cl.csv")
    
    with open('data_cl.csv','w') as f:
        writer = csv.writer(f)
        writer.writerow(time)
        f.close()
    df_cl.to_csv('data_cl.csv', mode='a', index=False, header=True)
 
if __name__=='__main__':
    get_userData()