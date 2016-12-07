# FB-Spider
A program which accepts the id of a Facebook page.
It makes a table in .html format of the latest 5 posts and the respective latest 5 comments per post.

The number of posts and comments can be changed by editing the graph.py file.
# Get Started

Install all the dependencies listed in `requirements.txt`.

You would require a Facebook developer account to get an access token : https://developers.facebook.com/

Register your app and replace the 'YOUR_ACCESS_TOKEN' in `graph.py` by your User Token : https://developers.facebook.com/tools/accesstoken/.

# Instructions

1. Clone the repository to your machine.

2. Open your terminal and run 'python graph.py'

3. Enter the page-id of the page you want to scrape.

	You can get it from www.findmyfbid.com
	
	Please note that this app will only work for public pages and not from profiles of other people.
	That would require permission from the user.
4. Enjoy the contents in a table format.
   A file called 'Table.html' would be made in the folder itself.
   You can open it and see the table.
