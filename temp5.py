class Mixer:
    def mixer(self):
        x = self.a + self.b
        print(x)


class Writer(Mixer):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def upper(self):
        print(self.a.upper())

    def lower(self):
        print(self.b.lower())

w = Writer('fwefwfew', 'hrthrthr')
w.upper()
w.lower()
w.mixer()



