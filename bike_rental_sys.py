class bikeshop:
    def __init__(self,stock):
        self.stock = stock

    def displaybike(self):
        print("Total Bike", self.stock)

    def rentforbike(self,q):

        if q <= 0 :
            print("Enter the positive value or greater than zero")

        elif q>self.stock :
            print("Enter the value less than stock")

        else:
            print("Total Price is ", q*1000)
            print("Total bikes is ", self.stock -q)

while True:
    obj = bikeshop(500)
    uc = int(input("""
---------------------------------------------------------------------------------------
1- Display Stocks
2- Rent a bike
3- Exit

Enter your Choice: """))

    if uc==1:
        obj.displaybike()
    elif uc==2:
        n = int(input("Enter qty of bikes you want...."))
        obj.rentforbike(n)
    else:
        break
    continue




