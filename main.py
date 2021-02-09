def main():
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")

    direction = input('You are at a cross road. Where do you want to go? Type "left" or "right"\n').lower()
    if direction == "right":
        result = "You fell into a hole. Game Over."
    if direction == "left":
        lake_option = input(
            'You have come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. ' \
            'Type "swim" to swim across. \n').lower()
        if lake_option == "swim":
            result = "You get attacked by an angry trout. Game Over."
        if lake_option == "wait":
            color = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and '
                          'one blue. Which colour do you choose? \n').lower()
            color_mapping = {
                "red": "It's a room full of fire. Game Over.",
                "yellow": "You found the treasure! You Win!",
                "blue": "You enter a room of beasts. Game Over."
            }
            result = color_mapping.get(color, "No Rooms Found")
    print(result)


main()
