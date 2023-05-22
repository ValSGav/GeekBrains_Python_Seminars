values = [1, 23, 43, 'sdfasdf']
# def transformations(x): return x
transformation = lambda x: x


transformed_values = list(map(transformations, values))

if values == transformed_values:
    print("ok")
else:
    print("fail")
