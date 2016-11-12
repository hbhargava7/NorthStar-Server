def pull(): 
	data = x.fetchall()
	x = []
	for item in data: 
		x += (item['latitude'], item['longitude'])
	return x 