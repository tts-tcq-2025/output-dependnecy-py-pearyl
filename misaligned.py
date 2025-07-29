def get_major_colors():
    return ["White", "Red", "Black", "Yellow", "Violet"]

def get_minor_colors():
    return ["Blue", "Orange", "Green", "Brown", "Slate"]

def get_color_map():
    color_map = []
    major_colors = get_major_colors()
    minor_colors = get_minor_colors()
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            index = i * len(minor_colors) + j
            color_map.append((index, major, minor))
    return color_map

def format_color_map_line(entry):
    return (f'{index} | {major} | {minor}')

def print_on_console(line_content: str):
    print(line_content, end='')

def print_color_map(print_fn):
    color_map = generate_color_map()
    for entry in color_map:
        line = format_color_map_line(entry)
        print_fn(line)
    return len(color_map)




