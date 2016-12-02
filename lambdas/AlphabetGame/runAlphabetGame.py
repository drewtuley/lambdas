import json

from lambdas.AlphabetGame import alphabetGameAlpha

event_s = '''{
  "session": {
    "sessionId": "SessionId.0b119e53-52bc-4d8a-90dc-9f185fab0ab8",
    "application": {
      "applicationId": "amzn1.ask.skill.6f076142-1bf5-4fd2-9154-28afbc2d105c"
    },
    "attributes": {},
    "user": {
      "userId": "amzn1.ask.account.AGMFW4OGY5XT2T3WJ6X22OAB7DQCII44WMJNCQOOXRO22EUEECIZUMICMV2I7AIXQ7VFHOSTFQFDWKBKPXV3VQ6XM2C4SMTPBHWWTQMGK662DUVTDABBZAZA3J43I7W2J74MQCWS7T6KR7WAXRMUA7W47IMSU2S7U6KMUTRGCG7U4WEPTYRZBEYK3CJGKG7C7F4SBS2UGBADRWQ"
    },
    "new": true
  },
  "request": {
    "type": "IntentRequest",
    "requestId": "EdwRequestId.481600ad-a27f-4855-9b4a-b5d6d8a9926e",
    "locale": "en-GB",
    "timestamp": "2016-11-25T13:31:17Z",
    "intent": {
      "name": "PlayAlphabetGame",
      "slots": {
        "Category": {
          "name": "Category",
          "value" : "Animals"
        }
      }
    }
  },
  "version": "1.0"
}'''
event = json.loads(event_s)
context = {}
responseJson = alphabetGameAlpha.lambda_handler(event, context)
#print(event_s)
#print(responseJson)
print json.dumps(responseJson, sort_keys=True,
              indent=4, separators=(',', ': '))


event_launch = '''{
  "session": {
    "sessionId": "SessionId.eac7e3d0-c211-4639-921a-a6de10347d5c",
    "application": {
      "applicationId": "amzn1.ask.skill.6f076142-1bf5-4fd2-9154-28afbc2d105c"
    },
    "attributes": {},
    "user": {
      "userId": "amzn1.ask.account.AGMFW4OGY5XT2T3WJ6X22OAB7DQCII44WMJNCQOOXRO22EUEECIZUMICMV2I7AIXQ7VFHOSTFQFDWKBKPXV3VQ6XM2C4SMTPBHWWTQMGK662DUVTDABBZAZA3J43I7W2J74MQCWS7T6KR7WAXRMUA7W47IMSU2S7U6KMUTRGCG7U4WEPTYRZBEYK3CJGKG7C7F4SBS2UGBADRWQ"
    },
    "new": true
  },
  "request": {
    "type": "LaunchRequest",
    "requestId": "EdwRequestId.1904cb6d-e103-46ad-9d73-d5680108f7c0",
    "locale": "en-US",
    "timestamp": "2016-11-29T13:44:57Z"
  },
  "version": "1.0"
}
'''

event = json.loads(event_launch)
context = {}
responseJson = alphabetGameAlpha.lambda_handler(event, context)
#print(event_s)
#print(responseJson)
print json.dumps(responseJson, sort_keys=True,
              indent=4, separators=(',', ': '))