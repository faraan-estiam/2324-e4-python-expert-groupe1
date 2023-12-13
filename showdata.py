import json
with open('./data.json', 'r') as file :
    data = json.loads(file.read())
    data = data['nombre pronom']
    for k,v in data.items() :
        if v == 0:
            continue
        string = ''
        for i in range(v):
            string = string + '-'
        print(k,'\t',v,string)