# Tabular Output from Lists
# You have two lists: names = ["Alice", "Bob", "Charlie"] and scores = [85, 92, 78]. Print these lists as a simple table with columns “Name” and “Score”.
#
# Expected Output:
#
# Name       Score
# ---------------
# Alice      85
# Bob        92
# Charlie    78

names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

for i , j in zip(names,scores):
    print(f"{i:<10}{j:>5}"  )
