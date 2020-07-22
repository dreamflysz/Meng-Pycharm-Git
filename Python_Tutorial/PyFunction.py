def sum(a, *b):
    c = a

    for i in b:  # b is tuple
        c = c + i
    print(c)


sum(2, 4, -5)


def person(name, **datus):
    print(name)

    for i, w in datus.items():
        print(i, "=", w)


person('mengfei', age=33, type="Genius")

# def sth():
#
#     global g
#     g = 12
#
#     print("in fun ", g)
#
#     g = 0.2
#     print("in fun ", g)
#
# sth()®
#
# print("outside", g)


g = 10
print(id(g))


def sbdy():
    g = 12
    x = globals()['g']

    print(id(x))
    print("in fun ", g)

    # globals()['g'] = 11


sbdy()
print("outside", g)
