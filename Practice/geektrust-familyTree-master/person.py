class Person:
    """
    information about person his parents, sister and brother
    """
    brothers = []
    sisters = []

    def __init__(self, name, sex, mother=None, father=None):
        """
        assigns parents for the person
        :param name:name of person, who is going to be added as son and daughter
        :param sex: sex of person "M" for male, "F" for female
        :param mother: mother as a instance of Person class
        :param father: Father as a instance of Person class
        """
        self.name = name
        self.sex = sex
        self.mother = mother
        self.father = father
        self.sons = []
        self.daughters = []
        self.spouse = None
        self.generation = None

    def add_child(self, child):
        """
        adds son into persons son's list
        :param child: child as a instance of Person class
        """
        if child.sex == "M":
            self.sons.append(child)
        else:
            self.daughters.append(child)

    def add_spouse(self, spouse):
        """
        adds a person as spouse of this person
        :param spouse: a Person instance of a person, who is going to get married to this person
        """
        self.spouse = spouse

    @staticmethod
    def get_brothers(person):
        """
        gets a list of brothers of given person
        :param person: person an Instance of Person
        :return: a list of brothers(Instances of Person Class) of given person
        """
        if person is None:
            return []
        brothers_list = []
        if person.father:
            brothers_list = person.father.sons.copy()
            if person in brothers_list:
                brothers_list.remove(person)
        return brothers_list

    @staticmethod
    def get_sisters(person):
        """
        gets a list of sisters of given person
        :param person: person an Instance of  Person Class
        :return: a list of sisters(Instances of Person Class) of given person
        """
        if person is None:
            return []
        sisters_list = []
        if person.father:
            sisters_list = person.father.daughters.copy()
            if person in sisters_list:
                sisters_list.remove(person)
        return sisters_list

    @staticmethod
    def get_children(person):
        """
        :param person: person an Instance of Person class, that given Familys relatives are going to be retrieved
        :return: a list of person objects of children of that given person
        """
        if person is None:
            return []
        return person.sons + person.daughters

    @staticmethod
    def get_grand_daughter(person):
        offsprings = person.sons + person.daughters
        grand_daughters = []
        for person in offsprings:
            grand_daughters.extend(person.daughters)
        return grand_daughters

    @staticmethod
    def get_mother(person):
        if person.mother:
            return [person.mother]
        return []

    @staticmethod
    def get_father(person):
        if person.father:
            return [person.father]
        return []

    @staticmethod
    def get_sons(person):
        return person.sons

    @staticmethod
    def get_daughters(person):
        return person.daughters
