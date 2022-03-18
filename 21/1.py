import requests

links = ["https://translate.yandex.by/fro=tabbar",
        "https://kinogo.by/21789-the-addams-family_2019.htm",
        "http://docs.google.com/spreadshe/",
        "https://python-scripts.com/reqsts",
        "http://avgrodno.by/raspisanie/"
        ]

for link in links:
    print('_____________________________________________', link)
    try:
        response = requests.get(link)
        print (response.status_code, requests.status_codes._codes[response.status_code]) #2
        
        response_in_str = response.content.decode('UTF-8')  #3 and 4
        print(response.headers) #5 
    except:
        print("Connection error!")
    
   
  