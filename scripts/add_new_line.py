import sys

def add_new_line(file_path):
    metadata = ["title", "category", "date", "modified", "author", "authors", "tags"]
    with open(file_path, 'rt') as f:
        lines = f.readlines()
    new_lines = []
    for line in lines:
        if line.split(":")[0] in metadata:
            new_line = line
        elif line.strip('\n') == "":
                continue
        else:
            new_line = '\n'+ line.strip('\n')+'\n'
        new_lines.append(new_line)

    with open(file_path, 'wt') as f:
        f.writelines(new_lines)
    
def remove_new_line(file_path):
    metadata = ["title", "category", "date", "modified", "author", "authors"]
    with open(file_path, 'rt') as f:
        lines = f.readlines()
    new_lines = []
    for line in lines:
        try:
            if line.split(":")[0] in metadata:
                continue
        except:
            continue
    new_lines = [l.strip('\n') + '\n' for l in lines]
    with open(file_path, 'wt') as f:
        f.writelines(new_lines)

if __name__ == "__main__":
    add_new_line(sys.argv[1])
    # remove_new_line(sys.argv[1])
