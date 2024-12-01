import random
import cv2 as cv
import argparse
import turtle
from matplotlib import pyplot as plt
from scipy.spatial import KDTree
import numpy


### OpenCV global variables
lower_threshold = 100
ratio = 3
kernel_size = 3
blur_type = "none"
blur_intensity = 1
pixer_render_number = 4
cluster_number = 8
list_color_centers = []
list_pixel_cluster = []


### Image global variables
image_selected = "./images/licorne.png"


### Argparse Definition
parser = argparse.ArgumentParser(
    prog="Monet Maker",
    description="Monet Marker takes an images to redraw it using OpenCV functions",
)


### Functions
def setup_argparse_parameters():
    """Setup all program arguments
    using argparse"""
    parser.add_argument("-l", "--lower", help="Define lower threshold", type=int)
    parser.add_argument("-r", "--ratio", help="Define ratio", type=int)
    parser.add_argument("-n", "--name", help="Image name from images path", type=str)
    parser.add_argument(
        "-b",
        "--blur",
        help="Blur type for detailed images",
        choices=["gaussian", "classic", "median"],
    )
    parser.add_argument(
        "-bi", "--bintensity", help="Blur intensity for detailed images", type=int
    )
    parser.add_argument(
        "-p", "--pixel", help="Number pixel to render at a time", type=int
    )
    parser.add_argument(
        "-c", "--color", help="Define color number", type=int
    )


def setup_globals_from_arguments():
    """Use program argument from argparse
    to replace default global values"""
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
    if args.color is not None:
        global cluster_number
        cluster_number = args.color
    if args.pixel is not None:
        global pixer_render_number
        pixer_render_number = args.pixel


def apply_blur(img):
    """Takes image as param and apply OpenCV Blur"""
    if blur_type == "classic":
        img = cv.blur(img, (blur_intensity, blur_intensity))
    elif blur_type == "gaussian":
        img = cv.GaussianBlur(img, (blur_intensity, blur_intensity), 0)
    elif blur_type == "median":
        img = cv.medianBlur(img, blur_intensity)
    return img


def get_invert_threshold(canny_img):
    """Take Canny mask as parameter
    Returns image with inverted threshold"""
    ret, tresh = cv.threshold(
        canny_img, lower_threshold, lower_threshold * ratio, cv.THRESH_BINARY_INV
    )
    return tresh


def get_img_outlines_with_binary_threshold():
    """Take an image as parameter and return
    outlines from this image after Canny, Threshold treatment"""
    img = cv.imread(image_selected, cv.IMREAD_GRAYSCALE)
    assert img is not None, "file could not be read, check with os.path.exists()"
    img = apply_blur(img)
    img_canny = cv.Canny(img, lower_threshold, lower_threshold * ratio, kernel_size)
    return get_invert_threshold(img_canny)


def setup_gui():
    """Setup Turtle settings for GUI"""
    screen = turtle.Screen()
    screen.setup(width, height)
    screen.setworldcoordinates(0, 0, width, height)
    turtle.hideturtle()
    turtle.colormode(255)
    turtle.speed(0)
    turtle.tracer(0)

def draw_humanized_tree(kdtree, points , colors):
    """Draw line by line image, using k-d tree and NNS from scipy"""
    turtle.penup()

    start_idx = random.randint(0, len(points) - 1)
    start_point = points[start_idx]
    turtle.goto(start_point[0], height - start_point[1])
    turtle.dot(1 , (colors[0] , colors[1] , colors[2]))

    remaining_points = set(range(len(points)))
    remaining_points.remove(start_idx)

    current_point = start_point

    pixel_count = 0

    while remaining_points:
        _, indices = kdtree.query([current_point], len(points))

        nearest_idx = None
        for idx in indices[0]:
            if idx in remaining_points:
                nearest_idx = idx
                break

        nearest_point = points[nearest_idx]
        turtle.goto(nearest_point[0], height - nearest_point[1])
        turtle.dot(1 , (colors[0] , colors[1] , colors[2]))

        pixel_count += 1

        if pixel_count == pixer_render_number:
            pixel_count = 0
            turtle.update()
            turtle.tracer(0)

        current_point = nearest_point
        remaining_points.remove(nearest_idx)


def list_color():
    global list_color_centers
    global list_pixel_cluster
    result_color = cv.imread(image_selected)
    result_color = cv.cvtColor(result_color, cv.COLOR_BGR2RGB)
    result_color = apply_blur(result_color)
    pixel_values = result_color.reshape((-1, 3))
    pixel_values = numpy.float32(pixel_values)
    criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 100, 0.2)
    k = cluster_number
    _, labels, (centers) = cv.kmeans(pixel_values, k, None, criteria, 10, cv.KMEANS_RANDOM_CENTERS)
    centers = numpy.uint8(centers)
    labels = labels.flatten()
    segmented_image = centers[labels.flatten()]
    segmented_image = segmented_image.reshape(result_color.shape)
    list_color_centers = centers
    list_pixel_cluster = segmented_image

def color_coords(list_pixels):
    global currenth
    currentw = width
    currenth = height
    img_coor = []
    for rows in list_pixels:
        currentw = width
        for pixel in rows:
            tmp = [-currentw + width , -currenth + height, pixel[0] , pixel[1] , pixel[2]]
            img_coor.append(tmp)
            currentw -= 1
        currenth -= 1
    return img_coor


### Program run
setup_argparse_parameters()
setup_globals_from_arguments()

result = get_img_outlines_with_binary_threshold()
height, width = result.shape

setup_gui()

black_pixels = [
    (x, y) for x in range(width) for y in range(height) if result[y, x] == 0
]

kdtree = KDTree(black_pixels)
list_points = kdtree.data.tolist()
draw_humanized_tree(kdtree , list_points , [0, 0,0])

list_color()
img_coor = color_coords(list_pixel_cluster)
pixels = []
for x in list_color_centers:
    pixels = []
    if x[0] <= 240 and x[1] <= 240 and x[2] <= 240:
        for y in img_coor:
            if y[2] == x[0] and y[3] == x[1] and y[4] == x[2]:
                pixels.append([y[0] , y[1]])
        kdtree = KDTree(pixels)
        list_points = kdtree.data.tolist() 
        draw_humanized_tree(kdtree, list_points , x)
turtle.done()
    