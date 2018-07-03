from urllib.request import urlopen
html = urlopen('http://localhost:8888/tree').read().decode('utf-8')
print(html)


import re
res = re.findall(r"<title>(.+?)</title>", html)
print(res[0])

res = re.findall(r"<p>(.*?)</p>", html, flags= re.DOTALL)
print(res[0])

res = re.findall(r'href="(.*?)"', html)
print("\nAll links: ", res)