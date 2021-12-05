from person import Person


class Family:
    """
    Handles a family members and gives information about the members through functions
    """
    members = []
    relation_list = ["Brothers", "Sisters", "Cousins", "Paternal Uncles",
                     "Maternal Uncles", "Paternal Aunts", "Maternal Aunts",
                     "Brother in laws", "Sister in laws", "Mother",
                     "Father", "Children", "Son", "Daughter", "Granddaughter"]

    def __init__(self, leader_man):
        """
        fundamental person for a family(right now its king), with that Man, we will start a family
        :param leader_man: first man in the family
        """
        self.leader_man = leader_man
        self.members.append(leader_man)

    def marriage_of_a_family_member(self, member, spouse):
        """
        new wedding in family, spouse is new person in family
        :param member: member of the family, who is going to get married
        :param spouse: new person who is going to get married to family member and going to added in family
        """
        member.add_spouse(spouse)
        spouse.add_spouse(member)
        # set the generation number tp new spouse member in family
        spouse.generation = member.generation
        self.add_member_in_family(spouse)

    def add_new_born(self, parent_name, child_name, sex):
        """
        adds a new born to family and also to its parents
        :param parent_name: parent name either of mother or father
        :param child_name: new child name, which is going to be added in family
        :param sex: child sex
        """
        parent = self.find_member_by_name(parent_name)
        if parent is None:
            print("No person name " + parent_name)
        if parent.spouse is None:
            print("Single parent can't have children")
        if parent.sex == "M":
            child = Person(child_name, sex, mother=parent.spouse, father=parent)
            child.generation = parent.generation + 1
            Family.connect_new_born_to_parent(child, [parent, parent.spouse])
        else:
            child = Person(child_name, sex, mother=parent, father=parent.spouse)
            child.generation = parent.generation + 1
            Family.connect_new_born_to_parent(child, [parent, parent.spouse])
        self.add_member_in_family(child)

    @staticmethod
    def connect_new_born_to_parent(child, parents):
        """
        Connects a child(a Person object) to its parents(adding into sons and daughters list)
        :param child: Child who is going to get added into list of sons or daughters
        :param parents: list of parents of child
        """
        if child.sex == "M":
            for parent in parents:
                parent.sons.append(child)
        else:
            for parent in parents:
                parent.daughters.append(child)

    def add_member_in_family(self, new_member):
        """
        adds a new member to the family
        :param new_member:  new member that is a instance of Person class
        """
        self.members.append(new_member)

    def find_member_by_name(self, name):
        """
        finding a person with his name in the family
        :param name: name of a person in string format
        :return: a Person object or None
        """
        for member in self.members:
            if member.name == name:
                return member
        return None

    @staticmethod
    def get_brother_in_laws(person):
        """
        :param person: person an Instance of Person class
        :return: a list of person objects of brother-in-laws of given person
        """
        if person is None:
            return []
        brother_in_laws = []
        # brother-in_laws are spouse's brothers and husbands of siblings(girl siblings)
        # get spouse's brothers
        spouse_brothers = Person.get_brothers(person.spouse)
        brother_in_laws.extend(spouse_brothers)
        # husbands of siblings
        girl_siblings = Person.get_sisters(person)
        for girl in girl_siblings:
            if girl.spouse:
                brother_in_laws.append(girl.spouse)
        return brother_in_laws

    @staticmethod
    def get_sister_in_laws(person):
        """
        :param person: person an Instance of Person class
        :return: a list of person objects of sister-in-laws of given person
        """
        if person is None:
            return []
        sister_in_laws = []
        # brother-in_laws are spouse's brothers and husbands of siblings(girl siblings)
        # get spouse's brothers
        spouse_sisters = Person.get_sisters(person.spouse)
        sister_in_laws.extend(spouse_sisters)
        # husbands of siblings
        boy_siblings = Person.get_brothers(person)
        for boy in boy_siblings:
            if boy.spouse:
                sister_in_laws.append(boy.spouse)
        return sister_in_laws

    @staticmethod
    def get_uncles(person, parent):
        """
        :param person: person an Instance of Person class
        :param parent: Either mother or father instance, so according to that either
        we will get paternal aunt to maternal aunts
        :return: a list of person objects of uncles of given person(either maternal or paternal)
        """
        if person is None:
            return []
        # paternal uncles are father's brothers and fathers's brother-in-law's
        uncles = []
        if parent and parent.father:
            parent_brothers = Person.get_brothers(parent)
            uncles.extend(parent_brothers)
        parent_brother_in_laws = Family.get_brother_in_laws(parent)
        uncles.extend(parent_brother_in_laws)
        return uncles

    @staticmethod
    def get_aunt(person, parent):
        """
        :param person: person an Instance of Person class, that given Family's relatives are going to be retrieved
        :param parent: Either mother or father instance, so according to that either
        we will get paternal aunt to maternal aunts
        :return: a list of person objects of aunts of given person(either maternal or paternal)
        """
        if person is None:
            return []
        # paternal aunt are father's sisters and fathers's sister-in-law's
        aunts = []
        if parent and parent.father:
            sisters = Person.get_sisters(parent)
            aunts.extend(sisters)
        sister_in_laws = Family.get_sister_in_laws(parent)
        aunts.extend(sister_in_laws)
        return aunts

    @staticmethod
    def get_cousins(person):
        """
        :param person: person an Instance of Person class, that given Familys relatives are going to be retrieved
        :return: a list of person objects of cousins of that given person
        """
        if person is None:
            return []
        mother = person.mother
        father = person.father
        cousins = []
        mother_sibling = Person.get_brothers(mother) + Person.get_sisters(mother)
        for sibling in mother_sibling:
            cousins.extend(Person.get_children(sibling))
        father_sibling = Person.get_brothers(father) + Person.get_sisters(father)
        for sibling in father_sibling:
            cousins.extend(Person.get_children(sibling))
        return cousins
