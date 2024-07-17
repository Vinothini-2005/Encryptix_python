# importing json module

import json

class TaskManager:           # contructor 
    def __init__(self, filepath='tasks.txt'):
        self.filepath = filepath
        self.tasks = self.load_tasks()

    def load_tasks(self):     #load the tasks in the json file
        try:
            with open(self.filepath, 'r') as file:
                tasks = json.load(file)
                return tasks
        except FileNotFoundError:
            return []

    def save_tasks(self):       #save the task in the json
        with open(self.filepath, 'w') as file:
            json.dump(self.tasks, file)

    #add the task given by the user
    def add_task(self, description):
        task = {
            'description': description,
            'completed': False
        }
        self.tasks.append(task)
        self.save_tasks()

    # update the given task
    def update_task(self, index, completed):
        if 0 <= index < len(self.tasks):
            self.tasks[index]['completed'] = completed
            self.save_tasks()

    # delete the task that is aready given by the user
    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            self.save_tasks()

    #display the task
    def get_tasks(self):
        return self.tasks
