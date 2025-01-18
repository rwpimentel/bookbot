def main():
 
    # vars
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = word_count(text)
    letter = count_chars(text)
    rpt = report(text)

    # actions
    #print("The book text is", text)
    #print("The word count is", count)
    print(letter)


    return 0

# functions
def get_book_text(text):
    with open(text) as f:
        return f.read()

def word_count(text):
    lstring = str.split(text)
    return len(lstring)

def count_chars(text):
    text = text.lower()
    dict = {}

    for i in range(0, len(text)):
        #if (text[i].isalpha()):
        if text[i] in dict:
            dict[text[i]] += 1
        else:
            dict[text[i]] = 1
    return dict

def report(text):

    text = count_chars(text)
   
    for i in range(0, len(text)):
        if (text[i].isalpha()):
            print("yes")

    return None    

main()