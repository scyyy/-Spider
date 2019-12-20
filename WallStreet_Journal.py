from bs4 import BeautifulSoup
import requests
import time
from tqdm import tqdm
import requests
import xlwt,xlrd
from xlutils.copy import copy
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

string1 = 'china'
string2 = 'chinese'
string3 = 'Beijing'
string4 = 'huawei'

options = webdriver.ChromeOptions()
options.add_argument('User-Agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3","Accept-Encoding":"gzip","Accept-Language":"zh-CN,zh;q=0.9","Cache-Control":"max-age=30","Upgrade-Insecure-Requests":"1')
prefs={'profile.default_content_setting_values': {'images': 2}}
options.add_experimental_option('prefs',prefs)
browser = webdriver.Chrome('/Users/scy/Desktop/Python/Davos/chromedriver',options=options)
browser.get('https://www.wsj.com/search/term.html?KEYWORDS=Davos&min-date=2009/01/01&max-date=2019/12/13&isAdvanced=true&daysback=1y&meta=China&andor=AND&sort=date-desc&ns=prod/accounts-wsj&page=12')
Sign_in = browser.find_element_by_xpath('//*[@id="full-header"]/div/div/div/header/div[1]/div/div[1]/div/a[2]')
browser.execute_script("arguments[0].click();",Sign_in)
browser.find_element_by_id("username").clear()
browser.find_element_by_id("username").send_keys("jianyangsong1998@163.com")
browser.find_element_by_id("password").clear()
browser.find_element_by_id("password").send_keys("19980530HUhu")
Next = browser.find_element_by_xpath('//*[@id="basic-login"]/div[1]/form/div/div[6]/div[1]/button')
browser.execute_script("arguments[0].click();",Next)
time.sleep(5)
Continue = browser.find_element_by_xpath('//*[@id="email-verification"]/div/div[2]/div/div[2]/div/div/button[2]')
browser.execute_script("arguments[0].click();",Continue)
# cookies = browser.get_cookies()
# print(cookies)

# Cookie = {'domain': 'sso.accounts.dowjones.com', 'expiry': 1732678450, 'httpOnly': False, 'name': 'ki_r', 'path': '/', 'secure': False, 'value': 'aHR0cHM6Ly93d3cud3NqLmNvbS9zZWFyY2gvdGVybS5odG1sP0tFWVdPUkRTPURhdm9zJnBhZ2U9MQ%3D%3D'}, {'domain': 'sso.accounts.dowjones.com', 'expiry': 1732678450, 'httpOnly': False, 'name': 'ki_t', 'path': '/', 'secure': False, 'value': '1574912050531%3B1574912050531%3B1574912050531%3B1%3B1'}, {'domain': '.dowjones.com', 'httpOnly': False, 'name': 's_sq', 'path': '/', 'secure': False, 'value': 'djglobal%3D%2526c.%2526a.%2526activitymap.%2526page%253DWSJ_Login_Login_Form%2526link%253DContinue%252520to%2526region%253Demail-verification%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253DWSJ_Login_Login_Form%2526pidt%253D1%2526oid%253DContinue%252520to%2526oidt%253D3%2526ot%253DSUBMIT'}, {'domain': 'sso.accounts.dowjones.com', 'httpOnly': False, 'name': 'sc.Status', 'path': '/', 'secure': False, 'value': '2'}, {'domain': 'sso.accounts.dowjones.com', 'httpOnly': False, 'name': 'sc.InTg', 'path': '/', 'secure': False, 'value': 'a'}, {'domain': '.dowjones.com', 'httpOnly': False, 'name': 's_cc', 'path': '/', 'secure': False, 'value': 'true'}, {'domain': '.dowjones.com', 'expiry': 1638070448, 'httpOnly': False, 'name': 'AMCV_CB68E4BA55144CAA0A4C98A5%40AdobeOrg', 'path': '/', 'secure': False, 'value': '-1891778711%7CMCIDTS%7C18229%7CMCMID%7C37928332457746331093231349101912037537%7CMCAAMLH-1575516848%7C11%7CMCAAMB-1575516848%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1574919248s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C2.4.0'}, {'domain': '.dowjones.com', 'expiry': 1590464047, 'httpOnly': False, 'name': 'optimizelyEndUserId', 'path': '/', 'secure': False, 'value': 'oeu1574912047100r0.47748709502789266'}, {'domain': 'sso.accounts.dowjones.com', 'expiry': 1732700045.588694, 'httpOnly': True, 'name': 'did', 'path': '/', 'secure': True, 'value': 's%3Av0%3Aedb6ff10-118f-11ea-86e2-7b722dc00c38.Hw0FtvD7ElpiqLm3JqKbIwMbrST7cejA5zZhsni2PDg'}, {'domain': 'sso.accounts.dowjones.com', 'httpOnly': False, 'name': 'sc.ASP.NET_SESSIONID', 'path': '/', 'secure': False, 'value': 'undefined'}, {'domain': 'sso.accounts.dowjones.com', 'expiry': 1576208054.009801, 'httpOnly': True, 'name': 'auth0', 'path': '/', 'secure': True, 'value': 's%3AiluJN4m2AjycImq4N187YL49-ZZnPgW5.lSqkcl5hJY%2FywshmgxrePM3ttWES0eHbbalxHRQSymg'}, {'domain': '.dowjones.com', 'httpOnly': False, 'name': 'AMCVS_CB68E4BA55144CAA0A4C98A5%40AdobeOrg', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.dowjones.com', 'expiry': 1606448047, 'httpOnly': False, 'name': 'utag_main', 'path': '/', 'secure': False, 'value': 'v_id:016eb012baa60000eb21128f16bf03079023d07100bd0$_sn:1$_se:1$_ss:1$_st:1574913847785$ses_id:1574912047785%3Bexp-session$_pn:1%3Bexp-session$_prevpage:WSJ_Login_Login_Form%3Bexp-1574915647791$vapi_domain:dowjones.com'}, {'domain': '.dowjones.com', 'expiry': 1890272051.960535, 'httpOnly': True, 'name': 'djcs_route', 'path': '/', 'secure': False, 'value': 'd93bada1-3810-4f56-b54c-f9c341efea5a'}
# options = webdriver.ChromeOptions()
# options.add_argument('User-Agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"')
# prefs={'profile.default_content_setting_values': {'images': 2,'javascript':2}}
# options.add_experimental_option('prefs',prefs)
# browser = webdriver.Chrome('/Users/scy/Desktop/Python/Davos/chromedriver')
# url = 'https://www.wsj.com/search/term.html?KEYWORDS=Davos&page=1'
# browser.set_window_size(width=800, height=1000, windowHandle="current")
# browser.set_window_position(x=635, y=0)
# time.sleep(1)
# browser.get(url)
# for i in range(len(Cookie)):
# 	if 'expiry' in Cookie[i]:
# 		del Cookie[i]['expiry']
# 	browser.add_cookie(Cookie[i])
# time.sleep(2)
# browser.refresh()
Article_num = 1024
rd = xlrd.open_workbook('/Users/scy/Desktop/基于达沃斯新闻文本挖掘的中国国家经济形象研究/数据获取/数据/集合.xls')
wt = copy(rd)
sh = wt.get_sheet(0)
for page in range(1,12):
	for number in range(1,21):
		
		main = ''
		html_text = browser.page_source
		soup = BeautifulSoup(html_text,'html.parser')
		title = soup.select('section > div > div > div > div > ul > li:nth-of-type('+str(number)+') > div > div > h3 > a')
		times = soup.select('section > div > div > div > div > ul > li:nth-of-type('+str(number)+') > div > div > div > ul > li > time')
		for i in title:
			Title = i.get_text()
			Href = 'https://www.wsj.com' + i.get('href')
		for i in times:
			Time = i.get_text()
		Article = browser.find_element_by_xpath('/html/body/div[2]/div[5]/section[3]/div[1]/div[2]/div/div/ul[2]/li['+str(number)+']/div/div/h3/a')
		browser.execute_script("arguments[0].click();",Article)
		time.sleep(2)	

		if string1 in Title.lower() or string2 in Title.lower() or string3 in Title.lower() or string4 in Title.lower():
			html_text = browser.page_source
			soup = BeautifulSoup(html_text,'html.parser')
			mains1 = soup.select('#wsj-article-wrap > div.article-content > p')
			for i in mains1:
				main += ' ' + i.get_text().replace("\n"," ")
			mains2 = soup.select('#wsj-article-wrap > div.article-content > div > p')
			for i in mains2:
				main += ' ' + i.get_text().replace("\n"," ")
		else:
			html_text = browser.page_source
			soup = BeautifulSoup(html_text,'html.parser')
			mains1 = soup.select('#wsj-article-wrap > div.article-content > p')
			for i in mains1:
				if string1 in i.get_text().lower() or string2 in i.get_text().lower() or string3 in i.get_text().lower() or string4 in i.get_text().lower():
					main += ' ' + i.get_text().replace("\n"," ")
			mains2 = soup.select('#wsj-article-wrap > div.article-content > div > p')
			for i in mains2:
				if string1 in i.get_text().lower() or string2 in i.get_text().lower() or string3 in i.get_text().lower() or string4 in i.get_text().lower():
					main += ' ' + i.get_text().replace("\n"," ")
		
		if string1 in Title.lower() or string2 in Title.lower() or string3 in Title.lower() or string4 in Title.lower() or string1 in main.lower() or string2 in main.lower() or string3 in main.lower() or string4 in main.lower():
			Article_num += 1
			sh.write(Article_num,0,Article_num)
			sh.write(Article_num,3,main)
			sh.write(Article_num,1,Title)
			sh.write(Article_num,2,Time)
			sh.write(Article_num,4,Href)
			sh.write(Article_num,6,"Wall-street Journal")
		wt.save('/Users/scy/Desktop/基于达沃斯新闻文本挖掘的中国国家经济形象研究/数据获取/数据/集合.xls')#保存
		browser.back()
		print(Article_num)
		time.sleep(1)
	Next_page = browser.find_element_by_xpath('/html/body/div[2]/div[5]/section[3]/div[1]/div[2]/div/div/div[2]/menu/li[5]/a')
	browser.execute_script("arguments[0].click();",Next_page)
print("Finished")
browser.quit()