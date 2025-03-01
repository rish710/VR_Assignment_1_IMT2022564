import cv2
import matplotlib.pyplot as plt
import os

# Define image paths
image_paths = [
    'unstitched_images/left.png', 
    'unstitched_images/middle.png', 
    'unstitched_images/right.png'
]

# Create a directory to save keypoint images
output_dir = "keypoints_output"
os.makedirs(output_dir, exist_ok=True)

print("Detecting and displaying keypoints...")

# Detect and display keypoints for each image using ORB
orb = cv2.ORB_create()

for img_path in image_paths:
    image = cv2.imread(img_path)

    if image is None:
        print(f"Error: Could not read image {img_path}. Check the file path.")
        continue

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    keypoints, _ = orb.detectAndCompute(gray, None)

    # Draw only small red dots at keypoints
    img_with_keypoints = image.copy()
    for kp in keypoints:
        x, y = int(kp.pt[0]), int(kp.pt[1])
        cv2.circle(img_with_keypoints, (x, y), 2, (0, 0, 255), -1)  # Red dot

    # Convert BGR to RGB for Matplotlib display
    img_rgb = cv2.cvtColor(img_with_keypoints, cv2.COLOR_BGR2RGB)

    # Save the keypoint image
    filename = os.path.basename(img_path).split('.')[0] + "_keypoints.png"
    save_path = os.path.join(output_dir, filename)
    cv2.imwrite(save_path, img_with_keypoints)
    print(f"Saved keypoint image: {save_path}")

    # Display the image
    plt.figure(figsize=(6, 6))
    plt.imshow(img_rgb)
    plt.axis("off")
    plt.show()

print("Stitching images into a panorama...")

# Read images
images = [cv2.imread(img) for img in image_paths]

# Ensure all images were loaded successfully
if any(img is None for img in images):
    print("Error: One or more images could not be read. Check file paths.")
else:
    stitcher = cv2.Stitcher_create()
    status, panorama = stitcher.stitch(images)

    if status == cv2.Stitcher_OK:
        cv2.imwrite("panorama.png", panorama)
        panorama_rgb = cv2.cvtColor(panorama, cv2.COLOR_BGR2RGB)

        plt.figure(figsize=(10, 5))
        plt.imshow(panorama_rgb)
        plt.axis("off")
        plt.title("Stitched Panorama")
        plt.show()
    else:
        print("Stitching failed!")
