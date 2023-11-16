class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

class Stack:
    def __init__(self):
        self.top = None


    def push(self, x):
        new = Node(x)
        if self.top is None:
            self.top = new
            self.top.next = None
        else:
            new.next = self.top
            self.top = new

    def pop(self):
        if self.top is None:
            print("Stack is empty")
        elif self.top.next is None:
            print("Popped element: ", self.top.data)
            print("--------------------------------")
            self.top = None
        else:
            temp = self.top
            print("Popped element: ", self.top.data)
            print("--------------------------------")
            self.top = temp.next
            temp = None

    def palindra(self): # shows original, cleaned, reversed sentence, and if original sentence is a palindrome
        #displays cleaned and reversed sentence
        cleaned_sentence = ""
        reversed_sentence = ""

        print(f"Your sentence: {userInput}")

        if self.top is None:
            print("Stack is empty")
        else:
            temp = self.top

            while temp:
                cleaned_sentence = temp.data + cleaned_sentence
                temp = temp.next
            print(f"Cleaned sentence: {cleaned_sentence}")
            temp = self.top
            while temp:
                reversed_sentence += temp.data
                temp = temp.next
            print(f"Reversed sentence: {reversed_sentence}")

        if cleaned_sentence == reversed_sentence:
            print(f"Your sentence: {userInput} is a palindrome")
        else:
            print(f"Your sentence: {userInput} is not palindrome")


    def sentence(self, string):
        result = ""
        for char in string:
            if char.isalpha():
                result += char.lower()

        return result


s = Stack()
userInput = input("Enter a sentence: ")

final = s.sentence(userInput)

for x in final:
    s.push(x)
s.palindra()
