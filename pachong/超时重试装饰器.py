import requests
from retrying import retry


# @retry
@retry(stop_max_attempt_number=3)
def get_data(url):

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'
    }
    print(11111)
    response = requests.get(url, headers=headers, timeout=5)  # 超时时间
    print(response.status_code)
    return response


def test(url):
    response = get_data(url)
    return response


if __name__ == '__main__':
    url = 'https://www.google.com/'
    test(url)
