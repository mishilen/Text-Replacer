import sys

LENGTH: int = 5
ARG0: int = 1
ARG1: int = 3


def check_arg(args01: str, args02: str) -> int:
    if args01.startswith('-') and args02.startswith('-r'):
        if args01[1] == 'f':
            return 0
        elif args01[1] =='t':
            return 1
    elif args01.startswith('-r'):
            return 2

    return -1


def clean_file(filename: str, string: str, new_string: str) -> None:
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
    except Exception as e:
        sys.exit("Failure to read file")

    for i in range(len(lines)):
        lines[i] = lines[i].replace(string, new_string)
    
    try:
        with open(filename, 'w') as file:
            file.writelines(lines)
    except Exception as e:
        sys.exit("Failed to write to file")


def clean_text(text: str, string: str, new_string: str):
    print(text.replace(string, new_string))


def to_string() -> str:
    return f'''
    Usage: python replacer [OPTIONS] [COMMAND] [OPTIONS] [COMMAND]

    Options:
        -f          replace text in a file. (Supported format - txt, csv)
        -t          replace text directly in terminal
        -r          replace one string with another

    Example usage: replacer -t "This is so cool!!" -r "This" "Meow"
    '''


def main() -> None:
    if len(sys.argv) < LENGTH + 1:
        sys.exit(to_string())
    
    matching: int = check_arg(sys.argv[ARG0], sys.argv[ARG1]) 

    if matching == 0:
        clean_file(sys.argv[ARG0 + 1], sys.argv[LENGTH - 1], sys.argv[LENGTH])
    elif matching == 1:
        clean_text(sys.argv[ARG0 + 1], sys.argv[LENGTH - 1], sys.argv[LENGTH])
    elif matching == 2 and sys.argv[LENGTH - 1].startswith('-'):
        if sys.argv[LENGTH - 1].startswith('-f'):
            clean_file(sys.argv[LENGTH], sys.argv[ARG0 + 1], sys.argv[ARG0 + 2])
        elif sys.argv[LENGTH - 1].startswith('-t'):
            clean_text(sys.argv[LENGTH], sys.argv[ARG0 + 1], sys.argv[ARG0 + 2])
    else:
        sys.exit(to_string())

if __name__ == "__main__":
    main();
