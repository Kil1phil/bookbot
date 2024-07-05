def main():
    book_path= "books/frankenstein.txt"
    text=(get_book_text(book_path))
    num_words=get_word_count(text)
    
    counter_per_char=count_chars(text)
    
    print(f"--- Begin report of {book_path} ---")
    print (f"{num_words} words found in the document \n" )
    print_report(report_book(counter_per_char))
    print("--- End report ---")
def count_chars(text):
    text=text.lower()
    chars = {}
    for c in set(text):
       chars[c] = text.count(c)
    return chars



def get_book_text(path):
    with open (f"books/frankenstein.txt",encoding="utf8") as f:
        file_contents = f.read()
        return (file_contents)

def get_word_count(text):
    all_words=text.split()
    return (len(all_words))

def sort_on(dict):
    return dict["num"]

def print_report(list_of_chars):
    for char in list_of_chars:
        print(f"The '{char['name']}' character was found {char['num']} times")

def report_book(text):
    list_of_dict=[]
    t={}
    for a in text:
        
        if a.isalpha():
            t['name']=  a
            t['num'] =  text[a]
            list_of_dict.append(t)
            t={}
    #print(list_of_dict)
    list_of_dict.sort(reverse=True,key=sort_on)
    return (list_of_dict)



main()
