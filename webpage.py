import urllib.request, urllib.parse, urllib.error
fhand=urllib.request.urlopen('https://projecteuler.net/problem=24')
for line in fhand:
    print(line.decode().strip())
