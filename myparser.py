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

#---------- Insert ------------

def insert(statement):
    
    if statement[0] == "into":
        statement.pop(0)
        
        if statement[0] in keywords or statement[0] in datatypes:
            print("**** Error: Can not use a keywoard as table name ****")
            exit()
        else:
            if statement[0] in tables_map:
                table_select = statement[0]
                statement.pop(0)
                #check if table exists
                if statement[0] == "(":
                    statement.pop(0)
                    insert_seq_one(table_select, statement)
                    if statement[0] == "values":
                        statement.pop(0)
                        
                        if statement[0] == "(":
                            statement.pop(0)
                            insert_seq_two(table_select, statement)
                            
                            
                    else:
                        ("**** Error: Expected VALUES. Received " + statement[0] + " ****")

                else:
                    print("**** Error: Missing Parentheses ****")
                    exit()
            elif statement[0] in tables_map + "()":
                pass
            else:
                print("****Error table does not exist****")
                exit()

def insert_seq_one(table_name, statement):
    #Read through all variable names

    for i in tables_map[table_name]:
        
        if statement[0] == i[0]:
            statement.pop(0)
            if statement[0] == ",":
                statement.pop(0)
            elif statement[0] == ")":
                statement.pop(0)
                break
            else:
                print("**** Error: Missing comma between variables. ****")
                exit()
        elif statement[0] == i[0] + ",":
            statement.pop(0)
        #first two if statements check if value matches the stack of variables
        elif statement[0] == ")":
            statement.pop(0)
            break
        else:
            print("**** Error: Variable either in wrong order or does not exist in table. ****")
            exit()
   
        

def insert_seq_two(table_name, statement):

    i = 0
    while i < len(tables_map[table_name]):
        data_map = tables_map[table_name][i][1]
        data_map = re.sub("\(.*?\)", "", data_map)
        data_map = re.sub("\s", "", data_map)

        datatype_sub = ["int", "varchar", "float"]

        if datatype_sub[0] == data_map:
            if re.findall("^[0-9]*$", statement[0]):
                statement.pop(0)
                if statement[0] == ",":
                    statement.pop(0)
                elif statement[0] == ")":
                    statement.pop(0)
                else:
                    print("**** Error: Value must be followed by a comma. ****")
                    exit()
            else:
                print("**** Error: Value does match expected data type: int ****")
                exit()
            #Integer handling
        elif datatype_sub[1] == data_map:
            if re.findall("[a-z]|[A-Z]|[0-9]", statement[0]):
                rtest =  re.compile(r"\((\d+)\)")
                rx = int((rtest.findall(tables_map[table_name][i][1]))[0])
                if len(statement[0]) <= rx:
                    statement.pop(0)
                    if statement[0] == ",":
                        statement.pop(0)
                    elif statement[0] == ")":
                        statement.pop(0)
                    else:
                        print("**** Error: Value must be followed by a comma. ****")
                        exit()                 
                else:
                    print("**** Error: String exceeds maximum length. ****")
                    exit()  
            else:
                print("**** Error: Value does match expected data type: varchar ****")
                exit()
            #varchar handling
        elif datatype_sub[2] == data_map:
            if re.findall("[0-9]\.[0-9]", statement[0]):
                statement.pop(0)
                if statement[0] == ",":
                    statement.pop(0)
                elif statement[0] == ")":
                    statement.pop(0)
                else:
                    print("**** Error: Value must be followed by a comma. ****")
                    exit()
            else:
                print("**** Error: Value does match expected data type: float ****")
                exit()
            #float handling
           

        i += 1

    return

        


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



 