


class Customer:

    def __init__(self, name, address, phone):
        self.__name = name
        self.__address = address
        self.__phone = phone

    def set_name(self, name):
        self.__name = name
    
    def set_address(self, address):
        self.__address = address

    def set_phone(self, phone):
        self.__phone = phone
    
    def get_name(self):
        return self.__name
    
    def get_address(self):
        return self.__address
    
    def get_phone(self):
        return self.__phone
    


if __name__ == "__main__":
    customer = Customer("John", "123 Main Street", "555-1234")
    print(customer.get_name())
    print(customer.get_address())
    print(customer.get_phone())
    customer.set_name("Jane")
    customer.set_address("124 Main Street")
    customer.set_phone("555-1235")
    print(customer.get_name())
    print(customer.get_address())
    print(customer.get_phone())

