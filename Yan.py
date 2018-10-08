import json

datapath = r'C:\Users\A9204\Documents\GitHub\YanData\Yan.json'

file = open(datapath,encoding='utf-8').read()
data = dict(json.loads(file))['list']
tags = [i['tag'] for i in data]
yan  = [i['yan'] for i in data]

for i,j in zip(tags,yan):
    print(i)
    print(j)
    print('\n')