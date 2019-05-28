import requests

url = "https://www.qichacha.com/search"

# querystring = {"key":"%E6%B0%B4%E6%B3%B5"}
querystring = {"key":"机械"}

headers = {
    'Connection': "keep-alive",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36",
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'Referer': "https://www.qichacha.com/",
    'Cookie': "QCCSESSID=fbep92gvm62i4qrea4fp8hcrq4; "
              # "zg_did=%7B%22did%22%3A%20%2216afbe8726648c-05d771f02835eb-1333063-1fa400-16afbe8726843c%22%7D; "
              # "UM_distinctid=16afbe8728f303-0450a7f5fc30bf-1333063-1fa400-16afbe872905c3; "
              # "CNZZDATA1254842228=402823618-1559001498-https%253A%252F%252Fwww.baidu.com%252F%7C1559001498; "
              # "Hm_lvt_3456bee468c83cc63fb5147f119f1075=1559004476; hasShow=1; "
              # "_uab_collina=155900447626490191988896; "
              "acw_tc=6548caa115590044756263794e3d1c32179161c976f4d9a1c0288c84f2; ",
              # "Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1559004488; "
              # "zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201559004476014%2C%22updated%22%3A%201559004583969%2C%22info%22%3A%201559004476019%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.baidu.com%22%2C%22cuid%22%3A%20%225c5aa4d298c56a5e55bbf7ca7208cf14%22%7D",
    'Host': "www.qichacha.com",
    # 'cache-control': "no-cache"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)