from facepy import GraphAPI
import json
from json2html import *
import webbrowser
import click

cli=click.Group()
@cli.command()
@click.pass_context
def page_handler(ctx):	

	try:
		with open("userdata.txt", "x") as outfile:
			pass
	except FileExistsError:
		pass


	with open("userdata.txt","r")as outfile:
		s=outfile.read().strip()
		if s=="":
			click.clear()
			click.secho("No Access token found. Please provide the Access token.\n",fg="red",bold=True)
			ctx.invoke(access_token_handler,edit=True)
		outfile.seek(0)
		s=outfile.read().strip()
				
	graph= GraphAPI(s)
	click.clear()
	click.secho("Please enter the page-name:")
	PageName=input()

	search_res=graph.get('search?q='+PageName+'&type=page&limit=5')
	if search_res['data']:
		 for index,item in enumerate(search_res['data']):
		    # 	The 'data' key of 'search_res' dictionary is a list of dictionaries of 5 pages
		     print ((index+1),'	|	',item['name'])
	    
		 pno=int(input("Please enter the page no. : "))
		 pid=search_res['data'][pno-1]['id']
	        
	      
		 variable = graph.get(pid+'/posts?fields=comments.limit(5),link,full_picture,message&limit=5')

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
		 		try:
		 			variable['data'][i]['full_picture']='<div style="width:500px;height:500px;overflow:scroll"><img style="width:100%;height:auto" src=\"'+variable['data'][i]['full_picture']+'\"></div>'
		 		except:pass
		 		try:
		 			variable['data'][i]['link']='<a href=\"'+variable['data'][i]['link']+'\">'+variable['data'][i]['message']+'</a>'
		 		except:
		 			variable['data'][i]['link']='<a href=\"'+variable['data'][i]['link']+'\">link</a>'
		 		try:
		 			del variable['data'][i]['message']
		 		except:pass
		 except:pass

		#  	Removing 'data'
		 for i in range(0,len(variable['data'])):
		 	try:
		 		variable['data'][i]['comments']=variable['data'][i]['comments']['data']
		 	except:pass
		 variable['']=variable.pop('data')
		# 	Removing 'headers'
		 variable.pop('headers')


		 with open('data.json', 'w+') as outfile:
		     json.dump(variable, outfile)

		 table = json2html.convert(json = variable)

		 htmlfile=table.encode('utf-8')

		 f = open('Table.html','wb')
		 f.write(htmlfile)
		 f.close()

		#	replacing '&gt'  with '>' and  '&lt' with '<'
		 f = open('Table.html','r',encoding='utf-8')
		 s=f.read()
		 s=s.replace("&gt;",">")
		 s=s.replace("&lt;","<")
		 f.close()

		#	 writting content to html file
		 f = open('Table.html','w',encoding='utf-8')
		 f.write(s)
		 f.close()

		 #	output
		 webbrowser.open("Table.html")
	else:
		click.secho("We couldn't find anything for ",nl=False)
		click.secho(PageName,fg="blue",bold=True)



@cli.command()
@click.option('--edit/--show',default="True",help="--edit to edit the access token.\n--show to show the current access token.")
def access_token_handler(edit):
	
	try:
		with open("userdata.txt", "x") as outfile:
			pass
	except FileExistsError:
		pass

		
	if edit:
		token=input("Enter the access token\n")
		with open("userdata.txt", "w")as outfile:
			outfile.write(token)
	else:
		with open("userdata.txt", "r")as outfile:
			s=outfile.read().strip()
			if s=="":
				click.secho("No access token found.",fg="red",bold=True)
			else:
				click.secho("Access token is:\n")
				click.secho(s,fg="green",bold=True)
