# Cyfrowe przetwarzanie sygnałów i obrazów
# Authors:  Mariusz Wiśniewski, 241393
#           Kinga Marek, 235280

# Ćwiczenie 1. Napisz skrypt w Pythonie/Matlabie umożliwiający wczytywanie i wizualizację badanych sygnałów.
# Program powinien umożliwiać obserwowanie wycinka sygnału dla zadanego przedziału czasowego, skalowanie osi
# wykresów i ich opis oraz zapis dowolnego wycinka sygnału do pliku o podanej nazwie.

import matplotlib.pyplot as plt
import numpy as np


def load_and_show_data():
    ecg_data = [[] for i in range(12)]
    frequency = 1000  # set the frequency to 1000 Hz

    data = np.loadtxt("Data/ekg1.txt", delimiter=" ")
    for row in data:
        for i, ecg in enumerate(ecg_data):
            ecg.append(row[i])

    time = np.arange(len(ecg_data[0])) / frequency  # Create a set of time measurements

    for i, ecg in enumerate(ecg_data):
        plt.plot(time, ecg)
        plt.xlabel("time [s]")
        plt.ylabel("ECG [mV]")
        # plt.xlim(0, 0.1)  # select just a part of x axis to render
        # plt.ylim(0, 200)  # select just a part of y axis to render
        plt.savefig(f"Results/graph{i}.png")
        plt.show()


def main():
    load_and_show_data()


if __name__ == "__main__":
    main()
