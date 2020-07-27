import functions
import os


def create_new_note():
    current_time = functions.get_current_time()
    file_name = functions.name_file()
    note_name = functions.generate_note_name(current_time, file_name)
    os.system('clear')
    note = functions.create_note(note_name)
    print(file_name + ":")
    message = input("New note (type 'cancel' to exit): ")
    if message == "cancel":
        options_menu()
    else:
        note = functions.write_note(note, message)
        functions.save_and_close_note(note)
        options_menu()


def read_existing_notes():
    os.system('clear')
    path = functions.get_path()
    notes_list = functions.get_notes(path)
    for note in notes_list:
        print(note)
    choice = functions.get_choice()
    note = functions.get_the_note(choice, notes_list)
    page = functions.open_note(path, note)
    functions.reading(page)
    functions.save_and_close_note(page)


def reading_options(note):
    reading_option = input("Type 'edit' or 'exit'!")
    if reading_option == "exit":
        functions.save_and_close_note(note)
        read_existing_notes()
    elif reading_option == "edit":
        message = input("Edit note:")
        note = functions.write_note(note, message)
        functions.save_and_close_note(note)


def options_menu():
    os.system('clear')
    menu_choice = input("Welcome to 'Notes', the python diary!\n1: Create notes\n2: Read notes\n3: Exit\n")
    if menu_choice == "1":
        os.system('clear')
        create_new_note()
    elif menu_choice == "2":
        os.system('clear')
        read_existing_notes()
    elif menu_choice == "3":
        print("Good bye!")
        quit()
    else:
        os.system('clear')
        print("Invalid input! Please type the number of an option and press ENTER!")
        options_menu()


def notes():
    options_menu()
