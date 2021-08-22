def f(n):
    flist = []
    for i in range(1,n+1):
        if n%i == 0:
            flist.append(i)
    return(flist)

def check_prime(n):
    return(f(n) == [1,n])

def primeproduct(n):
    for i in range(1,n+1):
        if n%i == 0:
            if check_prime(i) and check_prime(n//i):
                return(True)
    return(False)

def delchar(s,c):
  if len(c)==1:
    return(s.replace(c,''))
  else:
    return(s)
  
def shuffle(l1,l2):
  t=max(len(l1),len(l2))
  ans=list()
  for i in range(t):
    try:
      ans.append(l1[i])
    except:
      pass
    try:
      ans.append(l2[i])
    except:
      pass
  return(ans)


import ast

def tolist(inp):
  inp = "["+inp+"]"
  inp = ast.literal_eval(inp)
  return (inp[0],inp[1])

def parse(inp):
  inp = ast.literal_eval(inp)
  return (inp)

fncall = input()
lparen = fncall.find("(")
rparen = fncall.rfind(")")
fname = fncall[:lparen]
farg = fncall[lparen+1:rparen]

if fname == "primeproduct":
   arg = parse(farg)
   print(primeproduct(arg))
elif fname == "delchar":
   (s1,s2) = parse(farg)
   print(delchar(s1,s2))
elif fname == "shuffle":
   (l1,l2) = parse(farg)
   print(shuffle(l1,l2))
else:
   print("Function", fname, "unknown")