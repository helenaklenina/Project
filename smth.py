import requests
import time

r2 = requests.get('https://api.vk.com/method/groups.getLongPollServer?',
                  params={'group_id': '179378864',
                          'access_token': 'c77108dcb98bfcba34d6e1677a95f543b0f6f3de916b192392edaffda02653d57b28e464a0474a0b6f4b3',
                          'v': '5.95'})
print(r2)
print(r2.text)
print(r2.json())

serv = r2.json()['response']['server']
key = r2.json()['response']['key']
ts = r2.json()['response']['ts']

serv += '?'
b1 = {"action": {
          "type": "text", 
          "payload": "{\"button\": \"1\"}", 
          "label": "Red" 
        }, 
        "color": "negative"
      }
b2 = {
        "action": { 
          "type": "text", 
          "payload": "{\"button\": \"2\"}", 
          "label": "Green" 
        }, 
        "color": "positive" 
      }
b3 = {
        "action": { 
          "type": "text", 
          "payload": "{\"button\": \"3\"}", 
          "label": "White" 
        }, 
        "color": "default" 
      }
b4 = {
        "action": { 
          "type": "text", 
          "payload": "{\"button\": \"4\"}", 
          "label": "Blue" 
        }, 
        "color": "primary" 
      }

kb = [b1,b2,b3,b4]
print(serv, ts)

while 5 < 10:
    r3 = requests.get(serv, params={'act': 'a_check', 'key': key, 'ts': ts})
    print(r3.json())
    if 'updates' in r3.json():
        l = list(r3.json()['updates'])
        for d in l:
            if 'object' in d:
                print('Победа')
                if 'from_id' in d['object']:
                    r = requests.get('https://api.vk.com/method/users.get?',
                                     params={'access_token': 'c77108dcb98bfcba34d6e1677a95f543b0f6f3de916b192392edaffda02653d57b28e464a0474a0b6f4b3',
                                    'v': '5.92',
                                    'user_ids': d['object']['from_id']})
                    print(r.json())
                    r = requests.get('https://api.vk.com/method/messages.send?',
                                     params={'user_id': d['object']['from_id'],
                                             ''' 'buttons'[{
                                                                      "action": {
                                                                           "type": "text",
                                                                           "payload": "{\"button\": \"1\"}",
                                                                           "label": "Red"
                                                                       },
                                                                       "color": "negative"
                                                                   },
                                                                   {
                                                                       "action": {
                                                                           "type": "text",
                                                                           "payload": "{\"button\": \"2\"}",
                                                                           "label": "Green"
                                                                       },
                                                                       "color": "positive"
                                                                   },
                                                                   {
                                                                       "action": {
                                                                           "type": "text",
                                                                           "payload": "{\"button\": \"3\"}",
                                                                           "label": "White"
                                                                       },
                                                                       "color": "default"}],
                    '''
                                             'random_id': 0,
                                             'message': 'Привет',
                                             'group_id': '179378864',
                                             'keyboard': kb,
                                             'access_token': 'c77108dcb98bfcba34d6e1677a95f543b0f6f3de916b192392edaffda02653d57b28e464a0474a0b6f4b3',
                                             'v': '5.95',
                                             })
                    rk = requests.get('https://api.vk.com/method/users.get?',
                                     params={
                                         'access_token': 'c77108dcb98bfcba34d6e1677a95f543b0f6f3de916b192392edaffda02653d57b28e464a0474a0b6f4b3',
                                         'v': '5.95',
                                         'user_ids': d['object']['from_id']})
                    print(rk.json())
                    print(r)
                    print(r.text)
    ts = r3.json()['ts']
    time.sleep(0.1)