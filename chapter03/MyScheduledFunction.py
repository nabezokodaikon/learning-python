import json

def lambda_handler(event, context):
    print('Hello')
    print(json.dumps(event))

#  {
        #  "action": "0001",
        #  "eventname": "foobar"
#  }
