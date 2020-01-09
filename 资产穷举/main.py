#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import sys
import os

def get(fund,p,dic):
	lastContent = last(fund)
	flag = False
	with open(dic,'r') as f:
		for line in f.read().splitlines():
			domain = p+'://'+line+'.'+fund
			if flag == False and lastContent != '' and domain != lastContent:
				continue
			elif lastContent != '' and domain == lastContent:
				flag = True
				continue
			if lastContent == '':
				flag = True
			if flag == True:
				print(domain)
				try:
					req = requests.get(domain,timeout=3)
					if req.status_code == 200:
						with open(fund+'.txt','a') as w:
							w.write(domain + '\n')
				except Exception:
					pass
				else:
					continue
				
def last(fund):
	content = ''
	if os.path.exists(fund+'.txt') == False:
		return content
	with open(fund+'.txt','r') as f:
		for line in f.read().splitlines():
			content = line
	return content		

if __name__ == '__main__':
	print('正在爬取'+sys.argv[1]+'的资产')
	get(sys.argv[1],sys.argv[2],sys.argv[3])