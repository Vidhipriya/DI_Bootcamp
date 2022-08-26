import random,string
def string_length(y):
    return "".join(random.choice(string.ascii_letters) for i in range(y))
print(string_length(5))