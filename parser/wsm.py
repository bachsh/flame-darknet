import json
from bs4 import BeautifulSoup

def parse(data):
	soup = BeautifulSoup(data['html'], 'lxml')
	posts = soup.find_all('div', class_='postbody')
	items = []
	for post in posts:
		item = {}
		###
		item['topic_content'] = post.find('h4', class_='entry-title').get_text()
		###
		username = post.find('li', class_='username')
		if username is None:         
			username = post.find('a', class_='username-coloured')    
		item['post_author'] = username.get_text()
		###        
		item['post_content'] = post.find('div', class_='entry-content').get_text()
		###
		item['url'] = data['url']
		###
		items.append(item)
		#print item['topic_content']
		#print item['post_authar']
		#print item['post_content']
		#print item['url']
	return items
