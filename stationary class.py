class Shop:
    def __init__(me, code,name, price,stock):
        me.code=code
        me.name=name
        me.price=price
        me.stock=stock
    def display(me):
        print("The code of the item is:",me.code)
        print("The name of the item is:", me.name)
        print("The price of the item is:", int(me.price))
        print("The stock of the item is:", int(me.stock))
        print("\n")
    def change(me,a):
        me.stock+=a
    def purchase(me,qty):
        if me.stock>=qty:
            me.stock-=qty
            print(me.code,me.name,qty)
            print("the price of the product is:",qty*me.price)
        else:
            print("sorry quantity not available")
    def search(me,code):
        code=int(input("enter code of the product"))
        if code==me.code:
            print("The details of the product is:", me.code,me.name,me.stock,me.price)
        else:
            print("The code doesnt exist")
    def search(me,name):
        if (me.name==name):
            return me
        else:
            return me
            
mycls=Shop(111,"pen",10,50)
mycls2=Shop(234,"ruler",5,100)
mycls3=Shop(290,"eraser",3,67)
obj=[mycls,mycls2,mycls3]
for i in obj:
    i.display()
sr_item="eraser"
for i in obj:
    re_obj=i.search(sr_item)
    if (re_obj!=False):

        break
mycls.display()
mycls.change(20)
mycls.display()
mycls.purchase(20)
mycls.display()
