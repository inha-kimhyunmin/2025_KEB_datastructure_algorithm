n, k = map(int, input().split())

pep = [x for x in range(1,n+1)]
result = list()

startpoint = 0
while pep:
    endpoint = (startpoint + k - 1) % len(pep)
    result.append(pep[endpoint])
    startpoint = endpoint
    pep.pop(endpoint)

print('<', end ='')
for i in range(len(result)):
    if i < len(result) - 1:
        print(result[i], end =', ')
    else:
        print(result[i], end ='>')