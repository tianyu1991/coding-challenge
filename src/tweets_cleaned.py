import json
from HTMLParser import HTMLParser
import re

data = open('ft5.txt', 'r')
lines = data.read().split('\n')
i=0
count=0
saveFile = open('ft1.txt','a')
while i<(len(lines)-1):
	#print lines[i]
	data2 = json.loads(HTMLParser().unescape(lines[i]))
	if data2.has_key("created_at"): 
		time = data2["created_at"].encode('utf-8')
		tweet = data2["text"].encode('utf-8')
		m=re.search( "([^:\.\\\/'@#0-9A-Za-z \t])",tweet)
		if m:
			tweet=re.sub( "([^:\.\\\/'@#0-9A-Za-z \t])" ,"",tweet)
			count=count+1
		tweet=re.sub("\/", "/", tweet)
		saveFile.write(tweet+" (timestamp:"+time+")")
		saveFile.write('\n')
	i+=2


c=str(count)
saveFile.write(c)
saveFile.write(" tweets contained unicode")
saveFile.write('\n')
saveFile.close()
data.close()
