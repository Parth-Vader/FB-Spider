# FB-Spider

[![forthebadge](http://forthebadge.com/images/badges/made-with-python.svg)](http://forthebadge.com)

 [![Join the chat at https://join.slack.com/t/kwoc2017-parth/shared_invite/enQtMjc1OTU3MDUwNzc0LTNkNzQzN2U5NzI0ZTNkM2I5MGM5MDIyYTYxMzFhNWYzNWYwMDIzMjNmYjM2MTA1NDc1NWU2Yjc0ZTYxNGZmNTA](https://img.shields.io/badge/Slack-Join%20chat-blue.svg)](https://join.slack.com/t/kwoc2017-parth/shared_invite/enQtMjc1OTU3MDUwNzc0LTNkNzQzN2U5NzI0ZTNkM2I5MGM5MDIyYTYxMzFhNWYzNWYwMDIzMjNmYjM2MTA1NDc1NWU2Yjc0ZTYxNGZmNTA)

A program which accepts the id of a Facebook page and transforms into a table of the latest 5 posts and the respective latest 5 comments per post. The table will be in .html format 

The number of posts and comments can be changed by editing the graph.py file.

# Table of contents

- [Get Started](#get-started)
- [Requirements](#requirements)
- [Instructions](#instructions)
- [Contribute](#contribute)

# Get Started

[(Back to top)](#table-of-contents)

You would require a Facebook developer account to get an access token : https://developers.facebook.com/

Register your app and replace the 'YOUR_ACCESS_TOKEN' in `graph.py` by your User Token : https://developers.facebook.com/tools/accesstoken/.


# Requirements

[(Back to top)](#table-of-contents)

Other than requiring Python3.x , you require the following libraries:<br>
* facepy<br>
* json<br>
* json2html<br>
* webbrowser<br>


# Instructions

[(Back to top)](#table-of-contents)

1. Clone the repository to your machine.

2. Open your terminal and change directory to your cloned project folder.

3. `$ pip3 install --editable . ` This will install all the requirements listed.

![demo](data/setup.gif)

4. Now run the program `$ python3 graph.py `

5. Enter the page name of the page you want to scrape. You see a display of 5 choices and then select one out. 

![demo](data/run.gif)

	Please note that this app will only work for public pages and not from profiles of other people.
	That would require permission from the user.
6. Enjoy the contents in a table format.
   A file called 'Table.html' would be made in the folder itself.
   You can open it and see the table.
   
# Contribute

[(Back to top)](#table-of-contents)

You can contribute to the repo via this really-simple steps:<br>
* Star and fork this repo.<br>
* Join the [(slack channel)](#fb-spider) . Discuss your ideas on how to improve the project with members or ask your doubts regarding the project.<br>
* Clone your repo.<br>
* Tackle down the issues or add your own innovations.<br>
* Pull Request<br>
