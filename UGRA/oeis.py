import requests

for i in range(10000, 1000,-1):
    temp = str(i)
    url = 'https://oeis.org/search?q=' + temp + '&sort=&language=&go=Search'
    r = requests.get(url)
    text = r.text.find("Displaying 1-10 ")
    if text == -1:
        print(text, i,"THAT's IT")
    else:
        print(text,i)
