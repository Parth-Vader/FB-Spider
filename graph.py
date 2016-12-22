from facepy import GraphAPI
import json
from json2html import *
import webbrowser
import re
graph= GraphAPI('YOUR_ACCESS_TOKEN')

print("Please enter the page-name:" )
PageName=raw_input()

search_res=graph.get('search?q='+PageName+'&type=page&limit=5')

for index,item in enumerate(search_res['data']):
    #The 'data' key of 'search_res' dictionary is a list of dictionaries of 5 pages
    print index+1,item['name']
    
pno=int(raw_input("Please enter the page no. : "))
pid=search_res['data'][pno-1]['id']        
      
variable = graph.get(pid+'/posts?fields=comments.limit(5){message},message&limit=5')

try:
	del variable['paging']
	for i in range(0,len(variable['data'])):
		del variable['data'][i]['id']
		try:
			del variable['data'][i]['comments']['paging']
			for j in range(0,len(variable['data'][i]['comments']['data'])):
				del variable['data'][i]['comments']['data'][j]['id']
				del variable['data'][i]['comments']['data'][j]['from']['id']
		except:pass
except:pass



with open('data.json', 'wb') as outfile:
    json.dump(variable, outfile)

#infoFromJson = json.loads(variable)
table = json2html.convert(json = variable)

n=len(re.findall(r"(?<=<td>http://)\S+(?=</td>)|(?<=<td>https://)\S+(?=</td>)",table))

def change_tag(matchobj):
	return "<a href=\""+matchobj.group(0)+"\">"+matchobj.group(0)+"</a>"

for i in range(0,n):
	table=re.sub(r"(?<=<td>)http://\S+(?=</td>)|(?<=<td>)https://\S+(?=</td>)",change_tag,table)


htmlfile=table.encode('utf-8')
#print(htmlfile)
f = open('Table.html','w')
f.write(htmlfile)
f.close()

webbrowser.open("Table.html")
