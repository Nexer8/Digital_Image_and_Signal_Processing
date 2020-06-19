import os
import skimage
from skimage import io, filters
from matplotlib.pyplot import subplot, imshow, title, show, rcParams
rcParams['figure.figsize'] = [10, 10]

image = io.imread(os.path.join(skimage.data_dir, 'grass.png'))  # low contrast image

# a) averaging filters
gaussian3 = filters.gaussian(image, sigma=3)
gaussian5 = filters.gaussian(image, sigma=5)
gaussian7 = filters.gaussian(image, sigma=7)

subplot(141), imshow(image, cmap='gray'), title('Original')
subplot(142), imshow(gaussian3, cmap='gray'), title('Gaussian, sigma=3')
subplot(143), imshow(gaussian5, cmap='gray'), title('Gaussian, sigma=5')
subplot(144), imshow(gaussian7, cmap='gray'), title('Gaussian, sigma=7')
show()

# b) median filter
median = filters.median(image)

subplot(121), imshow(image, cmap='gray'), title('Original')
subplot(122), imshow(median, cmap='gray'), title('Median filter applied')
show()
