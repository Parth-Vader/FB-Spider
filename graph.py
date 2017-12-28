from facepy import GraphAPI
import json
import sys
from json2html import *
import webbrowser
import click

@click.group()
def cli():
	pass	

#checks wether userdata.json is ready for use 
def error_check():
	try:
		with open("userdata.json", "x") as outfile:
			click.secho("Please Initialise ",fg="green",bold=True)
			sys.exit(0)
	except FileExistsError:
		try:
			with open("userdata.json","r") as outfile:
				data=json.load(outfile)
				if('token' in data and 'npa' in data and 'npo' in data):
					pass
				else:
					raise ValueError()	
		except ValueError:
			click.secho("User data may have been corrupted or not Initialised.Please Initialise",fg="red",bold=True)
			sys.exit(0)

#initialise the userdata.json
@cli.command('initialise',short_help="Initialise with the required info.")
def initialise():
	click.clear()
	click.secho("Enter the User access token",fg="green",bold=True)
	token=input()
	click.secho("Enter the no of result pages for your input.\nBy default it is set to 5.",fg="green",bold=True)
	try:
   		val = int(input())
   		npa=val
	except ValueError:
		npa=5
	click.secho("Enter the no of posts in the output page.\nBy default it is set to 5.",fg="green",bold=True)
	try:
   		val = int(input())
   		npo=val
	except ValueError:
		npo=5
	click.clear()
	click.secho("Data initialised succesfully",fg="green",bold=True)		
	with open("userdata.json","w") as outfile:
		data={'token':token,'npa':npa,'npo':npo}
		json.dump(data,outfile)
			
#shows the data stored in userdata.json file	
@cli.command('show',short_help='Shows the specified value stored.')
@click.option('--token',is_flag=bool,default=False,help='Shows the user access token stored.')
@click.option('--npa',is_flag=bool,default=False,help='Shows the default no of pages for given input.')
@click.option('--npo',is_flag=bool,default=False,help='Shows the default no of top post in the output.')
def show(token,npa,npo):
	error_check()
	with open("userdata.json","r") as outfile:
		data=json.load(outfile)
	if token:
		click.secho("User access token\n",fg="green",bold=True)
		click.secho(data['token'],fg="blue",bold=True)
	elif npa:
		click.secho("No of pages: ",nl=False,fg="green",bold=True)
		click.secho(str(data['npa']),fg="blue",bold=True)			
	elif npo:
		click.secho("No of posts: ",nl=False,fg="green",bold=True)
		click.secho(str(data['npo']),fg="blue",bold=True)	
	else:
		click.secho("Option not specified",fg="red",bold=True)
		sys.exit(0)			

#edits the data stored in userdata.json file
@cli.command('edit',short_help='edits the specified value stored.')
@click.option('--token',is_flag=bool,default=False,help='Edits the user access token stored.')
@click.option('--npa',is_flag=bool,default=False,help='Edits the no of pages.')
@click.option('--npo',is_flag=bool,default=False,help='Edits the no of top post.')
def edit(token,npa,npo):
	error_check()
	with open("userdata.json","r") as outfile:
		data=json.load(outfile)
	if token:
		click.secho("Enter the User access token\n",fg="green",bold=True)
		data['token']=input()
	elif npa:
		click.secho("Enter the no of pages: ",nl=False,fg="green",bold=True)
		try:
	   		val = int(input())
	   		if val<1:
	   			raise ValueError()
	   		else:	
	   			data['npa']=val
	   			click.secho("Data changed succesfully.",fg="green",bold=True)
		except ValueError:
			click.secho("Invalid value provided.",fg="red",bold=True)
	elif npo:
		click.secho("Enter the no of posts: ",nl=False,fg="green",bold=True)
		try:
	   		val = int(input())
	   		if val<1:
	   			raise ValueError()
	   		else:	
	   			data['npo']=val
	   			click.secho("Data changed succesfully.",fg="green",bold=True)
		except ValueError:
			click.secho("Invalid value provided.",fg="red",bold=True)
	else:
		click.secho("Option not specified",fg="red",bold=True)
		sys.exit(0)			
	with open("userdata.json","w") as outfile:
		json.dump(data,outfile)



#searches for the page name
@cli.command('search',short_help="Search the page.")
@click.argument('page',metavar="<Page name>",nargs=-1)
@click.option('--npa',default=-1,help='the no of pages.')
@click.option('--npo',default=-1,help='the no of top post.')
def get(page,npa,npo):
	error_check()
	search=""
	for i in page:
		search=search+str(i).strip()+" "
	if search.strip()=="":	
		click.clear()
		click.secho("No page name provided",fg="red",bold=True)
		search=input("enter the page name: ")
	if search.strip()=="":	
		click.clear()
		click.secho("No page name provided",fg="red",bold=True)
		sys.exit(0)
			
	with open("userdata.json","r")as outfile:
		getdata=json.load(outfile)		
	graph= GraphAPI(getdata['token'])
	click.clear()
	if npa==-1:
		search_res=graph.get('search?q='+search+'&type=page&limit='+str(abs(getdata['npa'])))
	else:
		search_res=graph.get('search?q='+search+'&type=page&limit='+str(abs(npa)))	
	if search_res['data']:
		 for index,item in enumerate(search_res['data']):
		    # 	The 'data' key of 'search_res' dictionary is a list of dictionaries of 5 pages
		    s='	'+str(index+1)+' |>  '+item['name']
		    click.secho(s,fg="blue",bold=True)
		 click.secho("Please enter the page no: ",nl=False,fg="green",bold=True)
		 try:
		 	val=int(input())
		 	if val>len(search_res['data']) or val<1:
		 		raise ValueError()
		 	else:
		 		pno=val	
		 except ValueError:
		 	click.secho("Invalid Page no",fg="red",bold=True)
		 	sys.exit(0)	
		 pid=search_res['data'][pno-1]['id']
		 if npo==-1: 
		 	variable = graph.get(pid+'/posts?fields=comments.limit(5),link,full_picture,message&limit='+str(abs(getdata['npo'])))
		 else:
		 	variable = graph.get(pid+'/posts?fields=comments.limit(5),link,full_picture,message&limit='+str(abs(npo)))


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
		click.secho(search,fg="blue",bold=True)
