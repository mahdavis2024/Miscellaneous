import requests
import datetime
import time

#just a fun thing.
def ping_github():

    '''Whenever I am actively studying this program pings to motivate me. Go me!'''
    
    print('I am studying PY & ML.')
    url = 'https://api.github.com/user/repos'
    headers = {
        'Authorization': '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',
        'Accept': 'application/vnd.github.v3+json'
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        print('Ping successful at', datetime.datetime.now())
    else:
        print('Ping failed at', datetime.datetime.now())

# Run the ping_github function every 5 minutes
while True:
    ping_github()
    time.sleep(300)  # 300 seconds = 5 minutes
