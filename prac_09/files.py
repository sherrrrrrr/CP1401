"""
Pseudocode:
start program
function question_4
    Read from file "name.txt" and greet the user
    in_file = open("name.txt", "r")
    text = in_file.read().strip()
    in_file.close()
    display "Greetings {text}!"
end function

function question_5
    prompt the user for file name and threshold value
    file_name = input("Enter the file name: ")
    threshold = float(input("Enter the threshold: "))

    set count to 0
    set total to 0

    Open the file and calculate the count and total values
    with open("recentrain.txt", 'r') as file
        for line in file
            value = float(line.strip())
            total += 1
            if value > threshold
                count += 1

    Calculate the percentage and display the results
    percentage = (count / total) * 100

    display "file_name"
    display "threshold"
    display "processing..."
    display "count, total, and percentage with message format"
end function

function question_6
    prompt the user for input and output file names, and search string
    input_file_name = input("Input file name: ")
    output_file_name = input("Output file name: ")
    search_string = input("Search string: ")

    Open the input and output files, and filter the lines
        with open(input_file_name, 'r') as input_file, open(output_file_name, 'w') as output_file
        for line in input_file
            if search_string in line
                output_file.write(line)

    display "Filtered lines have been written to {output_file_name}."
end function

end program
"""
def question_4():
    in_file = open("name.txt", "r")
    text = in_file.read().strip()
    in_file.close()

    print(f"Greetings {text}!")
def question_5():
    file_name = input("Enter the file name: ")
    threshold = float(input("Enter the threshold: "))

    count = 0
    total = 0

    with open("recentrain.txt", 'r') as file:
        for line in file:
            value = float(line.strip())
            total += 1
            if value > threshold:
                count += 1

    percentage = (count / total) * 100

    print(f"Filename: {file_name}")
    print(f"Threshold: {threshold}")
    print("Processing...")
    print(f"{count} out of {total} ({percentage:.1f}%) values in {file_name} are greater than {threshold}.")

def question_6():
    input_file_name = input("Input file name: ")
    output_file_name = input("Output file name: ")
    search_string = input("Search string: ")

    with open(input_file_name, 'r') as input_file, open(output_file_name, 'w') as output_file:
        for line in input_file:
            if search_string in line:
                output_file.write(line)

    print(f"Filtered lines have been written to {output_file_name}.")


question_4()
question_5()
question_6()
