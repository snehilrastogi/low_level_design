class Person(object):
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
        self.spouse = None
        self.is_part_of_shan = False
        self.generation = -1
        self.sons = []
        self.daughters = []
        self.father = None
        self.mother = None

    def set_spouse(self, spouse):
        self.spouse = spouse

    def set_is_part_of_shan(self, is_part):
        self.is_part_of_shan = is_part

    def set_generation(self, gen):
        self.generation = gen

    def add_son(self, son):
        self.sons.append(son)

    def add_daughter(self, daughter):
        self.daughters.append(daughter)

    def set_father(self, father):
        self.father = father

    def set_mother(self, mother):
        self.mother = mother

    def __unicode__(self):
        return self.__dict__

    def __repr__(self):
        return str(self.__dict__)