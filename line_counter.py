line_count = 0
empty_line_counter = 0
section_label = 0

with open("lyrics.txt", "r") as file:
    for each_line in file:
        if each_line == '\n':
            empty_line_counter = empty_line_counter + 1

        elif each_line.startswith('['):
            section_label = section_label + 1

        else:
            line_count = line_count + 1
    print('The total line number to recently, by Liana Flores is', line_count)
    print('empty lines', empty_line_counter)
    print('section is', section_label)