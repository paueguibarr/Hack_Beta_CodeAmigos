
# Take in value of n
print('Enter number of tosses to throw:')
n = input()

arr = [None] * int(n)

# Variables to store the wins
A_wins = 0
B_wins = 0
T_wins = 0


# Function to print the output
def printResult(arr, n):
    perm = []
    for i in range(0, n):
        perm.append(arr[i])
    calculateScore(perm)


def calculateScore(perm):
    global A_wins, B_wins, T_wins, A_score, B_score  # Declare global variables
    Alice = 0
    Bob = 0
    for i in range(len(perm) - 1):
        if perm[i] == 0 and perm[i + 1] == 0:
            Alice += 1
        if perm[i] == 0 and perm[i + 1] == 1:
            Bob += 1
    print('A - B score ', Alice - Bob)
    if Alice > Bob:
        A_wins += 1
    elif Bob > Alice:
        B_wins += 1
    else:
        T_wins += 1


# Function to generate all binary strings
def generateAllBinaryStrings(n, arr, i):
    if i == n:
        printResult(arr, n)
        return

    arr[i] = 0
    generateAllBinaryStrings(n, arr, i + 1)

    arr[i] = 1
    generateAllBinaryStrings(n, arr, i + 1)


# Call function
generateAllBinaryStrings(int(n), arr, 0)

print('A wins', A_wins)
print('B wins', B_wins)
print('T wins', T_wins)



