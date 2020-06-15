class Quote():
    def __init__(self, person, words):
        self.person = person
        self.words = words
    def who(self):
        return self.person
    def says(self):
        return self.words + '.'

class QuestionQuote(Quote):
    def says(self):
        return self.words + '?'

class ExclamationQuote(Quote):
    def says(self):
        return self.words + '!'

hunter = Quote('Elmer Fudd', "I'm hunting wabbits")
print(hunter.who(), 'says:', hunter.says())

hunter1 = QuestionQuote('Bug Bunny', "What's up, doc")
print(hunter1.who(), 'says:', hunter1.says())

hunter2 = ExclamationQuote('Daffy Duck', "It's rabbit season")
print(hunter2.who(), 'says:', hunter2.says())

class BabblingBrook():
    def who(self):
        return 'Brook'
    def says(self):
        return 'Babble'

brook = BabblingBrook()

def who_says(obj):
    print(obj.who(), 'says', obj.says())

who_says(hunter)
who_says(hunter1)
who_says(hunter2)
who_says(brook)
