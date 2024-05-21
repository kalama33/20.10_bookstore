# components

class Address:# Component
    def __init__(self, street, city, zipcode) -> None:
        self.street = street
        self.city = city
        self.zipcode = zipcode

    def __str__(self):
        """Street
            Zipcode City"""

        return f"{self.street}\n{self.zipcode} {self.city}"

address_obj = Address('Musterstreet 1', 33123, 'Buxtehude')
# print(address_obj)


class Employee: # Composite
    def __init__(self, id, name, address) -> None:
        self.id = id
        self.name = name
        self.address = address

    def get_employee(self):
        print(self.name)
        print(self.address)


emp1 = Employee(1, 'Bob', address_obj)
emp1.get_employee()