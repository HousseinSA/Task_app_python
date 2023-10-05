from functions import get_todos, change_todo
import time

date = time.strftime('%b %d,%Y, %H:%M:%S')
print(f"it's {date}")
todos = get_todos()
while True:
        user_action = input("type add, edit, complete , or show, exit, and clear\n")
        print(f'{date}\n')
        if user_action.startswith('add'):
            try:
                if user_action[4:] == "":
                    print('nothing to add.')
                elif user_action[4:] == 'add':
                    print('cannot add the phrase add to the list, try again.!')
                else:
                    add_todo = user_action[4:] + '\n'
                    todos.append(add_todo)
                    change_todo(todos)
            except ValueError:
                print('their is an error in the code.')
                continue
        elif user_action.startswith('show'):
            for index,todo in enumerate(todos):
                edited = todo.strip('\n')
                print(f'{index+1} - {edited}')
        elif user_action.startswith('edit'):
            try:
                editTodo = user_action[4:]
                find_todo = int(editTodo)-1
                if todos[find_todo]:
                    newTodo = input(f'edit todo {todos[find_todo]} \n')
                    todos[find_todo] = newTodo
                    change_todo(todos)
            except IndexError:
                print("did't find i valid index try again. \n")
                continue
            except ValueError:
                print('the index or value you typed is invalid.')
                continue
        elif user_action.startswith('complete'):
            try:
                remove_todo = user_action[9:]
                todo_to_remove = int(remove_todo)-1
                todo_to_edit = todos[todo_to_remove].strip('\n')
                print(f"{todo_to_edit} removed")
                todos.pop(todo_to_remove)
                change_todo(todos)
            except IndexError:
                print('the index your entered is invalid.')
            except ValueError:
                print('the value you entered is not i number')
                continue
        elif user_action.startswith('clear'):
            todos.clear()
            print('todo list cleared!')
            change_todo(todos)
        elif user_action.startswith("exit"):
            print('exiting program')
            break
        else:
            print('command unknown.')
