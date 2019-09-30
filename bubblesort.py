import os

colors = {
    "yellow": "\033[1;33;33m",
    "green": "\033[1;32;32m",
    "red": "\033[1;31;31m",
    "blue": "\033[1;34;34m"
}

endl = "\n"

latestSortings = []

# Function to recieve a colored string
def color(color:str, string:str):
    return colors[color] + string + "\033[0m"
#

# cls for windows, clear for linux etc
clearCommand = "cls" if os.sys.platform.__contains__("win") else "clear"

# Clears console
def clear():
    os.system(clearCommand)
#

# (comparison operator)
compOp = None

def comparison(c1:float, c2:float):
    if (compOp == ">"):
        return c1 > c2
    else:
        return c1 < c2
    #
#

def outputList(l:list):
    print("*", end = " ")
    for i in range(0, len(l)):
        if (i != len(l) - 1):
            print(l[i], end = ", ")
        else:
            print(l[i])
        #
    #
#

def bubbleSort(l:list):
    for i in range(0, len(l)):
        for j in range(0, len(l) - i - 1):
            check = comparison(l[j], l[j+1])
            if (check):
                l[j], l[j+1] = l[j+1], l[j]
            #
        #
    return l
#

def almostDone(l:list):
    clear()

    print(color("blue", "Select sorting option:"))
    print("1. Ascending (Low to High)")
    print("2. Descending (High to Low)")
    operator = input("> ")

    # We want to use the global compOp variable.
    # Not make a new local variable
    global compOp
    compOp = ">" if operator == "1" else "<"

    print(color("green", f"{endl}Result:{endl}"))
    sorting = bubbleSort(l)
    outputList(sorting)
    latestSortings.append(sorting)
    input(f'{endl}{color("yellow", "Press")} ENTER {color("yellow", "to restart.")}')
    main()
#

def main():
    clear()
    print(color("yellow", f"Bubble sort Algorithm {endl}"))
    if (len(latestSortings) > 0):
        print(f"{color('yellow', 'Latest sortings:')} Old to Newest")
        for i in range(len(latestSortings)):
            outputList(latestSortings[i])
        print(endl)
    #

    print(f"Please enter all numbers, {color('red', 'Done')} to stop the inputs.")
    answer = None
    unsortedList = []
    while (True):
        answer = input("> ").lower()
        if (answer == "done"):
            break
        try:
            answer = float(answer)
            if (answer.is_integer()):
                answer = int(answer)
            print(color("green", f"Added {answer}"))
            unsortedList.append(answer)
        except:
            print(color("red", f"ERROR: {answer} not an number. Try again."))
        #
    almostDone(unsortedList)
#

main()
