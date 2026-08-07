import json

with open("curriculum/tracks/computer_vision_deep_learning.json", "r", encoding="utf-8") as f:
    data = json.load(f)

theories = {
    "Pixels and Channels": """## How Computers See Images — Pixels, Channels, and Matrices

When you look at a photo, you see a dog, a sunset, or a face. When a computer looks at that same photo, it sees nothing but **numbers** — millions of them, arranged in a massive grid. Understanding how images are represented as numerical data is the first step to building any computer vision system.

### What is a Pixel?

A **pixel** (picture element) is the smallest unit of an image — a single dot of color. A 1920x1080 (Full HD) image contains 1920 * 1080 = **2,073,600 pixels**. Each pixel stores a number representing its brightness or color.

### Grayscale Images — One Number Per Pixel

In a grayscale image, each pixel is a single number from **0 (pure black)** to **255 (pure white)**. Values in between represent shades of gray.

```
A 4x4 grayscale image:

  [  0,  64, 128, 192]     Black ░░░░ Dark gray ▒▒▒ Light gray ▓▓▓ Almost white
  [ 32,  96, 160, 224]
  [ 48, 112, 176, 240]
  [ 64, 128, 192, 255]

Shape: (4, 4) — a 2D matrix (height x width)
Total values: 16
```

### Color Images — Three Numbers Per Pixel (RGB)

Color images use three **channels**: **Red**, **Green**, and **Blue**. Each pixel has three values (0-255), one per channel:

```python
# A single pixel's color:
pixel = [255, 0, 0]     # Pure Red   (R=255, G=0, B=0)
pixel = [0, 255, 0]     # Pure Green (R=0, G=255, B=0)
pixel = [0, 0, 255]     # Pure Blue  (R=0, G=0, B=255)
pixel = [255, 255, 255] # White      (all channels max)
pixel = [0, 0, 0]       # Black      (all channels zero)
pixel = [128, 128, 128] # Gray       (all channels equal)
```

### Image Shape — The Three Dimensions

```
A 1080p color image:
  Height:   1080 pixels
  Width:    1920 pixels
  Channels: 3 (R, G, B)

  Shape: (1080, 1920, 3)
  Total values: 1080 * 1920 * 3 = 6,220,800 numbers!

  That's 6.2 million numbers for ONE image.
  A 4K image: 3840 * 2160 * 3 = 24.9 million numbers!
```

### Images as NumPy Arrays

```python
import numpy as np

# Create a tiny 2x2 RGB image
image = np.array([
    [[255, 0, 0],   [0, 255, 0]],    # Row 0: Red pixel, Green pixel
    [[0, 0, 255],   [255, 255, 0]]   # Row 1: Blue pixel, Yellow pixel
])

print(image.shape)    # (2, 2, 3) — 2 rows, 2 cols, 3 channels
print(image.dtype)    # uint8 — unsigned 8-bit integer (0-255)

# Access the red channel of the top-left pixel:
print(image[0, 0, 0])  # 255 (full red)
```

### Common Image Formats and Channels

| Format | Channels | Description |
|---|---|---|
| **Grayscale** | 1 | Single intensity value per pixel |
| **RGB** | 3 | Red, Green, Blue |
| **RGBA** | 4 | RGB + Alpha (transparency) |
| **BGR** | 3 | Blue, Green, Red (OpenCV's default!) |
| **HSV** | 3 | Hue, Saturation, Value (useful for color detection) |

This numerical representation is why AI can process images — neural networks are just mathematical functions, and images are just numbers.""",

    "OpenCV Intro": """## OpenCV — The Swiss Army Knife of Computer Vision

**OpenCV** (Open Source Computer Vision Library) is the most widely used library for image processing and computer vision. Imported as `cv2` in Python, it provides over 2,500 optimized algorithms for everything from reading images to face detection, object tracking, and camera calibration. If you're doing anything with images or video in Python, you'll use OpenCV.

### Core Functions

```python
import cv2
import numpy as np

# ─── READING AND WRITING ────────────────────────────────
# Read an image from disk
img = cv2.imread('photo.jpg')           # Returns a NumPy array
gray = cv2.imread('photo.jpg', cv2.IMREAD_GRAYSCALE)  # As grayscale

# Save an image to disk
cv2.imwrite('output.png', img)          # Save as PNG

# Display an image (in a desktop window)
cv2.imshow('My Image', img)
cv2.waitKey(0)                          # Wait for a key press
cv2.destroyAllWindows()                 # Close the window

# ─── COLOR SPACE CONVERSION ─────────────────────────────
# OpenCV loads images as BGR, not RGB!
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
```

### The BGR vs RGB Gotcha

This is the **#1 source of bugs** for OpenCV beginners:

```python
# OpenCV loads images as BGR (Blue, Green, Red)
# Most other libraries (Matplotlib, PIL, PyTorch) use RGB

# If you display an OpenCV image with Matplotlib:
import matplotlib.pyplot as plt
plt.imshow(img)  # Colors will look WRONG! (red and blue swapped)

# Fix: Convert BGR to RGB first
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  # Now colors are correct!
```

### Common Image Operations

```python
# Resize an image
resized = cv2.resize(img, (300, 200))  # (width, height)

# Crop a region of interest
roi = img[100:300, 50:250]  # [y_start:y_end, x_start:x_end]

# Rotate an image 90 degrees
rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

# Blur an image (noise reduction)
blurred = cv2.GaussianBlur(img, (5, 5), 0)

# Edge detection
edges = cv2.Canny(gray_img, threshold1=100, threshold2=200)

# Draw on images
cv2.rectangle(img, (50, 50), (200, 200), (0, 255, 0), 2)  # Green rectangle
cv2.putText(img, 'Hello', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)
```

### The 4 Essential OpenCV Functions

| Function | Description | Use Case |
|---|---|---|
| `cv2.imread()` | Load an image from disk into memory | Starting any CV pipeline |
| `cv2.cvtColor()` | Convert between color spaces (BGR, RGB, HSV, Gray) | Preprocessing for models |
| `cv2.imwrite()` | Save an image to disk | Storing results |
| `cv2.imshow()` | Display an image in a GUI window | Debugging and visualization |

These four functions are the foundation of every OpenCV workflow — load, process, save, display.""",

    "The Perceptron": """## The Artificial Neuron — Where Deep Learning Begins

The **Perceptron** is the simplest possible neural network — a single artificial neuron. Invented in 1957 by Frank Rosenblatt, it's the building block from which all modern deep learning architectures (CNNs, Transformers, GANs) are constructed. Understanding how one neuron works is the key to understanding how billions of them work together.

### How a Biological Neuron Works

```
Biological Neuron:
  Dendrites receive signals from other neurons
  → Cell body sums up all incoming signals
  → If the sum exceeds a threshold, the neuron FIRES
  → Signal travels down the Axon to other neurons

Artificial Neuron (Perceptron):
  Inputs receive data (like pixel values)
  → Multiply each input by a learnable Weight
  → Sum up all weighted inputs + add a Bias
  → Pass through an Activation Function
  → Output the result
```

### The Mathematical Formula

```
Output = Activation( (x1 * w1) + (x2 * w2) + ... + (xn * wn) + bias )

Where:
  x1, x2, ..., xn = Input values (features)
  w1, w2, ..., wn = Weights (learned during training)
  bias             = An offset term (also learned)
  Activation()     = A function that introduces non-linearity
```

### Step by Step Example

```python
# Inputs (e.g., features of a house)
x1 = 0.5   # Size (normalized)
x2 = 0.8   # Location score (normalized)

# Weights (learned during training)
w1 = 0.2   # How much size matters
w2 = -0.5  # How much location matters (negative = inverse)

# Bias
bias = 0.1

# Step 1: Weighted sum
weighted_sum = (x1 * w1) + (x2 * w2)
# = (0.5 * 0.2) + (0.8 * -0.5)
# = 0.1 + (-0.4) = -0.3

# Step 2: Add bias
total = weighted_sum + bias
# = -0.3 + 0.1 = -0.2

# Step 3: Activation function
# Step function: output 1 if total > 0, else 0
output = 1 if total > 0 else 0
# = 0 (because -0.2 is not > 0)
```

### Activation Functions

Activation functions introduce **non-linearity**. Without them, stacking neurons would just be multiplying matrices — no matter how deep, it would still be a linear function.

| Function | Formula | Range | Use Case |
|---|---|---|---|
| **Step** | 1 if x > 0, else 0 | {0, 1} | Original perceptron (not used today) |
| **Sigmoid** | 1 / (1 + e^(-x)) | (0, 1) | Binary classification output |
| **ReLU** | max(0, x) | [0, inf) | Hidden layers (most popular!) |
| **Tanh** | (e^x - e^(-x)) / (e^x + e^(-x)) | (-1, 1) | Hidden layers, RNNs |
| **Softmax** | e^xi / sum(e^xj) | (0, 1) | Multi-class classification output |

```python
import math

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def relu(x):
    return max(0, x)

def step(x):
    return 1 if x > 0 else 0

# Our example: total = -0.2
print(step(-0.2))     # 0
print(relu(-0.2))     # 0
print(sigmoid(-0.2))  # 0.45 (close to 0.5, uncertain)
```

### From One Neuron to Neural Networks

A single neuron can only learn **linear boundaries** (straight lines). But when you stack neurons in layers, the network can learn arbitrarily complex patterns — curves, shapes, and abstract concepts. That's the magic of deep learning.""",

    "Multi-dimensional Math": """## Tensors — The Language of Deep Learning

A **Tensor** is the fundamental data structure in deep learning frameworks like PyTorch and TensorFlow. It's essentially a multi-dimensional array of numbers — identical to a NumPy array in concept, but with two superpowers: it can run on **GPUs** for massive parallel speedups, and it can automatically track **gradients** for backpropagation.

### Tensor Dimensions

```
0D Tensor (Scalar): A single number
  tensor(42)
  Shape: ()

1D Tensor (Vector): A list of numbers
  tensor([1, 2, 3, 4, 5])
  Shape: (5,)

2D Tensor (Matrix): A grid of numbers
  tensor([[1, 2, 3],
          [4, 5, 6]])
  Shape: (2, 3)

3D Tensor: A "stack" of matrices
  An RGB image: 3 channels x 224 rows x 224 columns
  Shape: (3, 224, 224)

4D Tensor: A "batch" of 3D tensors
  A batch of 32 RGB images: 32 images x 3 channels x 224 x 224
  Shape: (32, 3, 224, 224)
```

### Why Not Just Use NumPy?

| Feature | NumPy | PyTorch Tensor |
|---|---|---|
| **CPU computation** | Yes | Yes |
| **GPU computation** | No | Yes (`.to('cuda')`) |
| **Automatic gradients** | No | Yes (`requires_grad=True`) |
| **Deep learning integration** | Manual | Native |
| **Performance on GPU** | N/A | 10-100x faster for matrix ops |

```python
import torch
import numpy as np

# NumPy: CPU only
np_array = np.array([[1, 2], [3, 4]])

# PyTorch: Can move to GPU
tensor = torch.tensor([[1, 2], [3, 4]])
gpu_tensor = tensor.to('cuda')  # Now on GPU!

# Automatic gradients (for training neural networks)
x = torch.tensor([2.0], requires_grad=True)
y = x ** 2  # y = 4.0
y.backward()  # Compute gradient: dy/dx = 2x = 4.0
print(x.grad)  # tensor([4.0])
```

### Basic Tensor Operations

```python
import torch

a = torch.tensor([[1, 2], [3, 4]])
b = torch.tensor([[10, 20], [30, 40]])

# Element-wise operations
c = a + b       # [[11, 22], [33, 44]]
d = a * b       # [[10, 40], [90, 160]]  (element-wise, NOT matrix multiply)

# Matrix multiplication
e = a @ b       # [[70, 100], [150, 220]]  (dot product)
e = torch.matmul(a, b)  # Same thing

# Reshaping
f = a.reshape(1, 4)   # [[1, 2, 3, 4]]
g = a.reshape(4, 1)   # [[1], [2], [3], [4]]
h = a.unsqueeze(0)     # [[[1, 2], [3, 4]]]  Add batch dimension

# Common creation functions
zeros = torch.zeros(3, 3)      # 3x3 matrix of zeros
ones = torch.ones(2, 4)        # 2x4 matrix of ones
rand = torch.randn(3, 3)       # 3x3 matrix of random normals
```

### Tensors in Deep Learning

Every piece of data in a neural network is a tensor:

```
Input image:  (batch_size, channels, height, width)  → (32, 3, 224, 224)
Text tokens:  (batch_size, sequence_length)           → (16, 512)
Weights:      (input_features, output_features)       → (784, 256)
Predictions:  (batch_size, num_classes)                → (32, 10)
```

Understanding tensor shapes and operations is the most important skill for working with deep learning — everything is tensor manipulation.""",

    "Convolutional Neural Networks": """## CNNs — How Neural Networks See Images

**Convolutional Neural Networks (CNNs)** are the architecture that revolutionized computer vision. Before CNNs, image recognition accuracy was around 70%. After the introduction of AlexNet in 2012, accuracy jumped to 85%+ and has continued climbing to superhuman levels. CNNs are designed specifically to exploit the spatial structure of images.

### Why Standard Neural Networks Fail on Images

```
Problem with Dense (Fully Connected) layers:

A 224x224 RGB image = 224 * 224 * 3 = 150,528 input values

Dense layer with 1000 neurons:
  150,528 inputs * 1000 neurons = 150 MILLION parameters (just one layer!)
  → Way too many parameters to train
  → Ignores spatial structure (adjacent pixels are related!)
  → Treats pixel at (0,0) the same as pixel at (223,223)

CNN approach:
  A 3x3 filter has only 9 parameters (+ 1 bias = 10)
  That same filter slides across the ENTIRE image
  → Shares parameters everywhere
  → Respects spatial locality (nearby pixels matter!)
  → 150 million parameters reduced to just 10
```

### How Convolution Works

```
Input Image (5x5):          Filter/Kernel (3x3):
┌─────────────────┐         ┌───────────┐
│ 1  1  1  0  0   │         │ 1  0  1   │
│ 0  1  1  1  0   │    *    │ 0  1  0   │
│ 0  0  1  1  1   │         │ 1  0  1   │
│ 0  0  1  1  0   │         └───────────┘
│ 0  1  1  0  0   │
└─────────────────┘

Step 1: Place filter at top-left corner
  1*1 + 1*0 + 1*1 + 0*0 + 1*1 + 1*0 + 0*1 + 0*0 + 1*1 = 4

Step 2: Slide filter one position right
  1*1 + 1*0 + 0*1 + 1*0 + 1*1 + 1*0 + 0*1 + 1*0 + 1*1 = 3

... continue sliding across the entire image
```

### The CNN Architecture

```
Input Image (224x224x3)
       ↓
┌──────────────────────────┐
│  CONV LAYER 1            │  Learns edges (horizontal, vertical, diagonal)
│  32 filters of 3x3       │  Output: 224x224x32
│  + ReLU activation       │
└──────────┬───────────────┘
           ↓
┌──────────────────────────┐
│  POOLING LAYER 1         │  Reduces spatial size by half
│  MaxPool 2x2             │  Output: 112x112x32
└──────────┬───────────────┘
           ↓
┌──────────────────────────┐
│  CONV LAYER 2            │  Learns shapes (circles, corners, textures)
│  64 filters of 3x3       │  Output: 112x112x64
│  + ReLU activation       │
└──────────┬───────────────┘
           ↓
┌──────────────────────────┐
│  POOLING LAYER 2         │  Reduces again
│  MaxPool 2x2             │  Output: 56x56x64
└──────────┬───────────────┘
           ↓
┌──────────────────────────┐
│  FLATTEN                 │  Convert 56x56x64 → 200,704 values
└──────────┬───────────────┘
           ↓
┌──────────────────────────┐
│  FULLY CONNECTED         │  Make the classification decision
│  Dense(200704 → 10)      │  Output: 10 class probabilities
│  + Softmax               │
└──────────────────────────┘
```

### What Each Layer Learns

| Layer Depth | What It Detects | Examples |
|---|---|---|
| **Early layers** | Low-level features | Edges, corners, colors |
| **Middle layers** | Mid-level features | Textures, patterns, shapes |
| **Deep layers** | High-level features | Eyes, wheels, windows |
| **Final layers** | Object concepts | "This is a cat" / "This is a car" |

### Famous CNN Architectures

| Model | Year | Key Innovation |
|---|---|---|
| **LeNet-5** | 1998 | First practical CNN (handwritten digits) |
| **AlexNet** | 2012 | Proved CNNs work at scale (ImageNet winner) |
| **VGGNet** | 2014 | Deeper is better (16-19 layers) |
| **GoogLeNet** | 2014 | Inception modules (parallel convolutions) |
| **ResNet** | 2015 | Skip connections (152 layers!) |
| **EfficientNet** | 2019 | Balanced scaling of depth/width/resolution |""",

    "Don't Start from Scratch": """## Transfer Learning — Why You Should (Almost) Never Train From Scratch

**Transfer Learning** is the most important practical technique in modern deep learning. Instead of training a model from scratch (which requires millions of images and thousands of GPU hours), you download a model that has already been trained on a massive dataset like ImageNet (14 million images, 1000 categories), and **fine-tune** it on your specific task. This works because the features learned by the model (edges, textures, shapes) are universal.

### The Intuition

```
Training from scratch:
  - Your dataset: 500 images of cats vs dogs
  - The model starts knowing NOTHING
  - It must learn: What is an edge? What is a corner? What is fur?
                   What is a face? What makes a cat different from a dog?
  - Result: Terrible accuracy (not enough data to learn everything)

Transfer Learning:
  - Download ResNet-50 (trained on 14 million images)
  - It ALREADY knows: edges, corners, textures, shapes, eyes, ears, fur
  - You only need to teach it: "These features → cat. Those features → dog"
  - Result: 95%+ accuracy with just 500 images!
```

### How It Works — Freeze and Replace

```
Pre-trained ResNet-50 (trained on ImageNet, 1000 classes):

Layer 1-48: Feature Extraction (edges → shapes → objects)
  ╔═══════════════════════════════════════╗
  ║  FREEZE these layers!                 ║
  ║  Don't change the weights.            ║
  ║  They already know how to "see."      ║
  ╚═══════════════════════════════════════╝

Layer 49: Final Classification (1000 classes → cat, dog, car, ...)
  ╔═══════════════════════════════════════╗
  ║  REPLACE this layer!                  ║
  ║  Original: Dense(2048 → 1000)         ║
  ║  New:      Dense(2048 → 2)            ║
  ║  (Just cat vs dog now)                ║
  ╚═══════════════════════════════════════╝
```

### Implementation in PyTorch

```python
import torch
import torch.nn as nn
from torchvision import models

# 1. Download pre-trained ResNet-50
model = models.resnet50(pretrained=True)

# 2. FREEZE all layers (don't update their weights)
for param in model.parameters():
    param.requires_grad = False

# 3. REPLACE the final classification layer
# Original: model.fc = nn.Linear(2048, 1000) (ImageNet classes)
model.fc = nn.Linear(2048, 2)  # Now: cat vs dog (2 classes)

# 4. Only the new layer's parameters will be trained
# model.fc.weight.requires_grad = True (automatically)
```

### Fine-Tuning Strategies

| Strategy | What It Does | When to Use |
|---|---|---|
| **Feature Extraction** | Freeze everything, train only the last layer | Small dataset (<1000 images) |
| **Fine-tune top layers** | Freeze early layers, train last few layers | Medium dataset (1K-10K images) |
| **Full fine-tuning** | Unfreeze all layers, train with tiny learning rate | Large dataset (10K+ images) |

```python
# Feature Extraction (simplest)
for param in model.parameters():
    param.requires_grad = False
model.fc = nn.Linear(2048, num_classes)

# Fine-tune top layers (intermediate)
for param in model.parameters():
    param.requires_grad = False
for param in model.layer4.parameters():  # Unfreeze last block
    param.requires_grad = True
model.fc = nn.Linear(2048, num_classes)

# Full fine-tuning (most flexible)
# Don't freeze anything, use a VERY small learning rate
optimizer = torch.optim.Adam(model.parameters(), lr=1e-5)
```

### Popular Pre-trained Models

| Model | Parameters | Top-1 Accuracy | Speed |
|---|---|---|---|
| **ResNet-50** | 25M | 76.1% | Fast |
| **EfficientNet-B0** | 5M | 77.1% | Very fast |
| **ViT-Base** | 86M | 81.8% | Medium |
| **ConvNeXt** | 89M | 83.8% | Medium |

Transfer learning is why you can build a production-quality image classifier in an afternoon with just a few hundred images.""",

    "Bounding Boxes": """## Object Detection — Finding and Localizing Objects in Images

**Object Detection** goes beyond image classification. While classification asks "What is in this image?", object detection asks "What objects are in this image, **where** are they, and how confident am I?" Each detected object gets a **bounding box** — a rectangle drawn around it — along with a class label and a confidence score.

### Classification vs Detection vs Segmentation

```
Image Classification:
  Input: An image of a park
  Output: "Dog" (one label for the whole image)

Object Detection:
  Input: An image of a park
  Output: 
    Dog  at (120, 80, 300, 250) confidence 0.95
    Cat  at (400, 150, 520, 310) confidence 0.87
    Tree at (50, 10, 200, 400) confidence 0.72

Instance Segmentation:
  Input: An image of a park
  Output: Pixel-level masks for each object (exact shape, not just a box)
```

### What is a Bounding Box?

A bounding box is defined by four coordinates:

```
(x_min, y_min) ─────────────────────┐
│                                    │
│          DETECTED OBJECT           │
│                                    │
│              "Dog"                 │  height = y_max - y_min
│          confidence: 0.95          │
│                                    │
└────────────────────── (x_max, y_max)
                width = x_max - x_min
```

### Bounding Box Formats

```python
# Format 1: Corner format (x_min, y_min, x_max, y_max)
# Used by: Faster R-CNN, most evaluation tools
bbox = [100, 50, 300, 200]

# Format 2: Center format (cx, cy, width, height)
# Used by: YOLO
bbox = [200, 125, 200, 150]

# Format 3: Normalized (0 to 1, relative to image size)
# Used by: YOLO training labels
bbox = [0.42, 0.35, 0.42, 0.42]

# Conversion:
def corner_to_center(x_min, y_min, x_max, y_max):
    cx = (x_min + x_max) / 2
    cy = (y_min + y_max) / 2
    w = x_max - x_min
    h = y_max - y_min
    return cx, cy, w, h
```

### Popular Object Detection Models

| Model | Type | Speed | Accuracy | Best For |
|---|---|---|---|---|
| **YOLO v8** | One-stage | Very fast (30+ FPS) | Good | Real-time video, edge devices |
| **Faster R-CNN** | Two-stage | Slow (5 FPS) | Very high | High-accuracy applications |
| **SSD** | One-stage | Fast (20 FPS) | Moderate | Mobile devices |
| **DETR** | Transformer | Medium | High | End-to-end detection |

### One-Stage vs Two-Stage Detectors

```
Two-stage (Faster R-CNN):
  Step 1: Region Proposal Network → "There might be objects HERE and HERE"
  Step 2: Classify each proposed region → "This one is a dog, this is a cat"
  → More accurate, but slower

One-stage (YOLO):
  Step 1: Look at the entire image ONCE
  Step 2: Predict all bounding boxes and classes simultaneously
  → Less accurate, but MUCH faster (real-time!)
```

The tradeoff between speed and accuracy is the central tension in object detection. YOLO prioritizes speed ("You Only Look Once"), while Faster R-CNN prioritizes accuracy.""",

    "Generative Adversarial Networks": """## GANs — The Art of Adversarial Creation

**Generative Adversarial Networks (GANs)**, invented by Ian Goodfellow in 2014, are one of the most creative innovations in AI. A GAN consists of two neural networks locked in a competitive game: one creates fake data, the other tries to detect the fakes. Through this adversarial training, the creator becomes so skilled that its outputs become indistinguishable from reality.

### The Forger vs The Detective

```
┌──────────────────┐          ┌──────────────────┐
│   GENERATOR      │          │  DISCRIMINATOR   │
│   (The Forger)   │          │  (The Detective) │
│                  │          │                  │
│ Input: Random    │  Fake    │ Input: An image  │
│ noise vector     │ ──────→  │ (real OR fake)   │
│                  │          │                  │
│ Output: A fake   │          │ Output: "Real"   │
│ image            │          │ or "Fake"        │
│                  │          │ (probability)    │
└──────────────────┘          └──────────────────┘

Training loop:
1. Generator creates a batch of fake images from random noise
2. Discriminator sees both real images (from dataset) and fakes
3. Discriminator learns to tell them apart
4. Generator learns from its failures (gets better at fooling)
5. Repeat until the Discriminator can't tell real from fake (50/50)
```

### The Training Process

```python
# Simplified GAN training loop
for epoch in range(num_epochs):
    for real_images in dataloader:
        # ─── Train Discriminator ───────────────────────
        # Show it real images → should predict "Real" (1.0)
        real_pred = discriminator(real_images)
        real_loss = loss_fn(real_pred, torch.ones_like(real_pred))
        
        # Generate fake images from random noise
        noise = torch.randn(batch_size, latent_dim)
        fake_images = generator(noise)
        
        # Show Discriminator the fakes → should predict "Fake" (0.0)
        fake_pred = discriminator(fake_images.detach())
        fake_loss = loss_fn(fake_pred, torch.zeros_like(fake_pred))
        
        d_loss = real_loss + fake_loss
        d_loss.backward()
        d_optimizer.step()
        
        # ─── Train Generator ──────────────────────────
        # Generator wants Discriminator to predict "Real" for its fakes
        fake_pred = discriminator(generator(noise))
        g_loss = loss_fn(fake_pred, torch.ones_like(fake_pred))
        
        g_loss.backward()
        g_optimizer.step()
```

### The Nash Equilibrium

Training converges when neither network can improve:

```
Epoch 1:   Generator: 🎨 (terrible) | Discriminator: 🔍 (easily catches fakes)
Epoch 10:  Generator: 🎨🎨 (better)  | Discriminator: 🔍🔍 (still catching most)
Epoch 100: Generator: 🎨🎨🎨 (good)  | Discriminator: 🔍🔍🔍 (struggling)
Epoch 500: Generator: 🎨🎨🎨🎨🎨     | Discriminator: 🔍 (50/50 guessing)

At equilibrium: P(real) = P(fake) = 0.5
```

### Types of GANs

| GAN Variant | Innovation | Application |
|---|---|---|
| **DCGAN** | Uses convolutional layers | Image generation |
| **StyleGAN** | Style-based generation, incredible quality | Face generation |
| **Pix2Pix** | Image-to-image translation (paired data) | Sketch → Photo |
| **CycleGAN** | Image translation without paired data | Horse → Zebra |
| **SRGAN** | Super-resolution | Enhance low-res images |
| **BigGAN** | Scaled up with class conditioning | High-res class-specific images |

### GAN Applications

- **Face generation** (ThisPersonDoesNotExist.com)
- **Image super-resolution** (enhance blurry photos)
- **Style transfer** (apply Van Gogh's style to your photo)
- **Data augmentation** (generate synthetic training data)
- **Video game asset generation** (textures, characters)
- **Drug discovery** (generate molecular structures)""",

    "ViT Architecture": """## Vision Transformers — When Attention Replaced Convolutions

The **Vision Transformer (ViT)**, introduced by Google in 2020, challenged the decade-long dominance of CNNs in computer vision. Instead of using convolutions to process images, ViT chops the image into a grid of **patches**, treats each patch like a word in a sentence, and feeds them into a standard Transformer architecture — the same architecture behind GPT and BERT.

### The Key Insight: An Image is Worth 16x16 Words

```
Traditional CNN:
  Image → Slide small filters across the image → Detect features
  Receptive field grows slowly (layer by layer)
  Local context only (nearby pixels)

Vision Transformer:
  Image → Chop into patches → Treat patches as "tokens" → Self-Attention
  EVERY patch can attend to EVERY other patch from layer 1
  Global context immediately (entire image)
```

### How ViT Works — Step by Step

```
Original Image (224 x 224 pixels)
            ↓
Step 1: SPLIT into patches
  ┌────┬────┬────┬─────────┐
  │ P1 │ P2 │ P3 │ ... P14 │  Each patch is 16x16 pixels
  ├────┼────┼────┼─────────┤  224/16 = 14 patches per row
  │P15 │P16 │P17 │ ... P28 │  14 x 14 = 196 patches total
  ├────┼────┼────┼─────────┤
  │    │    │    │ ...     │
  ├────┼────┼────┼─────────┤
  │    │    │    │ ...P196 │
  └────┴────┴────┴─────────┘
            ↓
Step 2: FLATTEN each patch into a 1D vector
  Each 16x16x3 patch = 768 values
  Result: 196 vectors of length 768
            ↓
Step 3: LINEAR PROJECTION (embedding)
  Each flattened patch → embedded into a D-dimensional space
  Like word embeddings in NLP!
            ↓
Step 4: ADD positional embeddings
  Patch embeddings don't know their position in the image
  Add learned positional embeddings (just like in GPT)
            ↓
Step 5: ADD a [CLS] token
  Prepend a special classification token
  Total sequence: 1 + 196 = 197 tokens
            ↓
Step 6: TRANSFORMER ENCODER
  Multi-Head Self-Attention + MLP, repeated L times
  Every patch attends to every other patch!
            ↓
Step 7: CLASSIFICATION HEAD
  Take the [CLS] token's output → MLP → Class prediction
```

### Self-Attention: Why It Matters for Vision

```
CNN: The bottom-right pixel of a car can only "see" nearby pixels
     It takes MANY layers to combine local features into global understanding

ViT: Every patch can attend to every other patch in ONE layer!
     
     Self-Attention example:
     Patch at [car wheel] attends to:
       - [car body] → high attention (related)
       - [road] → medium attention (context)
       - [sky] → low attention (not related)
     
     The model learns WHICH patches are relevant to each other.
```

### ViT Model Sizes

| Model | Layers | Hidden Dim | Heads | Params |
|---|---|---|---|---|
| **ViT-Tiny** | 12 | 192 | 3 | 5.7M |
| **ViT-Small** | 12 | 384 | 6 | 22M |
| **ViT-Base** | 12 | 768 | 12 | 86M |
| **ViT-Large** | 24 | 1024 | 16 | 307M |
| **ViT-Huge** | 32 | 1280 | 16 | 632M |

### ViT vs CNN: When to Use Which

| Criteria | CNN | ViT |
|---|---|---|
| **Small dataset (<10K)** | Better (built-in inductive bias) | Worse (needs lots of data) |
| **Large dataset (>100K)** | Good | Better (scales with data) |
| **Speed (inference)** | Fast | Slower (attention is O(n^2)) |
| **Global context** | Requires deep stacking | Immediate (self-attention) |
| **State-of-the-art** | Competitive | Leading (with pre-training) |""",

    "Reading and Displaying": """## Loading Images with OpenCV — Your First Computer Vision Step

Every computer vision pipeline starts with loading an image from disk into memory. **OpenCV** (imported as `cv2` in Python) is the industry-standard library for this. When OpenCV reads an image, it converts the file into a **NumPy array** — a multi-dimensional grid of numbers that represents pixel values. This numerical representation is what allows you to manipulate, analyze, and feed images into neural networks.

### Reading Images

```python
import cv2
import numpy as np

# ─── Basic image reading ────────────────────────────────
img = cv2.imread('photo.jpg')             # Read as color (BGR)
print(type(img))                          # <class 'numpy.ndarray'>
print(img.shape)                          # (height, width, channels) e.g., (480, 640, 3)
print(img.dtype)                          # uint8 (values 0-255)

# ─── Reading modes ──────────────────────────────────────
color = cv2.imread('photo.jpg', cv2.IMREAD_COLOR)       # Default: BGR color
gray = cv2.imread('photo.jpg', cv2.IMREAD_GRAYSCALE)    # Grayscale (1 channel)
unchanged = cv2.imread('photo.jpg', cv2.IMREAD_UNCHANGED)  # Include alpha channel

# ─── Error handling (important!) ────────────────────────
img = cv2.imread('nonexistent.jpg')
if img is None:
    print("Error: Image not found!")  # imread returns None, not an error!
```

### Displaying Images

```python
# ─── Display in a window ────────────────────────────────
cv2.imshow('Window Title', img)    # Open a window with the image
cv2.waitKey(0)                     # Wait indefinitely for a key press
cv2.destroyAllWindows()            # Close all OpenCV windows

# ─── Display with Matplotlib (better for Jupyter) ──────
import matplotlib.pyplot as plt

# IMPORTANT: Convert BGR to RGB first!
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(rgb_img)
plt.title('My Image')
plt.axis('off')
plt.show()
```

### Common Operations After Loading

```python
# Get image properties
height, width, channels = img.shape
total_pixels = height * width
print(f"Image: {width}x{height}, {channels} channels, {total_pixels} pixels")

# Access a specific pixel (row, col)
pixel = img[100, 200]           # BGR values at row 100, col 200
blue, green, red = pixel        # Remember: BGR order!

# Crop a region of interest
roi = img[50:200, 100:300]      # [y_start:y_end, x_start:x_end]

# Resize
resized = cv2.resize(img, (300, 200))  # (width, height) — note the order!

# Save to disk
cv2.imwrite('output.png', img)
```

The key takeaway: in OpenCV, images are just NumPy arrays. This means you can use all of NumPy's powerful array operations on them — slicing, indexing, mathematical operations, and more.""",

    "Color Spaces": """## Color Spaces — How Color is Represented in Computer Vision

A **color space** is a mathematical model for representing colors as numbers. Different color spaces emphasize different properties of color, and choosing the right one for your task can make a huge difference in your computer vision pipeline. OpenCV supports seamless conversion between dozens of color spaces.

### The Big Three Color Spaces

**RGB (Red, Green, Blue)** — The most intuitive color model. Each pixel has three values (0-255) for red, green, and blue intensity. This is what your monitor uses to display colors.

```
Red:   (255, 0, 0)      → Pure red
Green: (0, 255, 0)      → Pure green
Blue:  (0, 0, 255)      → Pure blue
White: (255, 255, 255)  → All channels max
Black: (0, 0, 0)        → All channels zero
Yellow: (255, 255, 0)   → Red + Green
```

**BGR (Blue, Green, Red)** — OpenCV's default! When you load an image with `cv2.imread()`, the channels are in BGR order, not RGB. This is a common source of bugs when mixing OpenCV with other libraries.

**HSV (Hue, Saturation, Value)** — Separates color information from brightness, making it ideal for color detection and filtering.

```
H (Hue):        0-179 in OpenCV (the "color" — red, blue, green)
S (Saturation):  0-255 (how "vivid" the color is)
V (Value):       0-255 (how "bright" the color is)

Why HSV is useful for color detection:
  In RGB, a "red" object can have wildly different RGB values 
  depending on lighting (shadow, sunlight, fluorescent).
  
  In HSV, "red" is always at Hue ≈ 0 or 170, regardless of brightness.
  Just filter by Hue!
```

### Converting Between Color Spaces

```python
import cv2

img_bgr = cv2.imread('photo.jpg')  # Loaded as BGR

# BGR → RGB (for Matplotlib display or PyTorch models)
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

# BGR → Grayscale (for edge detection, thresholding)
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

# BGR → HSV (for color detection and filtering)
img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)

# Detect red objects using HSV
lower_red = (0, 120, 70)
upper_red = (10, 255, 255)
mask = cv2.inRange(img_hsv, lower_red, upper_red)
```

### When to Use Each Color Space

| Color Space | Best For | Why |
|---|---|---|
| **BGR/RGB** | Display, neural network input | Standard representation |
| **Grayscale** | Edge detection, OCR, thresholding | Reduces complexity (1 channel vs 3) |
| **HSV** | Color detection, object tracking | Separates color from brightness |
| **LAB** | Color correction, histogram equalization | Perceptually uniform |
| **YCrCb** | Skin detection, video compression | Separates luminance from chrominance |

### The BGR→RGB Trap

```python
# THIS IS WRONG (common mistake):
img = cv2.imread('photo.jpg')   # BGR
plt.imshow(img)                 # Matplotlib expects RGB
# Result: Red and blue are SWAPPED! 😱

# THIS IS CORRECT:
img = cv2.imread('photo.jpg')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb)             # Colors are correct! ✓
```

Always convert BGR → RGB when passing OpenCV images to Matplotlib, PIL, or deep learning models (PyTorch, TensorFlow). This is the single most common bug in computer vision code.""",

    "Conv2D Layers": """## Convolutional Layers — The Feature Detectors of Deep Learning

A **Conv2D layer** (2D Convolutional Layer) is the core building block of any CNN. It applies a set of learnable **filters** (also called kernels) that slide across the input image, detecting specific features like edges, textures, and shapes. Each filter produces a **feature map** — a 2D grid highlighting where that feature appears in the image.

### How Conv2D Works

```
Input: RGB image (3 channels, 224x224)

Filter/Kernel: A small 3x3 grid of learnable weights
  (Each filter is actually 3x3x3 = 27 weights for 3 input channels)

The filter SLIDES across the image:
  Position (0,0): Multiply filter with image patch → one output value
  Position (0,1): Slide right one pixel → another output value
  Position (0,2): Slide right again → another output value
  ...continue until the entire image is covered...

Result: One 2D feature map per filter
  16 filters → 16 feature maps → output has 16 channels
```

### Key Parameters

```python
import torch.nn as nn

conv = nn.Conv2d(
    in_channels=3,     # Number of input channels (RGB = 3)
    out_channels=16,   # Number of filters (= number of output channels)
    kernel_size=3,     # Filter size (3x3)
    stride=1,          # How many pixels the filter moves each step
    padding=1           # Zeros added around the border to preserve size
)

# Input shape:  (batch, 3, 224, 224)
# Output shape: (batch, 16, 224, 224)  ← same spatial size due to padding=1
```

### Understanding the Parameters

| Parameter | What It Controls | Typical Values |
|---|---|---|
| **in_channels** | Depth of input (3 for RGB, 1 for grayscale) | 3, 1, 64, 128 |
| **out_channels** | Number of features to detect | 16, 32, 64, 128, 256, 512 |
| **kernel_size** | Size of the sliding filter | 3 (most common), 5, 7 |
| **stride** | Step size of the filter | 1 (default), 2 (halves spatial size) |
| **padding** | Border padding to control output size | 0, 1, 'same' |

### Output Size Formula

```
Output size = (Input size - Kernel size + 2 * Padding) / Stride + 1

Example: Input=224, Kernel=3, Padding=1, Stride=1
  = (224 - 3 + 2*1) / 1 + 1 = 224  (same size!)

Example: Input=224, Kernel=3, Padding=0, Stride=2
  = (224 - 3 + 0) / 2 + 1 = 111.5 → 111  (halved!)
```

### Building a CNN in PyTorch

```python
import torch.nn as nn

class SimpleCNN(nn.Module):
    def __init__(self, num_classes=10):
        super().__init__()
        self.features = nn.Sequential(
            nn.Conv2d(3, 32, kernel_size=3, padding=1),   # (3→32)
            nn.ReLU(),
            nn.MaxPool2d(2),                                # 224→112
            nn.Conv2d(32, 64, kernel_size=3, padding=1),  # (32→64)
            nn.ReLU(),
            nn.MaxPool2d(2),                                # 112→56
            nn.Conv2d(64, 128, kernel_size=3, padding=1), # (64→128)
            nn.ReLU(),
            nn.AdaptiveAvgPool2d(1),                        # 56→1
        )
        self.classifier = nn.Linear(128, num_classes)
    
    def forward(self, x):
        x = self.features(x)     # (batch, 128, 1, 1)
        x = x.view(x.size(0), -1) # (batch, 128)
        x = self.classifier(x)    # (batch, num_classes)
        return x
```

The conv layer is where the magic happens in a CNN — it automatically learns what features matter for your task during training.""",

    "Pooling Layers": """## Pooling Layers — Shrinking Feature Maps Without Losing Information

**Pooling layers** reduce the spatial dimensions (height and width) of feature maps while retaining the most important information. This serves three critical purposes: it reduces computational cost, controls overfitting, and increases the receptive field of subsequent layers. The most common type is **Max Pooling**.

### How Max Pooling Works

```
Input feature map (4x4):
┌────┬────┬────┬────┐
│  1 │  3 │  2 │  4 │
├────┼────┼────┼────┤
│  5 │  6 │  1 │  2 │
├────┼────┼────┼────┤
│  3 │  2 │  8 │  0 │
├────┼────┼────┼────┤
│  1 │  0 │  3 │  7 │
└────┴────┴────┴────┘

MaxPool2d(kernel_size=2, stride=2):
  Take the MAX value from each 2x2 region:

  max(1,3,5,6)=6    max(2,4,1,2)=4
  max(3,2,1,0)=3    max(8,0,3,7)=8

Output (2x2):
┌────┬────┐
│  6 │  4 │
├────┼────┤
│  3 │  8 │
└────┴────┘

Input: 4x4 (16 values) → Output: 2x2 (4 values)
Spatial dimensions cut in HALF. Strongest activations preserved.
```

### Types of Pooling

```python
import torch.nn as nn

# Max Pooling — keeps the strongest activation (most common)
pool = nn.MaxPool2d(kernel_size=2, stride=2)

# Average Pooling — takes the average of each region
pool = nn.AvgPool2d(kernel_size=2, stride=2)

# Global Average Pooling — reduces entire feature map to 1x1
pool = nn.AdaptiveAvgPool2d(1)
# Input: (batch, 128, 7, 7) → Output: (batch, 128, 1, 1)
```

### Why Pool?

| Benefit | Explanation |
|---|---|
| **Reduce computation** | Halving spatial dims → 4x fewer values to process |
| **Control overfitting** | Fewer parameters → less chance of memorizing noise |
| **Translation invariance** | A feature is detected whether it's at pixel (10,10) or (12,12) |
| **Larger receptive field** | After pooling, each value represents a larger image region |

### Pooling in a CNN Architecture

```
Conv(3→32) → ReLU → MaxPool(2x2)   Input: 224×224 → Output: 112×112
Conv(32→64) → ReLU → MaxPool(2x2)  Input: 112×112 → Output: 56×56
Conv(64→128) → ReLU → MaxPool(2x2) Input: 56×56   → Output: 28×28
Conv(128→256) → ReLU → MaxPool(2x2) Input: 28×28  → Output: 14×14

After 4 pooling layers: 224×224 → 14×14 (256x smaller area!)
But now with 256 channels of rich feature information.
```

### Max Pooling vs Average Pooling

| Type | What it Keeps | Best For |
|---|---|---|
| **Max Pooling** | Strongest activation (sharpest feature) | Feature detection (edges, objects) |
| **Average Pooling** | Average activation (smoothed response) | Reducing noise, final layers |
| **Global Average Pooling** | One value per channel | Replacing fully connected layers |

Modern architectures often use **Global Average Pooling** (AdaptiveAvgPool2d(1)) instead of flattening + dense layers at the end of the network, which dramatically reduces parameter count.""",

    "Intersection over Union (IoU)": """## IoU — The Gold Standard Metric for Object Detection

**Intersection over Union (IoU)**, also called the Jaccard Index, is the primary metric used to evaluate how well a predicted bounding box overlaps with the ground truth bounding box. It measures the quality of a detection by comparing the area of overlap between the two boxes against the total area covered by both boxes combined.

### The Formula

```
                  Area of Overlap
IoU = ─────────────────────────────────────
        Area of Union (Combined Area)

     ┌───────────────────┐
     │  Predicted Box    │
     │     ┌─────────────┼──────────┐
     │     │ OVERLAP     │          │
     │     │ (Intersect) │          │
     └─────┼─────────────┘          │
           │       Ground Truth Box │
           └────────────────────────┘

IoU = Intersection Area / Union Area
Union = Area(Predicted) + Area(Ground Truth) - Intersection
```

### IoU Values and What They Mean

```
IoU = 1.0:  Perfect overlap (boxes are identical)
  ┌──────────┐
  │ Pred =   │  Both boxes are exactly the same
  │ Ground   │
  │ Truth    │
  └──────────┘

IoU = 0.75: Good detection (significant overlap)
  ┌──────────┐
  │  Pred ┌──┼──────┐
  │       │  │      │ Ground Truth
  └───────┼──┘      │
          └─────────┘

IoU = 0.5:  Acceptable (standard threshold for "correct")
  ┌──────────┐
  │  Pred    │
  │    ┌─────┼────┐
  └────┼─────┘    │ Ground Truth
       └──────────┘

IoU = 0.0:  No overlap at all (completely wrong)
  ┌──────┐        ┌──────┐
  │ Pred │        │  GT  │
  └──────┘        └──────┘
```

### Computing IoU in Code

```python
def compute_iou(box1, box2):
    # Each box: (x_min, y_min, x_max, y_max)
    x1 = max(box1[0], box2[0])
    y1 = max(box1[1], box2[1])
    x2 = min(box1[2], box2[2])
    y2 = min(box1[3], box2[3])
    
    # Intersection area
    intersection = max(0, x2 - x1) * max(0, y2 - y1)
    
    # Union area
    area1 = (box1[2] - box1[0]) * (box1[3] - box1[1])
    area2 = (box2[2] - box2[0]) * (box2[3] - box2[1])
    union = area1 + area2 - intersection
    
    return intersection / union if union > 0 else 0

# Example
predicted = (100, 100, 300, 300)
ground_truth = (150, 150, 350, 350)
print(f"IoU: {compute_iou(predicted, ground_truth):.2f}")  # ~0.33
```

### IoU Thresholds in Practice

| Threshold | Name | Use Case |
|---|---|---|
| **IoU >= 0.5** | Standard | PASCAL VOC benchmark (AP@50) |
| **IoU >= 0.75** | Strict | High-quality detections |
| **IoU >= 0.5:0.95** | Comprehensive | COCO benchmark (AP@[.5:.05:.95]) |

The COCO dataset uses the mean of IoU from 0.5 to 0.95 in steps of 0.05, giving a more thorough evaluation of detection quality across different overlap thresholds.""",

    "Generator vs Discriminator": """## The GAN Architecture — Generator and Discriminator

A **GAN** (Generative Adversarial Network) consists of exactly two neural networks that are trained simultaneously in a competitive game. The **Generator** creates fake data trying to fool the other network, while the **Discriminator** tries to distinguish real data from the fakes. This adversarial training process drives both networks to continuously improve.

### The Generator — From Noise to Images

The Generator takes a **random noise vector** (typically 100-512 random numbers sampled from a normal distribution) and transforms it into a realistic image through a series of upsampling layers.

```
Random Noise Vector (z):
  [0.23, -1.05, 0.67, 0.12, ..., -0.89]  ← 100 random numbers
            ↓
  Dense Layer: 100 → 4×4×512
            ↓
  ConvTranspose2d: 4×4×512 → 8×8×256     (upsample)
            ↓
  ConvTranspose2d: 8×8×256 → 16×16×128   (upsample)
            ↓
  ConvTranspose2d: 16×16×128 → 32×32×64  (upsample)
            ↓
  ConvTranspose2d: 32×32×64 → 64×64×3    (final image)
            ↓
  Fake Image: (64, 64, 3) RGB image
```

**Key insight:** The Generator NEVER sees real images during training. It only learns from the Discriminator's feedback (the gradient signal). Different random noise vectors produce different images — the noise vector is like a "seed" that determines what the output looks like.

### The Discriminator — Real or Fake?

The Discriminator is essentially a binary classifier. Given an image, it outputs a single probability: how confident it is that the image is real.

```
Input Image (64×64×3):
  Could be a REAL image from the dataset
  OR a FAKE image from the Generator
            ↓
  Conv2d: 64×64×3 → 32×32×64        (downsample)
            ↓
  Conv2d: 32×32×64 → 16×16×128      (downsample)
            ↓
  Conv2d: 16×16×128 → 8×8×256       (downsample)
            ↓
  Flatten → Dense → Sigmoid
            ↓
  Output: 0.87  (87% confident it's REAL)
```

### The Training Objectives

```python
# Generator's goal:
#   Maximize P(Discriminator says "real" for Generator's fakes)
#   Generator WINS when Discriminator outputs 1.0 for fake images

# Discriminator's goal:
#   Maximize P(correctly classifying real AND fake)
#   Output 1.0 for real images
#   Output 0.0 for fake images
#   Discriminator WINS when it correctly identifies all fakes
```

### Why Random Noise?

```
Each point in the noise space maps to a different image:

z = [0.0, 0.0, ...]  → A woman with glasses
z = [1.0, 0.0, ...]  → A man without glasses
z = [0.5, 0.5, ...]  → Something in between

By smoothly changing the noise vector, you get smooth 
transitions in the output image. This is called "walking 
through the latent space" and it proves the Generator 
truly understands the structure of the data.
```

The balance between Generator and Discriminator is delicate. If the Discriminator becomes too strong too quickly, it provides no useful gradient for the Generator to learn from. If the Generator becomes too strong, it might "mode collapse" — producing only one type of image that happens to fool the Discriminator.""",

    "Loss Functions": """## GAN Loss Functions — Balancing the Adversarial Game

Training a GAN is notoriously difficult because you're optimizing two competing objectives simultaneously — the Generator wants to create better fakes, while the Discriminator wants to catch them. The **loss function** defines what "better" means for each network, and getting it right is the difference between photorealistic outputs and garbage.

### The Original GAN Loss (Minimax)

```
The GAN game is a minimax optimization:

  min_G max_D V(D, G) = E[log D(x)] + E[log(1 - D(G(z)))]
  
  Where:
    D(x)    = Discriminator's output for real images (should be 1)
    D(G(z)) = Discriminator's output for fake images (should be 0)
    G(z)    = Generator's output from noise z
```

### Discriminator Loss

The Discriminator wants to **maximize** its ability to correctly classify real and fake:

```python
# For REAL images: D should output 1.0 (high confidence = real)
real_loss = -log(D(real_image))     # Low when D(real) is close to 1

# For FAKE images: D should output 0.0 (high confidence = fake)  
fake_loss = -log(1 - D(G(noise)))   # Low when D(fake) is close to 0

d_loss = real_loss + fake_loss

# In PyTorch:
criterion = nn.BCELoss()
d_loss_real = criterion(D(real_images), torch.ones(batch_size))   # Label = 1
d_loss_fake = criterion(D(fake_images), torch.zeros(batch_size))  # Label = 0
d_loss = d_loss_real + d_loss_fake
```

### Generator Loss

The Generator wants to **maximize** the probability that the Discriminator classifies its fakes as real:

```python
# Generator wants D(G(z)) to be close to 1.0
g_loss = -log(D(G(noise)))

# In PyTorch:
fake_images = G(noise)
g_loss = criterion(D(fake_images), torch.ones(batch_size))  # Label = 1!
# Note: Generator uses label 1 (real) for its fakes —
# it's trying to FOOL the discriminator
```

### Common GAN Training Failures

| Problem | Symptom | Cause |
|---|---|---|
| **Mode Collapse** | Generator produces only 1-2 types of images | Generator found a shortcut that always fools D |
| **Training Instability** | Loss oscillates wildly, images get worse | Learning rates too high, architecture mismatch |
| **Vanishing Gradients** | Generator stops learning (D is too strong) | Discriminator converges too fast |
| **Non-convergence** | Neither network improves | Poorly balanced architectures |

### Improved Loss Functions

```
Original GAN Loss (2014): Simple but unstable
Wasserstein Loss (WGAN, 2017): More stable, measures "earth mover's distance"
Hinge Loss: Used in BigGAN, good for large-scale generation
Least Squares (LSGAN): Smoother gradients, less mode collapse
```

Training a GAN is more art than science. Practitioners often monitor the Discriminator's accuracy: if it's ~50% (random guessing), the Generator is winning. If it's ~100%, the Discriminator is too strong and the Generator can't learn.""",

    "Image Patches": """## Turning Images into Token Sequences — How ViT Processes Images

The core innovation of Vision Transformers is treating image patches as tokens — exactly like words in NLP. Instead of feeding raw pixels into a Transformer (which would be computationally impossible for large images), ViT **splits the image into a grid of fixed-size patches**, flattens each patch into a vector, and processes the resulting sequence with standard self-attention.

### The Patch Extraction Process

```
Original Image: 224 x 224 pixels

Patch Size: 16 x 16 pixels

Number of patches per row: 224 / 16 = 14
Number of patches per column: 224 / 16 = 14
Total patches: 14 x 14 = 196

Each patch is a small "tile" of the image:
  ┌─────┬─────┬─────┬─────┬──── ... ────┐
  │ P1  │ P2  │ P3  │ P4  │    ... P14  │
  │16x16│16x16│16x16│16x16│    ...      │
  ├─────┼─────┼─────┼─────┼──── ... ────┤
  │ P15 │ P16 │ P17 │ P18 │    ... P28  │
  ├─────┼─────┼─────┼─────┼──── ... ────┤
  │ ... │ ... │ ... │ ... │    ...      │
  ├─────┼─────┼─────┼─────┼──── ... ────┤
  │P183 │P184 │P185 │P186 │    ...P196  │
  └─────┴─────┴─────┴─────┴──── ... ────┘
```

### From Patches to Tokens

```python
# Each 16x16 RGB patch = 16 * 16 * 3 = 768 values
# Flatten each patch into a 1D vector of 768 values

patch_1 = [0.12, 0.34, 0.56, ..., 0.89]  # 768 numbers
patch_2 = [0.45, 0.67, 0.23, ..., 0.11]  # 768 numbers
...
patch_196 = [0.78, 0.91, 0.43, ..., 0.55]  # 768 numbers

# These are EXACTLY like word embeddings in NLP!
# Just as GPT processes a sequence of word tokens,
# ViT processes a sequence of image patch tokens.
```

### The Math: Sequence Length

```
Image size: H x W
Patch size: P x P

Number of patches (sequence length) = (H / P) x (W / P)

Common configurations:
  224x224 image, 16x16 patches → (224/16)^2 = 14^2 = 196 tokens
  224x224 image, 32x32 patches → (224/32)^2 = 7^2  = 49 tokens
  384x384 image, 16x16 patches → (384/16)^2 = 24^2 = 576 tokens

Trade-off:
  Smaller patches = more tokens = more detail = more computation
  Larger patches  = fewer tokens = less detail = faster
```

### Why Patches Instead of Pixels?

```
Naive approach: Treat each pixel as a token
  224 x 224 = 50,176 tokens
  Self-attention complexity: O(n^2) = O(50,176^2) = O(2.5 billion)
  → IMPOSSIBLE to compute!

Patch approach: Group 16x16 pixels into one token
  196 tokens
  Self-attention complexity: O(196^2) = O(38,416)
  → Totally manageable!
```

### Implementation

```python
import torch
import torch.nn as nn

class PatchEmbedding(nn.Module):
    def __init__(self, img_size=224, patch_size=16, in_channels=3, embed_dim=768):
        super().__init__()
        self.num_patches = (img_size // patch_size) ** 2  # 196
        
        # Use a Conv2d with kernel_size = patch_size and stride = patch_size
        # This extracts and projects patches in one operation!
        self.projection = nn.Conv2d(
            in_channels, embed_dim,
            kernel_size=patch_size, stride=patch_size
        )
    
    def forward(self, x):
        # x: (batch, 3, 224, 224)
        x = self.projection(x)      # (batch, 768, 14, 14)
        x = x.flatten(2)            # (batch, 768, 196)
        x = x.transpose(1, 2)      # (batch, 196, 768) — sequence of patch embeddings
        return x
```

This is the bridge between the visual world and the Transformer architecture: images become sequences, pixels become embeddings, and vision becomes a sequence modeling problem.""",

    "Self-Attention in Vision": """## Self-Attention in Computer Vision — Global Context in One Layer

**Self-Attention** is the mechanism that gives Vision Transformers their power. Unlike convolutions, which can only see a small local neighborhood of pixels (the kernel size), self-attention allows **every patch to look at every other patch** in the image in a single layer. This means a patch containing a car wheel can directly attend to a patch containing the car body, regardless of how far apart they are.

### Local vs Global Receptive Field

```
CNN (Local Receptive Field):
  A 3x3 convolution can only see 9 neighboring pixels
  To see the whole image, you need MANY stacked layers
  
  Layer 1: each pixel sees a 3x3 area
  Layer 2: each pixel sees a 5x5 area (because inputs are already 3x3)
  Layer 3: each pixel sees a 7x7 area
  ...
  Layer 50: finally sees the entire 224x224 image
  → Global context requires DEPTH

ViT Self-Attention (Global Receptive Field):
  EVERY patch attends to EVERY other patch in ONE layer
  
  Layer 1: patch at (0,0) can attend to patch at (13,13)
  → Global context from THE VERY FIRST LAYER
```

### How Self-Attention Works in Vision

```
Given 196 patch embeddings (each is a 768-dim vector):

Step 1: Create Query (Q), Key (K), Value (V) for each patch
  Q = patch_embedding @ W_Q   (What am I looking for?)
  K = patch_embedding @ W_K   (What do I contain?)
  V = patch_embedding @ W_V   (What information can I provide?)

Step 2: Compute attention scores
  Score(patch_i, patch_j) = Q_i · K_j / sqrt(d_k)
  
  High score = patch_i should pay attention to patch_j
  Low score  = patch_j is irrelevant to patch_i

Step 3: Softmax to get attention weights
  Weights = softmax(scores)  → sums to 1.0 for each patch

Step 4: Weighted sum of Values
  Output_i = sum(weight_ij * V_j for all patches j)
  
  Each patch's output is a blend of information from all patches,
  weighted by how relevant each other patch is.
```

### Visual Example of Attention

```
Image of a dog in a park:
  ┌────────────────────────────┐
  │  sky  │ tree │ tree │ sky  │
  ├───────┼──────┼──────┼──────┤
  │ grass │ DOG  │ DOG  │grass │  ← Patches containing the dog
  ├───────┼──────┼──────┼──────┤
  │ grass │grass │ ball │grass │
  └───────┴──────┴──────┴──────┘

When processing the "DOG" patch:
  Attention to other "DOG" patches:  HIGH (0.35) ← same object
  Attention to "ball" patch:         MEDIUM (0.15) ← related object
  Attention to "grass" patches:      LOW (0.08) ← background
  Attention to "sky" patches:        VERY LOW (0.02) ← irrelevant

The model learns WHICH patches are relevant to each other.
A dog patch knows to look at other dog patches and the ball.
```

### Multi-Head Attention

Instead of one attention pattern, ViT uses **multiple heads** — each head learns to attend to different aspects:

```
Head 1: Attends to spatial neighbors (local texture)
Head 2: Attends to same-color patches (color coherence)
Head 3: Attends to same-object patches (semantic grouping)
Head 4: Attends to background patches (context)
...
Head 12: Attends to edges and boundaries
```

### Why Self-Attention Beats Convolution (at Scale)

| Property | Convolution | Self-Attention |
|---|---|---|
| **Receptive field** | Local (3x3, 5x5) | Global (entire image) |
| **Parameter sharing** | Same filter everywhere | Different attention per position |
| **Computational cost** | O(n * k^2) | O(n^2 * d) |
| **Scales with data** | Saturates | Keeps improving |
| **Inductive bias** | Strong (locality, translation invariance) | Weak (needs more data) |

Self-attention gives ViTs a **global** receptive field from the very first layer — this is why they excel on large datasets where understanding long-range relationships between image regions matters.""",

    "The Forward Process": """## The Forward Diffusion Process — Destroying Images with Noise

The **Forward Process** is the first half of how diffusion models work. It takes a clean, sharp image and gradually destroys it by adding small amounts of **Gaussian noise** at each time step, until the image becomes pure random static. The forward process itself is not learned — it follows a fixed mathematical schedule. The AI's job is to learn the **reverse** of this process.

### The Intuition

```
Imagine dropping ink into a glass of clear water:

t=0:   Clear water with a distinct ink drop (clean image)
t=10:  Ink starts spreading, you can still see the drop shape
t=50:  Ink has spread significantly, shape is blurry
t=200: Water is uniformly murky (heavy noise)
t=1000: Water is completely uniform gray (pure noise)

The forward process is like this diffusion of ink.
You can't "un-stir" the ink easily.
But if you knew EXACTLY how much ink spread at each step,
you could mathematically reverse it!
That's what the neural network learns to do.
```

### Step by Step

```
t=0: Original clean image x_0
  [Sharp photo of a cat]

t=100: Slightly noisy (you can still see the cat clearly)
  x_100 = sqrt(alpha_100) * x_0 + sqrt(1 - alpha_100) * noise

t=500: Very noisy (you can barely make out the shape)
  x_500 = sqrt(alpha_500) * x_0 + sqrt(1 - alpha_500) * noise

t=1000: Pure Gaussian noise (the cat is completely gone)
  x_1000 ≈ noise  (just random static)
```

### The Mathematics

```
At each time step t, noise is added according to a schedule:

  x_t = sqrt(alpha_bar_t) * x_0 + sqrt(1 - alpha_bar_t) * epsilon

Where:
  x_0         = The original clean image
  x_t         = The noisy image at time step t
  alpha_bar_t = A decreasing value from ~1.0 to ~0.0
  epsilon     = Random Gaussian noise ~ N(0, I)

The noise schedule (beta):
  beta_1 = 0.0001 (tiny amount of noise at start)
  beta_2 = 0.0002
  ...
  beta_T = 0.02   (more noise near the end)
  
  alpha_t = 1 - beta_t
  alpha_bar_t = product of all alpha_1 to alpha_t
```

### The Noise Schedule

```
Time step:    0 ──────────────────────────────── T (1000)
Signal:       Strong ──────────────────────────── Zero
Noise:        Zero ────────────────────────────── Maximum

alpha_bar_t:  1.0 ─────────── 0.5 ────────────── 0.0
              (pure signal)  (equal mix)         (pure noise)
```

### Why This Works

The key insight is that the forward process is **simple and deterministic** (just keep adding noise), but the reverse process (removing noise) requires a powerful neural network to learn. The network is trained to predict:
- What noise was added at step t (epsilon prediction)
- What the slightly less noisy image looks like (x_{t-1} prediction)

By training on millions of images, the network learns the general structure of images — edges, textures, objects, faces — and uses this knowledge to reconstruct images from pure noise.""",

    "The Reverse Process": """## The Reverse Diffusion Process — Creating Images from Noise

The **Reverse Process** is where the actual AI magic happens. Starting from pure random noise, a neural network (typically a **U-Net**) learns to gradually remove noise — step by step — until a clean, coherent image emerges. This is the process that generates new images in models like Stable Diffusion, DALL-E, and Midjourney.

### The Core Idea

```
Forward Process (destroying):
  Clean image → Add noise → Add noise → ... → Pure noise
  (Easy, deterministic, no AI needed)

Reverse Process (creating):
  Pure noise → Remove noise → Remove noise → ... → Clean image
  (Hard! Requires a trained neural network)

The network is trained to answer ONE question:
  "Given this noisy image at time step t,
   what noise was added?"
  
  If we know what noise was added, we can subtract it!
```

### Step by Step Generation

```
Step T (start with pure noise):
  x_1000 = random_noise()
  [Pure static — no recognizable content]

Step T-1:
  predicted_noise = UNet(x_1000, t=1000)
  x_999 = x_1000 - predicted_noise  (slightly less noisy)
  [Still looks like noise, but mathematically cleaner]

Step T-2:
  predicted_noise = UNet(x_999, t=999)
  x_998 = x_999 - predicted_noise
  
  ... (repeat for hundreds of steps) ...

Step 100:
  [A blurry shape starts emerging — maybe a face?]

Step 50:
  [Details are forming — eyes, nose, hair]

Step 1:
  predicted_noise = UNet(x_1, t=1)
  x_0 = x_1 - predicted_noise
  [A clean, sharp, realistic image!]
```

### The U-Net Architecture

```
The U-Net is the standard architecture for noise prediction.
It has an encoder-decoder structure with skip connections:

Input: Noisy image x_t + Time embedding t
                    ↓
Encoder (downsample):
  64x64x3 → 32x32x64 → 16x16x128 → 8x8x256 → 4x4x512
  (compress spatial info, capture global context)
                    ↓
Bottleneck: 4x4x512
  (most compressed representation)
                    ↓
Decoder (upsample):
  4x4x512 → 8x8x256 → 16x16x128 → 32x32x64 → 64x64x3
  (reconstruct spatial detail)
                    ↓
Output: Predicted noise epsilon

Skip connections: Encoder features are concatenated with
decoder features at each level, preserving fine details.
```

### Training the U-Net

```python
# Simplified training loop
for batch in dataloader:
    clean_images = batch               # x_0: real images
    t = random_timestep()              # Random t from 1 to T
    noise = torch.randn_like(clean_images)  # Random noise
    
    # Add noise to create x_t (forward process)
    noisy_images = add_noise(clean_images, noise, t)
    
    # U-Net predicts what noise was added
    predicted_noise = unet(noisy_images, t)
    
    # Loss: How close was the prediction to the actual noise?
    loss = MSE(predicted_noise, noise)
    
    loss.backward()
    optimizer.step()
```

### Why the Reverse Process Works

The U-Net learns the **statistical structure of images** from millions of training examples. When it sees noisy data:
- It recognizes: "This pattern of noise is hiding what looks like an eye"
- It predicts: "This specific noise was added to create this pattern"
- We subtract the predicted noise: "Now the eye is clearer"

Each denoising step refines the image slightly, and after hundreds of steps, a completely new, coherent image emerges from pure randomness.""",

    "Latent Diffusion": """## Latent Diffusion — Making Image Generation Fast and Practical

**Latent Diffusion Models (LDMs)**, the architecture behind Stable Diffusion, solve a critical problem: running the diffusion process directly on high-resolution images is incredibly slow and memory-intensive. LDMs fix this by performing the noising and denoising in a compressed **latent space** — a much smaller representation of the image — and then decoding the result back to full resolution.

### The Problem with Pixel-Space Diffusion

```
Pixel-Space Diffusion (DALL-E 2, original approach):
  512x512x3 image = 786,432 values
  U-Net must process ALL 786,432 values at EVERY denoising step
  50 steps * 786,432 values = 39 million operations per generation
  → Requires massive GPUs (40+ GB VRAM)
  → Takes minutes per image
  → Impractical for consumer hardware

Latent Diffusion (Stable Diffusion):
  512x512x3 image → VAE Encoder → 64x64x4 latent = 16,384 values
  U-Net processes only 16,384 values at each step
  50 steps * 16,384 values = 819,200 operations
  → 48x less computation!
  → Runs on consumer GPUs (6-8 GB VRAM)
  → Generates images in seconds
```

### The Architecture

```
Text Prompt: "A cat wearing sunglasses on a beach"
                    ↓
┌────────────────────────────────────────────────────────┐
│                TEXT ENCODER (CLIP)                      │
│  Converts text to numerical embeddings                 │
│  "cat sunglasses beach" → [0.23, -0.45, 0.78, ...]   │
└────────────────────┬───────────────────────────────────┘
                     │ Text embeddings guide the U-Net
                     ↓
┌────────────────────────────────────────────────────────┐
│              LATENT DIFFUSION PROCESS                   │
│                                                         │
│  Random latent noise (64×64×4)                         │
│         ↓                                               │
│  U-Net denoises in LATENT SPACE (not pixel space!)     │
│  Guided by text embeddings via Cross-Attention          │
│  50 denoising steps                                     │
│         ↓                                               │
│  Clean latent representation (64×64×4)                 │
└────────────────────┬───────────────────────────────────┘
                     ↓
┌────────────────────────────────────────────────────────┐
│                VAE DECODER                              │
│  Decompresses latent → full resolution image           │
│  64×64×4 → 512×512×3                                   │
└────────────────────────────────────────────────────────┘
                     ↓
              Final Image (512×512)
```

### The VAE (Variational Autoencoder)

The VAE is the compression engine:

```
VAE Encoder (Compressor):
  Input:  512×512×3 image (786,432 values)
  Output: 64×64×4 latent (16,384 values)
  Compression ratio: 48x!

VAE Decoder (Decompressor):
  Input:  64×64×4 latent
  Output: 512×512×3 image
  Reconstructs the full-resolution image from the compressed representation
```

### Why Latent Space Works

The VAE learns that most of the information in an image is **redundant**. A 512×512 photo of a sunset can be represented with far fewer numbers because:
- Large areas have similar colors (sky gradient)
- Patterns repeat (waves, clouds)
- Fine details can be regenerated from coarse structure

The latent space captures the **essential structure** of the image, discarding redundant pixel-level details that the decoder can regenerate.

### Stable Diffusion Pipeline

```python
from diffusers import StableDiffusionPipeline

pipe = StableDiffusionPipeline.from_pretrained(
    "stabilityai/stable-diffusion-2-1"
).to("cuda")

image = pipe(
    prompt="A cat wearing sunglasses on a beach",
    num_inference_steps=50,    # Number of denoising steps
    guidance_scale=7.5,         # CFG scale (how closely to follow prompt)
).images[0]

image.save("cat_beach.png")
```

Latent Diffusion made generative AI accessible to everyone — you can run Stable Diffusion on a gaming laptop, not just a data center.""",

    "Text Encoders": """## Text-to-Image Guidance — How Text Controls Image Generation

In text-to-image diffusion models like Stable Diffusion, the text prompt must be converted from human language into a numerical format that the U-Net can use to guide the denoising process. This is done by a **text encoder** (typically CLIP), and the guidance is injected into the U-Net through a mechanism called **Cross-Attention**.

### The Text Encoding Pipeline

```
User's prompt: "A golden retriever playing in snow"
                    ↓
Step 1: TOKENIZATION
  Split into tokens: ["a", "golden", "retriever", "playing", "in", "snow"]
  Convert to IDs:    [49406, 3878, 12791, 2412, 530, 4106, 49407]
  (Padding to max length, typically 77 tokens)
                    ↓
Step 2: TEXT ENCODER (CLIP)
  Each token → embedding vector (768 or 1024 dimensions)
  The encoder processes the full sequence with self-attention
  
  Output: (77, 768) — 77 token embeddings of 768 dimensions each
  This captures the MEANING and relationships between words
                    ↓
Step 3: CROSS-ATTENTION in the U-Net
  At each layer of the U-Net, the text embeddings guide the denoising
  
  Query (Q): From the noisy image features
  Key (K):   From the text embeddings
  Value (V): From the text embeddings
  
  The image "asks" the text: "What should I look like here?"
```

### How Cross-Attention Injects Text

```
Cross-Attention mechanism:

  Image features          Text embeddings
  (spatial positions)     (token meanings)
       ↓                       ↓
       Q ─── dot product ─── K
               ↓
         Attention weights
       (which words matter for which image regions?)
               ↓
       Weighted sum of V (text values)
               ↓
       Image features now "know" what the text says
```

### What CLIP Understands

CLIP (Contrastive Language-Image Pre-training) was trained on 400 million image-text pairs from the internet. It learned to align the meaning of text with the meaning of images:

```
CLIP was trained to understand:
  "dog"           ↔ images of dogs
  "golden retriever" ↔ images of golden retrievers
  "playing in snow"  ↔ images of playful snow scenes
  
  It even understands compositions:
  "a cat wearing a top hat" → combines cat + hat concepts
  "cyberpunk cityscape at sunset" → combines style + scene + lighting
```

### Why Cross-Attention (Not Just Concatenation)?

```
Naive approach: Concatenate text embedding with image features
  → Text influences ALL pixels equally
  → Can't create spatial composition ("cat on the LEFT, dog on the RIGHT")

Cross-Attention approach:
  → Different image regions attend to different words
  → The word "cat" gets high attention in the left region
  → The word "dog" gets high attention in the right region
  → Enables spatial control and composition!

Example attention pattern for "A red car on a green road":
  Image region [car area] → high attention to "red" and "car"
  Image region [road area] → high attention to "green" and "road"
  Image region [sky area]  → low attention to all words (fills in naturally)
```

### Text Encoder Models

| Model | Used By | Token Limit | Dimensions |
|---|---|---|---|
| **CLIP ViT-L/14** | SD 1.5, SD 2.0 | 77 tokens | 768 |
| **OpenCLIP ViT-bigG** | SD XL (second encoder) | 77 tokens | 1280 |
| **T5-XXL** | Imagen, PixArt | 256 tokens | 4096 |

The quality of the text encoder directly determines how well the model understands your prompts. This is why models with better text encoders (like SDXL with dual CLIP encoders) follow complex prompts more accurately.""",

    "Classifier-Free Guidance": """## Classifier-Free Guidance — Controlling Prompt Adherence

**Classifier-Free Guidance (CFG)** is the technique that controls how strictly a diffusion model follows your text prompt. Without CFG, the model tends to generate generic, "safe" images. With CFG, you can dial up prompt adherence — but push it too high and the image becomes oversaturated and artifact-ridden.

### How CFG Works

The key idea: at each denoising step, the model generates **two** noise predictions simultaneously:

```
Input: Noisy image at time step t

Prediction 1: CONDITIONAL (with text prompt)
  noise_cond = UNet(noisy_image, t, text_embedding)
  "What noise to remove to get an image that matches the prompt"

Prediction 2: UNCONDITIONAL (without text prompt)
  noise_uncond = UNet(noisy_image, t, empty_embedding)
  "What noise to remove to get a generic image"

Final noise = noise_uncond + CFG_scale * (noise_cond - noise_uncond)
```

### The CFG Scale

```
CFG_scale = 1.0:  Use only the conditional prediction
  → Image loosely matches the prompt
  → More diverse, creative, but less controlled

CFG_scale = 7.5:  Default for most models (sweet spot)
  → Good balance of quality and prompt adherence
  → Sharp, coherent images that follow the prompt well

CFG_scale = 15.0: Strong guidance
  → Image strictly follows every detail of the prompt
  → Colors may start to become oversaturated

CFG_scale = 20.0+: Extreme guidance
  → Image is "fried" — oversaturated, artifacts, unnatural
  → Too much amplification of the prompt signal
```

### Visual Example

```
Prompt: "A serene mountain lake at sunset"

CFG = 1.0:  [Blurry, abstract, vaguely landscape-ish]
             Colors are muted, composition is random

CFG = 7.5:  [Sharp mountain lake with beautiful sunset colors]
             Good composition, realistic, follows prompt well

CFG = 15.0: [Very saturated sunset, dramatic mountains]
             Following prompt aggressively, colors getting extreme

CFG = 25.0: [Oversaturated mess, artifact-ridden, "deep fried"]
             The math has amplified the signal too much
```

### The Mathematics

```
guided_noise = noise_uncond + cfg_scale * (noise_cond - noise_uncond)

When cfg_scale = 1.0:
  guided_noise = noise_uncond + 1.0 * (noise_cond - noise_uncond)
               = noise_cond  (just the conditional prediction)

When cfg_scale = 7.5:
  guided_noise = noise_uncond + 7.5 * (noise_cond - noise_uncond)
  The difference between conditional and unconditional is AMPLIFIED
  by 7.5x, pushing the result further in the direction of the prompt

When cfg_scale > 10:
  The amplification starts to OVERSHOOT, creating artifacts
```

### CFG Scale Guidelines

| CFG Scale | Effect | Best For |
|---|---|---|
| **1.0-3.0** | Very creative, loose, diverse | Abstract art, exploration |
| **5.0-7.5** | Balanced quality and adherence | General purpose (recommended) |
| **8.0-12.0** | Strong adherence, vivid | Specific compositions |
| **15.0+** | Over-guided, artifacts | Usually too much |

CFG is a crucial knob for users of diffusion models — it's the primary way to balance between creative freedom and prompt accuracy.""",

    "Schedulers and Samplers": """## Noise Schedulers and Samplers — The Art of Denoising

The **scheduler** (also called a **sampler**) determines **how noise is removed** during the reverse diffusion process. Different schedulers use different mathematical strategies to traverse the path from pure noise to a clean image. The choice of scheduler dramatically affects image quality, generation speed, and artistic style.

### What a Scheduler Does

```
The scheduler answers: 
  "At step t, how much noise should I remove to get x_{t-1}?"

Pure noise (t=T) ────────────────────────── Clean image (t=0)
  x_1000         x_750         x_500         x_250         x_0

The scheduler decides:
  - How big each step should be
  - Whether to add randomness (stochastic) or not (deterministic)
  - How many total steps are needed for a good image
```

### Popular Schedulers

| Scheduler | Steps Needed | Speed | Quality | Style |
|---|---|---|---|---|
| **DDPM** | 1000 | Very slow | High | The original |
| **DDIM** | 50-100 | Medium | High | Deterministic (same seed = same image) |
| **Euler** | 20-30 | Fast | Good | Sharp, clean |
| **Euler Ancestral** | 20-30 | Fast | Good | More creative, varied |
| **DPM++ 2M** | 20-30 | Fast | Very high | Excellent quality-speed tradeoff |
| **DPM++ 2M Karras** | 20-30 | Fast | Excellent | Industry standard |
| **LCM** | 4-8 | Extremely fast | Good | Near real-time generation |

### Steps vs Quality Trade-off

```
Steps = 4 (LCM):     [Rough, but recognizable. Near real-time.]
Steps = 10:           [Decent quality, fast.]
Steps = 20 (sweet spot): [Good quality, reasonable speed.]
Steps = 50:           [High quality, slower.]
Steps = 100:          [Marginal improvement over 50, much slower.]
Steps = 150:          [No visible improvement. Wasting compute.]
```

### Deterministic vs Stochastic

```
DETERMINISTIC (DDIM, Euler):
  Same seed + same prompt + same settings = EXACTLY the same image
  Every time. Perfectly reproducible.
  
  Great for: Reproducible results, systematic exploration

STOCHASTIC (Euler Ancestral, DPM++ SDE):
  Same seed + same settings = SLIGHTLY different image each time
  Randomness is injected at each step.
  
  Great for: Creative exploration, varied outputs
```

### Why Modern Schedulers Are Better

The original DDPM (2020) needed 1000 steps to generate one image. Modern schedulers achieve comparable or better quality in 20-30 steps:

```
DDPM (2020):    1000 steps → 1 image in ~60 seconds
DDIM (2020):    50 steps   → 1 image in ~3 seconds
Euler (2022):   20 steps   → 1 image in ~1.2 seconds  
DPM++ (2022):   20 steps   → 1 image in ~1.2 seconds (better quality)
LCM (2023):     4 steps    → 1 image in ~0.3 seconds (near real-time!)
```

This 250x speedup (from DDPM to LCM) is what made real-time AI image generation possible.""",

    "Inpainting": """## Inpainting — Editing Specific Regions of an Image

**Inpainting** is a technique that allows you to selectively modify part of an existing image while leaving the rest untouched. You provide the diffusion model with three inputs: the original image, a **binary mask** indicating which region to regenerate, and a text prompt describing what should appear in the masked area. The model then generates new content that seamlessly blends with the surrounding pixels.

### How Inpainting Works

```
Original Image:               Binary Mask:
┌────────────────────┐        ┌────────────────────┐
│                    │        │ ████████████████████│ (black = keep)
│   Person wearing   │        │ ████████████████████│
│   a red hat        │        │ ████████████████████│
│   ┌──────┐         │        │ ████┌──────┐████████│
│   │ RED  │ ←hat    │        │ ████│ WHITE│████████│ (white = regenerate)
│   │ HAT  │         │        │ ████│ MASK │████████│
│   └──────┘         │        │ ████└──────┘████████│
│                    │        │ ████████████████████│
└────────────────────┘        └────────────────────┘

Prompt: "a blue cowboy hat"

Result:
┌────────────────────┐
│                    │
│   Person wearing   │
│   a blue cowboy hat│ ← Only the masked region changed!
│   ┌──────┐         │
│   │ BLUE │         │
│   │COWBOY│         │
│   └──────┘         │
│                    │ ← Rest of the image is UNCHANGED
└────────────────────┘
```

### The Three Required Inputs

| Input | Format | Description |
|---|---|---|
| **Original Image** | RGB image (e.g., 512×512×3) | The base image to edit |
| **Binary Mask** | Grayscale image (512×512×1) | White = regenerate, Black = keep |
| **Text Prompt** | String | What to generate in the masked area |

### The Inpainting Process

```
Step 1: Apply mask to original image
  Known pixels (black mask) = original image values
  Unknown pixels (white mask) = filled with noise

Step 2: Run reverse diffusion, but at EACH step:
  - Only denoise the MASKED region
  - Keep unmasked pixels fixed to the original image
  - The model generates new content that matches the edges

Step 3: Blend the generated region with the original
  Final = original * (1 - mask) + generated * mask
```

### Use Cases

| Use Case | What You Mask | New Prompt |
|---|---|---|
| **Object replacement** | The object to replace | Description of new object |
| **Background change** | Everything except the subject | New background description |
| **Defect removal** | The defect/watermark | Empty prompt or "clean surface" |
| **Extension** | Canvas edges (outpainting) | Description of extended scene |
| **Style change** | Specific region | Same content, different style |

### Implementation

```python
from diffusers import StableDiffusionInpaintPipeline
from PIL import Image

pipe = StableDiffusionInpaintPipeline.from_pretrained(
    "stabilityai/stable-diffusion-2-inpainting"
).to("cuda")

original = Image.open("photo.png").resize((512, 512))
mask = Image.open("mask.png").resize((512, 512))  # White = edit area

result = pipe(
    prompt="a blue cowboy hat with silver studs",
    image=original,
    mask_image=mask,
    num_inference_steps=50,
    guidance_scale=7.5,
).images[0]

result.save("edited_photo.png")
```

The quality of inpainting depends heavily on the mask — a well-drawn mask that follows object boundaries produces much cleaner results than a rough rectangular selection.""",

    "ControlNet": """## ControlNet — Precise Spatial Control Over Image Generation

**ControlNet** solves one of the biggest limitations of text-to-image models: text prompts are terrible at describing exact spatial layouts. "A person standing on the left with their arm raised" might produce anything from a yoga pose to a wave. ControlNet adds a **spatial guide image** (like an edge map, pose skeleton, or depth map) that tells the model exactly WHERE things should be.

### The Problem ControlNet Solves

```
Text-only generation:
  Prompt: "A person doing a martial arts kick"
  
  Generation 1: Person doing a roundhouse kick facing left
  Generation 2: Person doing a high kick facing right
  Generation 3: Person in a karate stance from behind
  → You can't control the exact pose!

ControlNet generation:
  Prompt: "A person doing a martial arts kick"
  + Control image: OpenPose skeleton of specific kick pose
  
  Generation 1: Person doing THAT EXACT kick from THAT EXACT angle
  Generation 2: Same pose, different person appearance
  Generation 3: Same pose, different clothing style
  → Exact spatial control!
```

### How ControlNet Works

```
┌────────────────────────────────────────────────────┐
│                 Stable Diffusion                    │
│                                                     │
│  Text Prompt ──→ Text Encoder ──→ Cross-Attention  │
│                                         ↓           │
│  Random Noise ──→ U-Net ←── ControlNet Features    │
│                     ↓           ↑                   │
│               Denoised Image    │                   │
│                              ControlNet             │
│                                 ↑                   │
│                          Control Image              │
│                     (edge map, pose, depth)          │
└────────────────────────────────────────────────────┘

The ControlNet is a COPY of the U-Net's encoder, locked (frozen).
It processes the control image and injects spatial features 
into the main U-Net at multiple resolution levels.

The original Stable Diffusion weights are NOT modified.
```

### ControlNet Preprocessors

Different preprocessors extract different spatial information:

| Preprocessor | Input | Output | Best For |
|---|---|---|---|
| **Canny Edge** | Any image | Edge map (white lines on black) | Architectural details, shapes |
| **OpenPose** | Image with people | Skeleton (joints and connections) | Human poses, dance, martial arts |
| **Depth Map (MiDaS)** | Any image | Grayscale depth map | 3D composition, perspective |
| **Normal Map** | Any image | Surface orientation map | 3D surfaces, lighting |
| **Segmentation** | Any image | Colored region map | Scene composition |
| **Scribble** | Hand drawing | Simple sketch | Quick concept art |
| **Line Art** | Any image | Clean line drawing | Illustrations, manga |

### Using ControlNet in Practice

```python
from diffusers import ControlNetModel, StableDiffusionControlNetPipeline
from PIL import Image

# Load ControlNet for OpenPose
controlnet = ControlNetModel.from_pretrained(
    "lllyasviel/control_v11p_sd15_openpose"
)

pipe = StableDiffusionControlNetPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    controlnet=controlnet
).to("cuda")

# The control image: an OpenPose skeleton
pose_image = Image.open("martial_arts_pose.png")

result = pipe(
    prompt="a ninja doing a flying kick, cinematic lighting",
    image=pose_image,
    num_inference_steps=30,
).images[0]

result.save("controlled_ninja.png")
```

### Multi-ControlNet

You can combine multiple ControlNets for even more precise control:

```python
# Combine Canny (for edges) + Depth (for 3D) + OpenPose (for pose)
# Each ControlNet adds a different spatial constraint
# The model respects ALL of them simultaneously
```

ControlNet turned text-to-image from "generate something vaguely like this" to "generate exactly this composition with this specific layout" — a game-changer for professional and creative applications."""
}

# Handle duplicate "Bounding Boxes" - we already have it once
# The second one in "Object Detection (YOLO)" section is different
theories_obj_det_bbox = """## Object Detection Coordinates — How YOLO Predicts Boxes

In object detection, the model doesn't just classify what's in an image — it also predicts the **exact location** of each object using a bounding box. The four values that define a bounding box — `x`, `y`, `w`, `h` — are the core output format for detectors like YOLO (You Only Look Once).

### YOLO's Grid-Based Prediction

```
YOLO divides the image into a grid (e.g., 7x7 = 49 cells):

┌────┬────┬────┬────┬────┬────┬────┐
│    │    │    │    │    │    │    │
├────┼────┼────┼────┼────┼────┼────┤
│    │    │ 🚗 │    │    │    │    │  ← Cell containing car's center
├────┼────┼────┼────┼────┼────┼────┤
│    │    │    │    │    │    │    │
├────┼────┼────┼────┼────┼────┼────┤
│    │    │    │    │    │    │    │
├────┼────┼────┼────┼────┼────┼────┤
│    │    │    │    │    │    │    │
├────┼────┼────┼────┼────┼────┼────┤
│    │    │    │    │    │ 🐕 │    │  ← Cell containing dog's center
├────┼────┼────┼────┼────┼────┼────┤
│    │    │    │    │    │    │    │
└────┴────┴────┴────┴────┴────┴────┘

Each cell predicts:
  - (x, y): Center of the box RELATIVE to the cell (0 to 1)
  - (w, h): Width and height RELATIVE to the full image (0 to 1)
  - confidence: P(object exists) * IoU(pred, truth)
  - class_probs: Probability for each class (car, dog, person, ...)
```

### The Four Bounding Box Values

```
For YOLO format (normalized, relative):
  x = 0.5  → Center is horizontally in the middle of its cell
  y = 0.3  → Center is 30% down from the top of its cell
  w = 0.4  → Box width is 40% of the image width
  h = 0.25 → Box height is 25% of the image height

For Corner format (absolute pixels):
  x_min = 100  → Left edge at pixel 100
  y_min = 50   → Top edge at pixel 50
  x_max = 300  → Right edge at pixel 300
  y_max = 200  → Bottom edge at pixel 200
  
  Width = x_max - x_min = 200 pixels
  Height = y_max - y_min = 150 pixels
  Area = 200 * 150 = 30,000 square pixels
```

### Converting Between Formats

```python
# YOLO (center, normalized) → Corner (absolute pixels)
def yolo_to_corner(x, y, w, h, img_width, img_height):
    x_min = int((x - w/2) * img_width)
    y_min = int((y - h/2) * img_height)
    x_max = int((x + w/2) * img_width)
    y_max = int((y + h/2) * img_height)
    return x_min, y_min, x_max, y_max

# Corner (absolute pixels) → YOLO (center, normalized)
def corner_to_yolo(x_min, y_min, x_max, y_max, img_width, img_height):
    x = ((x_min + x_max) / 2) / img_width
    y = ((y_min + y_max) / 2) / img_height
    w = (x_max - x_min) / img_width
    h = (y_max - y_min) / img_height
    return x, y, w, h
```

### YOLO Output Structure

For each grid cell, YOLO predicts:
```
[x, y, w, h, confidence, class_1_prob, class_2_prob, ..., class_n_prob]
```

After prediction, **Non-Maximum Suppression (NMS)** removes duplicate detections of the same object by keeping only the box with the highest confidence for each object."""

# Apply patches
patched = 0
for course_name, course_data in data.items():
    for lesson in course_data.get("lessons", []):
        title = lesson["title"]
        # Handle the duplicate "Bounding Boxes" title
        if title == "Bounding Boxes" and course_name == "Object Detection (YOLO)":
            old_len = len(lesson.get("theory", ""))
            lesson["theory"] = theories_obj_det_bbox
            new_len = len(lesson["theory"])
            print(f"  OK {title} (YOLO): {old_len} -> {new_len} chars")
            patched += 1
        elif title in theories and theories[title] is not None:
            old_len = len(lesson.get("theory", ""))
            lesson["theory"] = theories[title]
            new_len = len(lesson["theory"])
            print(f"  OK {title}: {old_len} -> {new_len} chars")
            patched += 1

with open("curriculum/tracks/computer_vision_deep_learning.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"\nPatched {patched} lessons in computer_vision_deep_learning.json")
