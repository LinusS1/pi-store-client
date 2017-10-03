"""Download and install part for the client."""
#IMPORTS
import requests
import time

def startInstall():
	pass

def startDownload(download):
	name = download.get_suggested_filename()
	path = "/home/linus/Downloads/"+name
	r = requests.get(download.get_uri())
	with open(path,'wb') as f:
		f.write(r.content)
	print(4)	
	time.sleep(1000)
	print(6)
	
	# Next!
