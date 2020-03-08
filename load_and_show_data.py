# Cyfrowe przetwarzanie sygnałów i obrazów
# Author: Mariusz Wiśniewski, 241393

import matplotlib.pyplot as plt
import numpy as np


def load_and_show_data():
    ecg_data = [[] for i in range(12)]
    frequency = 800  # set the frequency to 800 Hz

    data = np.loadtxt("Data/ekg1.txt", delimiter=" ")
    for row in data:
        for i, ecg in enumerate(ecg_data):
            ecg.append(row[i])

    time = (
        np.arange(len(ecg_data[0])) / frequency
    )  # Create a set of time measurements

    for i, ecg in enumerate(ecg_data):
        plt.plot(time, ecg)
        plt.xlabel("time [s]")
        plt.ylabel("ECG [mV]")
        plt.xlim(0, 0.1)  # select just a part of x axis to render
        plt.ylim(0, 200)  # select just a part of y axis to render
        plt.savefig(f"Results/graph{i}.png")
        # plt.show()


def main():
    load_and_show_data()


if __name__ == "__main__":
    main()
