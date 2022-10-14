def colors(color):
    return f"\u001b[{int(color)}m"


def squares():
    for row in range(5):
        pixels = ['x'] * 9
        if row == 0 or row == 4:
            for pixel in range(0, 2):
                pixels[pixel] = ' '
            for pixel in range(3, 6):
                pixels[pixel] = ' '
            for pixel in range(7, 9):
                pixels[pixel] = ' '
            console_row = ''
            for pixel in pixels:
                console_row = console_row + pixel + ' '
            print(console_row)
        elif row == 1 or row == 3:
            pixels[0] = ' '
            pixels[4] = ' '
            pixels[8] = ' '
            console_row = ''
            for pixel in pixels:
                console_row = console_row + pixel + ' '
            print(console_row)
        else:
            console_row = ''
            for pixel in pixels:
                console_row = console_row + pixel + ' '
            print(console_row)


green = colors('42')
yellow = colors('43')
red = colors('41')
end = colors('0')
print(green + '  ' + yellow + '    ' + end + '')
print(green + '  ' + red + '    ' + end + '')
squares()
