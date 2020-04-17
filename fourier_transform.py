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
    signal_duration = sample_length/fs
    time_step = 1/fs

    x_axis = np.arange(0, signal_duration, time_step)
    y_axis = np.sin(2 * np.pi * frequency * x_axis)

    plt.subplot(211)
    plt.plot(x_axis, y_axis)
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')

    # 2. Wyznacz dyskretną transformatę Fouriera tego sygnału i przedstaw jego widmo
    # amplitudowe na wykresie w zakresie częstotliwości [0, fs/2], gdzie fs oznacza
    # częstotliwość próbkowania.

    amplitude = np.abs(np.fft.fft(y_axis))
    frequencies = np.fft.fftfreq(y_axis.size, time_step)

    plt.subplot(212)
    plt.plot(frequencies, amplitude)
    plt.show()


if __name__ == "__main__":
    main()
