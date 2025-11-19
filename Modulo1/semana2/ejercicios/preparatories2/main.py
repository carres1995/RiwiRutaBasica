import crud

def main():
    while True:
        print("1. Add task ")
        print("2. mark tasks as completed")
        print("3. Delete task.")
        print("4. show task.")
        print("5. exit")
        
        option=int(input("Choose an option: "))
        if option == 1:
            name=input('task name: ')
            description=input('task description: ') 
            crud.create_task(name,description) 
        elif option == 2:
            print('1. si')
            print('2. no')
            mark =int(input("You want to mark task as finished? "))
            if mark == 1:
                id=int(input('Cual es el id: '))
                crud.state_task(id)
            else:
                print("Ok")
                continue
        elif option == 3:
            id=int(input('Cual es el id: '))
            crud.delete_task(id)
        elif option == 4:
            crud.show_tasks()
        elif option == 5:
            print("Thanks!!") 
            break 
        else: 
            print('Option not found')
            
            
if __name__== '__main__':
    main()                      
                         