import os
import time

def mainMenu(work_out_data):
  os.system('clear')
  print("Track your progress! buddyy🔥🔥")
  print("""
        1. Show Workout Menu
        2. Add Workout
        3. Delete Workout
        4. Show Workout Detail
        5. Exit 
""")
  
  userInput = int(input("Choose an option (1-5): "))
  if userInput == 1:
    showWorkout(work_out_data)
  elif userInput == 2:
    addWorkout(work_out_data)
  elif userInput == 3:
    deleteWorkout(work_out_data)
  elif userInput == 4:
    showDatailWO(work_out_data)
  elif userInput == 5:
    print("Thank you for using this tracking program! 🔥☠️")
  else:
    print("Invalid option. Please choose a valid option(1-5).")
    mainMenu(work_out_data)

def showWorkout(dataWO):
  os.system('clear')
  temp = dataWO["workouts"]
  for index, workOut in enumerate (temp):
    print(
      f"""
      ------------------------
      index     : {index}
      name      : {workOut["name"]}
      category  : {workOut["category"]}
      rep       : {workOut["reps"]}
      weight    : {workOut["weight"]} kg
      duration  : {workOut["duration"]} minutes
      -------------------------
      """
    )
  userInput = input("Would you like to return to the main menu? 1. Yes 2. No: ")
  if userInput == "1":
    mainMenu(dataWO)
  elif userInput == "2":
    print("Feel free to continue checking your workouts!🔥🔥🔥")
  else:
    print("Invalid input. Returning to the main menu by default.")
    time.sleep(2)
    mainMenu(dataWO)

def addWorkout(dataWorkOut):
  def category():
    print("Choose a category: 1. Strength, 2. Cardio, 3. Flexibility: ")
    userInput = int(input("Pilih kategori: "))
    if userInput == 1:
      return dataWorkOut["categories"][0]
    elif userInput == 2:
      return dataWorkOut["categories"][1]
    elif userInput == 3:
      return dataWorkOut["categories"][2]
    else:
      print("Invalid choice. Please try again.")
      category()

  temp = {
    "name": input("Enter the name of the workout: "),
    "category": category(),
    "reps": int(input("Enter the number of reps: ")),
    "weight": int(input("Enter the weight (in kg): ")),
    "duration": int(input("Enter the duration (in minutes): "))
  }
  os.system('clear')
  print("Your workout has been added, BUDDYY🔥🔥")
  dataWorkOut["workouts"].append(temp)
  userInput = input("Would you like to return to the main menu or add another workout? 1. Main Menu 2. Add Another Workout: ")
  if userInput == "1":
    mainMenu(dataWorkOut)
  if userInput == "2":
    addWorkout(dataWorkOut)
  else:
    print("Invalid choice. Returning to the main menu by default.")
    time.sleep(2)
    mainMenu(dataWorkOut)

def deleteWorkout(dataWO):
  os.system("clear")
  print("=== ☠️  Delete Workout Menu☠️  ===")
  temp = dataWO["workouts"]
  for index, workout in enumerate (temp):
    print(
      f"""
      ------------------------
      index         : {index}
      🏋️‍♀️  Name      : {workout["name"]}
      📂  Category  : {workout["category"]}
      🔢  Reps      : {workout["reps"]}
      🏋️‍♂️  Weight    : {workout["weight"]} kg
      ⏱️   Duration  : {workout["duration"]} minutes
      -------------------------
      """
    )
  userInput = int(input("\nEnter the index of the workout to delete: "))
  if 0<= userInput < len(temp):
    deleted_workout = dataWO["workouts"].pop(userInput)
    print(f"\n✅ Workout '{deleted_workout['name']}' has been successfully deleted.")
  else:
    print("\n❌ Invalid index. No workout was deleted.")
  userInput = input("Would you like to return to the main menu? 1. Yes 2. No: ")
  if userInput == "1":
    mainMenu(dataWO)
  elif userInput == "2":
    print("Thank you for using this tracking program! 🔥☠️")

def showDatailWO(dataWO):
  os.system("clear")
  print("=== Workout Detail Menu by Categories ===")
  temp = dataWO["workouts"]

  if not temp:
    print("\nNo workouts available. Please add some workouts first.")
    input("\nPress Enter to return to the main menu...")
    mainMenu(dataWO)
    return
  
  userInput = str(input("Type the category; Strength, Cardio, or Flexibility: ")).lower()
  if userInput == "strength" or userInput == "cardio" or userInput == "flexibility":
    for index, workOut in enumerate (temp):
      if workOut["category"].lower() == userInput :
        print(
          f"""
          ------------------------
          index     : {index}
          name      : {workOut["name"]}
          category  : {workOut["category"]}
          rep       : {workOut["reps"]}
          weight    : {workOut["weight"]} kg
          duration  : {workOut["duration"]} minutes
          -------------------------
          """
        )
    userInput = input("Would you like to return to the main menu? 1. Yes 2. No: ")
  else:
    print("The category does not exist")
    input("\nPress Enter to return to the Workout Detail Menu")
    showDatailWO(dataWO)

  if userInput == "1":
    mainMenu(dataWO)
  elif userInput == "2":
    print("Thank you for using this tracking program! 🔥☠️")
  else:
    print("\nInvalid choice. Returning to the main menu.")
    mainMenu(dataWO)

def main():
  categories = ["Strength", "Cardio", "Flexibility"]

  work_out_data = {
  "workouts": [
            {"name": "Bench Press", "category": categories[0], "reps": 15, "weight":50, "duration": 5},
            {"name": "Running", "category": categories[1], "reps": 0, "weight":0, "duration": 30},
            {"name": "Stretching", "category": categories[2], "reps":0 , "weight":0, "duration": 10},
        ],
  "categories": categories
}
  
  # work_out ={
  #   "name" : "Deadlift",
  #   "category": "Strength",
  #   "reps": 5,
  #   "weight": 300,
  #   "duration": 30
  # }
  # work_out_data["workouts"].append(work_out)
  mainMenu(work_out_data)
main()