import cv2 as cv
from matplotlib import pyplot as plt
import argparse


### OpenCV global variables
lower_threshold = 100
ratio = 3
kernel_size = 3
blur_type = "gaussian"
blur_intensity = 5


### Image global variables
image_selected = "./images/lion.jpg"


### Argparse Definition
parser = argparse.ArgumentParser(
                    prog='Monet Maker',
                    description='Monet Marker takes an images to redraw it using OpenCV functions')


### Plt Definition
plt.rcParams['toolbar'] = 'None'
plt.axis('off')


### Functions
def setup_argparse_parameters():
    '''Setup all program arguments
    using argparse'''
    parser.add_argument("-l", "--lower", help="Define lower threshold",
                    type=int)
    parser.add_argument("-r", "--ratio", help="Define ratio",
                    type=int)
    parser.add_argument("-n", "--name", help="Image name from images path",
                    type=str)
    parser.add_argument("-b", "--blur", help="Blur type for detailed images",
                    choices=["gaussian", "classic", "median"])
    parser.add_argument("-bi", "--bintensity", help="Blur intensity for detailed images",
                    type=int)


def setup_globals_from_arguments():
    '''Use program argument from argparse
    to replace default global values'''
    args = parser.parse_args()
    if args.lower is not None:
        global lower_threshold
        lower_threshold = args.lower
    if args.ratio is not None:
        global ratio
        ratio = args.ratio
    if args.name is not None:
        global image_selected
        image_selected = args.name
    if args.blur is not None:
        global blur_type
        blur_type = args.blur
    if args.bintensity is not None:
        global blur_intensity
        blur_intensity = args.bintensity
        if blur_intensity % 2 == 0:
            print("Error, blur intensity needs to be an odd number.")
            exit()
        
        
        
        
def apply_blur(img):
    '''Takes image as param and apply OpenCV Blur'''
    if blur_type == "classic":
        img = cv.blur(img , (blur_intensity , blur_intensity))
    elif blur_type == "gaussian":
        img = cv.GaussianBlur(img, (blur_intensity , blur_intensity) , 0)
    elif blur_type == "median":
        img = cv.medianBlur(img , blur_intensity)
    return img
        

def get_invert_threshold(canny_img):
    '''Take Canny mask as parameter
    Returns image with inverted threshold'''
    ret, tresh = cv.threshold(canny_img, lower_threshold , lower_threshold * ratio, cv.THRESH_BINARY_INV)
    return tresh


def get_img_outlines_with_binary_threshold():
    '''Take an image as parameter and return
    outlines from this image after Canny, Threshold treatment'''
    img = cv.imread(image_selected , cv.IMREAD_GRAYSCALE)
    assert img is not None, "file could not be read, check with os.path.exists()"
    img = apply_blur(img)
    img_canny = cv.Canny(img, lower_threshold , lower_threshold * ratio, kernel_size)
    return get_invert_threshold(img_canny)


### Program run
setup_argparse_parameters()
setup_globals_from_arguments()

result = get_img_outlines_with_binary_threshold()

plt.imshow(result, cmap='gray')
plt.show()