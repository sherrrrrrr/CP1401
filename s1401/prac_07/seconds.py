"""
Pseudocode:
start program

define the_duration as a list with values [0, 635, 1270, 1905, 2540, 3175]

for each duration in the_duration
    set formatted_duration to the result of duration_in_seconds(duration)
    print duration in seconds and formatted_duration

prompt for favorite_duration as integer
set the_favorite_duration to the result of duration_in_seconds(favorite_duration)
print message indicating the favorite duration in minutes and seconds

define function duration_in_seconds with parameter seconds
    set minutes to seconds divided by 60 and floored
    set remaining seconds to the remainder of seconds divided by 60
    return formatted string with minutes and seconds

end program
"""

def main():
    the_duration = [0, 635, 1270, 1905, 2540, 3175]

    for duration in the_duration:
        formatted_duration = duration_in_seconds(duration)
        print(f"{duration} seconds is {formatted_duration}")

    favorite_duration = int(input("Favorite duration in seconds: "))
    the_favorite_duration = duration_in_seconds(favorite_duration)
    print(f"You love {the_favorite_duration}")


def duration_in_seconds(seconds):
    minutes = seconds // 60
    seconds = seconds % 60
    return f"{minutes}m {seconds}s"


if __name__ == "__main__":
    main()

