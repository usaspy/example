import pickle
import json

d = {'name':'','num':1102}
try:
    f = open('d:/dump1.txt','w')
    json.dump(d,f)
finally:
    f.close()

try:
    f = open('d:/dump1.txt','r')
    json_str=json.load(f)
    print(json_str)
    print(json_str['num'])
    print(json_str['name'])


finally:
    f.close()
