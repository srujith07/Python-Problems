names = ["Alice", "Bob", "Charlie"] 
scores = [85, 92, 78]

for i , j in zip(names,scores):
    print(f"{i:<10}{j:>5}"  )
