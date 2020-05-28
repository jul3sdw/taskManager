#task_manager.py
#Written by:Julian de Wet
#Written on: 18/03/2020
#Task manager program that has both admin and ordinary users
#Admin change add users and look at different task and user stats

#imports
import datetime
import os
from datetime import date
from datetime import datetime
#Opening files
users = open('user.txt', 'r')
users2 = open('user.txt','a')
tasks2 = open('tasks.txt', 'a')
task_over = open('task_overview.txt', 'w')
user_over = open('user_overview.txt', 'w')
#declaring variables
i =0
q = 0
#declaring lists
password= []
username = []

options2=['r','a','va','vm','s','e','gr']
#Declaring dictionaries
login_check = {}
task_register = {}
dict_task ={}
#Declaring a variable for the current date
today = date.today()
#Declaring a variable to clear the screen when called
clear = lambda: os.system('cls')


#Defining a function that allows the admin to create a new user
def register_user():
    #User input for the new username
    new_username = input("Enter new user name - ")
    #While loop to check if the username has been created already
    while new_username in login_check:
        #Error message
        print('username in database already')
        new_username = input("Enter new user name - ")
    else:
        #User input for the new password
        new_password= input("Enter new password - ")
        print("New user successfully created")
        #Creating a list to add to the 'user.txt' file
        total = []
        total.append(new_username)
        total.append(new_password)
        users2.write('\n'+total[0]+', '+total[1])
        created = "New user successfully created"

#Defining a function that clears the screen when you are finished
def menu_return():
    #User input
    finished = input("press <ENTER> to return to menu").strip()
    #While loop to check if the user input is a valid entry
    while finished != "":
        finished = input("press <ENTER> to return to menu").strip()
    else:
        #Clears the screen
        clear()

#Defining a function to create a new task in 'task.txt'
def add_task():
    #user input for which user the task is assigned to
    register_task_user = input("Which user are you assigning this task to - ")
    #While loop to if input is a valid username
    while register_task_user not in login_check:
        #Error message
        print("Invalid username!!!")
        register_task_user = input("Which user are you assigning this task to - ")

    else:
        #User inputs for each category of the task
        register_task_title = input("Enter the tasks title - ")
        register_task = input("Enter what the task entails - ")
        register_task_date = input("Assign a due date for the task - ")
        #Converts current date to a more user friendly format
        month_fix = today.strftime('%d ''%b ''%Y')
        #All tasks must be created incomplete
        register_task_done = "No"
        #Dictionary to help organise the data
        task_register ={'user': register_task_user,
                        'title': register_task_title,
                        'task': register_task_title,
                        'date': register_task_date,
                        'done' : register_task_done
                        }
        print("Task successfully created")
        #Writing the new task to 'task.txt'
        tasks2.write('\n'+task_register['user']+', '+task_register['title']+', '+task_register['task']+', '+str(month_fix)+ ', '+task_register['date']+', '+task_register['done'])

#Defining a function to view all current tasks         
def view_all():
    #Opening file 'tasks.txt' to read from 
    task_view_all = open('tasks.txt','r')
    l=0
    #Outputting a string to make the function more user friendly
    print('\nAll current tasks: \n')
    #For loop to read 'tasks.txt' into a variable
    for task_line in task_view_all:
        #Counter to provide id numbers to each task
        l+=1
        #splitting each line into a list to make formatting the output simpler
        new_task = task_line.split(',')
        #Output each task in a user friendly manner
        print('ID number: '+str(l)+'\n'+'User: '+new_task[0]+'\nTask: '+new_task[1]+'\nTask details: '+new_task[2]+'\nDate assigned: '+new_task[3]+'\nDate due: '+new_task[4]+'\ndone: '+new_task[5])
    #Closing the file
    task_view_all.close()
    print('\n')
    
#Defining a function that lets you see and edit your own tasks
def view_mine():
    #Declaring variables
    m=0
    l =0
    #Declaring lists and dictionaries
    yes_no =['yes','no']
    new_number ={}
    yes = {}
    #opens file 'tasks.txt'
    tasks = open('tasks.txt','r+')
    #Output telling the user that these are their tasks
    print(username_input + '\'s tasks:\n')
    #For loop that reads from 'tasks.txt'
    for task_line in tasks:
        m+=1
        #Adding an id number to each task and splitting each line into a list
        new_task =[f"id number: {m}"]+ task_line.split(',')
        
        #If statement to only print out 
        if new_task[1] == username_input:
            #Arranging each task in a user friendly format
            total_task ='Task ID: '+new_task[0]+'\nUser: '+new_task[1]+'\nTask: '+new_task[2]+'\nTask details: '+new_task[3]+'\nDate assigned: '+new_task[4]+'\nDate due: '+new_task[5]+'\ndone: '+new_task[6]+'\n'
            #Creating a dictionary for each task
            new_number[m] = total_task
            yes[m] = ','.join(new_task)
                
            #Outputting each formatted task
            print(total_task)
    tasks.close()

    #User input to select which task to edit
    entered_number = input("enter id number of task you would like to edit ('-1' if you don't want to edit): ")
    #If statement to not edit a task
    if entered_number == '-1':      
            return
        #While loop Checks if id number is valid if not it asks user until the enter a valid one 
    while int(entered_number) not in new_number:
        entered_number = input("enter id number of task you would like to edit('-1' if you don't want to edit): ")
        #If statement to not edit a task
        if entered_number == '-1':      
            break
            
    else:
        #Creating a list using a based off the ID number of the task in the dictionary
        yes_test = yes[int(entered_number)].split(',')

        #While loop that tests whether the selected task is completed, if not it loops a request to input an incomplete task to edit
        while yes_test[6] == ' Yes\n':
            print('cannot edit a task marked as complete')
            entered_number = input("enter id number of task you would like to edit('-1' if you don't want to edit): ")
            yes_test = yes[int(entered_number)].split(',')
            if entered_number == '-1':      
                break
        else:
            
            print (new_number[int(entered_number)])
            #Input request to mark the task as complete
            complete = input("Would you like to mark this complete ")
            #if statement that tests whether or not you entered 'yes' to mark the task as complete    
            if complete.lower() == 'yes':
                print('marked as complete')
                #Creating a variable to store the new edited task 
                final = ""
                #Openning a 'tasks.txt' to read
                task_edit_read = open('tasks.txt','r')
                #For loop to replace 'no' with 'yes' for the selected task
                for line3 in task_edit_read:
                    l+=1
                    #IF statement to change the incomplete status of the selected task to complete
                    if l == int(entered_number):
                        completed = line3.replace('No','Yes')
                        final += completed
                        #else statement to keep unselected tasks unchanched
                    else:
                        final+=line3
                        print(final)
                        #openning 'tasks.txt' to write the new 'tasks.txt'
                        tasks_edit_write = open('tasks.txt','w')
                        #Rewriting the edited task
                        tasks_edit_write.write(final)
                print('marked as complete')          

            #IF statement to change either the username or due date
            if complete.lower() == 'no':
                joined =""
                #User input to choose how to edit the task
                task_edit = input("What are you changing about this task: ")
                #If statement to change the due date of the task
                if task_edit.lower() == 'due date':
                    new_date = input("Enter a new due Date: ")
                    #Openning the fie 'tasks.txt' to read from
                    task_edit_read = open('tasks.txt','r')
                    #Creating a variable to rewrite the task with the changed due date
                    final = ""
                    #for loop to read from 'tasks.txt'
                    for line3 in task_edit_read:
                        #Counter
                        l+=1
                        #if statement to change the due date and add it to the new task
                        if l == int(entered_number):
                            #Splits the task into a list so you can change the due date only
                            splitted = line3.split(', ')
                            #Replacing the old due date with the new due date
                            splitted[4] = new_date
                            #Join the new list together
                            joined = ', '.join(splitted)
                            #adding the new edited task back into what will be the new file
                            final+= joined
                        #Else statement to add the uneditted tasks to the file
                        else:
                            final+= line3
                        
                    print(final)
                    #Openning file 'tasks.txt' to write the editted task
                    task_edit_write = open('tasks.txt','w')
                    #Writing the editted task to the file
                    task_edit_write.write(final)

                #If statement to change the username the task is registered to
                elif task_edit.lower() == 'username':
                    #User input for the new username
                    new_username = input("new username: ")
                    #While loop to check if the new username is registered with the task manager
                    while new_username not in login_check:
                        #Error message
                        print("Invalid username!!!")
                        new_username = input("new username: ")

                        
                    else:                     
                        #opens the file 'tasks.txt'
                        task_edit_read = open('tasks.txt','r')
                        final = ""
                        #For loop to read file 'tasks.txt'                 
                        for line3 in task_edit_read:
                            #Counter
                            l+=1
                            #If statement
                            if l == int(entered_number):
                                completed = line3.replace(username_input,new_username)
                                final += completed
                            else:
                                final+=line3
                                    
                                print(final)
                                task_edit_write = open('tasks.txt','w')
                                task_edit_write.write(final)
                                
    #Closing all the files that have been opened                
            task_edit_read.close()
            task_edit_write.close()
    tasks.close()

#Declaring a function that finds the total number of users and tasks
def stats():
    print("Statistics:")
    #openning files
    user_stats = open('user_overview.txt','r')
    task_stats = open('task_overview.txt','r')
    #Declaring variable
    t=0
    #for loop to read from file
    for lines_stats in task_stats:
        #Counter
        t+=1
        #if statement to get the number of tasks from file 'task_overview.txt'
        if t ==2:
            split_stats = lines_stats.split(':\t\t')
            #Output the total number of tasks that have been created in a user friendly format
            print("Total tasks:\t"+split_stats[1])
    #Resetting the counter
    t=0
    #For loop to read file 'user_overview.txt'
    for lines_stats2 in user_stats:
        #Counter
        t+=1
        #If statement to get the number of users that are using 'task_manager'
        if t==2:
            split_stats2 = lines_stats2.split(':\t')
            #Outputting the number of users using 'task_manager' in a user friendly format
            print("Total users:\t"+split_stats2[1])
        
#Defining a function that generates reports about currently registered tasks and users
def generate_reports():
    #openning files
    task_report = open('tasks.txt','r')
    task_over = open('task_overview.txt', 'w')
    user_over = open('user_overview.txt', 'w')
    #declaring counting variables
    y = 0
    n = 0
    k = 0
    total_tasks = 0
    #dictionary to convert dates
    num_to_month={'Jan':1,
                      'Feb':2,
                      'Mar':3,
                      'Apr':4,
                      'May':5,
                      'Jun':6,
                      'Jul':7,
                      'Aug':8,
                      'Sep':9,
                      'Oct':10,
                      'Nov':11,
                      'Dec':12,
                      }

    #for loop to read from file 'tasks.txt'
    for line_report in task_report:
        #Counts the total tasks registered
        total_tasks +=1
        #Splits each line of the file into a list
        split=line_report.split(',')
        #This then splits a specific part of the line into words in a list
        due_date_split = split[4].split(' ')
        #Formatting the date
        due_date = f"{due_date_split[1]}/{num_to_month[due_date_split[2]]}/{due_date_split[3]}"
        #Converting the due date into a datetime data type
        due_date_final = datetime.strptime(due_date, '%d/%m/%Y').date()
        #if statement that counts how many tasks are complete
        if split[5] == ' Yes\n':
            y+=1
        elif split[5] == ' No\n':
            n+=1
            #If statement that counts how many tasks are overdue
            if today>due_date_final:
                k+=1
    #calculates the total percentage of tasks that are overdue
    percentage_overdue = k/total_tasks*100
    #Calculates the total percentage of tasks incomplete
    percentage_incomplete = n/total_tasks*100
    #writes the stats collected and worked out to file 'task_overview'
    task_over.write(f"Tasks Overview:\nTotal tasks:\t\t{total_tasks}\nCompleted tasks:\t{y}\nUncomplete tasks:\t{n}\nPercentage incomplete:\t{percentage_incomplete:.3}%\nTotal tasks Overdue:\t{k}\nPercentage overdue:\t{percentage_overdue:.3}%")

    #opening file 'user.txt to read from
    users_report = open('user.txt','r')
    #Declaring an empty list
    final=[]
    #For loop to read each line of the file 'user.txt'
    for user_report_line in users_report:
        #Splitting each line into a list so you can read each username separately from the password
        splitsed=user_report_line.split(',')
        #Adding each username to a list
        final+=splitsed[0]
        task_report = open('tasks.txt','r')
        #Declaring/resetting variables that will be used as counters
        y2=0
        n2=0
        j=0
        d =0

        #For loop to read from the file 'tasks.txt', it reads the tasks for each user
        for task_line2 in task_report:
            #Splits each line into a list
            split2=task_line2.split(',')
            #counter
            j+=1
            #Splits specific part of the list into another list
            split3 = split2[4].split(' ')
            split4 = split2[3].split(' ')
            #If staement that checks the completeness of each users task
            if split2[0] == splitsed[0]:
                #Formatting the due date
                due_date_user = f"{split3[1]}/{num_to_month[split3[2]]}/{split3[3]}"
                #Converting the due date to datetime data type
                due_date_user_final = datetime.strptime(due_date, '%d/%m/%Y').date()
                #If statement to count the number of complete tasks
                if split2[5] ==' Yes\n':
                    y2+=1
                elif split2[5] ==' No\n':
                    n2 +=1
                    #If statement to count the number of overdue tasks
                    if today>due_date_final:
                        d+=1

        #If statement to work out the percentafe of tasks overdue without crashing the program
        if d!=0:        
            percentage_overdue = d/(y2+n2)*100
        else:
            percentage_overdue=0.0
        percentage_total = (y2+n2)/j*100
        #If statement to work out the percentage of tasks completed without crashing the program
        if y2 !=0:
            percentage_completed = y2/(y2+n2)*100
        #prevents
        else:
            percentage_completed =0.0
        #If statement to work out the percentage of tasks incomplete without crashing the program
        if n2 !=0:
            percentage_incomplete =n2/(y2+n2)*100
        else:
            percentage_incomplete =0.0
        #If statement to work out the percentage of tasks completed without crashing the program
        if y2+n2 ==0:
            percentage_completed =0.0
        user_over.write(f"User Overview:\nTotal users:\t{i}\nTotal tasks:\t{total_tasks}\n{splitsed[0]}'s Overview:\n\tCompleted: {y2}\n\tIncomplete: {n2}\n\tpercentage of total: {percentage_total:.3}%\n\tPercentage complete: {percentage_completed:.3}%\n\tPercentage incomplete: {percentage_incomplete:.3}%\n\tPercentage overdue: {percentage_overdue:.3}%")

    #Closing all the opened files
    users_report.close()
    task_report.close()
    task_over.close()
    user_over.close()

#Outputs heading for login screen
print('Login:\n' + 50*'=')
#Outputs today's date
print(today)
#User input for username
username_input = input("Enter username -\t")

#For loop to read usernames and passwords from 'user.txt'
for line in users:
    #Counter to count total number of users
    i+=1
    #Splits the usernames and passwords up into separate lists
    username, password = line.strip().split(',')
    #Creating a dictionary with usernames as key words that link to their passwords
    login_check[username] = password.strip()

#While loop that tests whether the entered username is valid
while username_input not in login_check:
    #Error message
    print(50*'='+'\n'+"Incorrect username, try again:")
    username_input = input("Enter username -\t")
    #clears screen
    clear()

else:
    #User input for the password
    password_input = input("Enter password -\t")
    #While loop that tests whether the password is valid, loops the input until a valid username is provided
    while login_check[username_input] != password_input:
        print(50*'='+'\n'+"Incorrect password, try again:")
        password_input = input("Enter password -\t")
        #clears screen
        clear()

    else:
        #Clears screen
        clear()
        #If statement to display a menu suited for the admin
        if username_input == 'admin':
            #Infinite while loop so the user can return to the menu until exit option is selected
            while True:
                #Ouputs to say the login was successful and who is logged in
                print("login successful")
                print("You are logged in as admin")
                #User input that displays menu options for admin, Allows user to enter a choice
                options = input(50*'='+'\n'+"Please enter one of the following:\nr - register user\na - add task\nva - view all tasks\nvm - view my tasks\ngr - generate reports\ns - Statistics\ne - exit\n"+50*'='+'\n').lower()
                #Uses a list of valid responses to test whether the option entered was valid, loops until a valid option is entered
                while options not in options2:
                    print("you did not enter a valid value\n")
                    options = input(50*'='+'\n'+"Please enter one of the following:\nr - register user\na - add task\nva - view all tasks\nvm - view my tasks\ns - Statistics\ne - exit\n"+50*'='+'\n').lower
                else:
                    #clears screen
                    clear()

                    #If statement to allow the user to register a new user
                    if options == "r":
                        #Calls function to register a new user
                        register_user()
                        #Calls function to clear screen and direct the user back to the menu
                        menu_return()
                        continue

                    #If statement to allow the user to create a new task
                    elif options == "a":
                        #Calls function to register a new task
                        add_task()
                        #Calls function to clear screen and direct the user back to the menu
                        menu_return()
                        continue

                    #If statement to allow the user to view all currently registered tasks
                    elif options == "va":
                        #Calls function to view all tasks
                        view_all()
                        #Calls function to clear screen and direct the user back to the menu
                        menu_return()
                        continue

                    #If statement to allow the user to view/edit their currently registered tasks
                    elif options == 'vm':
                        #Calls function to view the users tasks
                        view_mine()
                        #Calls function to clear screen and direct the user back to the menu
                        menu_return()
                        continue

                    #If statement to allow the admin to view the total number of tasks and users registered
                    elif options == 's':
                        #Calls function to generate detailed reports as text files
                        generate_reports()
                        #Calls function to display the number of registered tasks and users
                        stats()
                        #Calls function to clear screen and direct the user back to the menu
                        menu_return()
                        continue

                    #If statement to allow the admin to create detailed reports as text files about the tasks and users registered
                    elif options == 'gr':
                        #Calls function to generate detailed reports as text files
                        generate_reports()
                        #Calls function to clear screen and direct the user back to the menu
                        menu_return()
                        continue
                        
                    #If statement to end program
                    elif options == 'e':
                        #Outputs log out message
                        print('logging out')
                        #clears the screen
                        clear()
                    #Breaks out of loop and ends program
                    break
                
        else:
            while True:
                #User input that displays menu options for normal user, Allows user to enter a choice
                options = input(50*'='+'\n'+"Please enter one of the following:\na - add task\nva - view all tasks\nvm - view my tasks\ne - exit\n"+50*'='+'\n').lower()
                #Uses a list of valid responses to test whether the option entered was valid, loops until a valid option is entered
                while options not in options2:
                    print("you did not enter a valid value\n")
                    options = input(50*'='+'\n'+"Please enter one of the following:\na - add task\nva - view all tasks\nvm - view my tasks\ne - exit\n"+50*'='+'\n').lower
                else:
                     #If statement to allow the user to create a new task
                    if options == "a":
                        #Calls function to register a new task
                        add_task()
                        #Calls function to clear screen and direct the user back to the menu
                        menu_return()
                        continue
                    
                    #If statement to allow the user to view all currently registered tasks
                    elif options == "va":
                        #Calls function to view all tasks
                        view_all()
                        #Calls function to clear screen and direct the user back to the menu
                        menu_return()
                        continue

                    #If statement to allow the user to view/edit their currently registered tasks
                    elif options == 'vm':
                        #Calls function to view the users tasks
                        view_mine()
                        #Calls function to clear screen and direct the user back to the menu
                        menu_return()
                        continue
                                    
                                        
                   #If statement to end program
                    elif options == 'e':
                        #Outputs log out message
                        print('logging out')
                        #clears the screen
                        clear()
                    #Breaks out of loop and ends program
                    break

                
                
            
                
#Closing open files           
users.close()
users2.close()
tasks2.close()
task_over.close()
user_over.close()
