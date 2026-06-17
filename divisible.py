print("enter a Number (numberator)")
numn = int(input())
print("enter a Number (denominator)")
numd = int(input())

if numn % numd==0:
    print("\n" +str(numn)+" is divisble by" +str(numd))
else:
    print("\n" +str(numn)+" is not divisble by" +str(numd))