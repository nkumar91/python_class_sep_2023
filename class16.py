# import datetime
# datetime = datetime.datetime.now()
# print(datetime.strftime("%I:%M %p %f"))

import json
x =  '{ "name":"John", "age":30, "city":"New York"}'
z = json.loads(x)
print(z)


list  = [{"val":10},{"val":20},{"val":30},{"val":40}]

print(type(json.dumps(list)))


#OOPS

