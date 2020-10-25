#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Author  : B1ueB0ne
# @File    : getorgdomain.py
# 通过网站备案信息获取同组织下的domain

import json
import sys
import requests
#from requests_html import HTML,HTMLSession

key = "xxxxxxxxxxxxxxx"
# 在此处配置key


class GetOrgDomain(object):

    def __init__(self, target_domain):
       self.target_domain =  target_domain

    def get_organization_name(self):
        tURL = "http://apidata.chinaz.com/CallAPI/NewDomain?key={}&domainName={}".format(key, self.target_domain)
        r = requests.get(tURL)
        organization_name =json.loads(r.text)["Result"]["CompanyName"]
        '''
        session = HTMLSession()
        tURL = "http://icp.chinaz.com/" + target_domain
        r = session.get(tURL)
        organization_name = r.html.xpath("//li[@class='bg-gray clearfix']/p/a/text()",first=True, _encoding="utf-8")
        print(organization_name)
        '''
        return organization_name

    def get_organization_domains(self):
        organization_name = self.get_organization_name()
        tURL = "http://apidata.chinaz.com/CallAPI/SponsorUnit?key={}&companyName={}".format(key, organization_name)
        r = requests.get(tURL)
        organization_domains_list =json.loads(r.text)
        return organization_domains_list    

if __name__ == '__main__':
    target_domain = sys.argv[1]
    print(target_domain)
    getOrgDomain = GetOrgDomain(target_domain)
    organization_domains_list = getOrgDomain.get_organization_domains()
    print(organization_domains_list)