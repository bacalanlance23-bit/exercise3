
def save_user():
    try:

        username = input("Enter username: ").strip()
        if username == "":
            raise ValueError("Username cannot be empty.")

        age_input = input("Enter age: ")
        age = int(age_input)  # possible ValueError

        if age <= 0:
            raise ValueError("Age must be a positive number.")

        with open("users.txt", "a") as file:
            file.write(f"{username} - {age}\n")

        print("User saved successfully!\n")

    except ValueError as ve:
        print(f"Input Error: {ve}")

    except Exception as e:
        print(f"Unexpected Error: {e}")

def display_users():
    try:
        print("Saved Users:/n")
        with open("users.txt", "r") as file:
            data = file.readlines()
            if not data:
                print("No users found.")
            else:
                for line in data:
                    print(line.strip())

    except FileNotFoundError:
        print("No file found yet. No users saved.")

    except Exception as e:
        print(f"Error reading file: {e}")

save_user()
display_users()

print("System complete.")