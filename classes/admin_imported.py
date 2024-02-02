from admin_exercise import Admin , Privileges , User

admin = Admin('John', 'Doe', 30, 'New York')
admin.privileges.privileges = [
    'can add post',
    'can delete post',
    'can ban user',
    ]

admin.privileges.show_privileges()