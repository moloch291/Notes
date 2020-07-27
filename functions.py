import datetime
import os


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


def get_path():
    path = "/home/moloch/IdeaProjects/pyary/"
    return path


def get_notes(path):
    notes_list = os.listdir(path)
    return notes_list


def get_choice():
    choice = input("Type in the name of the note you want to read!\n")
    return choice


def get_the_note(choice, notes_list):
    for note in notes_list:
        if choice == note:
            return note


def open_note(path, note):
    page = open(path + note, "r+")
    return page


def reading(page):
    lines = page.readlines()
    print(lines)
    return page
