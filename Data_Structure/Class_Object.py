class Computer:

    def __init__(dd, a, b):
        dd.cpu = a
        dd.ram = b

        print('Yoyo')

    def config(sd):
        print(sd, sd.cpu, sd.ram)


com1 = Computer("iP", 12)
com2 = Computer("iD", 13)

Computer.config(com1)
com1.config()
com2.config()


####

class Bus:
    wheels = 4

    def __init__(self):
        self.name = 111
        self.mpg = 222

    def update(s):
        return print(s, s.name, s.mpg)

    def comp(sel, otherone):
        if sel.name == otherone.name:
            return True
        else:
            return False


Bus.name = 99

bus1 = Bus()
bus2 = Bus()
bus1.mpg = 100

bus1.wheels = 100

print(bus1, bus1.name)
bus2.update()

if bus1.comp(bus2):
    print("same buddy")
else:
    print("Nope, different")
