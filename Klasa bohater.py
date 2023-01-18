class Hero:
    def __init__(self,wiek,klasa):
        self.age=wiek
        self.level=1
        self.hclass=klasa
        self.points_to_spend=0
        self.level=1
        self.experience=0
        self.next_level=1000
        self.points=334
        if self.hclass=="wicher":
            self.power=1
            self.knowledge=3
        elif self.hclass=="warrior":
            self.power=3
            self.knowledge=1
        else:
            self.power=2
            self.knowledge=2
    def level_up(self):
        if self.hclass=="wicher":
            self.power=self.power+1
            self.knowledge=self.knowledge+2
            self.points_to_spend=self.points_to_spend+5
            self.level=self.level+1
        elif self.hclass=="warrior":
            self.power=self.power+3
            self.knowledge=self.knowledge+1
            self.points_to_spend=self.points_to_spend+4
            self.level=self.level+1
        else:
            self.power=self.power+2
            self.knowledge=self.knowledge+2
            self.points_to_spend=self.points_to_spend+4
            self.level=self.level+1
    def stats(self):
        print(self.level)
        print(self.hclass)
        print(self.points_to_spend)
        print(self.power)
        print(self.knowledge)
        print(self.experience)
    def add_experience(self):
        self.experience=self.experience+self.points
        if self.experience>self.next_level:
            self.experience=self.experience-self.next_level
            self.next_level=self.next_level*2
            self.level_up()
        else:
            pass

Geralt=Hero(20,"witcher")