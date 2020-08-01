import os
import json
import requests

class MpDatabase():
    ACCESS_TOKEN = ""
    ENV = ""

    def __init__(self):
        pass

    def databaseAdd(self):
        url = f'https://api.weixin.qq.com/tcb/databaseadd?access_token={self.ACCESS_TOKEN}'
        
        with open("./items.jl") as jl:
            lines = []
            for line in jl.readlines():
                lines.append(line)
            text = ','.join(lines)
        
        
        query = '''
        db.collection("test").add({
            data: [
                ''' + text + '''
            ]
        })
        '''
        data = {
            "env": self.ENV,
            "query": query
        }

        res = requests.post(url, data=json.dumps(data))
        res = json.loads(res.content.decode(encoding='utf-8'))
        return res
        


md = MpDatabase()
res = md.databaseAdd()
print(res)
