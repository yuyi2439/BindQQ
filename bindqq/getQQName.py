import requests
from requests.packages import urllib3
import json

def GetQQName(QQnum):
    urllib3.disable_warnings()
    req = requests.get('https://r.qzone.qq.com/fcg-bin/cgi_get_portrait.fcg?uins='+QQnum,verify=False)
    str = req.content.decode('gbk')
    reg_json = json.loads(str[17:-1])
    QQName = reg_json[QQnum][6]
    return(QQName)