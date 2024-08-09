# Fitness Tracker
#### Video Demo: https://youtu.be/h5231pvnf6I
#### Description:
With this program, users are able to effectively track weightlifting progression in the exercises that you perform in the gym. This program allows users to add a weightlifting exercise you want and then input the amount of weight that was lifted, the number of sets performed, and the highest amount of reps that was achieved out of the sets performed. Since reading a CSV file can get tedious due to the columns not being aligned, this project also allows users to view your history of data of an exercise in a clean and formatted table. So if you would want to see if you are progressing in an exercise, reading the numbers would be incredibly easy.



### project.py:
This is the main script of the Fitness Tracker. It handles user interactions and brings together all its different features.

There are multiple functions in the file and they will be described below:

**main()**: It acts as the primary user interface for the application, allowing the user to choose one of the three options: New exericse, update existing exercise, view history.

**get_exercise_info()**: Gathers the weight, sets, and repititions of a particular exercise from the user.

**create_new_csv()**: Creates a new CSV file for a new exercise with the information gathered from the user.

**update_exercise()**: Updates an existing exercise's data with new inputted data from the user.

**check_format()**: Validates and formats the exercise data.

**make_table()**: Generates an easier and more readable table view of the exercise history.

### test_project.py:
This file contains unit tests for the 'project.py' script. It ensures that the functions work as intended.

The tests are described below:

**test_get_exercise_info()**: Tests if exercise information is correctly captured from the user.

**test_make_table()**: Checks the functionality of the history table generation.

**test_check_format()**: Verifies that the data inputted from the user is properly checked and catches incorrectly inputted information.



### External Libraries Used

**csv**: Handles csv operations.

**re**: Handles regular expressions.

**datetime**: For managing dates

**os**: For file path operations

**tabulate**: For formatting data into a table


### Design Choices

A major design choice I was conflicted on was deciding whether to allow the user to add repititions to each of the sets or to allow the user to just add the highest number of reps completed from all the sets. I believe that when tracking an exercise, if the weight stays the same but the highest number of reps completed increases, there is progression. Obsessing over the fact that you did one less repitition in the last set is nonsense if you increased the amount of reps completed in the first set.

I initially wrote the functions in 'python.py' to jump from one function to another. That made it quite difficult to write unit tests for the functions. So I changed the functions to return what was produced to 'main()' and let 'main()' transfer variables to other functions.

Nearing the end of my project, I decided to write the script to make it as user-friendly as possible. For example, when typing the exercise name, the user does not have to worry about capitalization or spaces. I wrote a few more lines of code to take care of it automatically.