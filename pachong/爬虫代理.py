import requests


url = 'https://www.medcaptain.com/'

proxies = {
    'https': '58.218.201.74:3274',
    # 'https': 'https://111.179.73.109:3256'   不能复制：ctrl+ shift+i
}

response = requests.get(url, proxies=proxies)
print(response.status_code)






