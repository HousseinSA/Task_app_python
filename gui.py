from functions import get_todos, change_todo
import PySimpleGUI as gui

label = gui.Text('Todo')
todo_list = gui.Listbox(get_todos(), key='todos', enable_events=True, size=[45, 10])
input_text = gui.Input(tooltip='add Todo', key='todo')
add_button = gui.Button('Add')
todo_list = gui.Listbox(get_todos(), key='todos', enable_events=True, size=[45, 10])
edit_button = gui.Button('Edit')
delete_button = gui.Button('Complete')
window = gui.Window('TODO-APP', layout=[[label], [input_text, add_button], [todo_list, edit_button, delete_button]],
                    font=('Helvetica', 15))
read, values = window.read()
print(read, values)
while True:
    todos= get_todos()
    read,values = window()
    print(read, values)
    match read:
        case "Add":
            if values['todo'] == "":
                continue
            todos.append(values['todo']+"\n")
            change_todo(todos)
            window['todos'].update(values = todos)
            window['todo'].update('')
        case "Edit":
            if values['todos'] == [] or values['todo'] == "":
                continue
            edit_todo = values['todos'][0]
            new_todo = values['todo']
            todo_index = todos.index(edit_todo)
            todos[todo_index] = new_todo
            window["todos"].update(values= todos)
            window['todo'].update('')
            change_todo(todos)
        case "Complete":
            if values['todos'] == [] or values['todo'] == "":
                continue
            delete_todo = values['todos'][0]
            index_todo = todos.index(delete_todo)
            todos.pop(index_todo)
            window['todos'].update(values= todos)
            change_todo(todos)
        case "todos":
            window['todo'].update(values['todos'][0])
        case gui.WINDOW_CLOSED:
            print('closing program')
            break
window.close()
