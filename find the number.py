import matplotlib.pyplot as plt
def search(ceiling, n):
    floor = 0
    guess = round(0.5 * ceiling)
    tries = 1
    while guess != n:
        if guess < n:
            floor = guess
            #print(f"the guess was {guess} and was lower than expected. ")
            guess = round(0.5 * (floor + ceiling))
            tries += 1
        else:
            ceiling = guess
            #print(f"the guess was {guess} and was higher than expected. ")
            guess = guess = round(0.5 * (floor + ceiling))
            tries += 1
    return(tries)
arr = []
#trying to find the average-case scenario for my algorithm.
iteration_coordinates = [0]
min_coordinates = [0]
average_coordinates = [0]
max_coordinates = [0]
k = 300
for a in range(1 ,k):
    for i in range(1,a):
        arr.append(search(a, i))
        iteration_coordinates.append(a)
        min_coordinates.append(min(arr))
        average_coordinates.append(sum(arr) / len(arr))
        max_coordinates.append(max(arr))
    #coordinates.append([a, min(arr), max(arr), sum(arr) / len(arr)])
#print(iteration_coordinates)
#print(min_coordinates)
#print(average_coordinates)
#print(max_coordinates)
plt.plot(average_coordinates, max_coordinates)

# naming the x axis
plt.xlabel('Iterations')
# naming the y axis
plt.ylabel('Average tries')

# giving a title to my graph
plt.title('My first graph!')

# function to show the plot
plt.show()

#print(f"The average-case scenario is: {sum(arr) / len(arr)}.")
#print(f"The best-case scenario is: {min(arr)}.")
#print(f"The worst-case scenario is: {max(arr)}.")
