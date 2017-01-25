from __future__ import print_function

import json
import csv
import time
import requests

import make_issues
from make_issues import REPO_NAME, REPO_OWNER, ACCESS_TOKEN

def read_github_issues(num_issues):

	issues = []
	url = 'https://api.github.com/repos/%s/%s/issues/' % (REPO_OWNER, REPO_NAME)
	# Create an authenticated session to create the issue
	session = requests.session()

	# Add the issue to our repository

	for i in range(1,num_issues+1):
		r = session.get(url + "{}".format(i), headers={"Authorization": "token {}".format(ACCESS_TOKEN)})
		if r.status_code == 200:
			print('Successfully retrieved Issue "%s"' % i)
			issues.append(json.loads(r.content))
		else:
			print('Could not retrieve Issue "%s"' % i)

		time.sleep(4)

	return issues


def check_and_upload_issues(path_to_spreadsheet, issues=None):
	if not issues:
		issues = read_github_issues(123)

	with open(path_to_spreadsheet, 'r') as csv_file:
		urls = csv.reader(csv_file)
		for url in urls:
			url = url[0]
			exists = False
			for issue in issues:
				if url in issue["body"]:
					exists = True
					break

			if exists is False:
				print("Making issue! simulated for {}".format(url))
				upload_issue(url)
				time.sleep(4)
			else:
				print("Already exists at {}".format(url))


def upload_issue(url):
	"""
		Provided a path to a spreadsheet iwth appropriate headers, uploades them as GitHub issues to climate mirror's datasets tracker
	:param spreadsheet: full path to spreadsheet with info.
	:return:
	"""
	labels = []
	labels.append("No Mirrors")

	if ".gov" not in url:
		labels.append("Priority: Low")

	name = "Dataset at {}".format(url)

	make_issues.make_github_issue(name, body="{}.\n\nSuggested in a large email containing many urls".format(url), labels=labels)
