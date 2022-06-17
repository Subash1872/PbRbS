 # using flask_restful
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import pickle

app = Flask(__name__)
api = Api(app)
@app.route('/display',methods=['GET'])
def display():
    return 'Hello'

@app.route('/prediction',methods=['POST'])
def post():
    pred=None
    data1 = request.get_json()	 # status code
    line = list(data1.values())
    for a in range(len(data1)):
        if(line[a] == 'Yes'):
            line[a] = 1
        if(line[a] == 'No'):
            line[a] = 0
    line.pop(0)
    line.pop(0)
    line.pop(1)
    line.pop(1)
    count_major = count_minor = 0
    if line[0]<24:
        line1,line2=line[1:6],line[6:13]
        if((sum(line1)>=2) or sum(line2)>=3 or (sum(line1)>=1 and sum(line2)>=1)):
            return {"Class":"Screen Immediately"}
        elif((sum(line1)>=1) or sum(line2)>=2):
            return {"Class":"Screen after one month"}
        else:
            return {"Class":"No risk"}

    if line[0]<36:
        line1,line2=line[1:7],line[8:15]
        if((sum(line1)>=2) or sum(line2)>=3 or (sum(line1)>=1 and sum(line2)>=1)):
            return {"Class":"Screen Immediately"}
        elif((sum(line1)>=1) or sum(line2)>=2):
            return {"Class":"Screen after one month"}
        else:
            return {"Class":"No risk"}
            
    if line[0]<48:
        line1,line2=line[1:7],line[8:14]
        if((sum(line1)>=2) or sum(line2)>=3 or (sum(line1)>=1 and sum(line2)>=1)):
            return {"Class":"Screen Immediately"}
        elif((sum(line1)>=1) or sum(line2)>=2):
            return {"Class":"Screen after one month"}
        else:
            return {"Class":"No risk"}

if __name__ == '__main__':
	app.run(debug=True,host='0.0.0.0')
