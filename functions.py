filepath = 'todos.txt'
def get_todos(pathname=filepath):
    with open(pathname, 'r') as file:
        todos = file.readlines()
    return todos

todos = get_todos()
def change_todo(change_todo ,pathanme =filepath):
    with open(pathanme, 'w') as file_local:
        file_local.writelines(change_todo)