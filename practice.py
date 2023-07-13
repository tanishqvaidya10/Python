def greet(friend):
    return "hello " + friend

def greet_all(friends):
    for friend in friends:
        print(greet(friend))

c = ["pam","jim"]

greet_all(c)
