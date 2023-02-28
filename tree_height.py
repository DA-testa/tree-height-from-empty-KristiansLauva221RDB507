import sys
import threading


def compute_height(n, parents):
    # create a dictionary to store the children of each node
    children = {i: [] for i in range(n)}

    # find the root node and populate the children dictionary
    root = -1
    for i in range(n):
        if parents[i] == -1:
            root = i
        else:
            children[parents[i]].append(i)

    # iterative function to find the height of each subtree
    stack = [(root, 1)]
    max_height = 1
    while stack:
        node, height = stack.pop()
        max_height = max(max_height, height)
        for child in children[node]:
            stack.append((child, height + 1))

    # compute the height of the whole tree
    return max_height


def main():
    # read input from stdin or file
    mode = sys.stdin.readline().strip()
    if mode == 'F':
        filename = sys.stdin.readline().strip()
        if "a" not in filename:
            with open(filename, 'r') as f:
                n = int(f.readline().strip())
                parents = list(map(int, f.readline().strip().split()))
        else:
            print("error")
    elif "I" in mode:
        n = int(sys.stdin.readline().strip())
        parents = list(map(int, sys.stdin.readline().strip().split()))
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
