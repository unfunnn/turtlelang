import random

# Required Variables

grid = [[None, None, None, None, None],
        [None, None, None, None, None],
        [None, None, None, None, None],
        [None, None, None, None, None],
        [None, None, None, None, None]]
turtle_pos = "00"
draw = True
prev_pos_list = []
current_process = None
temp_str = ""
temp_list = ["", ""]
final_str = ""
current_index = 0
prev_input = ""
conditional = True
used_waypoint_list = []


# Output the grid at the end

def output():
    for row in output_grid:
        total_str = ""
        for pixel in row:
            total_str += pixel + " "
        print(total_str)


# Gets the data from any given co-ord

def get_pixel(coord):
    try:
        return int(grid[int(coord[0])][int(coord[1])])
    except ValueError:
        grid[int(coord[0])][int(coord[1])]


print("turtlelang v1.0.0")
print("An esolang where you control a turtle and each position is a variable")
print(
    "Type \"exit\" to exit, \"open\" to open a .turt file, and \"compile\" to compile everything from this session into a single line")

while True:
    instructions = input(">>> ")
    len_instructions = len(instructions)
    i = 0
    position_waypoint_list = []
    character_i = 0
    while character_i < len_instructions:
        if instructions[character_i] == "_":
            position_waypoint_list.append(character_i)
        character_i+=1
    print(position_waypoint_list)

    if instructions == "exit":
        quit(0)
    elif instructions == "compile":
        print(prev_input)
    elif instructions == "open":
        file_path = input("File path:")
        with open(file_path) as f:
            lines = f.readlines()
        instructions = lines[0]
        len_instructions = len(instructions)
    elif instructions == "help":
        print("Docs are in the \"help.txt\" file")
    else:
        prev_input += instructions
        while i < len_instructions:
            if current_process is None:
                if instructions[i] == ">":
                    if int(turtle_pos[1]) + 1 <= 4:
                        turtle_pos_x = int(turtle_pos[1]) + 1
                        turtle_pos_y = int(turtle_pos[0])
                        if draw:
                            prev_pos_list.append(turtle_pos)
                        turtle_pos = str(turtle_pos_y) + str(turtle_pos_x)
                elif instructions[i] == "<":
                    if int(turtle_pos[1]) - 1 >= 0:
                        turtle_pos_x = int(turtle_pos[1]) - 1
                        turtle_pos_y = int(turtle_pos[0])
                        if draw:
                            prev_pos_list.append(turtle_pos)
                        turtle_pos = str(turtle_pos_y) + str(turtle_pos_x)
                elif instructions[i] == "^":
                    if int(turtle_pos[0]) - 1 >= 0:
                        turtle_pos_x = int(turtle_pos[1])
                        turtle_pos_y = int(turtle_pos[0]) - 1
                        if draw:
                            prev_pos_list.append(turtle_pos)
                        turtle_pos = str(turtle_pos_y) + str(turtle_pos_x)
                elif instructions[i] == "v":
                    if int(turtle_pos[0]) + 1 <= 4:
                        turtle_pos_x = int(turtle_pos[1])
                        turtle_pos_y = int(turtle_pos[0]) + 1
                        if draw:
                            prev_pos_list.append(turtle_pos)
                        turtle_pos = str(turtle_pos_y) + str(turtle_pos_x)
                elif instructions[i] == "~":
                    if draw:
                        draw = False
                    else:
                        draw = True
                elif instructions[i] == "%":
                    current_process = "var_set"
                elif instructions[i] == "@":
                    current_process = "out"
                elif instructions[i] == "$":
                    current_process = "in"
                elif instructions[i] == "+":
                    current_process = "add"
                elif instructions[i] == "-":
                    current_process = "sub"
                elif instructions[i] == "*":
                    current_process = "mul"
                elif instructions[i] == "/":
                    current_process = "div"
                elif instructions[i] == "?":
                    current_process = "if"
                    temp_list = ["", "", "", "", ""]
                elif instructions[i] == "&":
                    current_process = "rand"
                elif instructions[i] == "#":
                    current_process = "comment"
                elif instructions[i] == ".":
                    current_process = "dupe"
                elif instructions[i] == "|":
                    current_process = "literal_out"
                elif instructions[i] == "[":
                    current_process = "loop"
                    temp_list = ["", "", ""]
            else:
                if current_process == "var_set":
                    if instructions[i] == ":":
                        grid[int(turtle_pos[0])][int(turtle_pos[1])] = temp_str
                        temp_str = ""
                        current_process = None
                    else:
                        temp_str += instructions[i]
                elif current_process == "out":
                    if instructions[i] == ":":
                        print(str(grid[int(turtle_pos[0])][int(turtle_pos[1])]))
                        current_process = None
                elif current_process == "in":
                    if instructions[i] == ":":
                        inp = input()
                        try:
                            inp = int(inp)
                        except ValueError:
                            pass
                        grid[int(turtle_pos[0])][int(turtle_pos[1])] = inp
                        current_process = None
                elif current_process == "add":
                    if instructions[i] == ":":
                        grid[int(turtle_pos[0])][int(turtle_pos[1])] = int(get_pixel(temp_list[0])) + int(
                            get_pixel(temp_list[1]))
                        temp_str = ""
                        current_process = None
                        temp_list = ["", ""]
                        current_index = 0
                    elif instructions[i] == ",":
                        current_index += 1
                    else:
                        temp_list[current_index] += instructions[i]

                elif current_process == "sub":
                    if instructions[i] == ":":
                        grid[int(turtle_pos[0])][int(turtle_pos[1])] = int(get_pixel(temp_list[0])) - int(
                            get_pixel(temp_list[1]))
                        temp_str = ""
                        current_process = None
                        temp_list = ["", ""]
                        current_index = 0
                    elif instructions[i] == ",":
                        current_index += 1
                    else:
                        temp_list[current_index] += instructions[i]

                elif current_process == "mul":
                    if instructions[i] == ":":
                        grid[int(turtle_pos[0])][int(turtle_pos[1])] = int(get_pixel(temp_list[0])) * int(
                            get_pixel(temp_list[1]))
                        temp_str = ""
                        current_process = None
                        temp_list = ["", ""]
                        current_index = 0
                    elif instructions[i] == ",":
                        current_index += 1
                    else:
                        temp_list[current_index] += instructions[i]

                elif current_process == "div":
                    if instructions[i] == ":":
                        grid[int(turtle_pos[0])][int(turtle_pos[1])] = int(get_pixel(temp_list[0])) / int(
                            get_pixel(temp_list[1]))
                        temp_str = ""
                        current_process = None
                        current_index = 0
                        temp_list = ["", ""]
                    elif instructions[i] == ",":
                        current_index += 1
                    else:
                        temp_list[current_index] += instructions[i]
                elif current_process == "if":
                    if instructions[i] == ":":
                        if temp_list[2] == "=":
                            if get_pixel(temp_list[0]) == get_pixel(temp_list[1]):
                                judgement = 1
                            else:
                                judgement = 0
                        if temp_list[2] == "!":
                            if get_pixel(temp_list[0]) != get_pixel(temp_list[1]):
                                judgement = 1
                            else:
                                judgement = 0
                        if temp_list[2] == ">":
                            if get_pixel(temp_list[0]) > get_pixel(temp_list[1]):
                                judgement = 1
                            else:
                                judgement = 0
                        if temp_list[2] == "<":
                            if get_pixel(temp_list[0]) < get_pixel(temp_list[1]):
                                judgement = 1
                            else:
                                judgement = 0
                        if temp_list[4] == "":
                            if judgement == 1:
                                var_cont = temp_list[3]
                        else:
                            if judgement == 1:
                                var_cont = temp_list[3]
                            else:
                                var_cont = temp_list[4]
                        grid[int(turtle_pos[0])][int(turtle_pos[1])] = var_cont
                        current_process = None
                        temp_list = ["", ""]
                        current_index = 0
                    elif instructions[i] == ",":
                        current_index += 1
                    else:
                        temp_list[current_index] += instructions[i]
                elif current_process == "rand":
                    if instructions[i] == ":":
                        grid[int(turtle_pos[0])][int(turtle_pos[1])] = random.randint(int(temp_list[0]), int(temp_list[1]))
                        current_process = None
                        current_index = 0
                        temp_list = ["", ""]
                    elif instructions[i] == ",":
                        current_index += 1
                    else:
                        temp_list[current_index] += str(instructions[i])
                elif current_process == "dupe":
                    if instructions[i] == ":":
                        grid[int(temp_str[0])][int(temp_str[1])] = grid[int(turtle_pos[0])][int(turtle_pos[1])]
                        current_process = None
                        temp_str = ""
                    else:
                        temp_str += instructions[i]

                elif current_process == "literal_out":
                    if instructions[i] == ":":
                        current_process = None
                        print(temp_str)
                        temp_str=""
                    else:
                        temp_str+=instructions[i]

                elif current_process == "comment":
                    if instructions[i] == ":":
                        current_process = None

                elif current_process == "loop":
                    if instructions[i] == "]":
                        if temp_list[2] == "=":
                            if get_pixel(temp_list[0]) == get_pixel(temp_list[1]):
                                judgement = 1
                            else:
                                judgement = 0
                        if temp_list[2] == "!":
                            if get_pixel(temp_list[0]) != get_pixel(temp_list[1]):
                                judgement = 1
                            else:
                                judgement = 0
                        if temp_list[2] == ">":
                            if get_pixel(temp_list[0]) > get_pixel(temp_list[1]):
                                judgement = 1
                            else:
                                judgement = 0
                        if temp_list[2] == "<":
                            if get_pixel(temp_list[0]) < get_pixel(temp_list[1]):
                                judgement = 1
                            else:
                                judgement = 0
                        if judgement == 0:
                            found = False
                            for position_waypoint in position_waypoint_list:
                                if position_waypoint not in used_waypoint_list and found is False:
                                    i = position_waypoint
                                    found = True
                        elif judgement == 1:
                            found = False
                            for position_waypoint in position_waypoint_list:
                                if position_waypoint not in used_waypoint_list and found is False:
                                    used_waypoint_list.append(position_waypoint)
                                    found = True
                        current_process = None
                        temp_list = ["", ""]
                        current_index = 0
                    elif instructions[i] == ",":
                        current_index += 1
                    else:
                        temp_list[current_index] += instructions[i]
            if conditional:
                i += 1

        print(final_str)
        output_grid = [["⬜", "⬜", "⬜", "⬜", "⬜"],
                       ["⬜", "⬜", "⬜", "⬜", "⬜"],
                       ["⬜", "⬜", "⬜", "⬜", "⬜"],
                       ["⬜", "⬜", "⬜", "⬜", "⬜"],
                       ["⬜", "⬜", "⬜", "⬜", "⬜"]]

        for pos in prev_pos_list:
            output_grid[int(pos[0])][int(pos[1])] = "⬛"

        output_grid[int(turtle_pos[0])][int(turtle_pos[1])] = "▣"
        final_str = ""

        output()
