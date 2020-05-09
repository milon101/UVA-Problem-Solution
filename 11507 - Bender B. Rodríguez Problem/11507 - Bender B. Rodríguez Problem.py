import sys

input = sys.stdin
fields = []

bends={
       '+x': {'+y': '+y', '-y': '-y', '+z': '+z', '-z': '-z'}, 
       '-x': {'+y': '-y', '-y': '+y', '+z': '-z', '-z': '+z'}, 
       '+y': {'+y': '-x', '-y': '+x', '+z': '+y', '-z': '+y'}, 
       '-y': {'+y': '+x', '-y': '-x', '+z': '-y', '-z': '-y'}, 
       '+z': {'+y': '+z', '-y': '+z', '+z': '-x', '-z': '+x'}, 
       '-z': {'+y': '-z', '-y': '-z', '+z': '+x', '-z': '-x'} 
       }

while(True):
    n=int(input.readline())
    if n == 0:
        break
    else:
        fields.append(input.readline().split())

for i in fields:
    wire='+x'
    for j in i:
        if j != 'No':
            wire = bends[wire][j]
    print(wire)
