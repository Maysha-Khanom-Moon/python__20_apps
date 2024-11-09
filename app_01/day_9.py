while True:
    user_action = input('Type add, show, edit, complete, or exit: ')
    user_action = user_action.strip()
    
    # more user friendly
    # unindend the entire block: select --> shift + tab
    # we set the if-else condition with priority basis (top >> bottom)
    if 'add' in user_action or 'new' in user_action:
        # todo = input("Enter a todo: ") + '\n'
        todo = user_action[4:]
        
        with open("todos.txt", 'r') as file:
            todos = file.readlines()
        
        todos.append(todo)
        
        with open('todos.txt', 'w') as file:
            file.writelines(todos)
    
    
    elif 'show' in user_action:
        with open('todos.txt', 'r') as file:
            todos = file.readlines()
        
        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index+1} - {item}")
    
    
    elif 'edit' in user_action:
        number = int(input('Number of the todo to edit: '))
        with open('todos.txt', 'r') as file:
            todos = file.readlines()
        
        new_todo = input("Enter new todo: ") + '\n'
        todos[number - 1] = new_todo
        
        with open('todos.txt', 'w') as file:
            file.writelines(todos)
    
    
    elif 'complete' in user_action:
        # number = int(input("Number of the todo to complete: "))
        number = int(user_action[9: ])
        
        with open('todos.txt', 'r') as file:
            todos = file.readlines()
        
        todo_to_remove = todos.pop(number - 1)
        
        with open('todos.txt', 'w') as file:
            file.writelines(todos)
        
        message = f"todo '{todo_to_remove.strip("\n")}' was removed from the list"
        print(message)
    
    
    elif 'exit' in user_action:
        break
    
    else:
        print('command is not valid.')
    
print("Bye!")