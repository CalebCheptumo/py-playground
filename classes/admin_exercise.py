class User:
    def __init__(self, first_name, last_name, age, location):
        """Initialize name and age attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.login_attempts = 0
    
    def describe_user(self):
        """Describe the user"""
        print(f"The user's name is {self.first_name.title()} {self.last_name.title()} .")
        print(f"The user's age is {self.age} .")
        print(f"The user's location is {self.location.title()} .")

    def greet_user(self):
        """Greet the user"""
        print(f"Hello, {self.first_name.title()} {self.last_name.title()} .")

    def increment_login_attempts(self):
        """Increment the number of login attempts"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset the number of login attempts"""
        self.login_attempts = 0




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

