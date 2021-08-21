import requests


url = '  登陆接口 '
headers = {

}
data = {
    '账号': '',
    '密码': ''
}
session = requests.session()
session.post('登陆', headers=headers, data=data)    #  登陆后会将cookies保存在里面  登陆url获取：1.勾选preserve log  2.
session.get('首页')
# cookies=''
# cookies_list = cookies.split(': ')   分割   以参数代入   for   生成字典
# cookies = {}
response = requests.get(url, headers=headers, cookies=cookies)
print(response.status_code)
with open('re.html', 'w', encoding='utf-8') as f:
    f.write(response.content.decode())



