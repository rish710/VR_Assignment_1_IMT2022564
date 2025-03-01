#  Visual Recognition Assignment 1  
This assignment involves detecting, segmenting, and counting Indian coins using edge detection and region-based segmentation. Additionally, it requires extracting key points and stitching multiple overlapping images into a panorama.


### Rishit Mane - IMT2022564  

## 📌 Overview  
This repository contains solutions for Computer Vision Assignment 1, which consists of two main tasks:  
1. **Coin Detection and Segmentation** – Detecting, segmenting, and counting Indian coins in an image.  
2. **Image Stitching** – Creating a stitched panorama from multiple overlapping images.  

All implementations are in **Python**.  

---

## 📂 Repository Structure  

```
VR_Assignment1_IMT2022564/
│── Q1/                                         # Folder for Coin Detection and Segmentation
│   │── Q1_IMT2022564.py                        # Python script for coin detection
│   │── coin.png                                # Python script for coin detection
│   │── Coin_Detection_Result.jpg               # Final detected coin image with count
│   │── Edge_Detection_Result.jpg               # Image after edge detection
│   │── Segmentation_Result.jpg                 # Image after segmentation
│
│── Q2/                                         # Folder for Image Stitching
│   │── Q2_IMT2022564.py                    # Python script for image stitching
│   │── unstitched_images/                       # Folder containing input images for stitching
│   │── keypoints_output/                 # Folder with keypoints detected in the images
│   │── panorama.png             # Final processed stitched image
│
│── README.md                                   # Project documentation

```

---

## 🛠️ Dependencies  
Ensure the following Python packages are installed before running the scripts:  

```bash
pip install opencv-python numpy matplotlib imutils
```

---

## 🔧 Execution Instructions  
Run each script separately from the terminal or command prompt.  

### **1️⃣ Coin Detection and Segmentation**  
```bash
python Q1.py
```
**Expected Outputs:**  
- `Edge_Detection_Output.jpg` (Edges detected in the coin image)  
- `Segmentation_Output.jpg` (Segmented coins)  
- `Coin_Detection_Output.jpg` (Final output with detected coins and total count)  

### **2️⃣ Image Stitching (Panorama Creation)**  
```bash
python Q2.py
```
**Expected Outputs:**  
- `keypoints_output` (Folder with keypoints detected in the images)  
- `panorama.png` (Final processed stitched output)  

---

## 📊 Methodology  

### **Part 1: Coin Detection and Segmentation**  
#### 🔹 **Steps Followed:**  
1. Convert the image to grayscale.  
2. Apply Gaussian blur to remove noise.  
3. Use **Otsu’s Thresholding** to segment coins from the background.  
4. Apply **morphological operations** to refine segmentation.  
5. Use **Canny Edge Detection** to detect coin boundaries.  
6. Find **contours** of coins and fit **minimum enclosing circles**.  
7. Count the total coins detected and overlay the count on the final output.  

#### 📌 **Observations:**  
- Edge detection works well but introduces noise.  
- Otsu’s thresholding effectively isolates coins but may over-segment due to similar background intensities.  
- The final detection correctly identifies and counts coins, demonstrating robustness.  

---

### **Part 2: Image Stitching**  
#### 🔹 **Steps Followed:**  
1. Load multiple overlapping images.  
2. Use **ORB Feature Detector** to extract keypoints and descriptors.  
3. Match keypoints across images.  
4. Use OpenCV’s **Stitcher class** to align and merge images into a panorama.  
5. Remove black borders from the final stitched image.  

#### 📌 **Observations:**  
- **Keypoint Detection Efficiency**: ORB effectively detects keypoints but struggles in low-texture regions.  
- **Stitching Accuracy**: Works well when images have sufficient overlap.  
- **Challenges Encountered**:  
  - Poor keypoint matching can lead to misalignment.  
  - Lighting variations cause visible seams.  
- **Potential Improvements**: Using multi-band blending can enhance seamless transitions.  

---


## 🎯 Conclusion  
This project successfully demonstrates the use of **Computer Vision** techniques for:  
- **Object detection and segmentation** (Coin detection).  
- **Feature matching and image stitching** (Panorama generation).  

The methods used provide accurate results, though further improvements like **multi-band blending** for seamless stitching can be explored.  

---

## 📝 Author  
**Rishit Mane**  
IMT2022564  
