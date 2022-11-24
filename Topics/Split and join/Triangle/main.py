height_triangle = int(input())
for i in range(height_triangle):
    shift = height_triangle - (i + 1)
    print(" " * shift + "#" * (2 * height_triangle - 1 - 2 * shift) + " " * shift)
