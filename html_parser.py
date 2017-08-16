# coding:utf8
import re
from bs4 import BeautifulSoup
class HtmlParser(object):

	#获取新的urls集合
	def _get_new_urls(self, page_url, soup,base_url):
		new_data = set()  #new_data 实际上是收藏夹里面每个问题的url;
		#url的格式
		links = soup.find_all('a', href=re.compile(r"^/question/[a-zA-Z0-9_]*/answer/[a-zA-Z0-9_]"))
		for link in links:
			new_url = link['href']
			new_full_url = base_url + new_url
			new_data.add(new_full_url)
		return new_data

	def _get_new_data(self, soup):
		#改成下载图片，明天再写吧 困困困
		img_urls = set()
		imglinks = soup.find_all('img', src=re.compile(r"^https://[a-zA-Z0-9/.]*.g")) #正则很有可能有问题 后期要检查
		for imglink in imglinks:
			new_img_url = imglink['src']
			new_full_imgurl = new_img_url
			img_urls.add(new_full_imgurl)
		return img_urls

	def  parse(self,page_url, html_cont, base_url):
		if page_url is 	None or html_cont is None:
			return
		soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
		new_urls = self._get_new_urls(page_url,soup,base_url)
		return new_urls
	def  parse2(self,question_cont):
		if question_cont is None:
			return
		soup = BeautifulSoup(question_cont, 'html.parser', from_encoding='utf-8')
		new_urlss = self._get_new_data(soup)
		return new_urlss
