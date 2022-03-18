from urllib.request import urlopen
from urllib.parse import urlparse

links = [ "https://kinogo.la/", 
    "https://vk.com/audios204894078?section=all", 
    "https://www.youtube.com/", 
    "https://translate.yandex.by/?ui=ru", 
    "https://e.mail.ru/inbox/"
    ]

for link in links:
    request = urlopen(link)
    print(f'Статус код: {request.code};  Информация стасус кода:{request.msg}') #1, 4

    url = urlparse(link) #2
    elements_url = { 'Scheme' : url.scheme,
        'Hostname' : url.hostname,
        'Port': url.port,
        'Path' : url.path,
        'Params' : url.params,
        'Query' : url.query,
        'Fragment' : url.fragment,
            }

    for elem in elements_url:   #3
        if elements_url[elem]:
            print(f"{elem}: {elements_url[elem]}")
        else:
            print(f"{elem}: Not definded")

    information = request.read(34).decode("utf8") #5

    print(information)
    print('.........................')




   
