class Event():
    def __init__(me,date,time,venue,budget):
        me.date=date
        me.time=time
        me.venue=venue
        me.budget=budget
    def cal_budget(me):
        me.budget=me.foodhead * me.particount
    def show(me):
        print("DATE:",me.date,"TIME:",me.time,"VENUE:",me.venue,"BUDGET:",me.budget)

class Conference(Event):
    def __init__(me,date,time,venue,budget,tracks,eventname,chiefguest):
        super().__init__(date,time,venue,budget)
        me.tracks=tracks
        me.eventname=eventname
        me.chiefguest=chiefguest
    def change_title(me,name):
        me.eventname=name
    def show(me):
        super().show()
        print("TRACK:",me.tracks,"EVENTNAME:",me.eventname,"CHIEF GUEST:", me.chiefguest)
    
class Birthday(Event):
    def __init__(me,date,time,venue,budget,returngift,celabratorname,cakeflav,foodhead,particount):
        super().__init__(date,time,venue,budget)
        me.returngift=returngift
        me.celabratorname=celabratorname
        me.cakeflav=cakeflav
        me.foodhead=int(foodhead)
        me.particount=int(particount)
    def change_flav(me,name):
        me.cakeflav=name
    def show(me):
        super().show()
        print("RETURN GIFT",me.returngift,"CELABRATOR NAME:",me.celabratorname,"CAKE FALVOUR",me.cakeflav,"FOOD PER HEAD",me.foodhead,"PARTY COUNT:",me.particount)

a=Conference("19-02-2025","4:45","ground","50000","swiftie","birthday","stefi shobika")
a.change_title("bachelors party")
a.show()

b=Birthday("19-02-2025","4:45","ground","50000","PLANT","SHAWN ELIJAH","CHOCOLATE TRUFFLE","130","100")
b.change_flav("RED VELVET")
b.show()
b.cal_budget()