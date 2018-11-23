import requests,ddt,json
import numpy
import logging.config
import logging
import time
# pip install pyecharts-snapshot
# need SetUp phantomjs[.log,too much info]

logging.basicConfig(
    level = logging.DEBUG,
    filename = "logging.log",
    format = '[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',
    datefmt = '%Y-%m-%d %H:%M:%S',
    filemode = 'a')




def get_data():
    file = open('write_txt.txt','r')
    js = file.read()
    data = json.loads(js)#read
    api_url = "https://fundhdtest.eastmoney.com/ztapicmsapi2/shichang/Zan"
    return data,api_url

data,url = get_data()
suc = 0
fal = 0

def apidata_count(data,url,suc,fal):
    for data_lins in data:
    #m=self.beij()
        usernames,codes = data_lins
        pdata = requests.request("get",url,params=usernames)
        pdata = json.loads(pdata.text)
    # print(pdata)
        if pdata["errorCode"] == codes["errorCode"]:
            suc = suc + 1
        else:
            print(pdata["errorMessage"])
            fal = fal +1
            logging.error("test%s is error"%(suc))
    return suc,fal
from pyecharts import Pie
import random
def proportion_image():
    x,y = apidata_count(data,url,suc,fal)
    attr = ["SUCCESS","FAILED"]
    attr_ydata = []
    attr_ydata.append(x)
    attr_ydata.append(y)
    print(attr_ydata)
    pie = Pie("PIE EXAMPLE",width=1000,height=600)
    pie.add(
        "ZPY",
        attr,
        attr_ydata,
        radius=[50,55],
        center=[25,50],
        is_random=True,
    )
    pie.add(
        "ZPY",
        attr,
        attr_ydata,
        radius=[0,45],
        center=[25,50],
        rosetype="area",
    )
    pie.render("./pie_TEST.html")

proportion_image()







