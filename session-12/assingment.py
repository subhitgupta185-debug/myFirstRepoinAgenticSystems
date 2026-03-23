import json

data = ''' {
  "id": "req_123",
  "status": "success",
  "result": {
    "text": "Hello world",
    "confidence": 0.98
  }
}
'''

a = json.loads(data)

request_id = a["id"]
status = a["status"]
text_result = a["result"]["text"]
confidence_score = a["result"]["confidence"]

print("Your request ID : ",request_id)
print("Your status: " , status)
print("text_result : ", text_result )
print("Your confidence level : ", confidence_score)


if confidence_score < 0.9:
    print("warning : Low confidence level")


follows_up = {
    "request_id" : request_id,
    "status" : "Processed",
    "original status" : status,
}

json_output = json.dumps(follows_up, indent = 4)

with open("response.json", "w") as file :
    file.write(json_output)