import matplotlib.pyplot as plt
def average_tries_unique_element(number):
    n = 0
    for i in range(1,number+1):
        n += number / i
    return n
number_of_element = []
number_of_avgtries = []
for i in range(1, 1001):
    number_of_element.append(i)
    number_of_avgtries.append(average_tries_unique_element(i))
print(number_of_element)
print(number_of_avgtries)


plt.plot(number_of_element, number_of_avgtries)
plt.xlabel('number of elements')
plt.ylabel('number of average tries')
plt.title('Probability distribution')
plt.show()
