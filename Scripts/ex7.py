import os
import skimage
from skimage import io
from matplotlib.pyplot import subplot, imshow, title, show, savefig, hist, subplots_adjust
from skimage.exposure import equalize_hist
import numpy as np

low_contrast_image = io.imread(os.path.join(skimage.data_dir, 'moon.png'))   # low contrast image
high_contrast_image = io.imread('./Data/images/too_bright.png')   # high contrast image

low_contrast_equalized = np.asarray(equalize_hist(low_contrast_image) * 255, dtype='uint8')
high_contrast_equalized = np.asarray(equalize_hist(high_contrast_image) * 255, dtype='uint8')


subplot(241), imshow(low_contrast_image, cmap='gray'), title('Low contrast image')
subplot(242), hist(low_contrast_image.flatten(), 256, range=(0, 256))

subplot(243), imshow(high_contrast_image, cmap='gray'), title('High contrast image')
subplot(244), hist(high_contrast_image.flatten(), 256, range=(0, 256))

subplot(245), imshow(low_contrast_equalized, cmap='gray'), title('Equalized contrast')
subplot(246), hist(low_contrast_equalized.flatten(), 256, range=(0, 256))

subplot(247), imshow(high_contrast_equalized, cmap='gray'), title('Equalized contrast')
subplot(248), hist(high_contrast_equalized.flatten(), 256, range=(0, 256))

subplots_adjust(hspace=1.02)
show()
