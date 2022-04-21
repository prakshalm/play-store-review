import sys
sys.path.append('/home/ubuntu/prakshal_mehra')
from helper import *
from import_modules import *
from thefuzz import fuzz

def get_userData():
    df_cx=get_data_cmdb(
        """
        select 
        o.user_id, u.user_name, u.user_phone, o.order_status
        from orders o join tbl_user u on u.user_id = o.user_id 
        where o.processing_at > now() - interval '10 days';
        """
    )
    df_cx.to_csv('data_cx.csv',index=False)

    df_cl=get_data_cmdb(
        """
        select
        o.user_id, tl.name, tl.phone_number, o.order_status 
        from orders o join team_leaders tl on tl.id = o.team_leader 
        where o.processing_at > now() - interval '10 days';
        """
    )
    df_cl.to_csv('data_cl.csv',index=False)
 
if __name__=='__main__':
    get_userData()