import os
import skimage
from skimage import io
from matplotlib.pyplot import subplot, imshow, title, show, subplots_adjust

constant = 1.5
m = 0.45
e = 8
gamma = 0.67


def point_operation(img, method):
    for row in range(0, img.shape[0]):
        for col in range(0, img.shape[1]):
            temp = method(img[row][col])
            if temp > 255:
                img[row][col] = 255
            elif temp < 0:
                img[row][col] = 0
            else:
                img[row][col] = temp
    return img


def multiply(val):
    return val * constant


def change_dynamic_range(val):
    if val == 0:
        return 1
    else:
        return 1 / (1 + (m / val) ** e)


def gamma_correction(val):
    return constant * (val ** gamma)


image = io.imread(os.path.join(skimage.data_dir, 'camera.png'))

# a) mnożenie obrazu przez stałą T(r) = c * r, gdzie c jest stałą
multiplied1 = point_operation(image.copy(), multiply)

constant = 3.0
multiplied2 = point_operation(image.copy(), multiply)

constant = 0.02
multiplied3 = point_operation(image.copy(), multiply)

subplot(141), imshow(image, cmap='gray'), title('Original')
subplot(142), imshow(multiplied1, cmap='gray'), title('c=1.5')
subplot(143), imshow(multiplied2, cmap='gray'), title('c=3.0')
subplot(144), imshow(multiplied3, cmap='gray'), title('c=0.02')
show()

# b) Zmiana dynamiki skali szarości (kontrastu)
changed_dynamic1 = point_operation(image.copy(), change_dynamic_range)

m = 0.2
changed_dynamic2 = point_operation(image.copy(), change_dynamic_range)

m = 0.8
changed_dynamic3 = point_operation(image.copy(), change_dynamic_range)

m = 0.45
e = 2
changed_dynamic4 = point_operation(image.copy(), change_dynamic_range)

e = 12
changed_dynamic5 = point_operation(image.copy(), change_dynamic_range)

subplot(231), imshow(image, cmap='gray'), title('Original')
subplot(232), imshow(changed_dynamic1, cmap='gray'), title('m=0.45, e=8')
subplot(233), imshow(changed_dynamic2, cmap='gray'), title('m=0.2, e=8')
subplot(234), imshow(changed_dynamic3, cmap='gray'), title('m=0.8, e=8')
subplot(235), imshow(changed_dynamic4, cmap='gray'), title('m=0.45, e=2')
subplot(236), imshow(changed_dynamic5, cmap='gray'), title('m=0.45, e=12')

subplots_adjust(hspace=1.02)
show()

# c) Korekcja gamma
constant = 1.5
gamma_corrected1 = point_operation(image.copy(), gamma_correction)

gamma = 0.3
gamma_corrected2 = point_operation(image.copy(), gamma_correction)

gamma = 0.1
gamma_corrected3 = point_operation(image.copy(), gamma_correction)

subplot(141), imshow(image, cmap='gray'), title('Original')
subplot(142), imshow(gamma_corrected1, cmap='gray'), title('c=1.5, gamma=0.67')
subplot(143), imshow(gamma_corrected2, cmap='gray'), title('c=1.5, gamma=0.3')
subplot(144), imshow(gamma_corrected3, cmap='gray'), title('c=1.5, gamma=0.1')
show()
