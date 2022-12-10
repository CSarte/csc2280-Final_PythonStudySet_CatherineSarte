# Name:  Catherine Sarte
# Date:  12/09/2022
# Email: csarte250@gmail.com
# Course: Introduciton to Computer Science
# Section: CSC 2280
# Assignment: Cram Sesh/ Final Project

# Description:.....

# Honor Code: “I will practice academic and personal integrity and excellence of character  
# and expect the same from others.”


import tkinter as tk
from tkinter import *
from tkinter import filedialog
import random

#Global lists to be used throughout code
questions = []
answers = []
mastery_count = [] 
focus_count = []
open_questions = []
loop_count = 1
total_mastery_count = []
total_focus_count = []

#Function to take user enter question_set list and number of questions to create answer and question lists 
def find_questions_answers(num_questions, question_set):
    #Split the question_set into a list of lines where each line aternates with the questions and answer
    questions_w_answers = (question_set.splitlines())
    
    #If the length of questions_w_answers is less than the amount of questions and answers that the user is calling for
    # , tell user that their entry is invalid 
    if len(questions_w_answers) < (int(num_questions) * 2):
        #create error widnow to display invalid entry
        endProgram = Tk()
        endProgram.title("Error")
        endProgram.configure(background="white")
        Label(endProgram, text='''The number of questions you gave does not match the number
            questions in the file.''',
              bg="white", fg = "black", font="Times").pack()
        Label(endProgram, text="Please try again",
          bg="white", fg = "black", font="Times").pack()
        addSet(x = 1)
    #Loop until questions and answers within the file have been seperated 
    for i in range(0, int(num_questions)*2, 2):  
        #Set next questions in the set to quesiton list
        questions.append(questions_w_answers[i])
        #Set next answer in the set to answer list 
        answers.append(questions_w_answers[i+1])
        
    #Go back to main window to display found questions with answers
    main()
# end of find_questions_answers function
    
    
#Function to ask user if they actually want to close the program or not
def end_program_function():
    #Button Function to enter if they want to leave the program
    def yes_Click():
        #End Program
        exit()
    # end yes_click funciton
    
    #Button Function to enter if they changed their mind and don't want to leave the program 
    def no_Click():
        #Go back the main menu
        main()
    # end no_click function
    
    #Window to display goodbye message and make sure that they want to exit
    endProgram = Tk()
    endProgram.title("Exit")
    endProgram.configure(background="white")
    Label(endProgram, text="Good Study Session!",
          bg="white", fg = "black", font="Times").pack()
    Label(endProgram, text="Are you sure that you want to exit?",
      bg="white", fg = "black", font="Times").pack()

    #This button is to confirm that the user wants to exit
    yes_button = tk.Button(endProgram, text="Yes", padx = 40, pady = 6,
                     fg = "black", bg = "white", command = yes_Click)
    yes_button.pack(pady=20)
    
    #This button is for the user to go back to the menu if they don't want to exit
    no_button = tk.Button(endProgram, text="No", padx = 40, pady = 6,
                        fg = "black", bg = "white", command = no_Click)
    no_button.pack(pady=20)
    
    tk.Frame(endProgram, bg="white")
# end of end_program_function

   
#Button Function to collect/create studyset from the user 
def addSet():
    #Varible to check if this is the first time they opened the window
    intro = 0
   
   #Button Function for user to enter their study set questions from a file dialog
    def open_text():
        #set window placement to not get in the way of dialog box
        setNUM.geometry('670x600+700+50')
        
        #Open file dialog box and save the enter text value into text_file
        text_file= filedialog.askopenfilename(initialdir="C:/gui/", title = "open text files",
                                              filetypes = (("TextFiles", "*.txt"),))
        #OPen the test_file selected to collect data
        text_file = open(text_file, 'r')
        #Read the number of lines within the text_file
        num_lines = text_file.read()
        #Insert the all of the lines from the text_file to the collect_Questions text box
        collect_Questions.insert(END, num_lines)
        #Close Users file for them 
        text_file.close()
    # end open_text function
        
    #Button Function so user can edit the study set on text file then save and finalize the questions
    def save_text():
        #Loop until user entry has been analyzed and is valid
        while True:
            #If the user entry in num_questions is a number check if it is within the proper range of questions
            if num_questions.get().isdigit():
                #If the value from num_questions entry box is less than or equal to 50 and greater than or equal to 3, save data
                if int(num_questions.get()) <= 50 and int(num_questions.get()) >= 3:
                    #Officially save entry number value to user_NumQuestions
                    user_NumQuestions = num_questions.get()
                    #Set the window geometry to not get in the way of the dialog box
                    setNUM.geometry('670x600+700+50')
                    #Open file dialog box and collect text file chosen from the user to save to text_file
                    text_file = filedialog.askopenfilename(initialdir="C:/gui/", title = "open text files",
                                                          filetypes = (("TextFiles", "*.txt"),))
                    #Open text_file selected to write into
                    text_file = open(text_file, 'w')
                    #Write the data from collect_Questions text box into the chosen text_file
                    text_file.write(collect_Questions.get(1.0, END))
                    
                    #From the data entered in the text box, save it into a string variable question_set
                    question_set = collect_Questions.get(1.0, "end-1c")
                    #Call funciton to evaluate the question_set entered by the user and assign the asnwer and questions using user_NumQuestions
                    find_questions_answers(user_NumQuestions, question_set)
                #Else, the num_questions value is greater than or less than 3
                else:
                    break
            #Else, num_questions is not a digit and invalid so break 
            else:
                break
        #Create window user that the user_NumQuestions value was invalid
        info = Tk()
        info.title("Error")
        info.configure(background="white")
        Label(info, text="You must enter a number less than or equal to 50 and greater than or equal to 3 into the Number of Questions entry box.", bg="white",
              fg = "black", font="Times").pack()
        Label(info, text="Please try again.", bg="white",
              fg = "black", font="Times").pack()
    # end save_text funciton
        
    #Function to instruct user how to enter their study set  
    def creation_instruct():
        #Create and display window that explains to the user how to enter their study set
        info = Tk()
        info.title("Instructions")
        info.geometry('650x650+50+50')
        info.configure(background="white")
        Label(info, text="HOW TO UPLOAD A STUDY SET", bg="white",
              fg = "black", font="Times").pack()
        Label(info, text='''1. Make your studyset text file
-- Make a text file that lists out your study set.
-- It should be ordered question on the first line and then given answer on
     the line right after.
     EX: 1. What happens when a cat jumps? (Questions)
         It lands on it's feet (Answer)
-- It is recommended to number the questions in your set and not the answer.
-- Save this under a proper name and then make a copy of it
     (You should only use the copy in the program).
2. To upload set hit the "Enter Set" button or just type your text into the
     white box on the set entry window
 -- After hitting "Enter Set" browse through your folders to find the copy
      of the text file you saved
 -- Hit open. The text from the file should display in teh text entry box.
 3. Make any necessary edits
  -- Make sure your answers and questions are properly notated
  -- Add any questions you forgot
 4. Enter the number of questions you are studying into the text entry
     box next to the "How many questions?" label
 -- You must have at least three questions and no more than 50.
 -- The number you enter should line up with the text file you uploaded.
 5. Once you are finished editing hit the "Save file" button.
 -- Search the browser again and reopen the copy of the text file from
       before to save and edits and finalize your questions.''', bg="white",
              fg = "black", font="Times").pack()
    # end creation_instruct function
        
    #Function to lift the setNUm, stud set creaton window above the main
    def lift_window():
        #Lift window
        setNUM.lift()
        #Assign how to lift
        setNUM.after(1000, lift_window)
    # end lift_window function
        
    #Create and displau studyset creation window
    setNUM = Tk()
    lift_window()
    setNUM.title("Study Set")
    setNUM.geometry('670x600+700+50')
    setNUM.configure(background="white")
    Label(setNUM, text="ENTER YOUR STUDY SET", bg="white", fg = "black", font="Times").pack()
    Label(setNUM, text="Before you begin anything you must enter the number of questions you want to study",
          bg="white", fg = "black", font="Times").pack()
    Label(setNUM, text="Enter the number in the text box below (Must be less than 50).",
      bg="white", fg = "black", font="Times").pack()
    
    #Create and display a text entry box to collect the file with answers and quesitons from the user
    collect_Questions = Text(setNUM, width = 60, height = 10, font=("Helvetica", 16))
    collect_Questions.pack(pady=20)
    
    #Button to open users text file that holds their questions
    open_button = tk.Button(setNUM, text="Enter Set", padx = 40, pady = 6,
                     fg = "black", bg = "white", command = open_text)
    open_button.pack(pady=20)
    
    #Button to save edits made to text file and finalize questions
    save_button = tk.Button(setNUM, text="Save File", padx = 40, pady = 6,
                        fg = "black", bg = "white", command = save_text)
    save_button.pack(pady=20)
    
    #Button that reopens the study set isntructions for the user
    instruct_button = tk.Button(setNUM, text="Help", padx = 40, pady = 6,
                                fg = "black", bg = "white", command = creation_instruct)
    instruct_button.pack(pady=20)
    
    #Ask user for the amount of questions they are entering
    Label(setNUM, text="How many questions?.",
      bg="white", fg = "black", font="Times").place(x= 200, y = 80)
   
   #Create and display a text entry box to collect num_Questions from the user
    num_questions = tk.Entry(setNUM) 
    num_questions.place(x=400, y = 80)
    
    #if intro is 0 show user the instructions 
    if intro == 0:
        #Make intro 1 to make sure instructions are no longer automatically displayed
        intro = 1
        #Call instruction function
        creation_instruct()
    tk.Frame(setNUM, bg="white")
# end addSet function

#Button function that reset the learning program values and then restarts it
def reset_learning_program():
    #Call the global functions that are being edited
    global mastery_count 
    global focus_count 
    global open_questions
    global loop_count
    global total_mastery_count
    global total_focus_count

    #Set total mastery count index variable
    loop = 0
    #Loop until mastercount is added into saved total mastery count
    for idx in mastery_count:
        #Add indexed mastery count to current total mastery count index
        total_mastery_count[loop] += idx
        #Add one to mastery count index variable
        loop += 1

    #Set total focus count index variable
    loop = 0
    #Loop until focuscount is added into saved total focus count
    for idx in focus_count:
        #Add indexed focus count to current total focus count index
        total_focus_count[loop] += idx
        #Add one to focus count index variable
        loop += 1
        
    #reset the global variables for the learn program function
    mastery_count = [0] * len(answers)
    focus_count = [0] * len(answers)
    open_questions = []
    loop_count = 1
    #Call learn program function
    learn_program_function()
# end reset_learning_program function

#Button Funciton to display the summary analysis from the learning program
def main_menu_summary():
    #Call the global varaible being altered
    global mastery_count 
    global focus_count 
    global total_mastery_count
    global total_focus_count
    
    #Set total mastery count index variable
    loop = 0
    #Loop until mastercount is added into saved total mastery count
    for idx in mastery_count:
        #Add indexed mastery count to current total mastery count index
        total_mastery_count[loop] += idx
        #Add one to mastery count index variable
        loop += 1

    #Set total focus count index variable
    loop = 0
    #Loop until focuscount is added into saved total focus count
    for idx in focus_count:
        #Add indexed focus count to current total focus count index
        total_focus_count[loop] += idx
        #Add one to focus count index variable
        loop += 1
    
    #Call main function with learning_complete set to 1
    main(learning_complete = 1)
# end main_menu_summary function

#Function used to renter the learn_program_function for the next question
def next_question_function():
    learn_program_function()
    

#Button function that takes user through the learning program
def learn_program_function():
    #Call global variable to be edited
    global loop_count
    
    #Button function the starts the learning program
    def start_game():
        #Call the global variable that are to be edited
        global mastery_count 
        global focus_count 
        global open_questions
        global loop_count

        #Disable the start/next question button
        start_button.config(state="disabled")

        #Button function that is entered when user chooses the correct answer
        def user_correct():
            #add one to the index of the question they got right
            mastery_count[random_idx] += 1
            #Destroy last learnProgram window 
            learnProgram.destroy()
            #Call next_question_function to move onto the next question
            next_question_function()
        # end user_correct function
        
        #Button function that is entered when user chooses the wrong answer
        def user_wrong():
            #add one to the index of the question they got wrong
            focus_count[random_idx] += 1
            #Destroy last learnProgram window 
            learnProgram.destroy()
            #Call next_question_function to move onto the next question
            next_question_function()
        # end user_wrong function
        
        #Button Function that checks if the open ended user entry was correct
        def check_open_ended():
            #Set variables for the function
            letters_wrong = 0
            loop = 0
            computer_answer = answers[random_idx]
            #Set varible that gets value from open ended user entry
            user_answer = open_ended_userResponse.get()
            
            #If the length of the user response is equal to the correct computer answer, check if answer is right
            if len(user_answer) == len(computer_answer):
                #Loop until each letter of the correct answer has been looped
                for current_letter in computer_answer:
                    #If the current letter in the correct answer does not equal the letter in the user reponse, letter wrong
                    if current_letter != (user_answer[loop]):
                        #Add to save another letter wrong
                        letters_wrong += 1
                    loop += 1
            #Else, userresponse is automatically wrong
            else:
                #Set letter_wrong to value identifying that user is wrong
                letters_wrong = 3
            #If the number of letters wrong from user response is less than 2 they are right
            if letters_wrong <= 2:
                #Call the function to save that user was right
                user_correct()
            #Else, wrong letter count exceeds 2 and user is wrong
            else:
                #Call function to save that use is wrong
                user_wrong()
        
        #Loop until a question has been created or user has completed the learning program
        while True:
            #Collect a random index numbers in range of the length of questions
            random_idx = random.randint(0,len(questions)-1)
            
            #If the value at the random index has not been mastered 3 times and open questions list does not equal questions list, user is still in multiple choice
            if (mastery_count[random_idx] != 3 and open_questions != questions):#fix

                #Assign the question to be asked used the random index
                next_question = questions[random_idx]
                #Assign the matching correct answer using random index
                correct_answer = answers[random_idx]
                
                #Make a new list copy from the answers list
                answer_set = answers.copy()
                #Remove the correct answer from the copy list
                answer_set.remove(correct_answer)
                #Randomly select a wrong answer from the copy list
                false_answer1 = random.choice(answer_set)
                #Remove that wrong answer from the copy list
                answer_set.remove(false_answer1)
                #Assign the secong wrong answer from the copy list
                false_answer2 = random.choice(answer_set)
                
                #Save the chosen asnwers to display into a list that the user will choose from 
                user_choices = [correct_answer, false_answer1, false_answer2]
                
                #Break the loop
                break
            #Else, if the value at the random index is less than 4 and the open questions list equals the questions list, the user gets an open_ended question
            elif mastery_count[random_idx] < 4 and open_questions == questions:
                #Assign the next question using the random index
                next_question = questions[random_idx]
                #Assign the matching correct answer with the random index
                correct_answer = answers[random_idx]
                #Break the loop
                break
            
            #Else, either the user has mastered a qestion 3 times or they have mastered it 4 times and went through open_ended quesitons
            else: 
                #IF questions has been mastered the quesiton at the random index 3 times and they have not entered open_ended, and the question is not yest in open_ended question list, continue
                if mastery_count[random_idx] == 3 and open_questions != questions and ((questions[random_idx]) not in open_questions):
                    #Add the newly mastered question from random index to the open_questions list
                    open_questions.append(questions[random_idx])
        
                    #If the length of the open_question list is the same as teh questions list, then all questions have been mastered three times
                    if (len(open_questions)) == (len(questions)):
                        count = 0
                        #Loop until all mastery indexes have been determiend as masted/ greater than or qual to 3
                        for i in range(len(mastery_count)):
                            if mastery_count[i] >= 3:
                                count += 1
                        #If all indexes have been mastered to 3 then set open_ended questions
                        if count == 3:
                            #Make opened ended questions a copy of the questions list to create proper order
                            open_questions = questions.copy()
                #If the sum of the indexes in the mastery count is greates the the length of questions times 4 then the learning program has been completed.
                if sum(mastery_count) >= (len(questions)*4):
                    
                    #Display end of learningprogram completion window
                    end_learn_window = Tk()
                    end_learn_window.title("Completed")
                    end_learn_window.geometry('650x650+50+50')
                    end_learn_window.configure(background="white")
                    Label(end_learn_window, text="YOU DID IT!!!", bg="white",
                          fg = "black", font="Times").pack()
                    Label(end_learn_window, text='''Congratulations! You successfully completed the learning program.
Now you can either reset the program for better test results
or go back to the main menu for a more extensive Learning Summary.''', bg="white",
                          fg = "black", font="Times").pack()
                    Label(end_learn_window, text = "Learning Program Summary: ". format(sum(mastery_count)), bg="white",
                          fg = "black", font="Times").pack()
                    Label(end_learn_window, text = "Number of Questions: {}". format(loop_count-1), bg="white",
                          fg = "black", font="Times").pack()
                    Label(end_learn_window, text = "Total Correct: {}". format(sum(mastery_count)), bg="white",
                          fg = "black", font="Times").pack()
                    #Display the current amount of questions answered incorrectly 
                    Label(end_learn_window, text = "Total Incorrect: {}". format(sum(focus_count)), bg="white",
                      fg = "black", font="Times").pack()
                    
                    #Button for user to reset the learning program and start again, using reset_leearning_program function
                    reset_Button = tk.Button(end_learn_window, text = "Reset", padx = 40, pady = 6,
                                        fg = "black", bg = "white", command = reset_learning_program)
                    reset_Button.pack()
                    #Button for user to exit and enter the main menu summary using main_menu_summary function
                    mainMenu_Button = tk.Button(end_learn_window, text = "Return to Main", padx = 40, pady = 6,
                                        fg = "black", bg = "white", command = main_menu_summary)
                    mainMenu_Button.pack()
                    
                    #Distroy the learnProgram window
                    learnProgram.destroy()
                    
                    #Break the loop
                    break
            

        
        #Display the question number 
        Label(learnProgram, text = "Question {}". format(loop_count), bg="light blue",
          fg = "black", font="Times").pack()
        #Display the current amount of questions answered correctly
        Label(learnProgram, text = "Total Correct: {}". format(sum(mastery_count)), bg="light blue",
          fg = "black", font="Times").pack()
        #Display the current amount of questions answered incorrectly 
        Label(learnProgram, text = "Total Incorrect: {}". format(sum(focus_count)), bg="light blue",
          fg = "black", font="Times").pack()
        #Display the next question to be answered
        Label(learnProgram, text = "Answer the Question:", bg="light blue",
                                     fg = "black", font="Times").place(x = 350, y = 500)
        Label(learnProgram, text = "{}". format(next_question), bg="white",
                                     fg = "black", font="Times").place(x = 560, y = 500)
        
        
        #Variables to verify that there is a wrong choice and correct choice button
        correct_given = 0
        wrong_given = 0
        #if the user is not ready for open ended questions yet display multiple choice
        if open_questions != questions:
            place = 600 
            # shuffle the list of answers to be displayed
            random.shuffle(user_choices)
            
            # Now do a for loop and just loop over those three answers
            for i in range(3):
                if user_choices[i] == correct_answer:
                    #Make and display button with the correct answer command
                    clicker = tk.Button(learnProgram, text = user_choices[i], padx = 40, pady = 6,
                              fg = "black", bg = "white", command = user_correct)
                    clicker.place(x = 700, y = place)
                    #Mark that a correct answer button has been made

                else:
                    #Make and display button with wrong answer command
                    clicker = tk.Button(learnProgram, text = user_choices[i], padx = 40, pady = 6,
                                        fg = "black", bg = "white", command = user_wrong)
                    clicker.place( x = 700, y = place)
                    #Mark that an incorrect answer button has been made

                # update places
                place += 100
                    
                    
        #Else, the user is ready for open ended questions
        else:
            #Dsiplay the instruction
            Label(learnProgram, text="Type the answer into the entry box. Then hit submit.", bg="light blue",
                  fg = "black", font="Times").pack()
            #Make entry box for user answer to the questions
            open_ended_userResponse = tk.Entry(learnProgram) 
            open_ended_userResponse.place(x=600, y = 850, width = 80, height = 15)
            
            #Make button for user to enter there response to be checked 
            enter_UserResponse = tk.Button(learnProgram, text = "Enter", padx = 40, pady = 6,
                                            fg = "black", bg = "white", command = check_open_ended)
            enter_UserResponse.place( x = 800, y = 850)
            

        #Add to the number question that the user is on
        loop_count += 1
    # end of Start_game function
    
    #Function to tell the user how to work the learn program 
    def creation_instruct():
        #Function to lif window to the front
        def lift_window():
            #Lift the information window
            info.lift()
            info.after(1000, lift_window)
        # end of lift window function
        
        #Make and display info window to show learning program isntrucitons
        info = Tk()
        info.title("Instructions")
        info.geometry('600x400+50+50')
        info.configure(background="white")
        Label(info, text="HOW TO USE THE LEARNING PROGRAM", bg="white",
              fg = "black", font="Times").pack()
        Label(info, text=''' This learning program will repeat the question set to you mutliple
times, until it is mastered.The program will begin with mutliple choice
questions: select the correct choice out of three options, then hit
next question after your results are recorded.You will move onto
open ended questions: These questions require you to type out the
matching answer to the question exactly, with 3 letter typo leniancy.
You can end the learning program any time by hitting done in the corner.
Although, it is recommended that you completely finish it. ''', bg="white",
              fg = "black", font="Times").pack()
        lift_window()
    # end of creation_instruct function
    
    #Make and display learnProgram window
    learnProgram = Tk()
    learnProgram.title("Learn")
    learnProgram.geometry('600x400+50+50')
    learnProgram.configure(background="light blue")
    learnProgram.attributes('-fullscreen', True)
    Label(learnProgram, text="Answer the question", bg="light blue",
          fg = "black", font="Times").pack()
    Label(learnProgram, text="Make sure that you have read the instructions before you begin", bg="light blue",
          fg = "black", font="Times").pack()
    
    #Button for the instruciton window and calls creation_instruct
    instruct_button = tk.Button(learnProgram, text="Help", padx = 40, pady = 6,
                                fg = "black", bg = "white", command = creation_instruct)
    instruct_button.place( x = 1000, y = 10)
    
    #If the loop is being entered for the first time 
    if loop_count == 1:
        #Call function to display the instruction window
        creation_instruct()
    
    #If the learning program is being entered after the first time
    if loop_count > 1:
        #Make button to get the next_quesiton using the start_game command
        start_button = tk.Button(learnProgram, text="Next Question", padx = 40, pady = 6,
                                fg = "black", bg = "white", command = start_game)
        start_button.place( x = 1000, y = 850)
    #Else, the program is being entered for the first time
    else:
        #Make button to start the game using the start_game command
        start_button = tk.Button(learnProgram, text="Start", padx = 40, pady = 6,
                                fg = "black", bg = "white", command = start_game)
        start_button.place( x = 1000, y = 850)
        
    frame = tk.Frame(learnProgram, bg="white")
# end learn_program_funciton
   
#Create and display the main window    
mainWindow = Tk()
mainWindow.title("Cram Sesh")
mainWindow.configure(background="#0464A2")
#Make window full screen 
mainWindow.attributes('-fullscreen', True)
Label(mainWindow, text="WELCOME TO CRAM SESH", bg="#0464a2", fg = "white", font="Times").pack()
Label(mainWindow, text="Time to get ready for that test!", bg="#0464a2", fg = "white", font="Times").pack()
Label(mainWindow, text="Click the button to begin entering the information you wish to be tested on.",
      bg="#0464a2", fg = "white", font="Times").pack()

#Study set creation button. Once clicked will lead to create set function.
setCreate = tk.Button(mainWindow, text="Create your study set", padx = 40, pady = 6,
                     fg = "black", bg = "white", command = addSet)
setCreate.pack()
#Make exit button to end program
appExit = tk.Button(mainWindow, text="X", padx = 20, pady = 2,
                     fg = "white", bg = "red", command = end_program_function)
appExit.place(x=1350, y = 10)


#Fucniton holds the main window, where the program begins and ends
def main(learning_complete = 0):
    #Call global variables 
    global mastery_count 
    global focus_count
    global total_mastery_count 
    global total_focus_count 
        
    #If the question sets have been entered
    if questions != [] and answers != []:
        
        #If the learning_complete = 1 then they have finished the learning program
        if learning_complete == 1:
            #Disable the create set button
            setCreate.config(state="disabled")
            
            #Make the correct and incorrect answers be displayed next to the question and answer set
            listbox = Listbox(mainWindow, width=100, height=15)
            listbox.insert(1, "Results:")
            #Loop until all of the correct and incorect numbers for each quesiton hae been displayed
            for i in range (len(questions)):
                listbox.insert(i+1,"Correct: " + str(total_mastery_count[i]) + "   Incorrect: " + str(total_focus_count[i]))
            #Place orrect and incorrect list
            listbox.place(x = 700, y = 200)
            
            #MAke a new lsitbox to display the questions that the user should focus on before the test
            focus_listbox = Listbox(mainWindow, width = 50, height = 15)
            focus_listbox.insert(1, "Questions to focus on:")
            
            #Loop until all of the questions to focus on have been displayed
            for i in range (len(questions)-1):
                #If the idex in total focus list at the iteration number is 15 percent or more of the total questions wrong list add that question to set
                if total_focus_count[i] / (sum(total_focus_count)) >= 0.15:
                    focus_listbox.insert(i+1, str(questions[i]))
                    
            #Place foucs queations list
            focus_listbox.place(x = 800, y = 200)
            
            #create diagnostic Display for potential grade
            #If total_mastery_count is 50% or more of total questions display that projected grade is C- or lower, suggest studying more
            if sum(total_mastery_count) / ((sum(total_focus_count)) + (sum(total_mastery_count))) <= 0.5:
                Label(mainWindow, text="C-: F", bg="white", fg = "red", font="Verdana 32 bold").place(x=10, y = 10)
                Label(mainWindow, text='''You have achieved 50% or less correct answers
out of the total questions.
It is suggested that you study more before your test.''', bg="white", fg = "black", font="times").place(x=10, y = 70)
            #Else, if total_mastery_count is between 25% and 50% of total questions display that projected grade is C to B-,
            #at a good spot but study more if want A
            elif sum(total_mastery_count) / ((sum(total_focus_count)) + (sum(total_mastery_count))) > 0.5 and sum(total_mastery_count) / ((sum(total_focus_count)) + (sum(total_mastery_count))) <= 0.75:
                Label(mainWindow, text="B-: C", bg="white", fg = "orange", font="Verdana 32 bold").place(x=10, y = 10)
                Label(mainWindow, text='''You have achieved 75% or less correct answers
out of the total questions, but more than 50%.
It is suggested that you study more before your test.''', bg="white", fg = "black", font="times").place(x=10, y = 70)
            #If total_mastery_count is between 25% and 5% of total questions display that projected grade is B to A, They should be ready
            elif sum(total_mastery_count) / ((sum(total_focus_count)) + (sum(total_mastery_count))) > 0.75 and sum(total_mastery_count) / ((sum(total_focus_count)) + (sum(total_mastery_count))) <= 0.95:
                Label(mainWindow, text="A : B", bg="white", fg = "dark yellow", font="Verdana 32 bold").place(x=10, y = 10)
                Label(mainWindow, text='''You have achieved 95% or less correct answers
out of the total questions, but more than 75%.
You'll do great on the test.''', bg="white", fg = "black", font="times").place(x=10, y = 70)
            #Else total_mastery_count is between 4% or lower they should Ace the test
            else:
                Label(mainWindow, text="A", bg="white", fg = "green", font="Verdana 32 bold").place(x=10, y = 10)
                Label(mainWindow, text='''You have achieved 94% or more correct answers
out of the total questions.
You should ace that test!''', bg="white", fg = "black", font="times").place(x=10, y = 70)
        #Else, the learning program has not yet been entered
        else:
            #Make button to allow user to enter the learning program using rest_learning_program function
            learnProgram = tk.Button(mainWindow, text="Learn Set", padx = 40, pady = 6,
                             fg = "black", bg = "white", command = reset_learning_program)
            learnProgram.pack()
            
            #Set total count global varable values to match the length of the answers list
            total_mastery_count = [0] * (len(answers))
            total_focus_count = [0] * (len(answers))
            
            #Display list box for question and answers
            listbox = Listbox(mainWindow, width=100, height=50)
            listbox.insert(1, "Question and Answer list:")
            #Loop until all of the questions and answers have been displayed
            for i in range (len(questions)):
                listbox.insert(i+1,"{}.".format(i+1) + questions[i] + "---" + answers[i] )
            
            listbox.place(x = 20, y = 200)

        frame = tk.Frame(mainWindow, bg="white")
      

    #Call and display main window
    frame = tk.Frame(mainWindow, bg="white")
    frame.pack()
    
    mainWindow.mainloop()
# end of main function    
   
#Call main function
main()



