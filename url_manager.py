# coding:utf8

class UrlManager(object):

	def __init__(self):
		self.new_urls = set() #set()用于创建一个集合
		self.old_urls = set()

	#仅初始化使用，后面一般都使用add_new_urls
	def add_new_url(self,url):
		if url is None:
			return
		if url not in self.new_urls and url not in self.old_urls:
			self.new_urls.add(url) #保证不会爬取重复页面

	def has_new_url(self):
		return len(self.new_urls) != 0

	def get_new_url(self):
		new_url = self.new_urls.pop() #获取并移除url
		self.old_urls.add(new_url)
		return new_url
	def add_new_urls(self,urls):
		if urls is None or len(urls) == 0:
			return
		
		for url in urls:
			self.add_new_url(url)
		