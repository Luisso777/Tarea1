from collections import namedtuple

from pip._vendor.distlib.compat import raw_input

N = int(raw_input())
headers = raw_input()
studiantes = namedtuple('studiantes',headers)
sttudiantes = []
for i in range(N):
     sttudiantes.append(studiantes(*raw_input().split()))
print sum(list(map(lambda x: float(x.MARKS),sttudiantes)))/len(sttudiantes)