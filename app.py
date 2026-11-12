def greet(name):
    return f"Welcome, {name}!"

def login(username, password):
    if username == "admin" and password == "1234":
        return "Login successful"

    return "Invalid credentials"


if __name__ == "__main__":
    print(greet("Pradeep"))
    print(login("admin", "1234"))