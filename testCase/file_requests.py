# -*- coding: utf-8 -*-
import time
import sys
import urllib
import requests
from testCase import file_util
import xlwt
import re
from xlrd import open_workbook

from xlutils.copy import copy
import os
from bs4 import BeautifulSoup

"""
一个账号只能查询100条，所以应该需要多个账号的源进行轮流查询




"""


rownum=1
def main(keyword):
    global rownum

    excel_path = os.path.dirname(os.path.abspath('.')) + '/testFile/result.xls'
    if not os.path.exists(excel_path):
        os.makedirs(excel_path)


    # 覆盖保存
    # book=xlwt.Workbook(encoding='gbk')
    # sheet=book.add_sheet('结果',cell_overwrite_ok=True)
    # 不覆盖保存
    book = open_workbook(excel_path)
    wb = copy(book)
    ws = wb.get_sheet('Sheet1')



    headers ={'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
             'Accept-Encoding':'gzip, deflate, br',
             'Accept-Language':'zh-CN,zh;q=0.9',
             'Cache-Control':'no-cache',
             'Connection':'keep-alive',
             'Host':'www.tianyancha.com',
             'Pragma':'no-cache',
              "Cookie":"ssuid=2560953996; TYCID=961361e079cd11e98d29c5003a75a1ca; undefined=961361e079cd11e98d29c5003a75a1ca; _ga=GA1.2.147424696.1558225951; aliyungf_tc=AQAAAGjE2x4TjA4AAANZceQwwtCR4cNA; bannerFlag=undefined; csrfToken=GsREV9iHzr9ZwDzabSCSepkM; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1558225951,1558232846,1558232910,1558957799; _gid=GA1.2.1140218349.1558957800; token=cc53e3ddff3642c39c745d5da85a73f4; _utm=739d7aae457c442ba7dd792c3fc9601f; tyc-user-info=%257B%2522claimEditPoint%2522%253A%25220%2522%252C%2522myAnswerCount%2522%253A%25220%2522%252C%2522myQuestionCount%2522%253A%25220%2522%252C%2522signUp%2522%253A%25220%2522%252C%2522explainPoint%2522%253A%25220%2522%252C%2522privateMessagePointWeb%2522%253A%25220%2522%252C%2522nickname%2522%253A%2522%25E8%2594%25BA%25E7%259B%25B8%25E5%25A6%2582%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522privateMessagePoint%2522%253A%25220%2522%252C%2522state%2522%253A%25220%2522%252C%2522announcementPoint%2522%253A%25220%2522%252C%2522isClaim%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522discussCommendCount%2522%253A%25220%2522%252C%2522monitorUnreadCount%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522claimPoint%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNTA3NDcwOTEzNCIsImlhdCI6MTU1ODk1ODA0OCwiZXhwIjoxNTkwNDk0MDQ4fQ.DjxRsfIKlNXfgQKz02yq9-iLklxJ7oQ1sPNtCvwv6CTf3d__jiMyEWxlHBl1nihnjw6C80GCG3m5qYwVwQInSw%2522%252C%2522pleaseAnswerCount%2522%253A%25220%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522bizCardUnread%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252215074709134%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNTA3NDcwOTEzNCIsImlhdCI6MTU1ODk1ODA0OCwiZXhwIjoxNTkwNDk0MDQ4fQ.DjxRsfIKlNXfgQKz02yq9-iLklxJ7oQ1sPNtCvwv6CTf3d__jiMyEWxlHBl1nihnjw6C80GCG3m5qYwVwQInSw; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1558958053",
             'Upgrade-Insecure-Requests':'1',
             'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
              "token":'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNTA3NDcwOTEzNCIsImlhdCI6MTU1ODMzNzY1NiwiZXhwIjoxNTg5ODczNjU2fQ.BGbzr3J8Z4sKbK9x72zuSjkPwRnS3Dke3xhr54bWi3NI6QEtp3FI9FjsOygMwJ6Q-tnIF8VYYzf4uXyVqGIhtw'
             }

    for page in range(1,2):
        # startUrl = 'https://www.tianyancha.com/search?key=%s&checkFrom=searchBox' % keyword  # urllib.quote(keyword)
        startUrl= 'https://www.tianyancha.com/search/?key={}'.format(keyword)
        resultPage = requests.get(startUrl, headers=headers,verify=False) # 在请求中设定头，cookie
        resultPage.encoding = resultPage.apparent_encoding
        print(resultPage.content)
        # ls = BeautifulSoup(resultPage.content, "html.parser")
        # tag_soup = ls.findAll(class_='content')
        # print(tag_soup.get_text())


        # reponse=re.findall('<div class="content"><div class="header">(.*?)<span class="site">',resultPage.text,re.S)
        res = re.findall(r'<div class="logo -w88".*?<em>(.*?)</em>.*?href="(.*?)"[\s\S]*?title="(.*?)".*?电话：</span><span ><span>(.*?)<.*?邮箱.*?<span.*?>(.*?)</span>', resultPage.text, re.S)

        # for i in reponse:
        #     print(i)
        head=['公司名','链接','法人','电话','邮箱']
        for q in range(len(head)):
            ws.write(0,q,head[q])
        if res != []:
            for j in range(len(res[0])):
                ws.write(rownum, j, res[0][j])
            rownum += 1
            wb.save(excel_path)

        # for i in reponse:
        #     # res=re.findall('<a class="name.*?href="(.*?)".*?>(.*?)</a.*?法定代表人>*?>(.*?)<.*?class="link-hover-click">(.*?)<.*?class="link-hover-click">(.*?)<',str(i),re.S)
        #     # res = re.findall(r'<div class="logo -w88".*?<em>(.*?)</em>.*?href="(.*?)"[\s\S]*?title="(.*?)".*?电话.*?<span.*?>(.*?)<.*?邮箱.*?<span.*?>(.*?)</span>',str(i), re.S)
        #     # for i in res:
        #     #     print(i)




        time.sleep(10)






if __name__ == '__main__':


    keyword = 'Beijing Mingtai Yanshen Technology Co., Ltd.'

    main(keyword)