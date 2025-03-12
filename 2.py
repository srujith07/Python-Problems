
for i in range(11):
    pv_num = i - 1
    sm = i+pv_num

    if pv_num < 0:
        pv_num,sm = 0,0

    print (f"Current Number {i}  Previous Number  {pv_num}  Sum:  {sm}" )
