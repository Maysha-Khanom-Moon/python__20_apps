while True:
    user_action = input('Type add, show, edit, complete, or exit: ')
    user_action = user_action.strip()
    
    match user_action:
        case 'add':
            todo = input('Enter a todo: ') + '\n'
            
            '''
            # make sure, source code and txt file in the same directory
            
            r --> read
            w --> create or overwrite
            
            readlines --> return the list
            writelines --> set the list
            '''
            
            # we are taking the existing values before overwrite these
            file = open('todos.txt', 'r')
            todos = file.readlines()
            
            # crucial to avoid potential issues like data corruption and resource leaks.
            file.close()
            
            todos.append(todo)
            
            file = open('todos.txt', 'w')
            file.writelines(todos)
            
            # crucial to avoid potential issues like data corruption and resource leaks.
            file.close()
        
        
        case 'show':
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()
            
            # remove \n to cut the extra breakline
            for index, item in enumerate(todos):
                row = f'{index+1}- {item.replace('\n', '')}'
                print(row)
        
        
        case 'edit':
            number = int(input('Number of the todo to edit: '))
            number = number - 1
            new_todo = input('Enter new todo: ')
            todos[number] = new_todo
        
        case 'complete':
            number = int(input('Number of the todo to complete: '))
            todos.pop(number - 1)
        
        
        case 'exit':
            break

print('Bye!')