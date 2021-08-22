n = int(input())
m = int(input())

fn = []
for i in range(1,n+1):
    if n%i == 0:
        fn.append(i)

fm = []
for j in range(1,m+1):
    if m%j == 0:
        fm.append(j)

cf = []
for f in fn:
    if f in fm:
        cf.append(f)

print(cf[-1])