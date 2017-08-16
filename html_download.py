# coding:utf8
import requests

class HtmlDownloader(object):
	def download(self,url):
		if url is None:
			print('url is none')
			return None
		r = requests.get(url,headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36' })
		if r.status_code != 200:
			print('none 没下载下来页面：'+url)
			print(r.status_code)
			return None
		return r.text
