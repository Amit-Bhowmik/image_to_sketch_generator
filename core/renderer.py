import random
import turtle
import cv2

from config import (
    SCREEN_W, SCREEN_H,
    POINT_SKIP, PENCIL_JITTER, TRACER_N
)


def setup_turtle():
    screen = turtle.Screen()
    screen.title("Image to Sketch Converter")
    screen.setup(width=SCREEN_W, height=SCREEN_H)
    screen.bgcolor("white")
    screen.tracer(0, 0)     

    pen = turtle.Turtle(visible=False)
    pen.speed(0)
    pen.pensize(1)
    pen.color("black")
    pen.penup()

    return screen, pen


def draw_contours(screen, pen, contours: list, img_shape: tuple) -> None:
    img_h, img_w = img_shape[:2]
    draw_scale = _fit_scale(img_w, img_h)
    move_count = 0

    for contour in contours:
        points = contour[::POINT_SKIP]
        if len(points) < 2:
            continue

        pen.pensize(_pen_width(cv2.contourArea(contour)))
        sx, sy = points[0][0]
        tx, ty = _to_screen(sx, sy, img_w, img_h, draw_scale)
        pen.penup()
        pen.goto(_jitter(tx), _jitter(ty))
        pen.pendown()

        for point in points[1:]:
            x, y = point[0]
            tx, ty = _to_screen(x, y, img_w, img_h, draw_scale)
            pen.goto(_jitter(tx), _jitter(ty))
            move_count += 1

            if move_count % TRACER_N == 0:
                screen.update()

        pen.penup()

    screen.update()

def _fit_scale(img_w: int, img_h: int) -> float:
    return min((SCREEN_W - 80) / img_w, (SCREEN_H - 80) / img_h)


def _to_screen(x, y, img_w, img_h, scale) -> tuple:
    tx = (x - img_w / 2) * scale
    ty = (img_h / 2 - y) * scale
    return tx, ty


def _jitter(value: float) -> float:
    if PENCIL_JITTER > 0:
        return value + random.uniform(-PENCIL_JITTER, PENCIL_JITTER)
    return value


def _pen_width(area: float) -> float:
    if area > 5000:
        return 1.2
    if area > 500:
        return 1.0
    return 0.8