from urllib.parse import urlparse, urlunparse

url= "http://www.user.by:50/test.php;st?var=10#metka"

urlparse_url = urlparse(url) #1
tuple = tuple(url) #2


print ('3)протокол:', urlparse_url.scheme, '\n', '4)домен:', urlparse_url.hostname, '\n', '5)порт:', urlparse_url.port)
print ('6)Путь:', urlparse_url.path, '\n', '7)параметры:', urlparse_url.params)
print ('8)Строка запроса:', urlparse_url.query, '\n', '9)якорь:', urlparse_url.fragment)

urlunparse_url = urlunparse(urlparse_url) #10

print(urlunparse_url) #11