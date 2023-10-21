import matplotlib.pyplot as plt                 #for plotting simple graphs
import random                                   #generate random number
import time                                     #to track time
import numpy as np                              #python library for handling np numbers
from binarysearchtree import BinarySearchTree   #our binarysearchtree.py
from linkedlist import LinkedList               #our linkedlist.py
from scipy.optimize import curve_fit            #to find c and b constant (you can use any other method)

# 3.3.2 Function to generate a random tree of size n
def random_tree(n):
    trees = BinarySearchTree()
    for i in range(n):
        value = random.randint(1, 1000)
        trees.insert(value)
    return trees

# 3.3.3 Create a list of equally spaced numbers from 5 to 100 with a step size of 5
X = list(range(5, 101, 5))

# Constants for tree size and number of trees
TREE_SIZE = 1000
NUMBER_OF_TREES = 1000

# List to store average search times
Y = []
Y4 = []

# 3.3.4 Iterate over different tree sizes
for s in X:
    total_time = 0

    # 3.4.4 Generate 1000 random trees of size s and search for the value 42
    for i in range(NUMBER_OF_TREES):
        tree = random_tree(s)
        start_time = time.time()
        tree.search(42)
        end_time = time.time()
        total_time += (end_time - start_time)

    # Calculate the average search time and store it in Y
    average_time = total_time / NUMBER_OF_TREES
    #Actual Model (Y)
    Y.append(average_time)

    # 3.7 Generate Linkedlist with the values same with the trees, and search for the value 42
    for _ in range(NUMBER_OF_TREES):
        ll = LinkedList(limit=s)
        start_time = time.time()
        ll.search(42)
        end_time = time.time()
        total_time += (end_time - start_time)
    average_time = total_time / NUMBER_OF_TREES
    Y4.append(average_time)


# 3.4.3 Linear Model (Y2)
linear_model = lambda X, c, b: c * X + b
linear_params, _ = curve_fit(linear_model, X, Y)
c_linear, b_linear = linear_params
print("Linear Relationship Constants:")
print("c_linear =", c_linear)
print("b_linear =", b_linear)
# Create a list Y2 with estimates of average search time under an ideal linear relationship
Y2 = [c_linear * s + b_linear for s in X]



# 3.4.4 Logarithmic Model (Y3)
logarithmic_model = lambda X, c, b: c * np.log2(X) + b
logarithmic_params, _ = curve_fit(logarithmic_model, X, Y)
c_logarithmic, b_logarithmic = logarithmic_params
print("Logarithmic Relationship Constants:")
print("c_logarithmic =", c_logarithmic)
print("b_logarithmic =", b_logarithmic)
# Create a list Y3 with estimates of average search time under an ideal logarithmic relationship
Y3 = [c_logarithmic * np.log2(s) + b_logarithmic for s in X]

# Plot the three curves
# 3.4.5 3.4.1 3.7.1
plt.plot(X, Y)
plt.plot(X, Y2)
plt.plot(X, Y3)
plt.plot(X, Y4)



# Show the legend and plot (from Listing 13,14,15)
plt.legend(['BST', 'Linear', 'Logarithmic', 'Linkedlist'])
plt.xlabel('Size of trees/linkedlist')
plt.ylabel('Average search Time')
plt.title('Complexity Analysis: Binary Search Tree Search')
plt.ticklabel_format(axis='both', style='sci', scilimits=(0,0))
plt.show()


