def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    wordcount = len(text.split())
    print(wordcount)
   # print(text)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
main()
