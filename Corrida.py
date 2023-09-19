p = list(map(int,input().split()))
m = list(map(int,input().split()))
f = list(map(int,input().split()))
q = list(map(int,input().split()))
b = list(map(int,input().split()))
total = int(input())

p.pop(o)
m.pop(o)
f.pop(o)
q.pop(o)
b.pop(o)

p.sort()
m.sort()
f.sort()
q.sort()
b.sort()

precos = []

for i in range(len(p)):
    for j in range(len(m)):
        for k in range(len(f)):
            for l in range(len(q)):
                for m in range(len(b)):
                    x = port[i] + mat[j] + fis[k] + quim[m] + bio[n]
                    precos.append(x)
precos.sort(reverse=True)
result = 0
for i in range(total):
    result += precos[i]

print(result)