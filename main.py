import pprint

from helper.write_a_json import write_a_json as wj

from oop.car import Car


if __name__ == '__main__':

    c = Car()
    x = c.readModel("A3")

    for car in x:
        pprint.pprint(car)

    print(x)

    print("Job finished")
