# coding:utf8
import url_manager
import html_download
import html_parser
import html_outputer
import os
class SpiderMain(object):
	def __init__(self):
		self.urls = url_manager.UrlManager()
		self.downloader = html_download.HtmlDownloader()
		self.parser = html_parser.HtmlParser()
		self.outputer = html_outputer.HtmlOutputer()


	def craw(self, root_url, base_url):
		self.urls.add_new_url(root_url)
		while self.urls.has_new_url():
			try:
				new_url = self.urls.get_new_url()
				html_cont = self.downloader.download(new_url) #下载页面
				new_urls = self.parser.parse(new_url,html_cont,base_url) #解析页面
				for question_url in new_urls:
					question_cont = self.downloader.download(question_url)
					image_urls = self.parser.parse2(question_cont)
					self.outputer.collect_data(image_urls)
			except:
				print('该url访问出现问题:'+new_url)
				
			

if __name__ == "__main__":
	if os.path.exists('E:/fzxy'):
		print("爬虫启动，正在整合资源")
	else:
		os.makedirs('E:/fzxy')

	base_url="https://www.zhihu.com"
	collect_url=input('请输入收藏夹的地址 比如：https://www.zhihu.com/collection/39458545   :')#收藏夹地址
	pages_url=int(input('请输入爬取取本收藏夹多少页？  :'))
	for i in range(pages_url):
		root_url=collect_url+'?page='+str(i+1)
		obi_spider = SpiderMain()
		obi_spider.craw(root_url,base_url)