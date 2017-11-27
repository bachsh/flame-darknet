import json
from bs4 import BeautifulSoup

def parse(data):
	soup = BeautifulSoup(data['html'], 'lxml')
	posts = soup.find_all('table', class_='tborder')
	items = []
	for post in posts:
		item = {}
		###
                print post
		item['topic_content'] = post.find('span', class_='smalltext').find('strong').get_text()
                print post
		###
		username = post.find('span', class_='largetext').get_text()
		if username is None:         
			username = post.find('a', class_='username-coloured')    
		item['post_author'] = username
		###        
		item['post_content'] = post.find('div', {"id" : lambda L: L and L.startswith('pid_')}).get_text()
		###
		item['url'] = data['url']
		###
		items.append(item)
		#print item['topic_content']
		#print item['post_authar']
		#print item['post_content']
		#print item['url']
	return items
