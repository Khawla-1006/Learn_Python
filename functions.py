def seven_brothers() :
    print("Aapo")
    print("Eero")
    print("Juhani")
    print("Lauri")
    print("Simeoni")
    print("Timo")
    print("Tuomas")

def mean(x, y, z) :
    print((x + y + z)/3)

def print_many_times(text, times) :
    i = 0 
    while i < times :
        print(text)
        i+=1

def hash_square(x) :
    i = 0
    while i < x :
        print("#" * x)
        i += 1
    
def chessboard(a) : 
    i = 0
    j = 1 
    zero = "0"
    one = "1"
    while j < a :
        if j % 2 == 0 :
            zero += "0"
            one += "1"
        else :
            zero += "1"
            one += "0"
        j += 1
    while i < a :
        if i % 2 == 0 :
            print(zero)
        else : 
            print(one)
        i += 1


if __name__ == "__main__" :
    # seven_brothers()
    # mean(3,4,5)
    # print_many_times("hi", 6)
    # hash_square(5)
    chessboard(10)

