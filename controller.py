import view
import csv_create as my_file
# import xml_create as my_file


def Selection_processing():
    selection = view.User_selection()
    if selection == 1:
        Import_processing(view.User_data_entry())
    else:
        Export_processing()


def Export_processing():  # Экспорт файла
    my_file.File_reading()


def Import_processing(data):  # Импорт файла
    my_file.File_recording(data)
