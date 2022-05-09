class Address:
    def __init__(self, street, city):
        self.street = str(street)
        self.city = str(city)


class Person:
    def __init__(self, name, email):
        self.name = str(name)
        self.email = str(email)


class Contact(Address, Person):
    def __init__(self, street, city, name, email):
        Address.__init__(self, street, city)
        Person.__init__(self, name, email)

    def show(self):
        print(self.name, self.city)


a = Contact('injero', 'kimhae', 'jaemin', 'gun2475@naver.com')
a.show()
