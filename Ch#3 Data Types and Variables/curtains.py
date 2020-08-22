roll_width = 140
price_per_meter = 5

# prompt the user to input the window measurements in cm
window_height = input('Enter the height of the window (cm):')
window_with = input('Enter the width of the window (cm):')
 
curtain_width = float(window_with) * 0.75 + 20
curtain_length = float(window_height) + 15
 
 
# work out how many withs of clorth will be nedded 
# and figure out the total length of material for each curtain (in cm still)
widths = curtain_width / roll_width
total_length = curtain_length * widths
total_length = (total_length * 2) / 10
price = total_length * price_per_meter
print("you need", total_length ,"meter of cloth for", price)
