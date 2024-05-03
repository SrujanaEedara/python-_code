#You are given an integer, N. Your task is to print an alphabet rangoli of size N. (Rangoli is a form of Indian folk art based on creation of patterns.)
#Different sizes of alphabet rangoli are shown below:

def print_rangoli(size):
    a="abcdefghijklmnopqrstuvwxyz"
    lines=[]
    for row in range(size):
        print_="-".join(a[row:size])
        lines.append(print_[::-1]+print_[1:])
    width=len(lines[0])
    
    for row in range(size-1,0,-1):
        print(lines[row].center(width,'-'))
    
    for row in range(size):
        print(lines[row].center(width,'-'))
    

if __name__ == '__main__':

