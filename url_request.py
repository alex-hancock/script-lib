import urllib2
import json

def get_job_list():
	# Request API dump of Running URL's from Luigi server
	server = os.getenv("LUIGI_SERVER") + ":" + os.getenv("LUIGI_PORT", "8082") + "/api/"
	running_url = server + "task_list?data=%7B%22status%22%3A%22RUNNING%22%2C%22upstream_status%22%3A%22%22%2C%22search%22%3A%22%22%7D"

	local_job_list = {}
	for URL in list_of_URLs:
		name = URL[62:]
		suffix = ""
		name = name.split("%")[0] + suffix

	# Retrieve api tool dump from URL and read it into json_tools
	req = urllib2.Request(URL)
	response = urllib2.urlopen(req)
	text_tools = response.read()
	json_tools = json.loads(text_tools)
