num = 1
while num == 1:
    w1 = int(input("Enter w1:"))
    w2 = int(input("Enter w2:"))
    w3 = int(input("Enter w3:"))
    eng = int(input("Enter marks:"))
    urd = int(input("Enter marks:"))
    stat = int(input("Enter marks:"))
    sum_weight_num = (w1*eng)+(w2*urd)+(w3*stat)
    sum_wight  = w1+w2+w3
    weighted_average = sum_weight_num/ sum_wight
    print("the weighted_average is:",weighted_average)