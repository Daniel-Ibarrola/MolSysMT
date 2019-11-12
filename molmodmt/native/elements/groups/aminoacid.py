from molmodmt.native.elements import Group

class AminoAcid(Group):

    def __init__(self, index=None, id=None, name=None, type=None):

        super().__init__(index=index, id=id, name=name, type=type)

        self.lettercode = None

