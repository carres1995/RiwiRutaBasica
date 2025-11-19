import json
import csv
import os

os.makedirs("datos", exist_ok=True)

CSV='datos/datos.csv'
JSON='datos/datos.json'

def load_json():
    try:
        with open(JSON, 'r') as a:
            return json.load(a)
    except FileNotFoundError:
        return []
def load_csv():
    try:
        task=[]
        with open(CSV, 'r') as a:
            reader=csv.DictReader(a)  
            for r in reader:
                task.append(r)
    except FileNotFoundError:
        pass
    return task            

def save_json(task):
    with open(JSON,'w') as a:
            json.dump(task,a, indent=2)
            
def save_csv(task):
    with open(CSV, 'w', newline='') as a:
        write=csv.DictWriter(a, fieldnames=['id','task', 'description','state'])
        write.writeheader()
        for t in task:
            write.writerow(t)               
            