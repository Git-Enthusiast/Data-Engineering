# TASK: Improve this program WITHOUT changing what it prints.
# Run it first and note the three numbers it prints.
def calc(a,b):
    x=a*b
    if x>100:
        x=x-(x*0.1)
    print(x)
def CalcTwo(A,B):
    X=A*B
    if X>100 :
      X=X-(X*0.1)
    print(X)
def f(p,q,r):
    t=p*q
    if t>100:
        t=t-(t*0.1)
    t=t+(t*r)
    print(t)
calc(100,3)
CalcTwo(20,10)
f(50,4,0.2)
