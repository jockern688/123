file1=input("Dictionary file =>")
print(file1)
file2=input("Input file => ")
print(file2)
file3=input("Keyboard file => ")
print(file3)
words_dict = dict()
keyboards = dict()
letter_map = [chr(i) for i in range(97,123)]

with open(file1, "r") as file:
    for line in file:
        words = line.strip().split(",")
        words_dict[words[0]] = words[1]


with open(file3, "r") as file:
    for line in file:
        keys = line.strip().split(" ") # [a, q, w, s, z]
        keyboards[keys[0]] = keys[1:]

def drop(word, pos):
    return word[:pos]+word[pos+1:]

def insert(word, pos):
    pass

def compare():
    filename = file2
    with open(filename, "r") as input_file:
        for line in input_file: # barely
            # FOUND
            word = line.strip()
            if words_dict.get(word):
                print("{:>15} -> FOUND".format(word))
            else:
                possible = dict()
                for i in range(len(word)):
                # DROP
                    droped = drop(word, i)
                    if words_dict.get(droped):
                        possible[droped] = words_dict.get(droped)
                # INSERT
                    for letter in letter_map:
                        if i < len(word)-1:
                            inserted = word[:i]+letter+word[i:]
                        else:
                            inserted = word + letter
                        if words_dict.get(inserted):
                            possible[inserted] = words_dict.get(inserted)
                # SWAP
                    if i<len(word)-1:
                        swaped = word[:i]+word[i+1]+word[i]+word[i+2:]
                        if words_dict.get(swaped):
                            possible[swaped] = words_dict.get(swaped)
                # REPLACE
                    replace_letter = keyboards.get(word[i])
                    for letter in replace_letter:
                        replaced = word[:i]+letter+word[i+1:]
                        if words_dict.get(replaced):
                            possible[replaced] = words_dict.get(replaced)

                if possible:
                    possible = sorted(possible.items(),key = lambda x:x[1],reverse = True)[:3]
                    possible = [i[0] for i in possible]
                    result = " ".join(possible)
                    print("{:>15} -> FOUND{:>3}: {}".format(word, len(possible), result))
                else:
                    print("{:>15} -> NOT FOUND".format(word))


if __name__ == '__main__':
    compare()
#input_words.txt  