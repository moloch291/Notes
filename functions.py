import datetime


def get_current_time():
    current_time = str(datetime.datetime.now())
    return current_time


def name_file():
    file_name = input("File name: ")
    return file_name


def generate_note_name(current_time, file_name):
    note_name = "'" + file_name + "' " + current_time
    return note_name


def create_note(note_name):
    note = open(note_name, "w+")
    return note


def write_note(note, message):
    note.write(message)
    return note


def save_and_close_note(note):
    note.close()
