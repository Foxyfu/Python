from urllib.parse import urlparse, urlunparse, urlunsplit,urlsplit

url = "https://lpgenerator.ru/blog/2011/04/25/url-adresa-i-celevye-stranicy/"
ftp = 'ftp://user:123456@mysite.ru'

url_1 = urlparse(url) #1
tuple = tuple(url) #2


print (
    '3)протокол:', url_1.scheme, '\n',
    '4)домен:', url_1.hostname, '\n',
    '5)порт:', url_1.port, '\n',
    '6)Путь:', url_1.path, '\n',
    '7)параметры:', url_1.params, '\n',
    '8)Строка запроса:', url_1.query, '\n',
    '9)якорь:', url_1.fragment
    )

urlunparse(url_1) #10

split_url = urlsplit(url) 
split_ftp = urlsplit(ftp) #12

print ('11)имя пользователя:',split_ftp.username, 'пароль:', split_ftp.password) 

urlunsplit(split_url)
urlunsplit(split_ftp) #13



