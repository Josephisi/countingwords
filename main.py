# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    text = open("story.txt", "r")
    reader = text.read()

    for line in reader:
        line = line.strip()
        line = line.lower()
        line = line.strip("/n,.?")
    words = reader.split(" ")
    return words
    
  

def count_words():
    text = read_file_content("story.txt")
    count = {}
    for words in text:
        if word in counts:
            counts[word] +=1
        else:
            counts [word] = 1
    for key in list(counts.keys()):
        print(key,":", counts[key])
    return count_words
print(count_word())
