import os
import sys
import cv2
from yolov5_hse.demo import detect_image, save_image

from yolov5_hse import __version__


def test_version():
    assert __version__ == "0.1.0"


sys.path.append("../")

root_dir = os.path.dirname(__file__)
weights = root_dir + "/model_float16_quant.tflite"
img_path = root_dir + "/image_test.jpeg"
img_small = root_dir + "/image_test_small.jpeg"
img_big = root_dir + "/image_test_big.jpeg"
class_names = root_dir + "/class_names.txt"


def test_image_regression():
    """visual regression test checks that we'll always get the same result"""

    duplicate_result = detect_image(weights, img_path, 416, 0.25, 0.45, class_names)
    save_image(img_path, duplicate_result)
    original_result = cv2.imread(
        "tests/original_image_result.jpg", cv2.IMREAD_GRAYSCALE
    )
    duplicate_result = cv2.imread(
        "tests/image_testyolov5_output.jpg", cv2.IMREAD_GRAYSCALE
    )
    difference = cv2.subtract(original_result, duplicate_result)
    assert cv2.countNonZero(difference) == 0


def test_big_small():
    """We should be sure that our algorithm works without
    any errors with the images of different sizes"""
    detect_image(weights, img_small, 416, 0.25, 0.45, class_names)
    detect_image(weights, img_big, 416, 0.25, 0.45, class_names)
