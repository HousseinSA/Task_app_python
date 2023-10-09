import PySimpleGUI as gui
import shutil

file_path = gui.Text('file path')
file_path_input = gui.Input(tooltip='file path')

file_name_select = gui.FileBrowse('choose')
zip_destination = gui.Text('zip path:')
zip_destination_input = gui.Input(tooltip='enter name')
zip_destination_select = gui.FolderBrowse('choose')
compress_button = gui.Button('compress')
completed= gui.PopupQuickMessage('Completed!')
window = gui.Window("File_zipper", layout=[[file_path, file_path_input, file_name_select], [zip_destination, zip_destination_input, zip_destination_select], [compress_button]])
window.read()
filepathvalue = file_path_input.get()
filedestinationValue= zip_destination_input.get()
shutil.make_archive('compressed-file', 'zip', filepathvalue ,filedestinationValue )
print('compress sucessfull')