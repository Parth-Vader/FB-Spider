from PyQt4 import QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
# Importing modules required for PyQt
from facepy import GraphAPI
import json
from json2html import *
import webbrowser

#Importing the modules for the script
import experiment
#Importing the design module
#################################################################


class FBSpider(QtGui.QMainWindow, experiment.Ui_MainWindow):
	def __init__(self):
		super(self.__class__, self).__init__()
		self.setupUi(self)
		self.pushButton.clicked.connect(self.accessCode)
		self.pushButton_2.clicked.connect(self.pageAccept)
		self.pushButton_3.clicked.connect(self.pageNumber)
		self.pushButton_4.clicked.connect(self.generateHTML)
		


	def accessCode(self):
		val = self.lineEdit.displayText()
		graph = GraphAPI(val)
		self.listWidget.addItem("Added")
		global graph
		

	def pageAccept(self):

		PageName = self.lineEdit_2.displayText()
		self.listWidget.addItem(PageName)
		search_res=graph.get('search?q='+PageName+'&type=page&limit=5')
		global search_res
		if search_res['data']:
			 for index,item in enumerate(search_res['data']):
			    # 	The 'data' key of 'search_res' dictionary is a list of dictionaries of 5 pages
			    	val = str(index+1)
			    	val1 = item['name']
			    	val2 = str(val1)
			    	self.listWidget.addItem(val+val2)


	def pageNumber(self):
		pno = int(self.lineEdit_3.displayText())
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
		f = open('Table.html','r', encoding='utf-8')
		s=f.read()
		s=s.replace("&gt;",">")
		s=s.replace("&lt;","<")
		f.close()

		#	 writting content to html file
		f = open('Table.html','w', encoding='utf-8')
		f.write(s)
		f.close()

	def generateHTML(self):
		
		webbrowser.open("Table.html")

################################################################
def main():
	app = QtGui.QApplication(sys.argv)
	form = FBSpider()
	form.show()
	app.exec_()

if __name__ == '__main__':
	main()
