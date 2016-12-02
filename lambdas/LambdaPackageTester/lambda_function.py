import json
import helper


def lambda_handler(event, context):
    helper.helper('Andrew')
    print(json.dumps(event, indent=4))
