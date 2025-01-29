print("🌟 Welcome to the Python Pattern Drawing Program!")
print("Choose a pattern type:")
print("1. Right-angled Triangle")
print("2. Square with Hollow Center")
print("3. Diamond")
print("4. Left-angled Triangle")
print("5. Hollow Square")
print("6. Pyramid")
print("7. Reverse Pyramid")
print("8. Rectangle with Hollow Center")

choice = int(input("Enter the number corresponding to your choice: "))

if choice in [1, 3, 4, 6, 7]:  # Patterns that need the number of rows
    rows = int(input("Enter the number of rows: "))
    if choice == 1:  # Right-angled Triangle
        # TODO: Loop through rows and print increasing stars
        for i in range(1, rows + 1):
            print('*' * i)

    elif choice == 3:  # Diamond
        # TODO: Create a diamond shape using loops
        for j in range(1, rows+1):
            p = 0
            for space in range(1, (rows - j) + 1):
                print(end=" ")

            while p != (2 * j - 1):
                print("*", end="")
                p += 1

            k = 0
            print()

        for i in range(rows, 1, -1):
            for space in range(0, rows+1 - i):
                print(" ", end="")
            for j in range(i, 2 * i - 1):
                print("*", end="")
            for j in range(1, i - 1):
                print("*", end="")
            print()

    elif choice == 4:  # Left-angled Triangle
        # TODO: Print decreasing stars for each row
        for k in range(rows, 0, -1):
            print('*' * k)

    elif choice == 6:  # Pyramid
        # TODO: Center-align stars to form a pyramid
        for j in range(1, rows+1):
            p = 0
            for space in range(1, (rows - j) + 1):
                print(end=" ")

            while p != (2 * j - 1):
                print("*", end="")
                p += 1

            k = 0
            print()

    elif choice == 7:  # Reverse Pyramid
        # TODO: Create an upside-down pyramid
        for i in range(rows+1, 1, -1):
            for space in range(0, rows+1 - i):
                print(" ", end="")
            for j in range(i, 2 * i - 1):
                print("*", end="")
            for j in range(1, i - 1):
                print("*", end="")
            print()

elif choice in [2, 5, 8]:  # Patterns that need size

    if choice == 2:  # Square with Hollow Center
        # TODO: Create a square with a hollow center
        size = int(input("Enter the size of the square/rectangle: "))
        for i in range(size):
            for j in range(size):
                if i == 0 or i == size-1 or j == 0 or j == size-1:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()

    elif choice == 5:  # Hollow Square
        size = int(input("Enter the size of the square/rectangle: "))        # TODO: Similar to choice 2 but ensure perfect square logic
        for i in range(size):
            for j in range(size):
                if i == 0 or i == size - 1 or j == 0 or j == size - 1:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()

    elif choice == 8:  # Rectangle with Hollow Center
        # TODO: Handle separate width and height inputs for rectangle
        width = int(input("Enter the width of the rectangle: "))
        height = int(input("Enter the height of the rectangle: "))
        for i in range(width):
            for j in range(height):
                if i == 0 or i == width - 1 or j == 0 or j == height - 1:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()

else:
    print("❌ Invalid choice! Please restart the program.")

# Step 5: Optional - Allow the user to restart or exit