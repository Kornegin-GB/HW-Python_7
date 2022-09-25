import view
import csv_create
import xml_create


def Selection_processing():
    selection = view.User_selection()
    if selection == 1:
        Import_processing_csv(view.User_data_entry())
    elif selection == 2:
        Export_processing_csv()
    elif selection == 3:
        Import_processing_xml(view.User_data_entry())
    else:
        Export_processing_xml()


def Export_processing_csv():  # Экспорт файла
    view.view_result(csv_create.File_reading())


def Import_processing_csv(data):  # Импорт файла
    csv_create.File_recording(data)


def Export_processing_xml():  # Экспорт файла
    view.view_result(xml_create.File_reading())


def Import_processing_xml(data):  # Импорт файла
    xml_create.File_recording(data)
