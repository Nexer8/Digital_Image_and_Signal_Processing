from skimage import io, filters
from matplotlib.pyplot import subplot, imshow, title, show, rcParams
from skimage.color import rgb2gray
rcParams['figure.figsize'] = [10, 10]

image = rgb2gray(io.imread('./Data/images/lenna_noisy.jpg'))  # high noise image

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
