import requests
url = "http://m.ip138.com/ip.asp?ip="
try:
	r = requests.get(url+"121.254.178.250")
	r.raise_for_status()
	r.encoding = r.apparent_encoding
	print(r.text[-500:])
except :
	print("fuck")