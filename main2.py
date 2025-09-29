class flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):
        return self.word + '('+ self.meaning+')'
    
flash = []
print("welcome to flashcard application")

#the following loop will be repeated until
#user stops to add the flashcards

while(True):
    word = input("enter the name you want to add to flashcard : ")
    meaning = input("enter the meaning of the word : ")

    flash.append(flashcard(word, meaning))
    option = int(input("do you want to add more flashcards? (1/0) : "))
    if(option):
        break
 
print("your flashcards are : ")
for i in flash:
    print(f"> {i}")
