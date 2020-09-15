from random import randint

def user_input():

    once_or_many = input("Would you like to run once or multiple times? (1 for once and 2 for multiple): ")
    if once_or_many == "1":
        number_of_doors = int(input("Enter number of doors: "))

        door_list = list(range(1, number_of_doors + 1, 1))
        #print(door_list)

        winning_door = randint(1, number_of_doors)
        #print("Winning Door: ", winning_door)

        door_selection = int(input("Please select a door: "))

        if (door_selection > number_of_doors or door_selection < 1):
            print("Door selected is invalid")
            return

        filtered_doors = list(filter(lambda a: a == door_selection or a == winning_door, door_list))

        #print(filtered_doors)

        decision = input("Would you like to switch doors? (Type 'yes' or 'no'): ")

        if decision in ('yes', 'Yes', 'y', 'Y'):
            if len(filtered_doors) == 1:
                print("You Lose!")
                print("\n")
            else:
                print("You Win!")
                print("\n")
        else:
            if len(filtered_doors) == 1:
                print("You Win!")
                print("\n")
            else:
                print("You Lose!")
                print("\n")

    else:
        win_count = 0
        lose_count = 0
        number_of_iterations = int(input("How many iterations: "))

        number_of_doors = int(input("Enter number of doors: "))

        door_list = list(range(1, number_of_doors + 1, 1))
        #print(door_list)

        change_each_time = input("Switch door every time? (Enter 'yes' or 'no'): ")

        for i in range(number_of_iterations):
            winning_door = randint(1, number_of_doors)

            door_selection = randint(1, number_of_doors)

            filtered_doors = list(filter(lambda a: a == door_selection or a == winning_door, door_list))

            if change_each_time in ('yes', 'Yes', 'y', 'Y'):
                if len(filtered_doors) == 1:
                    lose_count += 1
                else:
                    win_count += 1
            else:
                if len(filtered_doors) == 1:
                    win_count += 1
                else:
                    lose_count += 1

        win_percentage = (win_count / number_of_iterations) * 100
        lose_percentage = (lose_count / number_of_iterations) * 100

        print("------------------------")
        print("Win Percentage", win_percentage)
        print("")
        print("Lose Percentage", lose_percentage)
        print("------------------------")
        print("\n")

    user_input()


if __name__ == '__main__':

    user_input()


