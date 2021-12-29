import random


class Dice:
    def __init__(self):
        self.history = {}

    def History(self):
        for k, v in self.history.items():
            print(k, ':', v)

    def Roll(self, n, layers):
        throws = []
        total = 0
        session : str
        try:
           session = list(self.history.keys())[-1]
           session = int(session) + 1
        except:
            session = '1'
        if n == 1:
            t = random.randrange(1, layers)
            self.history[session] = t
            return {'Dices': str(f'{n}d{layers}'), 'Throws': t, 'Total': t}
        else:
            for times in range(0, n):
                t = random.randrange(1, layers)
                throws.append(t)
                total += t
            self.history[session] = str(throws)[1:-1]
        return {'Dices': str(f'{n}d{layers}'), 'Throws': str(throws)[1:-1], 'Total': total}



