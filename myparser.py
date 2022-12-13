import re
from index import index

keywords = {"select", "create", "insert", "table", "int", "varchar", "float"}

tables_map = {}

def create(statement):
    global tables_map

    if statement[0] == "table": 
        statement.pop(0)
        if statement[0] in keywords:
            print("**Error: Can't use a keyword as a table name")
            exit()
        else: 
            tables_map[statement.pop(0)] = []
            if statement[0] != "(":
                print("**Error: you are missing an open paranthesis in your create statement")
                exit()
            else: 
                pass
    else:
        print("**Error: create statement should be followed by the `table` keyword ")
        exit()
    print(tables_map)
    return

#key = value
#"users" = [("name", "varchar(20)"), ("id", "int")]



# stack_index = index(input)

statement_string = "create table users ( name varchar(20)"
statement_string_new = " ".join(statement_string.split())

statement = statement_string_new.split(" ")


if statement[0] == "create":
    statement.pop(0)
    create(statement)
elif statement[0] == "select":
    pass
elif statement[0] == "Insert":
    pass

# def parse():
    
#     if stack_index.get_stack():
#         print(stack_index.get_stack())
#         if re.findall("\s", stack_index.get_stack()[0]):
#             stack_index.pop_stack()
#             parse()
#             #Checks for white space and pops it off the stack
#         elif re.findall("SELECT", stack_index.stringify(6), re.IGNORECASE):
#             stack_index.popify(6)
#             select()
#             parse()
#             #once SELECT is found pop it off the stack, enter the select grammar and then return back to the parser
#         elif re.findall("INSERT", stack_index.stringify(6), re.IGNORECASE):
#             stack_index.popify(6)
#             insert()
#             parse()
#             #once INSERT is found pop it off the stack, enter the select grammar and then return back to the parser
#         elif re.findall("CREATE", stack_index.stringify(6), re.IGNORECASE):
#             stack_index.popify(6)
#             insert()
#             parse()
#             #once CREATE is found pop it off the stack, enter the select grammar and then return back to the parser
#     print(stack_index.get_stack())
#     return "compiled successfully."




def select():
    return 



def insert():
    return
 

# parse()
print("Does the paranteheses contain a +ve number?")
print(bool(re.match('\\([1-9]+$\\)', "(123)"))) 

# key     =  value
# "users" = [("name", "varchar(20)"), ("id", "int"), ("timeOfCreation, "float")]

# insert into users timeOfCreation float

#  create table users (name varchar(20), id int)

#  if entry[0:7] == "varchar":
#     if bool(re.match('\(^[1-9]+$\)', entry[7:]))





# select timeOfCreation from users