from datetime import datetime

class Task:
    def __init__(self, description:str, date:str, status:str):
        self.description = description
        self.date = date
        self.status = status


    def __str__(self):
        return f"Task description: {self.description}. Date: {self.date}. Status: {self.status}\n"


class ToDoList:
    def __init__(self):
        self.input_description = ""
        self.input_date = ""
        self.input_status = ""
        self.tasks = []


    def interface(self):
        print("\nOptions:")
        print("1. Add Task")
        print("2. Edit Task")
        print("3. Delete Task")
        print("4. Display Tasks")
        print("5. Exit\n")


    def handle_user_input(self,openDescription:bool =True,openDate:bool =True, openStatus:bool =True):
        while openDescription:
            self.input_description = input("Enter task description:\n")
            if self.input_description:
                openDescription = False
            else:
                print("You did not enter task description\n")

        while openDate:
            self.input_date = input("Enter due date DD-MM-YYYY\n")
            try: 
                datetime.strptime(self.input_date,"%d-%m-%Y")
                openDate = False 
            except:
                print("incorrect date format. use format of DD-MM-YYYY\n" )

        while openStatus: 
            self.input_status = input("Enter the current status. : to do later  : in progress  : finish\n").strip().lower()
            
            if self.input_status == "to do later" or self.input_status == "in progress" or self.input_status == "finish":
                openStatus = False
            else:
                print("incorrect status state chose one of the three options")

  
    def add_task(self):
            self.handle_user_input()
            self.tasks.append(Task(self.input_description,self.input_date,self.input_status))
            print("New task added successfully\n")


    def handle_index_input(self,mode):
        while True:
            try:
                index = int(input(f"Enter the index of the task to {mode} "))
                index -=1
                if  0 <= index < len(self.tasks):
                    break      
            except:
                print("incorrect number of task")
        return index
    def is_tasks_empty(self):
        if not self.tasks:
            print("there is no tasks to edit\n")
            return True
        else: 
            return False


    def edit_task(self):
        if not self.tasks:
            print("No tasks in the list.\n")
            return

        self.display_tasks()
        index = self.handle_index_input("edit")

        while True:
            field = input("Enter the field that you want to edit: description , date or status ")
            if field == "description":
                self.handle_user_input(True,False,False)
                self.tasks[index].description = self.input_description
                break

            elif field == "date":
                self.handle_user_input(False,True,False)
                self.tasks[index].date = self.input_date
                break

            elif field == "status":
                self.handle_user_input(False,False,True)
                self.tasks[index].status = self.input_status
                break

            print("incorrect field name")

        print(f"Task number {index+1} edited successfully.")


    def delete_task(self):
        if not self.tasks:
            print("No tasks in the list.\n")
            return
        
        self.display_tasks()
        index = self.handle_index_input("delete")
        del self.tasks[index]
        print("Task deleted successfully.")


    def display_tasks(self):
        print("Tasks in To-Do List:\n")
    
        if not self.tasks:
            print("No tasks in the list.\n")

        else:
            for index, task in enumerate(self.tasks):
                print(f"Task {index+1}:")
                print(task)


def main():
    todo_list = ToDoList()

    while True:
       
        todo_list.interface()
        choice = input("Enter your choice: ")

        if choice == "1":    
            todo_list.add_task()

        elif choice == "2":
            todo_list.edit_task()

        elif choice == "3":
            todo_list.delete_task()
            
        elif choice == "4":
            todo_list.display_tasks()

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
