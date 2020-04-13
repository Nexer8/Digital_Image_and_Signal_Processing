# Cyfrowe przetwarzanie sygnałów i obrazów
# Authors:  Mariusz Wiśniewski, 241393
#           Kinga Marek, 235280

import matplotlib.pyplot as plt
import numpy as np


# Ćwiczenie 2. Celem ćwiczenia jest praktyczne wypróbowanie funkcji numpy.fft
# i numpy.ifft do wyznaczania prostej i odwrotnej transformaty Fouriera [1, 3].


def main():
    # 1. Wygeneruj ciąg próbek odpowiadający fali sinusoidalnej o częstotliwości 50 Hz
    # i długości 65536.

    frequency = 50  # set the frequency to 50 Hz
    sample_length = 65536
    fs = 65536  # sampling frequency

    x_axis = np.arange(sample_length)
    y_axis = np.sin(2 * np.pi * frequency * x_axis / fs)
    plt.plot(x_axis, y_axis)
    plt.xlabel('sample(n)')
    plt.ylabel('voltage(V)')
    plt.show()

    # 2. Wyznacz dyskretną transformatę Fouriera tego sygnału i przedstaw jego widmo
    # amplitudowe na wykresie w zakresie częstotliwości [0, fs/2], gdzie fs oznacza
    # częstotliwość próbkowania.

    # Część poniżej jest prawdopodobnie nieprawidłowa
    lower_bound = 1
    upper_bound = 3
    spacing = (upper_bound - lower_bound) / sample_length

    time = np.arange(lower_bound, upper_bound, spacing)
    amplitude = y_axis

    sp = np.fft.fft(y_axis)
    freq = np.fft.fftfreq(amplitude.shape[-1])
    plt.plot(freq, sp.real, freq, sp.imag)
    plt.show()


if __name__ == "__main__":
    main()
