from datetime import datetime
import csv
import time

FILE = 'SMART_GOAL.csv'
FILE_2 = 'SMART_GOAL_accomplished.csv'

class SMART:
    def display_command(self):
        print('COMMAND MENU: 🤓')
        print('command - Display command menu')
        print('create - Create new SMART objective')
        print('view - View all SMART Objectives')
        print('edit - Edit SMART Objective')
        print('delete - Delete a SMART Objective')
        print('goal_completed - Add a SMART Objective in your accomplishments')
        print('view_accomplishments - Display all your accomplishments')
        print('exit - Exit the program')
        print('----------------------------------------\n')
    def file_to_list(self, file_name):
        goal_2d_list = []
        with open(file_name, 'r', newline='') as csv_file:
            csv_read = csv.reader(csv_file)
            for line in csv_read:
                goal_2d_list.append(line)
        return goal_2d_list


    def list_to_file(self, goal_2d_list, file_name):
        with open(file_name, 'w', newline='') as csv_file:
            csv_write = csv.writer(csv_file)
            csv_write.writerows(goal_2d_list)
                
    def __init__(self, goal, objective, target_date, measurements):
        self.goal = goal
        self.objective = objective
        self.target_date = target_date
        self.measurements = measurements
    
    # Putting the goals into the 2d_list
    def goals_to_2dlist(self, goal_2d_list):
        goal_list = [self.goal, self.objective, self.target_date, self.measurements]
        goal_2d_list.append(goal_list)
        # print(goal_2d_list)
        # return goal_2d_list

# Displaying each SMART goals
    def display_goals(self, goals_2d_list):
        print('----------------------------------------')
        time.sleep(1.5)
        print("Displaying SMART Objectives...💪💪💪")
        print('----------------------------------------')
        time.sleep(1.5)
        for index, x in enumerate(goals_2d_list):
            print(f"\nSMART Objectives {index+1}:\n")
            time.sleep(2)
            print(f"Goal: {x[0]}")
            time.sleep(1)
            print(f"Objective: {x[1]}")
            time.sleep(1)
            print(f"Targeted Date: {x[2]}")
            time.sleep(1)
            print(f"Measurements: {x[3]}")
            time.sleep(1.3)
            print('----------------------------------------')
            time.sleep(1)


    def create_goals(self, goals_2d_list):
        time.sleep(1)
        print('----------------------------------------')
        time.sleep(1)
        print(f"Creating SMART Objective ({len(goals_2d_list)+1}) 💪\n")
        time.sleep(1.5)
    
        self.goal = input("Enter Goal: ")

        self.objective = input("Enter Objective: ")
        
        target_date = input("Target Date (MM/DD/YYYY): ")
        target_date_format = "%m/%d/%Y"
        target_date_obj = datetime.strptime(target_date, target_date_format)
        self.target_date = target_date_obj.strftime("%B %d, %Y")

        self.measurements = input("Enter Measurements: ")
    
        
        self.goals_to_2dlist(goals_2d_list)

        print("A new goal has been added!")


        
    def edit_smart(self, goals_2d_list:list):
        print("Select a SMART Objective (number) to edit...")
        time.sleep(1.5)
        self.list_only_goals(goals_2d_list)
        time.sleep(0.5)
        edit_smart = int(input("Enter Smart Objective (number) to edit: "))
        time.sleep(1)
        print('----------------------------------------\n')
        time.sleep(1)
        print(f"Editing Smart Objective ({edit_smart})...🤯\n")
        time.sleep(1.5)
        self.display_specific_smart_goal(edit_smart,goals_2d_list)
        time.sleep(1.5)
        print()
        edit_category = input("Pick SMART category to edit (goal/objective/date/measurement): ")
        time.sleep(1)
        print('----------------------------------------')

        if edit_category.lower() == 'goal':
            goals_2d_list[edit_smart-1][0] = input("Edit goal: ")
            time.sleep(1)
            print(f"The goal has been edited for SMART Objective {edit_smart}.\n")

        elif edit_category.lower() == 'objective':
            goals_2d_list[edit_smart-1][1] = input("Edit objective: ")
            print(f"The objective has been edited for SMART Objective {edit_smart}.\n")
            time.sleep(1)

        elif edit_category.lower() == 'date':
            target_date = input("Target Date (MM/DD/YYYY): ")
            target_date_format = "%m/%d/%Y"
            target_date_obj = datetime.strptime(target_date, target_date_format)
            goals_2d_list[edit_smart-1][2] =   target_date_obj.strftime("%B %d, %Y")
            time.sleep(1)
            print(f"The date has been edited for SMART Objective {edit_smart}.\n")
        
        elif edit_category.lower() == 'measurement':
            goals_2d_list[edit_smart-1][3] = input("Edit measurement: ")
            time.sleep(1)
            print(f"A measurement has been edited for SMART Objective ({edit_smart}).\n")
        
        time.sleep(1)
        print('----------------------------------------')


        
    def delete_goal(self, goals_2d_list:list):
        if len(goals_2d_list) == 0:
            print("Sorry, you do not have any goals listed")
        else: 
            print("Select a SMART Objectives (number) to delete... 😭")
            time.sleep(1.5)
            self.list_only_goals(goals_2d_list)
            delete_goal = int(input("Enter Smart Objectives (number) to delete: "))
            goals_2d_list.pop(delete_goal-1)
            time.sleep(1.3)
            print(f"\nSMART Objectives ({delete_goal}) has been deleted")
            time.sleep(1)
            print('----------------------------------------')   


    def goal_completed(self, goals_2d_list:list):
        print("Select SMART Objective (number) completed... 😎")
        time.sleep(1.5)
        self.list_only_goals(goals_2d_list)    
        accomplished_goal_index = int(input("Enter Smart Objectives (number) you have completed: "))
        print('------------------------------------')

        time.sleep(1.5)
        print(f"Transfering SMART Objectives ({accomplished_goal_index})...")
        goals_2d_list[accomplished_goal_index-1].append(datetime.now().date().strftime("%B %d, %Y"))
        # print(goals_2d_list)
        with open(FILE_2, 'a', newline='') as csv_file:
            csv_write = csv.writer(csv_file)
            csv_write.writerow(goals_2d_list[accomplished_goal_index-1])
        
        time.sleep(2)
        goals_2d_list.pop(accomplished_goal_index-1)
        print(f"\nSMART Objectives ({accomplished_goal_index}) is now in the completed section.")

        time.sleep(3)
        print("Congrats on your accomplishment! 🥳🎂🍾")
        print('----------------------------------------')

        time.sleep(3)
    
    def display_goals_completed(self):
        accomplishments_2d_list = self.file_to_list(FILE_2)
        print('----------------------------------------')
        time.sleep(1.5)
        print("Displaying completed SMART Objectives...🥳🎂🍾")
        print('----------------------------------------')
        time.sleep(1.5)
        for index, x in enumerate(accomplishments_2d_list):
            print(f"\nSMART Objectives ({index+1}):")
            time.sleep(2)
            print(f"Date Accomplished: {x[4]}")
            time.sleep(1.3)
            print(f"\nGoal: {x[0]}")
            time.sleep(1)
            print(f"Objective: {x[1]}")
            time.sleep(1)
            print(f"Targeted Date: {x[2]}")
            time.sleep(1)
            print(f"Measurements: {x[3]}")
            time.sleep(1.3)
            print('----------------------------------------')
            time.sleep(1)
        


# Side function
    def list_only_goals(self, goals_2d_list):
        print('----------------------------------------')
        time.sleep(1)
        for index, goal in enumerate(goals_2d_list):
            print(f"Smart Objective ({index+1}):\n")
            time.sleep(1)
            print(f"Main Goal: {goal[0]}")
            time.sleep(1)
            print('----------------------------------------')
            time.sleep(1)

    def display_specific_smart_goal(self, display_index, goals_to_2d_list):
        for index, x in enumerate(goals_to_2d_list):
            if index == display_index - 1:
                print(f"Goal: {x[0]}")
                time.sleep(1)
                print(f"Objective: {x[1]}")
                time.sleep(1)
                print(f"Targeted Date: {x[2]}")
                time.sleep(1)
                print(f"Measurement: {x[3]}")
                time.sleep(1)
                


def main():
    
    user_1 = SMART("", "", "", "")
    command = ''

    print("\nWelcome to SMART Objectives 😎\n")
    time.sleep(1)
    user_1.display_command()
    time.sleep(1)

    while command != 'exit':
        goals_2d_list = user_1.file_to_list(FILE)
        command = input("Enter a command: ")
        print()
        
        if command.lower() == 'create':
            # print(len(goals_2d_list))
            if len(goals_2d_list) >= 10:
                print("Sorry, your goal is currently full.")
            else:
                user_1.create_goals(goals_2d_list)
        
        elif command.lower() == 'command':
            user_1.display_command()

        elif command.lower() == 'view':
            user_1.display_goals(goals_2d_list)
        
        elif command.lower() == 'delete':
            user_1.delete_goal(goals_2d_list)
        
        elif command.lower() == 'edit':
            user_1.edit_smart(goals_2d_list)
        
        elif command.lower() == 'goal_completed':
            user_1.goal_completed(goals_2d_list)
        elif command.lower() == 'view_accomplishments':
            user_1.display_goals_completed()

        else:
            time.sleep(2)
            print("Sorry, please try again")
            time.sleep(1)
            print("-----------------------------")
            time.sleep(1)

        user_1.list_to_file(goals_2d_list, FILE)
    

    print("Bye!")

if __name__ == '__main__':
    main()
    
