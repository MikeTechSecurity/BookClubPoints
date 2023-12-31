# The Book Club Points in Python
# https://github.com/MikeTechSecurity/BookClubPoints.git

def calculate_points(num_books):
    # This function determines the number of points awarded 
    # based on the number of books purchased.
    
    # Check the number of books and return corresponding points
    if num_books == 0:
        return 0
    elif num_books == 1:
        return 5
    elif num_books == 2:
        return 15
    elif num_books == 3:
        return 30
    elif num_books >= 4:
        return 60

def main():
    try:
        # Ask the user to input the number of books they've purchased
        # Convert the string input to an integer value
        num_books = int(input("Enter the number of books purchased this month: "))

        # Check if the entered number of books is negative
        if num_books < 0:
            print("Error: You entered a negative number of books. Please try again.")
            return  # Exit the function

        # Calculate the points awarded using the calculate_points function
        points = calculate_points(num_books)

        # Display to the user the number of points they've earned
        print(f"You have been awarded {points} points.")
    
    except ValueError:
        # Handle the error if user enters a non-integer value
        print("Error: Please enter a valid number.")

# The entry point of the program
# This checks if the script is being run directly (not imported)
# If so, it will call the main function to execute the program
if __name__ == "__main__":
    main()
