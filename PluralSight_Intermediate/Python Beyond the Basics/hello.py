def hello(immutable):
    if immutable:
        cls = tuple
    else:
        cls = list
    return cls

seq = hello(immutable=True) #T in true has to be capital

t = seq("Bilal")
print(t)