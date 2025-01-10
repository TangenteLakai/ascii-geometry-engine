bin: list[list[int]] = []

def setup_bin(size) -> None:
    """Initialize a 2D list with zeros."""
    global bin
    if isinstance(size, tuple):
        bin = [[0 for _ in range(size[1])] for _ in range(size[0])]
    else:
        bin = [[0 for _ in range(size)] for _ in range(size)]

def print_bin() -> None:
    """Print the current bin structure."""
    for row in bin:
        for cell in row:
            if cell != 0:
                #print(" ", end="")
                print(" #", end="")
            else:
                print("  ", end="")
                #print(" ", end="")
        print()


def square(size: int) -> None:
    """Create a square pattern."""
    setup_bin(size)
    for i in range(size):
        for j in range(size):
            if i == 0 or i == size - 1 or j == 0 or j == size - 1:
                bin[i][j] = 1

def triangle(size: int) -> None:
    """Create a triangle pattern."""
    setup_bin(size)
    for i in range(size):
        for j in range(size):
            if j == 0 or j == i or i == size - 1:
                bin[i][j] = 1

def rectangle(height: int, width: int) -> None:
    """Create a rectangle pattern."""
    setup_bin((height, width))
    for i in range(height):
        for j in range(width):
            if i == 0 or i == height - 1 or j == 0 or j == width - 1:
                bin[i][j] = 1

def main() -> None:
    """Main function to select and display shapes."""
    print("1. Square\n2. Triangle\n3. Rectangle")
    choice = int(input("Select: "))

    if choice == 1:
        size = int(input("Size: "))
        square(size)
    elif choice == 2:
        size = int(input("Size: "))
        triangle(size)
    elif choice == 3:
        height = int(input("Height: "))
        width = int(input("Width: "))
        rectangle(height, width)
    else:
        print("Invalid choice. Please select 1, 2, or 3.")
    
    out = input("Do you want to view geometry before writing it to an image ? ([Y]es/[N]o) ")
    if out.lower() == "y" or out.lower() == "yes":
        print_bin()
    else:
        pass

if __name__ == "__main__":
    main()

bin: list[list[int]] = []

def setup_bin(size) -> None:
    """Initialize a 2D list with zeros."""
    global bin
    if isinstance(size, tuple):
        bin = [[0 for _ in range(size[1])] for _ in range(size[0])]
    else:
        bin = [[0 for _ in range(size)] for _ in range(size)]

def print_bin() -> None:
    """Print the current bin structure."""
    for row in bin:
        for cell in row:
            if cell != 0:
                print(" ", end="")
                print("#", end="")
            else:
                print(" ", end="")
                print(" ", end="")
        print()


def square(size: int) -> None:
    """Create a square pattern."""
    setup_bin(size)
    for i in range(size):
        for j in range(size):
            if i == 0 or i == size - 1 or j == 0 or j == size - 1:
                bin[i][j] = 1

def triangle(size: int) -> None:
    """Create a triangle pattern."""
    setup_bin(size)
    for i in range(size):
        for j in range(size):
            if j == 0 or j == i or i == size - 1:
                bin[i][j] = 1

def rectangle(height: int, width: int) -> None:
    """Create a rectangle pattern."""
    setup_bin((height, width))
    for i in range(height):
        for j in range(width):
            if i == 0 or i == height - 1 or j == 0 or j == width - 1:
                bin[i][j] = 1

def main() -> None:
    """Main function to select and display shapes."""
    print("1. Square\n2. Triangle\n3. Rectangle")
    choice = int(input("Select: "))

    if choice == 1:
        size = int(input("Size: "))
        square(size)
    elif choice == 2:
        size = int(input("Size: "))
        if size % 2 != 0:
            print("Triangle size must be even. Adjusting size to the next even number.")
            size += 1
        triangle(size)
    elif choice == 3:
        height = int(input("Height: "))
        width = int(input("Width: "))
        rectangle(height, width)
    else:
        print("Invalid choice. Please select 1, 2, or 3.")
    
    out = input("Do you want to view geometry before writing it to an image ? ([Y]es/[N]o) ")
    if out.lower() == "y" or out.lower() == "yes":
        print_bin()
    else:
        pass

if __name__ == "__main__":
    main()

