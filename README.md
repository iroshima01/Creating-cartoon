Cartoon Effect Image Processing

Table of Contents
1-Overview
2-Dependencies
3-Methods
4-Usage
5-Parameters

#Overview
This Python script provides functions for applying a cartoon effect to an input image. The cartoon effect is achieved by combining edge detection, smoothing, and color quantization techniques.

#Dependencies
The script relies on the following Python libraries:

*NumPy
*Pillow (PIL)

To install the dependencies, use the following command:

pip install numpy pillow

#Methods

1. Image Smoothing (Gaussian Blur)

Applies Gaussian Blur to the input image.

    Parameters:
    - input_image: PIL Image object
    - sigma: Standard deviation of the Gaussian filter

    Returns:
    - Smoothed PIL Image

2. Edge Detection (Difference of Gaussian)

Applies edge detection using the Difference of Gaussian method.

    Parameters:
    - input_image: PIL Image object
    - sigma: Standard deviation of the Gaussian filter for smoothing
    - k: Factor for the second Gaussian filter
    - threshold: Threshold for binarizing the edge map

    Returns:
    - Edge-detected PIL Image

3. Image Quantization

Applies image quantization to the L (luminance) channel of the LAB color space.

    Parameters:
    - input_image: PIL Image object
    - divisor: Divisor for quantizing the L channel
    - multiplier: Multiplier for quantizing the L channel

    Returns:
    - Quantized RGB PIL Image

4. Combine Edge and Quantized Image

Combines the edge-detected image and quantized image to create a cartoon effect.

    Parameters:
    - edge_image: Edge-detected PIL Image
    - quantized_image: Quantized RGB PIL Image

    Returns:
    - Combined PIL Image

#Usage
final(image_path,edge_sigma_param, k_param, threshold_param)

for taking input of the images:
in this line of code final(r"../report/{folder}/{file}.jpg", 2.8,
0.35, 9) rename {folder} as data and file as the name of the image in the folder data, for example img1, img2.

And for changing the output image altering the parameters in the code which calls the final method is enough.

If you want to run the code and see how it gives output with different parameter values, there are quantized_image.save("quantized.jpg"), edges_image.save("edges.jpg"), cartoon_image.save("cartooned.jpg"), smoothed_image.save("smoothed.jpg") lines in my code which are saving the output images to the code folder.

#Parameters
edge_sigma_param: Standard deviation for edge detection (Difference of Gaussian)
k_param: Factor for the second Gaussian filter in edge detection
threshold_param: Threshold for binarizing the edge map



