"""
封装ElasticSearch搜索引擎的SDK(library库)
"""
import requests
from dao import DB


class ESearch():
    def __init__(self,index):
        self.host = '121.199.63.71'
        self.port = '9201'
        self.index = index

    def create_index(self):
        url = f'http://{self.host}:{self.port}/{self.index}'
        # ES基于json数据进行交互所以上传的数据必须是json格式的数据
        # resp是请求响应的，通过resp.json()获取请求的json
        resp = requests.put(url,json={
                    "setting":{
                        "number_of_shards":5,
                        "number_of_replicas":1
                    }
                })
        resp_data = resp.json()
        if resp_data.get('acknowledged'):
            print("create index %s ok!" % self.index)

    def add_doc(self,doc_type,id=None,**values):
        url = f'http://{self.host}:{self.port}/{self.index}/{doc_type}/'
        if id:
            url += f"{id}"
        resp = requests.post(url,json=values)
        resp_data = resp.json()
        if resp_data.get("result") == "created":
            print("add doc %s ok!" % values)
        else:
            print("add doc %s error!" % values)

    def query(self,keyword):
        url = f'http://{self.host}:{self.port}/{self.index}/_search?/'
        resp = requests.get(url)
        resp_data = resp.json()
        if resp_data.get('hits').get('total') > 0:
            return {
                'code':1,
                'total': resp_data.get('hits').get('total'),
                'data':[data
                    for data in resp_data.get('hits').get('hits')
                ]
            }
        else:
            return {"code":1,"msg":"无"}

def init_index():
    # 连接数据库，将表数据添加到索引库中
    db = DB()
    # 查库

    es_ = ESearch('')

    pass