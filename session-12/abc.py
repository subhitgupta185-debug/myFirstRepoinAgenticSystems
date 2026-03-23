import json

data = '''{
"user_id" : "user_789",
"status" : "completed", 
"response" : {
        "message" : "Task executed succesfully",
        "accuracy" : 0.82    
    }
}
'''
dict = json.loads(data)

user_id = dict["user_id"]
status = dict["status"]
message = dict["response"]["message"]
accuracy_score = dict["response"]["accuracy"]

print("Your user id : ", user_id)
print("status : ", status)
print("your message : ", message)
print("accuracy", accuracy_score)


if accuracy_score < 0.85:
    print("warning : Your accuracy is low")

follow_up = {
    "status" : "completed",
    "accuracy" : 0.82,
    "original accuracy" : accuracy_score
}

result = json.dumps(follow_up, indent = 4)

with open("abc.json", "w") as f:
    f.write(result)