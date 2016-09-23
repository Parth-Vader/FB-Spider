from facepy import GraphAPI
import json
from json2html import *
import webbrowser
graph= GraphAPI('YOUR_ACCESS_TOKEN')

print("Please enter the page-id  " )
PageId=raw_input()

variable = graph.get(str(PageId)+'/posts?fields=comments.limit(5){message},message&since=today&limit=5')


import json
with open('data.json', 'wb') as outfile:
    json.dump(variable, outfile)

#infoFromJson = json.loads(variable)
table = json2html.convert(json = variable)
htmlfile=table.encode('utf-8')
#print(htmlfile)
f = open('Table.html','w')
f.write(htmlfile)
f.close()

webbrowser.open("Table.html")
