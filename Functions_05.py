
def ou_fun(a,b):
    def in_fun():
        return a + b
    return in_fun() + 5
a = ou_fun(4,5)

print(a)


