import json

import requests
import jsonpath
# url = 'https://www.lagou.com/wafcheck.json'
url = 'https://www.lagou.com/lbs/getALLCitySearchLavels.json'
# headers = 'Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)'
headers = {
    'User-Agent': 'Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)'
}
proxies = {
        'https': '117.57.100.107:4213',
        # 'https': '111.179.73.109:3256'   # 不能复制：ctrl+ shift+i
    }
# 获取数据
response = requests.get(url, headers=headers, proxies=proxies)
tiqu_date = response.content.decode()
print(tiqu_date)
# 把数据转成字典
zhang_date = json.loads(tiqu_date)
# 提取数据
print(jsonpath.jsonpath(zhang_date, '$..b..name'))

