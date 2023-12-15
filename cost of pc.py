#find cost of computers
cost=int(input("enter cost of one computer: "))
num=int(input("enter number computers: "))
cc=cost*num
print("cost of computers is ",cc,"\n")

#find the cost of furnitures
tnum=int(input("enter number of tables: "))
tcost=int(input("enter cost of one table: "))
cnum=int(input("enter number of chairs: "))
ccost=int(input("enter the cost of one chair: "))
tc=tnum*tcost+cnum*ccost
print("cost of furniture ",tc,"\n")

#fint the labour cost
hwork=int(input("enter number of hours worked: "))
whour=int(input("enter the wage for one hour: "))
lc=hwork*whour
print("labour cost is ",lc,"\n")

totalcost=cc+tc+lc
print("total cost is",totalcost)
