class Car(object):
    def __init__(self, reg_num, color):
        self.reg_num = reg_num
        self.color = color

    def __str__(self):
        return self.__dict__