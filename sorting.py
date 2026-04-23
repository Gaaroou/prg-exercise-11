import random
import matplotlib.pyplot as plt

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]

def selection_sort(seznam):
    seznam = seznam.copy()

    for x in range(len(seznam)):
        minimum_i = x
        for i in range(x + 1, len(seznam)):
            if seznam[i]< seznam[minimum_i]:
                minimum_i = i
        seznam[x], seznam[minimum_i] = seznam[minimum_i], seznam[x]
    return seznam

def bubble_sort(seznam_num):
    plt.ion()
    plt.show()
    seznam_num = seznam_num.copy()

    for x in range(len(seznam_num)):
        for y in range(len(seznam_num)-1):
            if seznam_num[y] > seznam_num[y+1]:
                seznam_num[y], seznam_num[y+1] = seznam_num[y+1], seznam_num[y]
                index_highlight1 = y
                index_highlight2 = y + 1
                colors = ["steelblue"] * len(seznam_num)
                colors[index_highlight1] = "tomato"
                colors[index_highlight2] = "tomato"
                plt.clf()
                plt.bar(range(len(seznam_num)), seznam_num, color=colors)
                plt.title("Bubble Sort")
                plt.pause(0.1)
    plt.ioff()
    plt.show()
    return seznam_num


if __name__ == "__main__":
    values = random_numbers(10)  # 10 čísel v rozsahu 0–100
    print(values)  # např. [42, 7, 91, 15, 63, 8, 57, 73, 2, 100]
    print(selection_sort(values))
    print(bubble_sort(values))
    # small = random_numbers(5, low=0, high=20)  # 5 čísel v rozsahu 0–20