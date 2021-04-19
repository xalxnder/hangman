import urllib.request

EASY = ['apple', 'happy', 'can', 'cake', 'bike', 'circle', 'dish', 'dance', 'egg', 'game', 'gate', 'baby']

MEDIUM = ['abash', 'abate', 'chronic', 'circumvent', 'classic', 'cognitive', 'ethnic', 'export', 'expense', 'eventually', 'legacy', 'legislate']

#Url to grab words
words_url = "https://www.mit.edu/~ecprice/wordlist.10000"
response = urllib.request.urlopen(words_url)
text = response.read().decode()
ADVANCED = text.splitlines()
