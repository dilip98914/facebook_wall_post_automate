import facebook

def get_api(cfg):
	#enter api using acces_token
	page_access_token=None
	graph=facebook.GraphAPI(cfg['access_token'])
	response=graph.get_object('me/accounts')
	#fetching data attribute of response object
	for page in response['data']:
		#find our page
		if page['id']==cfg['page_id']:
			page_access_token=page['access_token']
	graph=facebook.GraphAPI(page_access_token)
	return graph

def main():
	cfg={
	'page_id':'page_id',
	'access_token':'access_token'
	}
	api=get_api(cfg)
	print(dir(api))
	msg='Testing the temporary page'
	api.put_object("me", "feed", message=msg)

if __name__=="__main__":
	main()
