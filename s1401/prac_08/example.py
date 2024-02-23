"""
Pseudocode:
start program

places = []
place = input("Place: ")
while place != ""
    places.append(place.title())
    place = input("Place: ")

if places
    display ("On my holiday, I went to:")
    for place in places
        display (place)
    longest_place = places[0]
    for place in places
        if len(place) > len(longest_place)
            longest_place = place
    display ("The place with the longest name was", longest_place)
else
    display ("I went nowhere :(")

end program
"""

places = []
place = input("Place: ")
while place != "":
    places.append(place.title())
    place = input("Place: ")

if places:
    print("On my holiday, I went to:")
    for place in places:
        print(place)
    longest_place = places[0]
    for place in places:
        if len(place) > len(longest_place):
            longest_place = place
    print("The place with the longest name was", longest_place)
else:
    print("I went nowhere : ")