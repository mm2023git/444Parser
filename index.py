
import re


class index:
    #default constructor
    def __init__(self):
        self.stack = list()
    #constructor with input
    def __init__(self, input):
        self.stack = list()
        for character in input:
            self.stack.append(character)        

    def set_stack(self, input):
        for character in input:
            self.stack.append(character)
        return
        
    def get_stack(self):
        return self.stack
    #pops first item off array
    def pop_stack(self):
        self.stack.pop(0)

    #popify typically follows stringify uses to pop multiple items off the stack with one line
    def popify(self, x):
        for i in range(x):
            self.stack.pop(0)


    #Stringify allows you to create a string for longer 
    def stringify(self, x):
        retString = ""
        for i in range(x):
            if i == len(self.stack):
                retString = ""
                break
                #if the length is longer than the stack then it breaks and returns nothing
            retString += self.stack[i]

        return retString



    

        
    