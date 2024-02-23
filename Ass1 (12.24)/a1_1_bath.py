"""
CP1401 2023-SP53 Assignment 1
Program 1 – Bathtub Cost Calculator
Student Name: <Jiaxin Li>
Date started: <2023.12.06>

Pseudocode:
display "Trump Bathtubs Cost Calculator"
# Input
get width, length, thickness
# Processing
side_panel_height = 50
gold_price_per_cubic_centimetre = 1777
# Calculate
bottom_panel_area = width * length
side_panel_area = side_panel_height * length
end_panel_area = side_panel_height * width
# Output
if decimal_part.strip('0') == ''
    display "Required volume of gold = {total_volume:.1f} cubic centimetres"
else:
    display "Required volume of gold = {total_volume} cubic centimetres"

display "Your total price is ${total_price:.2f}"
"""

print("Trump Bathtubs Cost Calculator")
# Input
width = float(input("Width of tub: "))
length = float(input("Length of tub: "))
thickness = float(input("Gold thickness: "))
# Processing
side_panel_height = 50  # the height of bathtub panel (in centimetres)
gold_price_per_cubic_centimetre = 1777  # Price per cubic centimeter of gold

bottom_panel_area = width * length
side_panel_area = side_panel_height * length  # The area of the side panel
end_panel_area = side_panel_height * width  # The area of the end panel

total_area = bottom_panel_area + 2 * side_panel_area + 2 * end_panel_area
total_volume = total_area * thickness
total_price = total_volume * gold_price_per_cubic_centimetre

volume_as_str = str(total_volume)
decimal_part = volume_as_str.split('.')[1]
# Output
if decimal_part.strip('0') == '':
    print(f"Required volume of gold = {total_volume:.1f} cubic centimetres")   # Display required volume of gold
else:
    print(f"Required volume of gold = {total_volume} cubic centimetres")  # Display required volume of gold

print(f"Your total price is ${total_price:.2f}")