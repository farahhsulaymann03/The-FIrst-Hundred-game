# This is the First Hundred game.
# In this game every player starts from 0 and alternatively add a number from 1 to 10 to the sum.
# The player who reaches 100 first wins.

# This function toggles the player each turn.
def toggle_player(player):
    if player == "one":
        new_player = "two"
    else:
        new_player = "one"

    return new_player

# This function checks that the numbers entered by the players are less than or equals to ten.
def increment_checker(increment):
    new_increment = increment

    while new_increment > 10:
        new_increment = int(input("Please, enter a number between 1 and 10 only: "))

    return new_increment

# This function updates the total after each turn.
def total_incrementer(total, new_increment):
    total = total + new_increment
    print("The current total is " + str(total))
    return total

# This is the main function of the game.
def first_hundred():
    total = 0
    player = "one"

    print("Welcome to the First Hundred game.\nIn this game every player starts from 0 "
          "and alternatively add a number from 1 to 10 to the sum.\nThe player who reaches 100 first wins.")

    while total < 100:
        increment = int(input("Player " + player + "'s turn: "))
        new_increment = increment_checker(increment)
        total = total_incrementer(total, new_increment)

        if total > 100 or total == 100:
            print("Player " + player + " wins!")
            print("Thanks for playing the First Hundred game, we hope you enjoyed it!")

        player = toggle_player(player)


first_hundred()
