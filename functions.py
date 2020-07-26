import datetime
import os


def get_current_time():
    current_time = str(datetime.datetime.now())
    return current_time


def name_file():
    file_name = input("File name: ")
    return file_name


def generate_note_name(current_time, file_name):
    note_name = "'" + file_name + "' " + current_time + ".txt"
    return note_name


def create_note(note_name):
    note = open(note_name, "w+")
    return note


def write_note(note, message):
    note.write(message)
    return note


def save_and_close_note(note):
    note.close()


def get_path():
    path = "/home/moloch/IdeaProjects/pyary/"
    return path


def get_notes(path):
    notes_list = os.listdir(path)
    return notes_list


def get_choice():
    choice = input("Type in the name of the note you want to read!")
    return choice


def get_the_note(choice, notes):
    for note in notes:
        if choice[0, 6] == note[0, 6]:
            return note
        else:
            print("Invalid note name!")
            choice = get_choice()
            note = get_the_note(choice, notes)
            return note


def reading(note):
    note = open(note, "r+")
    return note
