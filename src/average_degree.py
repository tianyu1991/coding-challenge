from dateutil import parser
import re
import calendar

data = open('ft1.txt', 'r')
lines = data.read().split('\n')
saveFile = open('ft2.txt','a')
i=0
tags_dict={}
tags_list=list()
time_list=list()

while i<(len(lines)-2):	
	tag=re.findall("#(\w*)",lines[i])
	for n in range(0,len(tag)):
		tag[n]=tag[n].lower()
	time=re.findall("timestamp:([\w\s:+]*)\)",lines[i])	
	timestamp = calendar.timegm(parser.parse(time[0]).timetuple())	
	l=len(tag)
	if l>1:
		tags_list.append(tag)
		time_list.append(timestamp)
		del_num=0
		#remove tweets out of time
		while(timestamp-time_list[0]>=60):
			time_list.pop(0)
			del_tag=tags_list[0]
			tags_list.pop(0)
			del_l=len(del_tag)
			for n in range(0,del_l-1):
				m=del_l-1
				while m>n:
					num=0
					if( del_tag[m] not in tags_dict.get(del_tag[n]) or del_tag[n] not in tags_dict.get(del_tag[m])):
						m=m-1
						break
					for g in range(0,len(tags_list)-1):
						if (del_tag[n] in tags_list[g] and del_tag[m] in tags_list[g]):
							num+=1
							break
					if num==0:
						original_tag=list(tags_dict.get(del_tag[n]))
						original_tag.remove(del_tag[m])
						tags_dict[del_tag[n]]=original_tag
						original_tag=list(tags_dict.get(del_tag[m]))
						original_tag.remove(del_tag[n])
						tags_dict[del_tag[m]]=original_tag
					m=m-1
				n+=1		
		n=0
		#add new tweets
		while n<l:
			
			if tag[n] in tags_dict:
				original_tag=list(tags_dict.get(tag[n]))
				n2=0
				while n2<l:
					if (n2!=n and tag[n2] not in original_tag):
						original_tag.append(tag[n2])
					n2+=1 
				tags_dict[tag[n]]=original_tag
	
			else:
				tags_dict[tag[n]]=tag
			n+=1
	n=0
	#caculate the average number and save
	value=tags_dict.values()
	num=len(sum(value, []))-len(tags_dict)
	if len(tags_dict)>0: 
		average=format(float(num)/len(tags_dict),'.2f')
	else:
		average=format(0.00,'.2f')
	saveFile.write(str(average))
	saveFile.write('\n')
	i=i+1
saveFile.close()
data.close()
