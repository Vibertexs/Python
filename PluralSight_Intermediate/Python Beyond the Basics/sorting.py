scientis = ['Albert Einstien', 'Charles Darwin', 'Issac Newton', 'Neils Bohr', 'Bilal Khan']
x = sorted(scientis, key=lambda name: name.split()[-1]) #-1 is last name; 0 is first name
print(x)