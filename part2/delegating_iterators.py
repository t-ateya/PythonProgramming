from collections import namedtuple

Person = namedtuple('Person', 'first last')

class PersonNames:
    def __init__(self, persons:Person):
        try:
            self._persons = [person.first.capitalize() + " " + person.last.title()
                        for person in persons]
        except (TypeError, AttributeError):
            self._persons = []

    def __iter__(self):
        return iter(self._persons) #delegating



persons = [Person('michael', 'paLin'), Person('eric', 'idLe'), Person('john', 'cLeese')]

person_names = PersonNames(persons)
print(person_names._persons)

#We cannot iterate over the persons_names cause it's not an iterable. We need to make PersonNames class an iterable

for name in person_names:
    print(name)