# Remove empty strings from the list of strings
# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# Expected output:

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

res = list(filter(None, list1))
print(res)
