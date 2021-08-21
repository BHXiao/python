import requests
import json
import os
import time
import re

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}
string = input('请输入分享链接：')

shroturl = re.findall('[a-z]+://[\S]+', string, re.I | re.M)[0]
print(shroturl)
startpage = requests.get(url=shroturl, headers=headers, allow_redirects=False)
location = startpage.headers['location']
sec_uid = re.findall('(?<=sec_uid=)[a-zA-Z，0-9, _, -]+', location, re.M | re.I)[0]
getname = requests.get(url='https://www.iesdouyin.com/web/api/v2/user/info/?sec_uid={}'.format(sec_uid),
                       headers=headers).text
userinfo = json.loads(getname)
name = userinfo['user_info']['nickname']
print(userinfo['user_info']['nickname'])
Path = name
if os.path.exists(path=Path) == False:
    os.mkdir(path=Path)
else:
    print('directory exist')
os.chdir(path=Path)

year = ('2018', '2019', '2020', '2021')
month = ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12')
timepool = [x + '-' + y + '-01 00:00:00' for x in year for y in month]
print(timepool)
k = len(timepool)
for i in range(k):
    if i < k - 1:
        print('begintime=' + timepool[i])
        print('endtime=' + timepool[i + 1])
        beginarray = time.strptime(timepool[i], "%Y-%m-%d %H:%M:%S")
        endarray = time.strptime(timepool[i + 1], "%Y-%m-%d %H:%M:%S")
        t1 = int(time.mktime(beginarray) * 1000)
        t2 = int(time.mktime(endarray) * 1000)
        print(t1, t2)

        params = {
            'sec_uid': sec_uid,
            'count': 200,
            'min_cursor': t1,
            'max_cursor': t2,
            'aid': 1128,
            '_signature': 'PtCNCgAAXljWCq93QOKsFT7QjR'}
        awemeurl = 'https://www.iesdouyin.com/web/api/v2/aweme/post/?'
        awemehtml = requests.get(url=awemeurl, params=params, headers=headers).text
        data = json.loads(awemehtml)
        # print(data)
        # print(type(data))
        awemenum = len(data['aweme_list'])
        print(awemenum)
        for i in range(awemenum):
            videotitle = data['aweme_list'][i]['desc'].replace("?", "").replace("\"", "").replace(":", "")
            videourl = data['aweme_list'][i]['video']['play_addr']['url_list'][0]
            start = time.time()
            print('{} ===>downloading'.format(videotitle))
            with open(videotitle + '.mp4', 'wb') as v:
                try:
                    v.write(requests.get(url=videourl, headers=headers).content)
                    end = time.time()
                    cost = end - start
                    print('{} ===>downloaded ===>cost {}s'.format(videotitle, cost))
                except Exception as e:
                    print('download error')
