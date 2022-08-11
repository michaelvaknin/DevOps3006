import  requests
print("moshe")
try:
    response = requests.get("htgtf://github.com")
except BaseException as e:
    print("something went wrong")
    print(e.args)

try:
    f = int(input("enter number: "))
    r = 5 / 0
except ZeroDivisionError:
    print("could not divide by zero")
except ValueError:
    print("entar a legal number")
except BaseException:
    print("something went wrong , here is more")
    print(e.args)
print("haim")
