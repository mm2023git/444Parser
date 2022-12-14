import re
from index import index

keywords = {"select", "create", "insert", "table"}

datatypes = {"int", "varchar", "float"}

tables_map = {}
table_name = ""
column_name = ""
column_datatype = ""


def create(statement):
    global tables_map
    # checking if "table" after "create"
    if statement[0] == "table": 
        statement.pop(0)
        #Making sure a keyword isn't used for a table name
        if statement[0] in keywords or statement[0] in datatypes:
            print("****Error: Can not use a keyword as a table name ****")
            exit()
        # if table name is valid, go here
        else: 
            # get the table name
            table_name = statement.pop(0)
            #Add the table name to the hashmap
            tables_map[table_name] = []
            #if the next token isn't an open paranthesis, throw an error and exit
            if statement[0] != "(":
                print("****Error: you are missing an open paranthesis in your create statement ****")
                exit()
            #if the next token is an open paranthesis, continue
            else: 
                #pop the open parathesis from the list
                statement.pop(0)
                creating_iteration(statement, table_name)
                
    #if "table" after "create" is not provided you go here
    else:
        print("****Error: create statement should be followed by the `table` keyword ****")
        exit()
    return
                

def creating_iteration(statement, table_name):
    # check if column name isn't a keyword, if it is, throw and error and exit
    if statement[0] in keywords or statement[0] in datatypes: 
        print("****Error: Can not use a keyword as a column name ****")
        exit()
    #if the column name is valid, go here
    else:
        column_name = statement.pop(0)
        # checking if the column datatype is a supported datatype by the language, if it isn't, throw an error and exit
        if statement[0][0:7] not in datatypes:
            print("****Error: Make sure you are using a supported datatype for the columns ****")
            exit()
        # if the column datatype is valid, go here
        else: 
            #checking if the column datatype is a varchar
            if statement[0][0:7] == "varchar":
                #checking if the varchar datatype is given valid arguments, we only want negative numbers in the paranthesis after the varchar ex: varchar(20)
                if bool(re.match('\\([0-9]+\\)$', statement[1])):
                    column_datatype = statement.pop(0) + " " +  statement.pop(0)
                    tables_map[table_name].append((column_name, column_datatype))
                #if varchar isn't given valid argument, then throw an error and exit
                else:
                    print("****Error: Make sure the datatype varchar is of this format: varchar(+ve int) ****")
                    exit()
            else: 
                column_datatype = statement.pop(0)
                tables_map[table_name].append((column_name, column_datatype))
                if statement[0] != "," and statement[0] != ")":
                    print("****Error: 000Make sure you are using a supported datatype for the columns ****")
                    exit()
                
             
        if len(statement)>0 and statement[0] == ",":
            statement.pop(0)
            creating_iteration(statement, table_name)
        elif statement[0] == ")":
            statement.pop(0)
            print("Compiled Sucessfully")

    return

def insert(statement):
    
    if statement[0] == "into":
        statement.pop(0)
        print(statement)
        if statement[0] in keywords or statement[0] in datatypes:
            print("**** Error: Can not use a keywoard as table name ****")
            exit()
        else:
            print("test")
            if statement[0] in tables_map:
                table_select = statement[0]
                statement.pop(0)
                #check if table exists
                if statement[0] == "(":
                    statement.pop(0)
                    insert_seq_one(table_select, statement)
                  
                else:
                    print("**** Error: Missing Parentheses ****")
                    exit()
            elif statement[0] in tables_map + "()":
                pass
            else:
                print("****Error table does not exist****")
                exit()

def insert_seq_one(table_name, statement):
    for i in tables_map[table_name]:
        if statement[0] == tables_map[table_name][i][0]:
            statement.pop(0)
        elif statement[0] == table_name[table_name][i][0] + ",":
            statement.pop(0)
        

def select(statement):
    pass

                            
# --------------------- MAIN ---------------------

with open('input.txt', "r") as f:
    statements = f.read().replace('\n', ' ')

statements_array = statements.split(";")

statements_array = statements_array[0:len(statements_array)-1]


for statement_string in statements_array:
    statement_string = " ".join(statement_string.split())
    statement = statement_string.split(" ")
    # Create Statement
    if statement[0] == "create":
        statement.pop(0)
        create(statement)
        print(tables_map)

    # Insert Statement
    elif statement[0] == "Insert":
        # statement.pop(0)
        # insert(statement)
        pass
    # Insert Statement
    elif statement[0] == "insert":
        statement.pop(0)
        insert(statement)

    # Select Statement
    elif statement[0] == "select":
        # statement.pop(0)
        # select(statement)
        pass
    else:
        print("****Error: Beginning of an sql statement should start with create, insert, or select ****")
        exit()



 