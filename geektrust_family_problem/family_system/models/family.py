class Family(object):
    def __init__(self, name, king, queen,family_members=None):
        if family_members is None:
            family_members = []
        self.name = name
        self.king = king
        self.queen = queen
        self.family_members = family_members

    def add_family_member(self, family_member_obj):
        self.family_members.append(family_member_obj)

    def __unicode__(self):
        return self.__dict__

    def __repr__(self):
        return str(self.__dict__)

