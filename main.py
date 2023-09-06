def main():

   #Intialize List of books
    booklist = []

   # Initialize a variable for user choice
    choice = 0
    # Create a menu for the user using a while loop
    while choice != 5:
       print("** Andela Book Store **")
       print("1) Username")
       print("2) Passwords")
       print("3) Add your Favorite book")
       print("4) Book author")
       print("5)Quit")
       # Get user's choice as an integer input
       choice = int(input())
       if choice == 1:
           print("Entering your username")
           aBook = input()


    if __name__ == '__main__':
        main()