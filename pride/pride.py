from helpers import generate_cleaned_lines

def is_word_in_file(word, filename):
    count = 0
    for line in generate_cleaned_lines(filename):
        # line will be a string of each line of the file in order
        # Your code goes here.
        # Your code should do something with the word and line variables and assign the value to a variable for returning
        if line.find(word) > 0:
            count = count + 1
    return count

input_word = raw_input("Enter a word to search for:")
answer = is_word_in_file(input_word, 'pride.txt')
# Display the answer in some meaningful way
print "Found the word " +input_word+ " " +str(answer)+ " times."