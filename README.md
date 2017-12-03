# FB-Spider
A program which accepts the id of a Facebook page and transforms into a table of the latest 5 posts and the respective latest 5 comments per post. The table will be in .html format 

The number of posts and comments can be changed by editing the graph.py file.


# Get Started

You would require a Facebook developer account to get an access token : https://developers.facebook.com/

Register your app and replace the 'YOUR_ACCESS_TOKEN' in `graph.py` by your User Token : https://developers.facebook.com/tools/accesstoken/.


# Requirements
Other than requiring Python3.x , you require the following libraries:<br>
* facepy<br>
* json<br>
* json2html<br>
* webbrowser<br>


# Instructions

1. Clone the repository to your machine.

2. Open your terminal and change directory to your cloned project folder.

3. `$ pip3 install --editable . ` This will install all the requirements listed.

4. Now run the program `$ python3 graph.py `

3. Enter the page name of the page you want to scrape. You see a display of 5 choices and then select one out 

	Please note that this app will only work for public pages and not from profiles of other people.
	That would require permission from the user.
4. Enjoy the contents in a table format.
   A file called 'Table.html' would be made in the folder itself.
   You can open it and see the table.
   
# Contribute
You can contribute to the repo via this really-simple steps:<br>
* Star and fork this repo.<br>
* Clone your repo.<br>
* Tackle down the issues or add your own innovations.<br>
* Pull Request<br>
