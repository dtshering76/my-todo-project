FILEPATH = "todos.txt"
import time

now = time.strftime("%b, %m, %Y %H:%M:%S")
print(now)

def todo_fun(filepath=FILEPATH):
    """
    Read a file and return the to_do list
    items.
    """
    with open(filepath, 'r') as todo_local:
        todo_list_local = todo_local.readlines()
        return todo_list_local


def write_todo(todo_write, filepath=FILEPATH):
    """ Write the to_do list in the text file"""
    with open(filepath, 'w') as file:
        file.writelines(todo_write)


if __name__ == "__main__":
    print("This is from module py")
    print(todo_fun())
