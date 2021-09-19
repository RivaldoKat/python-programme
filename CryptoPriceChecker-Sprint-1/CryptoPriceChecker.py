class PriceChecker():
    # Constructor 
    def __init__(self):
        self.levelsList = []
    
    # Properties 
    # A property is defined like a method, but you use it in your 
    # code like a variable (no parentheses need to followed it when used in your code)
    # Refer: https://www.youtube.com/watch?v=jCzT9XFZ5bw
    # Refer BP411 slides: Week 2 - Chapter 10 - Slides about Encapsulation and properties 
    @property
    def levelsList(self):
        return self.__levelsList
    @levelsList.setter
    def levelsList(self, newValue):
        self.__levelsList = newValue    

    # Class Methods
    # =============

    # Method: Sort and Display the levelsList
    def displayList(self):
        print(chr(27) + "[2J") # Clear the screen
        print("Price Levels In The List")
        print("========================")
        # Sort the list in reverse order
        list = self.levelsList
        list.reverse()
        # Print the items in the list (Based on the above sort, numbers should appear from large to small.)
        for price in self.levelsList:
            print(f"${price}")

    # Display the menu and get user input about what methods to execute next
    def displayMenu(self):
        min = 0
        max = 3
        errorMsg = "Please enter a valid option between " + str(min) + " and " + str(max)

        print("MENU OPTIONS")
        print("============")
        print("1. Add a price level")
        print("2. Remove a price level")
        print("3. Remove all price levels")
        print("0. Exit the program")
        print(" ")   
        
        # Get user input. Keep on requesting input until the user enters a valid number between min and max 
        selection = 99
        while selection < min or selection > max:
            try:
                selection = int(input("Please enter one of the options: "))
            except:
                print(errorMsg) # user did not enter a number
                continue # skip the following if statement
            if(selection < min or selection > max):
                print(errorMsg) # user entered a number outside the required range
        return selection # When this return is finally reached, selection will have a value between (and including) min and max

    # Method: Append a new price level to the levelsList
    def addLevel(self):
        try:
            # Let the user enter a new float value and append it to the list
            newPriceLevel = float(input("Enter a new price level:"))
            if newPriceLevel <= 0:
                print("Incorrect value")
                self.addLevel()                
            else:
                self.levelsList.append(newPriceLevel)
        except:
            # Print and error message if the user entered invalid input
            print("Incorrect Value")
            self.addLevel()

    # Method: Remove an existing price level from the levelsList
    def removeLevel(self):
        try:
            # Let the user enter a new float value. If found in the list, remove it from the list
            newPriceLevel = float(input("Remove price level:"))

            if newPriceLevel in checkerObj.levelsList:
                self.levelsList.remove(newPriceLevel)
            else:
                 print("The price is not in list")
                 self.removeLevel()                
        except:
            # Print and error message if the user entered invalid input
             print("Enter a correct value")
             self.removeLevel()                

    # Method: Set levelsList to an empty list
    def removeAllLevels(self):
        # Set levelsList to an empty list
        self.levelsList.clear()

    # Method: Load levelsList using the data in levelsFile
    def readLevelsFromFile(self):
        try:
            # Set levelsList to an empty list
            self.levelsList.clear()

            # Open the file
            fromFile = open('levelsFile.txt', 'r')

            # Use a loop to read through the file line by line
            for line in fromFile:
                f_contents = fromFile.readline()
                # If the last two characters in the line is "\n", remove them
                print(end='')
                # Append the line to levelsList
                self.levelsList.append(line)
                
            # Close the file
            fromFile.close()
        except:
            return
         
    # Method: Write levelsList to levelsFile (override the existing file)
    def writeLevelIsToFile(self):
        # Open the file in a way that will override the existing file(if it already exists)
        f = open('levelsFile.txt', 'r')

        # Use a loop to iterate over levelsList item by item
        for levelList in self.levelsList:
            # Convert everything in the item to a string and then add \n to it - before writing it to the file
            f_content = f.readline()
            print(f_content + "\n")
        # Close the file
        f.close()

# *************************************************************************************************
#                                           Main Code Section
# *************************************************************************************************

# Create an object based on the PriceChecker class
checkerObj = PriceChecker()

# Load levelsList from the records in levelsFile
checkerObj.readLevelsFromFile()

# Display the levelsList and Menu; and then get user input for what actions to take
userInput = 99
while userInput != 0:
    checkerObj.displayList()
    userInput = checkerObj.displayMenu()
    if(userInput == 1):
        checkerObj.addLevel()
        checkerObj.writeLevelIsToFile() # Write levelIsList to LevelsFile
    elif(userInput == 2):
        checkerObj.removeLevel()
        checkerObj.writeLevelIsToFile()  # Write levelIsList to LevelsFile
    elif(userInput == 3):
        checkerObj.removeAllLevels()
        checkerObj.writeLevelIsToFile()  # Write levelIsList to LevelsFile
