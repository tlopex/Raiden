import requests
import hashlib
import json

url = 'https://hitokoto.limstash.com/score.php'
token = 'akHyJbNMhoR5KiFmZUzmysTtdKsFUivM6Kxnb0bP4g8OXR1K7fS86WLstKlaRZRc'

class Database(object):
    @staticmethod
    def request(action, data):
        data["action"] = action
        r = requests.post(url, data=data)
        return r
    
    @staticmethod
    def push(name, score, hp):
        encoded_checksum = (name + str(score) + str(hp) + token).encode()
        checksum = hashlib.sha3_512(encoded_checksum)
        
        data = {"name": name, "score": score, "hp": hp, "checksum": checksum.hexdigest()}
        result = Database.request("push", data)

        if result.status_code != 200 or result.text != "success":
            raise Exception(result.text)

    @staticmethod
    def get(limit):
        result = Database.request("get", {"limit":limit})

        if result.status_code != 200:
            raise Exception(result.text)

        return json.loads(s=result.text)
        

# database.push("test", 100, 10)
print(Database.get(8))
