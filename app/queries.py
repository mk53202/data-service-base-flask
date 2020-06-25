SQL_BASIC_SELECT='''
select * from device_up limit 10;
'''

SQL_BASIC_SELECT_WITH_TIME='''
select id, received_at, device_name, application_name, data, rx_info, object
from device_up
where (received_at > now() - interval '2 days') and (device_name = 'lora-app-node');
'''

# SQL_BASIC_SELECT_TO_JSON='''
# with t as (
# 	select * from device_up
# )
# select json_agg(t) from t;
# '''
