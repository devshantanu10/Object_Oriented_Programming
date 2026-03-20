class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def display(self):
        return f"Username: {self.username}, Email: {self.email}"


class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, username, email):
        user = User(username, email)
        self.users.append(user)
        print("User added successfully!")

    def remove_user(self, username):
        for user in self.users:
            if user.username == username:
                self.users.remove(user)
                print("User removed!")
                return
        print("User not found!")

    def find_user(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return None

    def show_all_users(self):
        if not self.users:
            print("No users available.")
        for user in self.users:
            print(user.display())


# Example usage
if __name__ == "__main__":
    manager = UserManager()

    manager.add_user("shantanu", "shantanu@gmail.com")
    manager.add_user("alex", "alex@gmail.com")

    manager.show_all_users()

    user = manager.find_user("shantanu")
    if user:
        print("Found:", user.display())

    manager.remove_user("alex")
    manager.show_all_users()