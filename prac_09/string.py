"""
Pseudocode:
start program
function question_1
    List of data strings
    data_strings = ["Result = 95%", "Final Score = 8%", "Relative Value = 178%",
                    "Something else that's very important = 9.2%", "x = 42%"]
    Process each data string

    for each string in data_strings
        equal_index = string.find("=")
        percentage_index = string.find("%")

        value = string[equal_index + 2: percentage_index]
        display value as a float
end function

function question_2
    Get the current year
    current_year = 2022
    next_year = current_year + 1

    prompt for Date of Birth (DOB)
    DOB = input("DOB: ")
    year_index = DOB.rfind("/") + 1
    year = DOB[year_index:]

    display "You were born in {year}."
    display "You will turn {next_year - int(year)} in {next_year}."
end function

function question_3
    Continuous loop until a blank input
    while True
        subject_code = input("Enter subject code: ")

        if subject_code == ""
            break the loop

        year_level = subject_code[2]

        if subject_code[:2] == "CP"
            it_string = " IT" if year_level != "5" else " Masters or other IT"
        else
            it_string = ""

        display "That is a {year_level.lower()}{'th' if year_level != '1' else 'st'}{it_string} subject."
end function

end program
"""
def question_1():
    data_strings = ["Result = 95%", "Final Score = 8%", "Relative Value = 178%",
                    "Something else that's very important = 9.2%", "x = 42%"]

    for string in data_strings:
        equal_index = string.find("=")
        percentage_index = string.find("%")

        value = string[equal_index + 2: percentage_index]
        print(float(value))


def question_2():
    current_year = 2022
    next_year = current_year + 1

    DOB = input("DOB: ")
    year_index = DOB.rfind("/") + 1
    year = DOB[year_index:]

    print(f"You were born in {year}.")
    print(f"You will turn {next_year - int(year)} in {next_year}.")

def question_3():
    while True:
        subject_code = input("Enter subject code: ")

        if subject_code == "":
            break

        year_level = subject_code[2]

        if subject_code[:2] == "CP":
            it_string = " IT" if year_level != "5" else " Masters or other IT"
        else:
            it_string = ""

        print(f"That is a {year_level.lower()}{'th' if year_level != '1' else 'st'}{it_string} subject.")


question_1()
question_2()
question_3()

