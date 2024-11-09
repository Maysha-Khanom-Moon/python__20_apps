while True:
    user_action = input('Type add, show, edit, complete, or exit: ')
    user_action = user_action.strip()
    
    match user_action:
        case 'add':
            todo = input('Enter a todo: ') + '\n'
            
            # file = open('todos.txt', 'r')
            # todos = file.readlines()
            # file.close()
            
            # recommended --> file is close implicitly
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            
            todos.append(todo)
            
            # file = open('todos.txt', 'w')
            # file.writelines(todos)
            # file.close()
            
            # recommended --> file is close implicitly
            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        
        
        case 'show':
            # file = open('todos.txt', 'r')
            # todos = file.readlines()
            # file.close()
            
            # recommended
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            
            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f'{index+1} - {item}'
                print(row)
            
        
        case 'edit':
            number = int(input('Number of the todo to edit: '))
            
            # file = open('todos.txt', 'r')
            # todos = file.readlines()
            # file.close()
            
            # recommended
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            
            new_todo = input('Enter new todo: ') + '\n'
            todos[number - 1] = new_todo
            
            # file = open('todos.txt', 'w')
            # file.writelines(todos)
            # file.close()
            
            # recommended
            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        
        
        case 'complete':
            number = int(input('Number of the todo to complete: '))
            
            # file = open('todos.txt', 'r')
            # todos = file.readlines()
            # file.close()
            
            # recommended
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            
            todo_to_remove = todos.pop(number - 1)
            
            # file = open('todos.txt', 'w')
            # file.writelines(todos)
            # file.close()
            
            # recommended
            with open('todos.txt', 'w') as file:
                file.writelines(todos)

            message = f"todo '{todo_to_remove.strip("\n")}' was removed from the list"
            print(message)
        
        
        case 'exit':
            break


print("Bye")