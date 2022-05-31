import sys


def detect():
    pass


def web_detect():
    pass


if __name__ == '__main__':
    # sys.argv = ["main.py", "", "", ""]
    command = sys.argv[1]
    if command == "detect":
        detect()
    elif command == "web_detect":
        web_detect()
    else:
        print('incorrect command')
