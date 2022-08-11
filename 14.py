import ast
my_file = open("config.json")
c = dict(ast.literal_eval(my_file.read()))
print(c["name"])
if c["name"] == "aviel":
    print("i love experts")


with open("names.txt" "a+") as my_file:
    for name in my_file.readlines():
        print(name.strip())