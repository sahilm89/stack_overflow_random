from bigfloat import sub, add, mul, div, sqr, sqrt, precision

a=1e-8
b=10
c=1e-8
p = 100

D = sub(sqr(b) , mul(4, mul(a,c) ), precision(p))

x1 = div( - add(b , sqrt(D, precision(p))) , mul(2,a), precision(p))
x2 = div( - sub(b , sqrt(D, precision(p))) , mul(2,a), precision(p))

print x1,x2
