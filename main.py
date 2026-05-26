from ui.dialogs import *
from core.processor import *
from core.renderer import *
import cv2
import turtle


def main():
    image_path = choose_image_file()

    if not image_path:
        show_info("No file selected", "You did not choose any image.")
        return

    try:
        img, edges = preprocess_image(image_path)
        contours = get_contours(edges)

        print(f"[Info] Image size : {img.shape[1]}×{img.shape[0]} px")
        print(f"[Info] Contours   : {len(contours)} shapes to draw")

        cv2.imwrite("sketch_edges_preview.png", edges)

        screen, pen = setup_turtle()
        draw_contours(screen, pen, contours, img.shape)

        show_info(
            "Done!",
            f"Sketch completed!\n\n"
            f"• {len(contours)} contours drawn\n"
            f"• Edge preview saved as: sketch_edges_preview.png"
        )

        turtle.done()

    except Exception as e:
        show_error("Error", f"Something went wrong:\n{e}")


if __name__ == "__main__":
    main()