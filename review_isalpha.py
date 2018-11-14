statement = input("Enter a word\n").lower()

if len(statement) > 0 and statement.isalpha():
    statement += statement[0] + "ay"
    statement = statement[1:len(statement)]
    print(statement)
else:
    print("A wrong statement was wrote")
