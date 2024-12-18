while True:
    user_action = input('Type add, show, edit, complete, or exit: ')
    user_action = user_action.strip()
    
    match user_action:
        case 'add':
            todo = input('Enter a todo: ') + '\n'
            
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()
            
            todos.append(todo)
            
            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()
        
        case 'show':
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()
            
            # brute force method
            '''
            new_todos = []
            for item in todos:
                new_item = item.strip('\n')
                new_todos.append(new_item)
            '''
            
            # list comprehension
            # [expression for item in iterable if condition] --> always return a list
            # new_todos = [item.strip('\n') for item in todos]
            
            for index, item in enumerate(todos):
                
                # item = item.replace('\n', '')
                item = item.strip('\n')
                row = f'{index+1}- {item}'
                print(row)
        
        case 'edit':
            number = int(input('Number of the todo to edit: '))
            number = number - 1
            
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()
            
            new_todo = input('Enter new todo: ')
            todos[number] = new_todo
            
            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()
        
        case 'complete':
            number = int(input('Number of the todo to complete: '))
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()
            
            todos.pop(number - 1)
            
            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()
            
        case 'exit':
            break

print('Bye!')