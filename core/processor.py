import cv2
import numpy as np
from config import (
    TARGET_WIDTH, CANNY_LOW, CANNY_HIGH,
    MIN_CONTOUR_AREA, APPROX_EPSILON
)


def preprocess_image(image_path: str):
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f"Could not read image: {image_path}")

    img = _resize(img)
    gray = _to_gray(img)
    gray = _enhance_contrast(gray)
    gray = _denoise(gray)
    edges = _detect_edges(gray)
    edges = _morphological_cleanup(edges)

    return img, edges


def get_contours(edges) -> list:
    raw = _find_contours(edges)
    filtered = _filter_and_approximate(raw)
    filtered.sort(key=cv2.contourArea, reverse=True)
    return filtered

def _resize(img):
    h, w = img.shape[:2]
    scale = TARGET_WIDTH / float(w)
    new_h = int(h * scale)
    return cv2.resize(img, (TARGET_WIDTH, new_h), interpolation=cv2.INTER_LANCZOS4)


def _to_gray(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


def _enhance_contrast(gray):
    clahe = cv2.createCLAHE(clipLimit=2.5, tileGridSize=(8, 8))
    return clahe.apply(gray)


def _denoise(gray):
    return cv2.bilateralFilter(gray, d=7, sigmaColor=50, sigmaSpace=50)


def _detect_edges(gray):
    edges_canny = cv2.Canny(
        gray, CANNY_LOW, CANNY_HIGH,
        apertureSize=3, L2gradient=True
    )

    edges_adaptive = cv2.adaptiveThreshold(
        gray, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY_INV,
        blockSize=9,
        C=4
    )

    return cv2.bitwise_or(edges_canny, edges_adaptive)


def _morphological_cleanup(edges):
    k2 = np.ones((2, 2), np.uint8)
    edges = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, k2, iterations=1)
    edges = cv2.morphologyEx(edges, cv2.MORPH_OPEN,  k2, iterations=1)
    return edges


def _find_contours(edges):
    result = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_TC89_KCOS)
    return result[0] if len(result) == 2 else result[1]


def _filter_and_approximate(contours) -> list:
    filtered = []
    for contour in contours:
        area = cv2.contourArea(contour)
        if area < MIN_CONTOUR_AREA:
            continue

        epsilon = APPROX_EPSILON if area > 200 else APPROX_EPSILON * 0.6
        approx = cv2.approxPolyDP(contour, epsilon, closed=False)

        if len(approx) >= 2:
            filtered.append(approx)

    return filtered