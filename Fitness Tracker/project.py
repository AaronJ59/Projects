import csv
import re
from datetime import date
import os
from tabulate import tabulate

def main():
    while True:
        decision = input("1: New exercise\n2: update existing exercise\n3: View history\nChoose a number: ")

        if decision.lower() in ("new exercise", "1"):
            new_exercise = input("What exercise would you like to add? ").lower()
            if " " in new_exercise:
                new_exercise = new_exercise.replace(" ", "_")
            new_ex_info = get_exercise_info(new_exercise)
            new_ex_info = check_format(new_ex_info)
            create_new_csv(new_ex_info)
            break



        elif decision.lower() in ("update existing exercise", "2"):
            existing_exercise = input("Which one: ").lower()
            if " " in existing_exercise:
                existing_exercise = existing_exercise.replace(" ", "_")
            existing_ex_info = get_exercise_info(existing_exercise)
            existing_ex_info = check_format(existing_ex_info)
            update_exercise(existing_ex_info)
            break



        elif decision.lower() in ("View history", "3"):
            while True:
                view_exercise_hist = input("Exercise: ")
                made_table = make_table(view_exercise_hist)
                print(made_table)
                if not made_table == "Exercise does not exist":
                    break
                break
            break

        else:
            print("Choose an option")





def get_exercise_info(exercise):
    filename = exercise
    filename = filename + ".csv"
    weight = input("How much did you lift in pounds? ")
    sets = input("How many sets? ")
    reps = input("Highest amount of reps performed: ")
    today = date.today()
    return weight, sets, reps, today, filename




def create_new_csv(information):
    weight, sets, reps, today, filename = information


    if not os.path.isfile(filename):
        with open(filename, 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            #Write headers
            csvwriter.writerow(["Weight(lb)", "Sets", "Reps", "Date"])
            csvwriter.writerow([weight, sets, reps, today])
    else:
        print("Exercise already exists. Update instead")
        return "Exercise already exists"




def update_exercise(existing_exercise):
    weight, sets, reps, today, filename = existing_exercise
    if os.path.isfile(filename):
        with open(filename, "a", newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow([weight, sets, reps, today])
    else:
        print("Exercise has not been added")
        return "Exercise has not been added"




def check_format(numbers):
    weight, sets, reps, today, filename = numbers
    while True:
        matches = re.search(r"[0-9]+", weight)
        if matches:
            weight = matches.group()
            break
        else:
            weight = input("Weight needs to be a number: ")

    while True:
        matches = re.search(r"[0-9]+", sets)
        if matches:
            sets = matches.group()
            break
        else:
            sets = input("Sets needs to be a number: ")

    while True:
        matches = re.search(r"[0-9]+", reps)
        if matches:
            reps = matches.group()
            break
        else:
            reps = input("Reps needs to be a number: ")


    return weight, sets, reps, today, filename

def make_table(exercise):
    if ".csv" not in exercise:
        exercise = exercise + ".csv"
    if os.path.isfile(exercise):
        rows = []
        headers=["Weight(lb)", "Sets", "Reps", "Date"]
        with open(exercise, "r") as csvfile:
            csvreader = csv.DictReader(csvfile)

            for row in csvreader:
                rows.append([row["Weight(lb)"], row["Sets"], row["Reps"], row["Date"]])

        return tabulate(rows, headers, tablefmt="grid")

    else:
        return "Exercise does not exist"






if __name__=="__main__":
    main()
