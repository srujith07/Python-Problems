

with open ("test.txt", 'r') as test_file , open ("new_file.txt", 'w+') as new_file:
    line_count = 1

    for i in test_file:
        if  line_count!= 5:
            new_file.write(i)
        line_count+=1
    print("Copied content from from test.txt to new_filke.txt by skipping line number 5")

