from facepy import GraphAPI
import json
from json2html import *
import webbrowser
graph= GraphAPI('YOUR_ACCESS_TOKEN')

print("Please enter the page-name:" )
PageName=raw_input()

search_res=graph.get('search?q='+PageName+'&type=page&limit=5')

for index,item in enumerate(search_res['data']):
    #The 'data' key of 'search_res' dictionary is a list of dictionaries of 5 pages
    print index+1,item['name']
    
pno=int(raw_input("Please enter the page no. : "))
pid=search_res['data'][pno-1]['id']        
      
variable = graph.get(pid+'/posts?fields=comments.limit(5),link,message&limit=5')
        
with open('data.json', 'wb') as outfile:
    json.dump(variable, outfile)

with open('data.json') as js:
	jsvar=json.load(js)
	del jsvar['paging']
	for i in range(0,5):
		del jsvar['data'][i]['id']
		del jsvar['data'][i]['comments']['paging']
		for j in range(0,len(jsvar['data'][i]['comments']['data'])):
			del jsvar['data'][i]['comments']['data'][j]['id']
			del jsvar['data'][i]['comments']['data'][j]['from']['id']

#infoFromJson = json.loads(variable)
table = json2html.convert(json = jsvar)
htmlfile=table.encode('utf-8')
#print(htmlfile)
f = open('Table.html','w')
f.write(htmlfile)
f.close()

webbrowser.open("Table.html")
