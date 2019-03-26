class MetaCollection(type):

    def __new__(cls, clsname, bases, dct):
        dct["COLLECTION"] = clsname
        return super().__new__(cls, clsname, bases, dct)


class Account(metaclass=MetaCollection):

    def __init__(self, number: str):
        if len(number) != 13:
            raise ValueError("The length of number must be equal to 13.")
        self.number = number


if __name__ == '__main__':

    correct_number = "7800000000000"
    acc = Account(correct_number)
    print("Class attrs: {}".format(Account.__dict__))

    invalid_number = "123"
    acc_wrong = Account(invalid_number)
