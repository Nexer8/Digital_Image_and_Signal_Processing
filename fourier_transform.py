# Cyfrowe przetwarzanie sygnałów i obrazów
# Authors:  Mariusz Wiśniewski, 241393
#           Kinga Marek, 235280

import matplotlib.pyplot as plt
import numpy as np


# Ćwiczenie 2. Celem ćwiczenia jest praktyczne wypróbowanie funkcji numpy.fft
# i numpy.ifft do wyznaczania prostej i odwrotnej transformaty Fouriera [1, 3].

# TODO: Improve positions of labels and titles on plots
# TODO: Consider changing window title (maybe not necessary with jupyter)
# TODO: any ideas for making this code shorter on cleaner? :)

def main():

    # common variables used in exercises 1-5

    sample_length = 65536
    fs = 65536  # sampling frequency
    signal_duration = sample_length/fs
    time_step = 1/fs

    # 1. Wygeneruj ciąg próbek odpowiadający fali sinusoidalnej o częstotliwości 50 Hz
    # i długości 65536.

    frequency = 50  # set the frequency to 50 Hz
    x_axis = np.arange(0, signal_duration, time_step)
    y_axis = np.sin(2 * np.pi * frequency * x_axis)

    plt.subplot(211)
    plt.plot(x_axis, y_axis)
    plt.title('Signal')
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')

    # 2. Wyznacz dyskretną transformatę Fouriera tego sygnału i przedstaw jego widmo
    # amplitudowe na wykresie w zakresie częstotliwości [0, fs/2], gdzie fs oznacza
    # częstotliwość próbkowania.

    fft_freq = np.abs(np.fft.fftfreq(int(fs/2), time_step))
    fft_amplitude = np.abs(np.fft.fft(y_axis[0:fft_freq.size]))

    plt.subplot(212)
    plt.plot(fft_freq, fft_amplitude)
    plt.title('Signal frequency spectrum')
    plt.xlabel('Frequency [Hz]')
    plt.ylabel('Amplitude')
    plt.show()

    # 3. Wygeneruj ciąg próbek mieszaniny dwóch fal sinusoidalnych
    # (tzn. ich kombinacjiliniowej) o częstotliwościach 50 i 60 Hz.
    # Wykonaj zadanie z punktu 2 dla tego sygnału.

    frequency_1 = 50
    frequency_2 = 60

    time_samples = np.arange(0, signal_duration, time_step)
    sample_1 = np.sin(2 * np.pi * frequency_1 * time_samples)
    sample_2 = np.sin(2 * np.pi * frequency_2 * time_samples)
    samples_sum = sample_1 + sample_2

    plt.subplot(411)
    plt.plot(time_samples, sample_1)
    plt.title('Frequency {} Hz'.format(frequency_1))
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')

    plt.subplot(412)
    plt.plot(time_samples, sample_2)
    plt.title('Frequency {} Hz'.format(frequency_2))
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')

    plt.subplot(413)
    plt.plot(time_samples, samples_sum)
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')

    fft_freq = np.abs(np.fft.fftfreq(int(fs/2), time_step))
    fft_amplitude = np.abs(np.fft.fft(samples_sum[0:fft_freq.size]))

    plt.subplot(414)
    plt.plot(fft_freq, fft_amplitude)
    plt.xlabel('Frequency [Hz]', labelpad=5)
    plt.ylabel('Amplitude')

    plt.show()

    # 4. Powtórz eksperymenty dla różnych czasów trwania sygnałów,
    # tzn. dla różnych częstotliwości próbkowania.

    def get_signal_duration(f_s):
        return sample_length/f_s

    def get_time_step(f_s):
        return 1/f_s

    def create_x_axis(f_s):
        return np.arange(0, get_signal_duration(f_s), get_time_step(f_s))

    def create_y_axis(freq, x):
        y = np.zeros(x.size)
        for f in freq:
            y += np.sin(2 * np.pi * f * x)
        return y

    fs = [50, 100, 500, 10000]
    signals_frequencies = [[50], [50, 100], [50, 100, 200]]

    for signals_freq in signals_frequencies:
        fft_freq = np.abs(np.fft.fftfreq(int(fs[0] / 2), get_time_step(fs[0])))
        signal_amplitude = create_x_axis(fs[0])
        fft_amplitude = np.abs(np.fft.fft(create_y_axis(signals_freq, signal_amplitude)[0:fft_freq.size]))

        plt.subplot(411)
        plt.plot(fft_freq, fft_amplitude)
        plt.title('Fs {} Hz'.format(fs[0]))
        plt.xlabel('Frequency [Hz]', labelpad=5)
        plt.ylabel('Amplitude')

        fft_freq = np.abs(np.fft.fftfreq(int(fs[1] / 2), get_time_step(fs[1])))
        signal_amplitude = create_x_axis(fs[1])
        fft_amplitude = np.abs(np.fft.fft(create_y_axis(signals_freq, signal_amplitude)[0:fft_freq.size]))

        plt.subplot(412)
        plt.plot(fft_freq, fft_amplitude)
        plt.title('Fs {} Hz'.format(fs[1]))
        plt.xlabel('Frequency [Hz]', labelpad=5)
        plt.ylabel('Amplitude')

        fft_freq = np.abs(np.fft.fftfreq(int(fs[2] / 2), get_time_step(fs[2])))
        signal_amplitude = create_x_axis(fs[2])
        fft_amplitude = np.abs(np.fft.fft(create_y_axis(signals_freq, signal_amplitude)[0:fft_freq.size]))

        plt.subplot(413)
        plt.plot(fft_freq, fft_amplitude)
        plt.title('Fs {} Hz'.format(fs[2]))
        plt.xlabel('Frequency [Hz]', labelpad=5)
        plt.ylabel('Amplitude')

        fft_freq = np.abs(np.fft.fftfreq(int(fs[3] / 2), get_time_step(fs[3])))
        signal_amplitude = create_x_axis(fs[3])
        fft_amplitude = np.abs(np.fft.fft(create_y_axis(signals_freq, signal_amplitude)[0:fft_freq.size]))

        plt.subplot(414)
        plt.plot(fft_freq, fft_amplitude)
        plt.title('Fs {} Hz'.format(fs[3]))
        plt.xlabel('Frequency [Hz]', labelpad=5)
        plt.ylabel('Amplitude')

        plt.show()

    # 5. Wyznacz odwrotne transformaty Fouriera ciągów wyznaczonych w zadaniu 2
    # i porównaj z ciągami oryginalnymi.
    fs = 65536

    # for signal in ex 1. - 50Hz

    fft_freq = np.abs(np.fft.fftfreq(int(fs/2), time_step))
    fft_amplitude = np.abs(np.fft.fft(y_axis[0:fft_freq.size]))

    plt.subplot(311)
    plt.plot(x_axis[0:fft_freq.size], y_axis[0:fft_freq.size])
    plt.title('Signal')
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')

    plt.subplot(312)
    plt.plot(fft_freq, fft_amplitude)
    plt.title('Signal frequency spectrum')
    plt.xlabel('Frequency [Hz]')
    plt.ylabel('Amplitude')

    inv_samples_sum = np.fft.ifft(fft_amplitude)

    plt.subplot(313)
    plt.plot(x_axis[0:inv_samples_sum.size], inv_samples_sum)
    plt.title('Signal after inverse fourier transform')
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')
    plt.show()

    # for signal in ex 2. - 50Hz + 60Hz

    fft_amplitude = np.abs(np.fft.fft(samples_sum[0:fft_freq.size]))

    plt.subplot(311)
    plt.plot(time_samples[0:fft_freq.size], samples_sum[0:fft_freq.size])
    plt.title('Signal')
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')

    plt.subplot(312)
    plt.plot(fft_freq, fft_amplitude)
    plt.title('Signal frequency spectrum')
    plt.xlabel('Frequency [Hz]')
    plt.ylabel('Amplitude')

    inv_samples_sum = np.fft.ifft(fft_amplitude)

    plt.subplot(313)
    plt.plot(time_samples[0:inv_samples_sum.size], inv_samples_sum)
    plt.title('Signal after inverse fourier transform')
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')
    plt.show()

if __name__ == "__main__":
    main()
