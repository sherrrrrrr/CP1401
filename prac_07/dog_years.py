"""
Pseudocode:
start program

set human_years to input "age in human years: " and convert to float
while human_years is greater than or equal to 0
    set dog_years to call human_years_convert_dog_years with human_years
    print "age in dog years is " and dog_years
    set human_years to input "age in human years: " and convert to float
end while

define function human_years_convert_dog_years with parameter human_years
    if human_years is less than or equal to 2
        set dog_years to human_years times 10.5
    else
        set dog_years to 21 plus (4 times (human_years minus 2))
    end if
    return dog_years
end function

if program is running as main
    call main
end if

end program
"""
def main():
    while True:
        human_years = float(input("Age in human years: "))
        if human_years < 0:
            break

        dog_years = human_years_convert_dog_years(human_years)
        print("Age in dog years is", dog_years)


def human_years_convert_dog_years(human_years):
    if human_years <= 2:
        dog_years = human_years * 10.5
    else:
        dog_years = 21 + 4 * (human_years - 2)

    return dog_years


if __name__ == "__main__":
    main()
