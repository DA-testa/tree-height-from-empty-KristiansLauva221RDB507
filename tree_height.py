import sys
import threading

def compute_height(n, parents):
    # create a list to store the children of each node
    children = [[] for _ in range(n)]

    # find the root node
    root = -1
    for i in range(n):
        if parents[i] == -1:
            root = i
        else:
            children[parents[i]].append(i)

    # recursive function to find the height of each subtree
    def find_height(node):
        heights = [0]
        for child in children[node]:
            heights.append(find_height(child))
        return max(heights) + 1

    # compute the height of the whole tree
    return find_height(root)


def main():
    input_type = input("")
    if input_type == "I":
        # read input from user
        n = int(input())
        parents = list(map(int, input().split()))
    elif input_type == "F":
        # read input from file
        filename = input("Enter filename: ")
        with open(filename) as f:
            n = int(f.readline())
            parents = list(map(int, f.readline().split()))
    else:
        print("Invalid input type")
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
