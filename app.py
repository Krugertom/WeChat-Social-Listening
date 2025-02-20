#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import pandas as pd 
import json
import numpy as np

#Key below refers to the Newrank API Key, available in the personal account details 

headers = {'Key': 'NEWRANK ACCOUNT KEY'}

#Wechat account ID available on the account profile page in Weixin

brand_name = np.array(["WECHAT ACCOUNT ID"])

#Date format should be as follows YYYY-MM-DD 00:00:00
#Multiple date ranges are allowed
#Max length of one month

from_dates = np.array(["2022-03-01 00:00:00"])
to_dates = np.array(["2022-04-01 00:00:00"])

all_results = []

for i in range(len(brand_name)):
    for j in range(len(from_dates)):
        data = {
          'account': brand_name[i],
          'from': from_dates[j],
          'to': to_dates[j],
          'page': '1',
          'size': '20'
        }
        print(data)
        
        #URL below is from NEWRANK API

        response = requests.post('https://api.newrank.cn/api/sync/weixin/account/articles', headers=headers, data=data)
        json_data = json.loads(response.text)
        all_results.append(pd.DataFrame(json_data["data"]))
        
        #SPECIFY THE FILE PATH BELOW 

final_results=pd.concat(all_results)
article_data = final_results.set_index('name')
article_data.to_csv("SPECIFIED PATH")
        
        
        
