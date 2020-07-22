import requests
import time
import threading
import gc
def start(url,extra_data,num):
    count=0
    while(count<num):
        sent(url,extra_data)
        count+=1
        time.sleep(1)
        print(count)
def sent(url,extra_data):
    #url="https://h5.guang.com/live/room/info.json?id=410821&idList=400303,411248,411001,405541,409786&neighbourRooms=410821,411248&enterSource=swipe&heartbeatMode=1&kdt_id=42806924&guangBusinessId=43748795&access_token=5e3000f435133f28bf5cd4cbd8b8e373"
    #url="https://h5.guang.com/live/room/info.json?id=425135&idList=400864,430193,428792,400717,422179,430945&neighbourRooms=430193,425135&enterSource=swipe&heartbeatMode=1&kdt_id=45616145&guangBusinessId=43750507&access_token=f134f6f94d963c2b9d12727b6f0182e7"
    #param={'signature':'asdas','timestamp':'154967561','nonce':'5213210','echostr':'hello world'}
    #headers = {'Extra-Data': '{"is_weapp":1,"sid":"YZ720687777729302528YZjVesyYIV","guangSid":"7206877776754442242sieF1zu","version":"2.15.7-a"}', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat','content-type':'application/json'}
    headers = {'Extra-Data': extra_data, 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat','content-type':'application/json'}
    requests.packages.urllib3.disable_warnings()
    s = requests.session()
    s.keep_alive = False
    print("开始发送请求")
    with requests.get(url,headers=headers,verify=False,timeout=5) as r:
        r.encoding='utf-8'
        html=r.text
        r.close()
        del(r,html)
        gc.collect()
    del(headers,s)
    gc.collect()
    print("请求发送完成")


if __name__ == "__main__":
    threadNum=input("开启线程数(1~10):\r\n")
    num = input("次数:\r\n")
    url = input("输入请求url:\r\n")
    extra_data=input("请输入extra_data:\r\n")
    for i in range(0,int(threadNum)):
        th=threading.Thread(target=start,args=(url,extra_data,int(num)))
        th.start()
        print("开启线程:"+str(i))
