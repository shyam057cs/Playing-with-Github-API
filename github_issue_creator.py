__author__ = 'Syam Sankar'

import json
from urllib2 import urlopen, Request, HTTPError

import poplib
import re
from email import parser

MY_GITHUB_URL = "https://api.github.com/repos/shyam057cs/Playing-with-Github-API/issues"
MY_TOKEN = "valid token"

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



def main():
    pop_conn = poplib.POP3_SSL('pop.gmail.com')
    pop_conn.user('devil057cs')
    pop_conn.pass_('plugin1234')

    regex = re.compile("<([a-zA-Z]+).*?>(.*?)</\\1>")
    #Get messages from server:
    messages = [pop_conn.retr(i) for i in range(1, len(pop_conn.list()[1]) + 1)]
    # Concat message pieces:
    messages = ["\n".join(mssg[1]) for mssg in messages]
    #Parse message intom an email object:
    messages = [parser.Parser().parsestr(mssg) for mssg in messages]
    extracted_body = "Empty Description"
    for message in messages:
        for part in message.walk():
            if part.get_content_type():
                body = part.get_payload(decode=True)
        extracted_body=  regex.findall(body)[0][1]
        create_issue(message['subject'], extracted_body)
    pop_conn.quit()

if __name__ == '__main__':
    main()

