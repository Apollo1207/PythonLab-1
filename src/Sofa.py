class Sofa:

    def __init__(self, width=100, height=200, color="blue", brand="Lusso"):
        self.width = width
        self.height = height
        self.color = color
        self.brand = brand

    def __del__(self):
        pass

    def __str__(self):
        return "Ширина: {} \t Висота: {} \t Колір: {} \t Бренд: {}" \
            .format(self.width, self.height, self.color, self.brand)

    y = 18

    @staticmethod
    def staticmethod():
        print(Sofa.y)
