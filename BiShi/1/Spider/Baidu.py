import re
import requests
import json
import pandas as pd

url='https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_aladin_banner'

response = requests.get(url)
#print(response.text)
data_html =  response.text
json_str=re.findall('"component":\[(.*)\],',data_html)[0]
json_dict = json.loads(json_str)#字符串转为字典
caseList=json_dict['caseList']
data_set=[]

for case in caseList:
    data_dict={}
    data_dict['省份']=case['area']
    data_dict['新增确诊']=case['confirmedRelative']
    data_dict['现有确诊']=case['curConfirm']
    data_dict['累计确诊']=case['confirmed']
    data_dict['累计治愈']=case['crued']
    data_dict['累计死亡']=case['died']
    data_set.append(data_dict)
    print(data_dict)#检查
    df=pd.DataFrame(data_set)
    df.to_csv('data.csv') #如用Excel打开csv文件需将编码改为ANSI，如用utf-8会在Excel中乱码