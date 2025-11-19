import data

task=data.load_csv()

def save(task):
    data.save_csv(task)
    data.save_json(task)
    
def create_task(name, description):
    global task
    id = len(task) + 1
    new ={
        'id':id,
        'task':name,
        'description':description,
        'state': 'earring'
    }
    task.append(new)
    #task=new
    save(task)
    return print(f"| ID {new['id']} | task {new['task']} | description {new['description']} | ")

def show_tasks():
    global task
    
    for t in task:
        print(f"| ID {t['id']:5} | task {t['task']:15} | description {t['description']:50} | state {t["state"]:15} |")
    return task

def delete_task(id:int):
    global task
    news= []
    for t in task:
        if id != t['id']:
            news.append(t) 
    if len(news) == len(task):
        print("ID not found")
        return False    
    task=news
    save(task)       
    print(f'Task delete id: {id}')  
    return True     
        
def state_task(id:int):
    global task
    for t in task:
        if id ==t['id']:
            if t['state'] == 'earring':
                t['state']= 'carried out'
                save(task)
            else:
                print('the task has already been completed')
    print('ID not found')
    return print(f"| ID {t['id']:5} | task {t['task']:15} | description {t['description']:50} | state {t["state"]:15} |")

                            