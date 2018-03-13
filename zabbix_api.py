#!/usr/bin/env python3

import requests
import json

headers = {'Content-Type': 'application/json'}

class zabbix_api(object):

    def __init__(self,url,user,password):
        self.url=url
        self.user=user
        self.password=password

    def get_token(self):
        text={"jsonrpc": "2.0","method": "user.login","params": {"user": self.user,"password": self.password},"id": 1}
        data=requests.post(self.url,data=json.dumps(text),headers=headers).json()
        return data['result']

    def get_host(self):
        token=self.get_token()
        text={"jsonrpc": "2.0","method": "host.get","params": {"output": ["hostid","host"],"selectInterfaces": ["interfaceid","ip"]},"id": 2,"auth": token}
        data=requests.post(url=self.url,data=json.dumps(text),headers=headers).json()
        return data


if __name__ == '__main__':
    url="http://zabbix.aityp.com/api_jsonrpc.php"
    app=zabbix_api(url,'admin','zabbix')
    data=app.get_host()
    print(data)
