import os
import skimage
from skimage import io, filters
from matplotlib.pyplot import subplot, imshow, title, show, rcParams
from skimage.color import rgb2gray
import numpy as np
rcParams['figure.figsize'] = [10, 10]

image = rgb2gray(io.imread(os.path.join(skimage.data_dir, 'chelsea.png')))

# a) Sobel filter usage
sobel = filters.sobel(image)

subplot(121), imshow(image, cmap='gray'), title('Original')
subplot(122), imshow(sobel, cmap='gray'), title('Filtered with Sobel filter')
show()

# Prewitt filter usage
prewitt = filters.prewitt(image)

subplot(121), imshow(image, cmap='gray'), title('Original')
subplot(122), imshow(prewitt, cmap='gray'), title('Filtered with Prewitt filter')
show()

# b) Sharpening with Laplacian
sharpened = np.clip(filters.laplace(image) + image, 0, 1)

subplot(121), imshow(image, cmap='gray'), title('Original')
subplot(122), imshow(sharpened, cmap='gray'), title('Sharpened with Laplacian')
show()
