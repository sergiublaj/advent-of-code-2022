INPUT_FILE = 'day07.txt'


class Node:
    def __init__(self, root):
        self.root = root
        self.children = []

    def add_child(self, child):
        self.children.append(child)


def part1():
    answer = 0
    command_line = False

    with open(INPUT_FILE) as commands:
        for command in commands.readlines():
            c = command.split(' ')
            if c[0] == '$':
                command_line = True
            

    return answer


def part2():
    return -1


def main():
    print(f'Answer #1: {part1()}')

    print(f'Answer #2: {part2()}')
        

if __name__ == '__main__':
    main()
