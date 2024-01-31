import numpy as np
from PIL import Image, ImageFilter, ImageChops


# Step 1: Image Smoothing (Gaussian Blur)

def image_smoothing(input_image, sigma):
    return input_image.filter(ImageFilter.GaussianBlur(sigma))


# Step 2: Edge Detection (Difference of Gaussian)
def edge_detection(input_image, sigma, k, threshold):
    gray = input_image.convert('L')
    smoothed = image_smoothing(gray, sigma)
    blurred = image_smoothing(gray, sigma * k)
    dog = ImageChops.difference(smoothed, blurred)
    edges = dog.point(lambda x: 0 if x >= threshold else 255)
    return edges


# Step 3: Image Quantization
def image_quantization(input_image, divisor, multiplier):
    lab_image = input_image.convert('LAB')

    # Converting LAB image to a NumPy array for manipulation
    lab_np = np.array(lab_image)

    # Quantizing the L (luminance) channel
    lab_np[:, :, 0] = (lab_np[:, :, 0] // divisor) * multiplier  # Quantize the L channel

    # Creating a new LAB image from the quantized NumPy array

    quantized_lab_image = Image.fromarray(lab_np, mode='LAB')
    # Converting the quantized LAB image back to RGB color space
    quantized_rgb_image = quantized_lab_image.convert('RGB')

    return quantized_rgb_image


# Step 4: Combine Edge and Quantized Image
def combine_edge_and_quantized(edge_image, quantized_image):
    # Convert the edge image to RGB mode to match quantized_image
    inverse_edges_rgb = edge_image.convert('RGB')

    # Multiply the inverse edges with the quantized image for each channel
    combined_image = ImageChops.multiply(inverse_edges_rgb, quantized_image)

    return combined_image


# Load the input image
def final(image_path, edge_sigma_param, k_param, treshold_param):
    edge_sigma = edge_sigma_param
    k = k_param
    treshold = treshold_param

    input_image = Image.open(image_path)

    # Apply image smoothing
    smoothed_image = image_smoothing(input_image, edge_sigma)

    # Apply edge detection
    edges_image = edge_detection(input_image, edge_sigma, k, treshold)

    # Apply image quantization
    quantized_image = image_quantization(input_image, divisor=9, multiplier=8)

    # Combine edges and quantized image to create a cartoon effect
    cartoon_image = combine_edge_and_quantized(edges_image, quantized_image)

    # Save the cartoon-like image

    quantized_image.save("quantized.jpg")
    edges_image.save("edges.jpg")
    cartoon_image.save("cartooned.jpg")
    smoothed_image.save("smoothed.jpg")


final(r"../report/{folder}/{file}.jpg", 2.8,
      0.35, 9)
