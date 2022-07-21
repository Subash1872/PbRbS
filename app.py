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
    yes_list=[[1,2,3,4,5,6,7,8,9,10,11,12,13],[1,2,3,4,5,6,9,10,11],[1,3,4,5,6,7,13,14],[2,3,5,9,10,11]]
    line = list(data1.values())
    line.pop(0)
    line.pop(0)
    line.pop(1)
    line.pop(1)
    count_major = count_minor = 0

    for a in range(1,len(line)):
        if(line[a] == 'Yes'):
            line[a] = 0
        if(line[a] == 'No'):
            line[a] = 1

    if(line[0]<=24):
        tar_list=yes_list[0]
    elif(line[0]<=36):
        tar_list=yes_list[1]
    elif(line[0]<=48):
        tar_list=yes_list[2]
    else:
        tar_list=yes_list[3]

    for i in range(1,len(line)):
        if i not in tar_list:
            #print(i)
            if(line[i]==1):
                line[i]=0
            else:
                line[i]=1   

    if line[0]<24:
        line1,line2=line[1:7],line[8:]
        #print(sum(line1))
        if((sum(line1)>=2) or sum(line2)>=3 or (sum(line1)>=1 and sum(line2)>=1)):
            return {'Class':'Screen Immediatly'}
        elif((sum(line1)>=1) or sum(line2)>=2):
            return {'Class':'Screen After one month'}
        else:
            return {'Class':'No risk'}

    if line[0]<36:
        line1,line2=line[1:8],line[9:]
        if((sum(line1)>=2) or sum(line2)>=3 or (sum(line1)>=1 and sum(line2)>=1)):
            return {'Class':'Screen Immediatly'}
        elif((sum(line1)>=1) or sum(line2)>=2):
            return {'Class':'Screen After one month'}
        else:
            return {'Class':'No risk'}

    if line[0]<48:
        line1,line2=line[1:10],line[11:]
        if((sum(line1)>=2) or sum(line2)>=3 or (sum(line1)>=1 and sum(line2)>=1)):
            return {'Class':'Screen Immediatly'}
        elif((sum(line1)>=1) or sum(line2)>=2):
            return {'Class':'Screen After one month'}
        else:
            return {'Class':'No risk'}

    if line[0]<72:
        line1,line2=line[1:6],line[7:]
        if((sum(line1)>=2) or sum(line2)>=3 or (sum(line1)>=1 and sum(line2)>=1)):
            return {'Class':'Screen Immediatly'}
        elif((sum(line1)>=1) or sum(line2)>=2):
            return {'Class':'Screen After one month'}
        else:
            return {'Class':'No risk'}

if __name__ == '__main__':
	app.run(debug=True,host='0.0.0.0')
