### Upload code adapted from https://gist.github.com/JeffPaine/3145490 to use access tokens instead
from __future__ import print_function

import json
import requests
import csv
import time

from token import ACCESS_TOKEN

# The repository to add this issue to
REPO_OWNER = 'climate-mirror'
REPO_NAME = 'datasets'


def upload_issues(spreadsheet):
	"""
		Provided a path to a spreadsheet iwth appropriate headers, uploades them as GitHub issues to climate mirror's datasets tracker
	:param spreadsheet: full path to spreadsheet with info.
	:return:
	"""
	items = read_spreadsheet(spreadsheet)
	for item in items:
		labels = []
		if item["status"].lower() in ["done", "complete"]:
			labels.append("One Mirror")
		else:
			labels.append("No Mirrors")

		if item["name"] is None or item["name"] == "":
			name = "Dataset at {}".format(item["desc_url"])
		else:
			name = item["name"]

		make_github_issue(name, body=make_body(item), labels=labels)
		time.sleep(5)


def read_spreadsheet(path):

	data = []
	with open(path, 'r') as spreadsheet:
		reader = csv.DictReader(spreadsheet)
		for row in reader:
			data.append(row)

	return data


def make_body(r):
	return "Name: {}\n" \
		   "Organization: {}\n" \
		   "Description URL: {}\n" \
		   "Download URL: {}\n" \
		   "File Types: {}\n" \
		   "Size: {}\n" \
		   "Status: {}".format(
		r["name"], r["org"], r["desc_url"], r["download_url"], r["file_types"], r["size"], r["status"])

def make_github_issue(title, body=None, assignee=None, milestone=None, labels=None):
    '''Create an issue on github.com using the given parameters.'''
    # Our url to create issues via POST
    url = 'https://api.github.com/repos/%s/%s/issues' % (REPO_OWNER, REPO_NAME)
    # Create an authenticated session to create the issue
    session = requests.session()

    # Create our issue
    issue = {'title': title,
             'body': body,
             'assignee': assignee,
             'milestone': milestone,
             'labels': labels}

    # Add the issue to our repository
    r = session.post(url, json.dumps(issue), headers={"Authorization": "token {}".format(ACCESS_TOKEN)})
    if r.status_code == 201:
        print('Successfully created Issue "%s"' % title)
    else:
        print('Could not create Issue "%s"' % title)
        print('Response:', r.content)

#make_github_issue('Issue Title', 'Body text', 'assigned_user', 3, ['bug'])