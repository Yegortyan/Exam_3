def Karta(nomerkarti):
    len_kar = len(str(nomerkarti)) - 4
    if len_kar <= 0 or len_kar % 4 != 0:
        return 'error'

    result = '*' * len_kar + str(nomerkarti)[-4:]
    return result
print(Karta('4142983256781234'))
print('----------------------------')

def Polindrom(slovo):
    return str(slovo) == str(slovo)[::-1]
print(Polindrom('шалаш'))
print(Polindrom('шалашшшшш'))
print('----------------------------')

class Tomato:

    states = {0: 'zvetok', 1: 'bobiwka', 2: 'bobiwka_zelenaya', 3: 'bobiwka_virosla'}

    def __init__(self, index):
        self._index = index
        self._state = Tomato.states[0]

    def grow(self):
        i = 0
        for value in Tomato.states.values():
            if value == self._state:
                self._state = Tomato.states[i + 1]
                break
            i += 1

    def is_ripe(self):
        return Tomato.states[list(Tomato.states.keys())[-1]] == self._state


class TomatoBush:
    def __init__(self, skolko):
        self.tomatoes = []
        for i in range(0, skolko):
            self.tomatoes.append(Tomato(i))
    def grow_all(self):
        for pomidor in self.tomatoes:
            Tomato.grow(pomidor)

    def all_are_ripe(self):
        for pomidor in self.tomatoes:
            if not Tomato.is_ripe(pomidor):
                return False
        return True
    
    def give_away_all(self):
        self.tomatoes.clear()

class Gardener:
    def __init__(self, name, kust):
        self.name = name
        self._plant = kust
    
    def work(self):
        TomatoBush.grow_all(self._plant)
        
    def harvest(self):
        if TomatoBush.all_are_ripe(self._plant):
            TomatoBush.give_away_all(self._plant)
            print('polyana nakrita')
        else:
            print("est' jeltie bobiwki, nizya @")
    def knowledge_base():
        print('Tomaty sozrevayut na kustah, a sadovodniki uhazhivayut za nimi i sobirayut urozhaj')

Gardener.knowledge_base()
kust = TomatoBush(5)
sadovodnik = Gardener('Oleg', kust)
sadovodnik.work()
sadovodnik.harvest()
sadovodnik.work()
sadovodnik.work()
sadovodnik.harvest()