# -*- coding: utf-8 -*-
import requests
from urllib.parse import unquote

keyword = unquote("水泵")
querystrings = {"key":keyword}

url = "https://www.tianyancha.com/search"

querystring = {"key":"%E6%9C%BA%E6%A2%B0"}

headers = {
    'Connection': "keep-alive",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36",
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'Referer': "https://www.tianyancha.com/",
    'Cookie': "aliyungf_tc=AQAAAJjwaF7LLwAAqrRBfAPWX0uTmDSG; ssuid=8334847722; bannerFlag=undefined; csrfToken=nF0ipE6f9uElIkOlx5Cfpt2y; TYCID=8bc67a1080e411e99aa353d434f18823; undefined=8bc67a1080e411e99aa353d434f18823; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1559005471; _ga=GA1.2.1662694729.1559005471; _gid=GA1.2.165883547.1559005471; _gat_gtag_UA_123487620_1=1; tyc-user-info=%257B%2522claimEditPoint%2522%253A%25220%2522%252C%2522myAnswerCount%2522%253A%25220%2522%252C%2522myQuestionCount%2522%253A%25220%2522%252C%2522signUp%2522%253A%25220%2522%252C%2522explainPoint%2522%253A%25220%2522%252C%2522privateMessagePointWeb%2522%253A%25220%2522%252C%2522nickname%2522%253A%2522%25E9%25BB%2584%25E8%25B1%2586%25E8%25B1%2586%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522privateMessagePoint%2522%253A%25220%2522%252C%2522state%2522%253A%25220%2522%252C%2522announcementPoint%2522%253A%25220%2522%252C%2522isClaim%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522discussCommendCount%2522%253A%25220%2522%252C%2522monitorUnreadCount%2522%253A%2522268%2522%252C%2522onum%2522%253A%25220%2522%252C%2522claimPoint%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODEzNzc5MTgxMyIsImlhdCI6MTU1OTAwNTQ4OCwiZXhwIjoxNTkwNTQxNDg4fQ.1Og9H1HhHeHhr6pHvbsmn2RVGhaHQDtIDCv43UaR4ljgIzvHMR1hMtLxoBpWRGqKiRrmxAZg6fm4w1-LWDs0Sw%2522%252C%2522pleaseAnswerCount%2522%253A%25220%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522bizCardUnread%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252218137791813%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODEzNzc5MTgxMyIsImlhdCI6MTU1OTAwNTQ4OCwiZXhwIjoxNTkwNTQxNDg4fQ.1Og9H1HhHeHhr6pHvbsmn2RVGhaHQDtIDCv43UaR4ljgIzvHMR1hMtLxoBpWRGqKiRrmxAZg6fm4w1-LWDs0Sw; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1559005497",
    'Host': "www.tianyancha.com",
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, headers=headers, params=querystring,verify=False)

print(response.content)