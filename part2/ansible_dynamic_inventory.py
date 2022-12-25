"""
    Used in ansible to get inventory dynamically

    Inventory.txt to inventory.py
    #Inventory File   -inventory.txt
    db_server ansible_host=192.168.1.1
    web_server ansible_host=192.168.1.2

    N.B: db_server and web_server are group of hosts
"""

#!/usr/bin/env python

#Get inventory data from source - CMDB or any other API
import argparse
import json 


def get_inventory_data():
    return {
        "databases":{
            "hosts": ["db_server"],
            "vars":{
                "ansible_ssh_pass":"Passw0rd", 
                "ansible_ssh_host":"192.160.1.1"
                }
        },
        "web":{
            "hosts": ["web_server"],
            "vars": {
                "ansible_ssh_pass":"Passw0rd", 
                "ansible_ssh_host":"192.160.1.2"}

        }
    }


def read_cli_args():
    global args 
    parser = argparse.ArgumentParser()
    parser.add_argument('--list', action='store_true')
    parser.add_argument('--host', action='store')
    args = parser.parse_args()
#Default main function

if __name__ == "__main__":
    global args 
    read_cli_args()
    inventory_data = get_inventory_data()
    if args and args.list:
        print(json.dumps(inventory_data))