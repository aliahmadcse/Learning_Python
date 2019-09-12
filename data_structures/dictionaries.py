# point={'x':1,'y':2}

point=dict(x=1,y=2)
# print(point['x'])
print(point.get('a',-1))
for key,value in point.items():
    print(key,value)