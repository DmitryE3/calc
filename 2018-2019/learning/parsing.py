import re
import ssl

from bs4 import BeautifulSoup as BS
from urllib.request import urlopen
from urllib.parse import urlparse

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url_x = str(input())
#url_x = 'http://en.ifmo.ru/en/contacts/Contacts.htm'
url_x = 'https://docs.djangoproject.com/en/1.11/'
f_pars = tuple(urlparse(url_x))
print(f_pars)
f_html = urlopen(url_x, context = ctx)
#f_html = open('mysite.html', 'r')
f_str = f_html.read()
f_str = f_str.decode('utf-8')
#f_bs = BS(f_str)
#print(f_bs.h1)

find_h1 = re.findall(r'<h1.+?>(.*?)</h1>', f_str)
str_new = ''

print(find_h1)
for i in find_h1:
    str_new += i
print(re.sub(r'<.*?>', ' ', str_new))