"""Download and install part for the client."""
#IMPORTS
import requests

def startInstall():
	pass

def startDownload(download):
	name = download.get_suggested_filename()
	path = "/home/linus/Downloads/"+name
	r = requests.get(download.get_uri())
	with open(path,'wb') as f:
		f.write(r.content)
	# Next!
