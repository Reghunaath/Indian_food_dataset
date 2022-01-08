from flask import Flask,request,jsonify
import requests as r
import json
app=Flask(__name__)
@app.route('/api',methods=['GET'])
def start():
    url = 'http://192.168.0.151:8090/json-rpc'
    if(request.args['m']=='color'):
        myobj = {
          "command": "color",
          "color": json.loads(request.args['c']),
          "priority": 50,
          "origin": "My Fancy App"
        }
    elif(request.args['m']=='effect'):
        myobj = {
          "command": "effect",
            "effect":{
           "name":request.args['c']
           },
          "priority": 50,
          "origin": "My Fancy App"
        }
    x = r.post(url,  json=myobj,headers = {"Authorization": "token 46a2032e-da1b-4c20-b690-27413aa43589"})
    #print(x)
    return x.json()
if __name__ == '__main__':
    app.run(host='192.168.0.243')
