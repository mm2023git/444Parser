import re
from index import index

keywords = {"select", "create", "insert", "table", "int", "varchar", "float"}

tables_map = {}

def create():
    if statement[0] == "table": 
        statement.pop(0)
        if statement[0] in keywords:
            print("Error: Can't use a keyword as a table name")
        else: 
            tables_map.add(statement.pop(0))
            if statement[0] != "(":
                print("you are missing an open paranthesis in your create statement")
            else: 
                pass
    else:
        print("create statement should be followed by the `table` keyword ")
    return

input = "   INSERT SELECT CREATE A"



stack_index = index(input)

statement = ["create", "table", "users"]

if statement[0] == "create":
    statement.pop(0)
    create(statement)
elif statement[0] == "select":
    pass
elif statement[0] == "Insert":
    pass

def parse():
    
    if stack_index.get_stack():
        print(stack_index.get_stack())
        if re.findall("\s", stack_index.get_stack()[0]):
            stack_index.pop_stack()
            parse()
            #Checks for white space and pops it off the stack
        elif re.findall("SELECT", stack_index.stringify(6), re.IGNORECASE):
            stack_index.popify(6)
            select()
            parse()
            #once SELECT is found pop it off the stack, enter the select grammar and then return back to the parser
        elif re.findall("INSERT", stack_index.stringify(6), re.IGNORECASE):
            stack_index.popify(6)
            insert()
            parse()
            #once INSERT is found pop it off the stack, enter the select grammar and then return back to the parser
        elif re.findall("CREATE", stack_index.stringify(6), re.IGNORECASE):
            stack_index.popify(6)
            insert()
            parse()
            #once CREATE is found pop it off the stack, enter the select grammar and then return back to the parser
    print(stack_index.get_stack())
    return "compiled successfully."




def select():
    return 



def insert():
    return
 

parse()