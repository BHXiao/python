import requests

url = 'https://www.baidu.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'
}

response = requests.get(url, headers=headers)
print(response.cookies)
# <RequestsCookieJar[<Cookie BAIDUID=FD7B4714E2C4E54DD4FF7EF93D086B0B:FG=1 for .baidu.com/>, <Cookie BIDUPSID=FD7B4714E2C4E54D3DEEA747F7D66452 for .baidu.com/>, <Cookie H_PS_PSSID= for .baidu.com/>, <Cookie PSTM=1621672745 for .baidu.com/>, <Cookie BDSVRTM=0 for www.baidu.com/>, <Cookie BD_HOME=1 for www.baidu.com/>]>

print(type(response.cookies))
# <class 'requests.cookies.RequestsCookieJar'>
# 使用方法从CookieJar中提取数据
ccookies = requests.utils.dict_from_cookiejar(response.cookies)
print(ccookies)



