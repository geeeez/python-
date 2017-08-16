# coding:utf8
import requests
import time
class HtmlOutputer:
	def collect_data(self,new_data):
		if new_data is None:
			print('下载图片时发生了问题')
			return
		for image in new_data:
			ir = requests.get(image, stream=True)
			if ir.status_code == 200:
				print('正在下载：'+image)
				path="E:\\fzxy\\" + str(int(time.time()))+".jpg"
				with open(path,'wb') as f:
					for chunk in ir:
						f.write(chunk)