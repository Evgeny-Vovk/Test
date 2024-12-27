# Input sentence
sentence = "The quick brown fox jumps over the lazy dog"  # A sentence to be converted to a wordlist

# Step 1: Convert the sentence into a list of words
wordlist = sentence.split()  # Use the split method to break the sentence into individual words

# Step 2: Reverse the wordlist
reversed_wordlist = wordlist[::-1]  # Reverse the list of words using slicing with a step of -1

# Output results
print("Original Wordlist:", wordlist)  # Display the original list of words
print("Reversed Wordlist:", reversed_wordlist)  # Display the reversed list of words
