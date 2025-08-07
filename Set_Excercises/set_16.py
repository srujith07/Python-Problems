# # Count Unique Words
# # Write a code to count the number of unique words in the given a sentence.
# #
# # Given:
# #
# # sentence = "dog is a simple animal dogs is selfless animal"
# # Expected Output:
# #
# # Number of unique words: 7
#
sentence = "dog is a simple animal dogs is selfless animal"
sentence = sentence.lower()
sentence = sentence.split()

sen_set = set(sentence)
print(len(sen_set))
