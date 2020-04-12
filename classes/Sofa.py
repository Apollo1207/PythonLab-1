class Sofa:
    my_str = "static_field"

    def __init__(self, width=None, height=None, color=None, brand=None):
        self.width = width
        self.height = height
        self.color = color
        self.brand = brand

    def __del__(self):
        print("Deleted fields:", self.width, self.height, self.color, self.brand)
        return

    def __str__(self):
        return "Width: {} \t Height: {} \t Color: {} \t Brand: {} \t Static field: {}" \
            .format(self.width, self.height, self.color, self.brand, Sofa.my_str)

    @staticmethod
    def get_str():
        return Sofa.my_str

    @classmethod
    def main(cls):
        obj_1 = Sofa(500)
        obj_2 = Sofa(1000, 1500)
        obj_3 = Sofa(2000, 2500, "purple", "Lusso")
        objects = [obj_1, obj_2, obj_3]
        for x in objects:
            print(x)
