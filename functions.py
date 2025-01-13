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



if __name__ == "__main__" :
    # seven_brothers()
    # mean(3,4,5)
    # print_many_times("hi", 6)
    hash_square(5)
