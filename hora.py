# Compute randomness
from definitions import digit_reduce, get_digits
from pprint import pprint
import matplotlib.pyplot as plt

if __name__ == '__main__':
    sums = (digit_reduce(sum(get_digits(i, 60)))%6 for i in range(0, 86400))

    results = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
    }

    for i in range(36000, 43200):
        sig = next(sums)
        results[sig] += 1

    numbers = 'Cero', 'Uno', 'Dos', 'Tres', 'Cuatro', 'Cinco'
    labels  = ['%s (%d)'%(numbers[i], results[i]) for i in range(6)]
    sizes   = [results[i] for i in range(6)]
    colors  = [
        '#e67e22',
        '#f1c40f',
        '#9b59b6',
        '#3498db',
        '#2ecc71',
        '#1dd2af',
    ]

    with plt.xkcd():
        fig = plt.figure()

        plt.pie(sizes,
            labels=labels,
            colors=colors,
            autopct='%1.2f%%',
            shadow=True,
            startangle=90
        )

        plt.axis('equal')

        fig.text(
            0.5,
            0.02,
            'Frecuencia de aparición de los módulos de 6, de 10 a 12 AM',
            ha='center',
            size='x-large',
        )

        plt.savefig("img/hora.png")

        plt.show()
