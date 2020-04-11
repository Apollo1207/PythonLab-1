from src.Sofa import *


def main():
    obj_1 = Sofa(500)
    obj_2 = Sofa(1000, 1500)
    obj_3 = Sofa(2000, 2500, "purple")
    print(obj_1.__str__())
    print(obj_2.__str__())
    print(obj_3.__str__())
    print(obj_1.staticmethod())


if __name__ == "__main__":
    main()
