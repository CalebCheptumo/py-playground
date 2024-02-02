from user import User

class Privileges:
    def __init__(self, privileges=[]):
        """Initialize the privileges attribute"""
        self.privileges = privileges

    def show_privileges(self):
        """Display the privileges this administrator has"""
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege.title()}")
        else:
            print("- This user has no privileges.")


class Admin(User):
    def __init__(self, first_name, last_name, age, location):
        """Initialize attributes of the parent class"""
        super().__init__(first_name, last_name, age, location)
        self.privileges = Privileges()
