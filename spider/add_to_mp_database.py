import os
import json
import requests
from dotenv import load_dotenv

project_folder = os.path.expanduser('~/gamer_news')
load_dotenv(os.path.join(project_folder, '.env'))


class MpDatabase():
    """push items.jl to wechat mini program database"""
    APPID = os.environ.get('WX_APPID')
    APPSECRET = os.environ.get('WX_APPSECRET')
    ENV = "gamer-news-vmczg"

    def __init__(self):
        pass

    def process_json_response(self, response):
        response.raise_for_status()

        j = response.json()
        print(j)

        errcode = j.get("errcode")
        if errcode:
            raise Exception(errcode)

        return j

    def getAccessToken(self):
        url = f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={self.APPID}&secret={self.APPSECRET}"

        res = requests.get(url)
        data = self.process_json_response(res)

        self.ACCESS_TOKEN = data["access_token"]
        


    def databaseAdd(self, file_path):
        if not os.path.exists(file_path) or not os.path.isfile(file_path):
            raise Exception(f"check file: {file_path}")

        if os.stat(file_path).st_size == 0:
            raise Exception(f"Empty file: {file_path}")

        url = f'https://api.weixin.qq.com/tcb/databaseadd?access_token={self.ACCESS_TOKEN}'
        
        news = {"data": []}
        with open(file_path) as jl:
            lines = []
            for line in jl.readlines():
                news["data"].append(json.loads(line))
        
        query = '''
        db.collection("news")
          .add({})
        '''.format(news)

        body = {
            "env": self.ENV,
            "query": query
        }

        res = requests.post(url, data=json.dumps(body))
        j = self.process_json_response(res)

        return j
        


if __name__ == "__main__":
    md = MpDatabase()
    md.getAccessToken()
    md.databaseAdd("./items.jl")
