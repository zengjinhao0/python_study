


class Parent:
    def myMethon(self):
        print('調用父類方法')

class Child(Parent):
    def myMethon(self):
        print('調用子类方法')


c=Child()
c.myMethon()
super(Child,c).myMethon()
