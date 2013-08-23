class Canvas:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.data = [['!'] * width for i in range(height)]

    def setpixel(self, row, col):
        self.data[row][col] = '*'

    def getpixel(self, row, col):
        return self.data[row][col]

    def display(self):
        print "\n".join(["".join(row) for row in self.data])
a=Canvas(4,5)
#a.setpixel(4,3)
print a.getpixel(4,3)
a.display()
