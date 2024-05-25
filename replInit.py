""" blassian replInit 
put stuff in here you want to use in the REPL.
In the REPL, import this as:

from replInit import *

"""

import os 
import requests 


atl_user = os.getenv("ATLASSIAN_USER") 
atl_pwd = os.getenv("ATLASSIAN_PWD")
atl_token = os.getenv("ATLASSIAN_API_TOKEN")
atl_base_url = os.getenv("ATLASSIAN_BASE_URL")
atl_api_url = os.getenv("ATLASSIAN_API_URL")
atl_rest_url = f"{atl_base_url}{atl_api_url}"
atl_creds = (atl_user, atl_token)

def print_atl_creds():
    print(f"user: {atl_user}, pws len: {len(atl_pwd)}, token len: {len(atl_token)}, rest url: {atl_rest_url}")

def get_resource(resource_id:str):
    return requests.get(atl_rest_url + resource_id,auth=atl_creds)
