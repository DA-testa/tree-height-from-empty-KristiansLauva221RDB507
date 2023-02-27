import sys
import threading
import numpy as np

def compute_height(n, parents):
    # create a NumPy array to store the children of each node
    children = np.empty((n,), dtype=np.ndarray)

    # find the root node
    root = -1
    for i in range(n):
        if parents[i] == -1:
            root = i
        else:
            if children[parents[i]] is None:
                children[parents[i]] = np.empty((0,), dtype=int)
            children[parents[i]] = np.append(children[parents[i]], i)

    # recursive function to find the height of each subtree
    def find_height(node):
        if children[node] is None:
            return 1
        else:
            heights = np.array([find_height(child) for child in children[node]])
            return np.max(heights) + 1

    # compute the height of the whole tree
    return find_height(root)


def main():
    # read input from stdin or file
    mode = input("Enter I for input from user or F for input from file: ")
    if mode == 'I':
        n = int(input("Enter the number of nodes: "))
        parents = list(map(int, input("Enter the parents of nodes: ").split()))
    elif mode == 'F':
        filename = input("Enter the file name: ")
        with open(filename, 'r') as f:
            n = int(f.readline().strip())
            parents = list(map(int, f.readline().strip().split()))
    else:
        print("Invalid input mode.")
        return

    # compute the height of the tree
    height = compute_height(n, parents)

    # print the result
    print(height)


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
