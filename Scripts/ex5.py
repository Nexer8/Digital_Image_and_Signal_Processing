import os
import skimage
from skimage import io, img_as_uint
from matplotlib.pyplot import imshow, title, show, savefig

image = io.imread(os.path.join(skimage.data_dir, 'coins.png'))

imshow(image, cmap='gray'), title('Original image')
io.imsave('./Data/images/' + 'coins.png', img_as_uint(image))    # save the image
savefig('./Data/images/' + 'coins_fig.png')     # save the figure
show()
