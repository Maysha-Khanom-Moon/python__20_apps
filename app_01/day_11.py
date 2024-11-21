def get_todos():
    with open('todos.txt', 'r') as file:
        todos = file.readlines()
    return todos

def set_todos(todos):
    with open('todos.txt', 'w') as file:
        file.writelines(todos)
    # return None


while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()
    
    if user_action.startswith('add'):
        todo = user_action[4: ] + '\n'
        
        todos = get_todos()
        
        todos.append(todo)
        
        set_todos(todos)
    
    
    elif user_action.startswith('show'):
        todos = get_todos()
        
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f'{index + 1} - {item}'
            print(row)
    
    
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5: ])
            number = number - 1
            
            todos = get_todos()
            
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'
            
            set_todos(todos)
        
        except ValueError:
            print("Your command is not valid.")
            # without continue it will be worked
            continue
        
    
    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9: ])
            
            todos = get_todos()
            
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
            
            set_todos(todos)
            
            message = f'Todo "{todo_to_remove}" was removed from the list.'
            print(message)
        
        except IndexError:
            # IndexError --> out of the range
            print('There is no item with that number.')
            # without continue it will be worked
            continue
    
    
    # elif 'exit' in user_action:
    elif user_action.startswith('exit'):
        break
    
    else:
        print('Command is not valid.')

print('Bye!')