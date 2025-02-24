dict = {'key1':'value1','key2':'value2'}
print(dict)
print(dict['key2'])

price_lookup = {'apple':5.0,'oranges':6.8,'milk':9.5}
print(price_lookup['apple'])

d = {'apple':5.55,'list1':['apple','oranges','milk'],'key':{'oranges':6.66}}

print(d['key']['oranges'])

d['key']['oranges'] = 9.9

print(d.keys())

print(d.items())