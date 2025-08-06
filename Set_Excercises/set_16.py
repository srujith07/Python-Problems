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
# sentence = "dog is a simple animal dogs is selfless animal"
# sentence = sentence.lower()
# sentence = sentence.split()
#
# sen_set = set(sentence)
# print(len(sen_set))

class Mobile:

    def __init__(self,model):

        self.model = model

    def get_model(self):
        print(self.model)

    def update_model(self,new_model):

        self.model = new_model


mobile_1 = Mobile("ONEPHONE")

mobile_1.get_model()

mobile_1.update_model("Oneplus")

mobile_1.get_model()
