class Person:
    def __init__(self, firstname,lastname):
        self.fn = firstname
        self.ln = lastname
    def __str__(self):
        return f'My name is {self.fn}{self.ln}'


a = Person('sarun', 'Gulyanon')
print(a)