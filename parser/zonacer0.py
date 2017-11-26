import json
from bs4 import BeautifulSoup

def parse(data):
	soup = BeautifulSoup(data['html'], 'lxml')
	posts = soup.find_all('div', class_='post_wrapper')
	items = []
	for post in posts:
		item = {}
		###
		item['topic_content'] = post.find('span',class_='post_subject').get_text()
		###
		username = post.find('a', class_='name') 
		item['post_author'] = username.get_text().strip()
		###        
		item['post_content'] = post.find('div', class_='inner').get_text()
		###
		item['url'] = data['url']
		###
		items.append(item)
		#print item['topic_content']
		#print item['post_authar']
		#print item['post_content']
		#print item['url']
	return items
