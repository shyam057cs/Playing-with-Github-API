__author__ = 'Syam Sankar'

import json
from urllib2 import urlopen, Request, HTTPError

MY_GITHUB_URL = "https://api.github.com/repos/shyam057cs/Playing-with-Github-API/issues"
MY_TOKEN = "valid_token"

def create_issue(title,body,url = MY_GITHUB_URL, token = MY_TOKEN, ):
    data = json.dumps({ "title": title, "body": body})

    request = Request(url)
    request.add_data(data)
    request.add_header('Authorization', 'token %s' % token)

    try:
        response = urlopen(request).read()
    except HTTPError, err:
        print "Unable to create the issue. Error:" + err
    else:
        print 'Successfully created the issue.'

        parsed = json.loads(response)
        return json.dumps(parsed, indent=4, sort_keys=True)

if __name__ == '__main__':
    create_issue("new title issue", "new body")

