import requests
url = 'https://10.100.100.254:8443'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'
}
response = requests.post(url, verify=False)   #  verify 核实 验证
print(response.status_code)
print(response.content.decode())   # conten 内容   decode  解码 破译      打印出网页代码

