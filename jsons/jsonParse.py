import json
data = ""


def jsonParse(topic, msgPayload):
    global data
    if topic == "RedTeam":
        if msgPayload != "":
            jsonData = json.loads(msgPayload)
            data = jsonData
            return data

def getData():
    global data
    if data == "":
        return None
    else:
        return data
