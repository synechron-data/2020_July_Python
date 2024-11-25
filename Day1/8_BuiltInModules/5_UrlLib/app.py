# from urllib.request import urlopen

# with urlopen('http://sixty-north.com/c/t.txt') as story:
#     story_words = []
#     for line in story:
#         line_words = line.decode('utf-8').split()
#         for word in line_words:
#             story_words.append(word)

# print(story_words)

# ----------------------------------------------------

# import urllib.request

# x = urllib.request.urlopen("https://www.google.com")
# # print(x.read())

# fo = open("myGoogle.html", "w+")
# fo.write(str(x.read()))

# -------------------------------------------------------------
import urllib.request

url = "https://www.google.com/search?q=Synechron"

headers = {}
headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
req = urllib.request.Request(url, headers=headers)

res = urllib.request.urlopen(req)
respData = res.read()

fo = open("googleResp.html", "w+")
fo.write(str(respData))
