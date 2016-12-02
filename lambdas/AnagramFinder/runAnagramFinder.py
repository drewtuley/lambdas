from lambdas.AnagramFinder import lambda_function
import json
import time


test1 = '''{
  "session": {
    "sessionId": "SessionId.98386ffc-2151-4fe2-a509-e3c6357e74d7",
    "application": {
      "applicationId": "amzn1.ask.skill.1ae70e31-d311-4c01-95e5-2c3531a3de5d"
    },
    "attributes": {},
    "user": {
      "userId": "amzn1.ask.account.AFPD2H7GWHEJAYTO7YMNJ4A4TZKKWIXFWSSTT2TZIOF7EPAZSLEKV4GOCOKU5MXAI5QWK62ONZ5H6WPWPWBYKOWLZGH23EXQ3BUMMQLLU23AQPMZRL52UABWEA76QXWN7IICEED4LC2TT7UVDPQLL54RNMXHHKURJPWXOYCSYNCCMLOIEJWFKLTUNLM3LOUYMSGOABI3KGXCPZA"
    },
    "new": true
  },
  "request": {
    "type": "IntentRequest",
    "requestId": "EdwRequestId.7ddd64e2-99ad-462f-88bc-2ca08987c0c4",
    "locale": "en-GB",
    "timestamp": "2016-12-01T10:42:59Z",
    "intent": {
      "name": "SolveAnagramIntent",
      "slots": {
        "Words": {
          "name": "Words",
          "value": "liars"
        }
      }
    }
  },
  "version": "1.0"
}'''
context = {}
event = json.loads(test1)
start = time.time();
responseJson = lambda_function.lambda_handler(event, context)
print('elapsed={}'.format(time.time()-start))
print json.dumps(responseJson, sort_keys=True,
              indent=4, separators=(',', ': '))

