def get_book_text(file_path):
    #A with block can be used to open a file:
    #The with block will automatically close the file when
    #the block is exited, cleaning up resources.
    with open(file_path) as f: 
        # .read() method to read the contents of a file into a string
        # f is a file object
        file_contents = f.read()
    return file_contents


def get_nums_of_text_book(text_book):
    text_book = text_book.split()
    return f"Found {len(text_book)} total words"

def get_numes_of_chars(text_book):
    dictt = {}
    text_book = text_book.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in text_book:
        if i in alphabet:
            if i not in dictt:
                dictt[i] = 1
            else:
                dictt[i] += 1
    return dictt

def sorted_dict(dictionary):
    d = sorted(dictionary.items(), key=lambda item: item[1], reverse=True)
    for i in d:
        print(f"{i[0]}: {i[1]}")

