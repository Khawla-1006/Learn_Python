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
            print(one)
        else : 
            print(zero)
        i += 1

#simpler solution :

def chessboarded(size):
    i = 0
    while i < size:
        if i % 2 == 0:
            row = "10"*size
        else:
            row = "01"*size

        # Remove extra characters at the end of the row
        print(row[0:size])
        i += 1

def squared(word, a) : 
    i = 0 
    while i < a :
        if i % 2 == 0 :
            string = word
        else : 
            #reversed string
            j = len(word) - 1
            string = ""
            while j > 0 :
                string += word[j] 
                j -= 1
        print(string[0 : a])
        i += 1


if __name__ == "__main__" :
    # seven_brothers()
    # mean(3,4,5)
    # print_many_times("hi", 6)
    # hash_square(5)
    # chessboard(10)
    # chessboarded(3)
    squared("khawla", 3)

