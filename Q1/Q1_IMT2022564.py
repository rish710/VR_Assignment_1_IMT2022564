import cv2
import numpy as np
import matplotlib.pyplot as plt

def load_image(image_path):
    # Loads an image from a given path.
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Image not loaded. Check the file path or ensure the image exists.")
        exit()
    print("Image loaded successfully.")
    return image

def preprocess_image(image):
    # Converts image to grayscale, applies Gaussian blur, and thresholding.
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (15, 15), 7)
    # Apply Otsu's thresholding for segmentation
    _, binary = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    return binary

def refine_segmentation(binary):
    # Applies morphological operations to refine segmentation.
    kernel = np.ones((3, 3), np.uint8)
    return cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel, iterations=2)

def detect_edges(binary):
    # Applies edge detection.
    return cv2.Canny(binary, 100, 200)

def detect_coins(image, binary):
    # Finds contours and detects coins in the image.
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    output = image.copy()
    coin_count = 0

    for contour in contours:
        if cv2.contourArea(contour) > 300:
            coin_count += 1
            (x, y), radius = cv2.minEnclosingCircle(contour)
            center, radius = (int(x), int(y)), int(radius)
            cv2.circle(output, center, radius, (0, 255, 0), 2)

    cv2.putText(output, f"Coins: {coin_count}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
    return output, coin_count

def save_results(edges, binary, output):
    # Saves the processed images
    cv2.imwrite("Edge_Detection_Result.jpg", edges)
    cv2.imwrite("Segmentation_Result.jpg", binary)
    cv2.imwrite("Coin_Detection_Result.jpg", output)

def display_results(edges, binary, output, coin_count):
    # Displays images using OpenCV and Matplotlib
    cv2.imshow("Edge Detection", edges)
    cv2.imshow("Segmentation", binary)
    cv2.imshow("Coin Detection", output)
    
    rgb_output = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)
    plt.imshow(rgb_output)
    plt.title(f"Detected Coins: {coin_count}")
    plt.axis("off")
    # plt.show()

    cv2.waitKey(0)
    cv2.destroyAllWindows()

image_path = "coin.png"
image = load_image(image_path)
binary = preprocess_image(image)
binary = refine_segmentation(binary)
edges = detect_edges(binary)
output, coin_count = detect_coins(image, binary)
save_results(edges, binary, output)
display_results(edges, binary, output, coin_count)
