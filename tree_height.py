import sys
import threading
import numpy

def compute_height(n, parents):
    paren = numpy.zeros(n)
    def height(i):
        if paren[i] != 0:
            return paren[i]
        if parents[i] == -1:
            paren[i] == 1
        else:
            paren[i] = height(parents[i])+1
        return paren[i]
    
    for i in range(n):
        height(i)
    return int(max(paren))

def main():
    mode = input()
    if "F" in mode:
        filename = input()
        if "a" not in filename:
            with open(str("test/"+filename), mode="r") as f:
                nav = int(f.readline())
                parent = list(map(int, f.readline().split()))
        else :
            print("error")
    elif "I"in mode:
        nav = int(input())
        parent = list(map(int, input().split()))
    else:
        print("Invalid input mode.")
    print(compute_height(nav, parent))
        
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
