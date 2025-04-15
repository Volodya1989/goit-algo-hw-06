from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    # реалізація класу
    pass


class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must have 10 digits.")
        super().__init__(value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number):
        self.phones.append(Phone(phone_number))

    def remove_phone(self, phone_number):
        phone_to_remove = next(
            (p for p in self.phones if p.value == phone_number), None)
        if phone_to_remove:
            self.phones.remove(phone_to_remove)
        else:
            raise ValueError("Phone number is not found!")

    def edit_phone(self, new_phone_number, old_phone_number):
        phone_to_edit = next((i for i, p in enumerate(
            self.phones) if p.value == old_phone_number), None)
        if phone_to_edit is not None:
            self.phones[phone_to_edit] = Phone(new_phone_number)
            print(
                f"Updated phone from {old_phone_number} to {new_phone_number}")

        else:
            raise ValueError(f"Phone number {old_phone_number} not found.")

    def find_phone(self, phone):
        return next((p for p in self.phones if phone == p.value), None)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        self.data.pop(name, None)

    def __str__(self):
        return "\n".join(map(str, self.data.values()))
