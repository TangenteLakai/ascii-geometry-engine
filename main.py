from PIL import Image, ImageDraw


bin: list[list[int]] = []
def setup_bin(size: int) -> None:
    global bin
    # Initialize a 2D list with zeros
    bin = [[0 for _ in range(size)] for _ in range(size)]

           
def main() -> None:
    print("1. Square\n2. Triangle")
    match int(input("Select: ")):
        case 1:
            size: int = int(input("Size: "))
            square(size)
        case 2:
            size: int = int(input("Size: "))
            if size % 2 == 0:
                triangle(size)
            else:
                size += 1
                triangle(size)

def square(size: int) -> None: 
    setup_bin(size)
    for i in range(size):
        for j in range(size):
            if i == 0 or i == size - 1:
                bin[i][j] = 1
            elif j == 0 or j == size - 1:
                bin[i][j] = 1


def triangle(size: int) -> None:
    setup_bin(size) 
    for i in range(size):
        for j in range(size):
            if j <= i:
                bin[i][j] = 1
    print(bin)

def export_image(bin_table: list[list[int]]):
    ...


if __name__ == "__main__":
    main()
