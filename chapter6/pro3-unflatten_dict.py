def unflatten(d):
    result = {}
    for k,v in d.iteritems():
        if '.' in k:
            k1, k2 = k.split('.', 1)
            v = {k2: v}
            k = k1
        result[k] = v
    return result
print unflatten({'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4})
