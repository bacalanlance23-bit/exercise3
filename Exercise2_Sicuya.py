try:
    note = input("Enter a short note/message: ")

    with open("notes.txt", "w") as file:
        file.write(note + "\n")

    print("\n--- File Content After Writing ---")
    with open("notes.txt", "r") as file:
        print(file.read())

    new_note = input("Enter another note to append:\n ")

    with open("notes.txt", "a") as file:
        file.write(new_note + "\n")

    print("--- Updated File Content ---\n")
    with open("notes.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("Error: File not found!")

except Exception as e:
    print("An error occurred:", e)