__author__ = 'Ioan Balaban'

lid = [5, 12, 7, 32, 1, 0, -4]
sorted = False

while not sorted:
    sorted = True
    for i in range(len(lid)-1):
      if lid[i + 1] < lid[i]:
        lio = lid[i]
        lid[i] = lid[i + 1]
        lid[i + 1] = lio
        sorted = False
    lio = lid
print(lio)

gasit = False
s = 8
while not gasit:
    gasit = True
    for i in range(len(lid)):
        for j in range(len(lid)):
            if lid[i] + lid[j] == s:
                gasit = True
if gasit == True:
    print('Am gasit')

