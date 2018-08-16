import requests
import os
url = "http://pic172.nipic.com/file/20180711/6817480_100801172031_2.jpg"
root = "//home//leiye//图片//photo1//"
path = root + url.split('/')[-1]
try:
	if not os.path.exists(root):
		os.mkdir(root)
	if not os.path.exists(path):
		r = requests.get(url)
		with open(path, 'wb') as f:
			f.wirte(r.content)
			f.close()
			print("OK")
	else:
		print("wenjianyicunzai")
except:
	print("fuck")
