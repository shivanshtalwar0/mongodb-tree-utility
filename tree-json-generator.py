import bson
import json


def generate_json(letter, max_child_count, level):
    paren = {
        "_id": {
            "$oid": str(bson.objectid.ObjectId())
        },
        "parent": None,
        "name": letter
    }
    result = []
    stack = []
    lev = 0
    stack.append(paren)
    result.append(paren)
    while(len(stack) != 0 and lev < level):
        parent = stack.pop()
        for child_coun in range(0, max_child_count):
            child_object_id = {
                "$oid": str(bson.objectid.ObjectId())
            }
            item = {
                "_id": child_object_id,
                "parent": parent['_id'],
                "name": letter+"_{0}_{1}".format(child_coun, lev)
            }
            stack.append(item)
            result.append(item)

        lev = lev+1
    return result


result = []
# variation of tree names for stress testing with large datasets
variation = 1
# how many level deep should we go
depth = 5
# no of children each level of tree
max_child = 2

for char in ['A','B','C','D','E','F',"G",'H','I','J','K','L','M',"N",'O','P',"Q",'R','S','T','U','V','W','X','Y','Z']:
    for var in range(0,variation):
        result+=generate_json(char+str(var),max_child,depth)
with open('./test.json', 'w') as outfile:
    outfile.write(json.dumps(result))
