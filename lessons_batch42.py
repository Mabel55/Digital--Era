"""
Batch 42: Expanding Computer Vision & Deep Learning Curriculum (OpenCV, CNNs, YOLO, GANs, ViT)
"""
import json, os

NEW_COURSES_BATCH42 = {
    "Image Processing Basics": {
        "tier": "Beginner",
        "aiRubric": "Assess OpenCV and image processing",
        "lessons": [
            {"title": "Reading and Displaying", "theory": "## OpenCV Basics\\nOpenCV is the standard library for computer vision. Images are loaded as NumPy arrays.", "instructions": "## Task: Load an Image\\nWrite the OpenCV function to read an image from the disk.", "starterCode": "import cv2\\n\\nimg = cv2.___('image.jpg')\\ncv2.imshow('Image', img)\\ncv2.waitKey(0)", "solution": "import cv2\\n\\nimg = cv2.imread('image.jpg')\\ncv2.imshow('Image', img)\\ncv2.waitKey(0)", "hint": "Use imread", "rubric": "Correctly uses cv2.imread."},
            {"title": "Color Spaces", "theory": "## BGR to RGB\\nBy default, OpenCV loads images in BGR format, but most Deep Learning models expect RGB format.", "instructions": "## Task: Convert Color Space\\nConvert the loaded image from BGR to RGB.", "starterCode": "import cv2\\n\\nimg_bgr = cv2.imread('image.jpg')\\nimg_rgb = cv2.cvtColor(img_bgr, cv2.___)", "solution": "import cv2\\n\\nimg_bgr = cv2.imread('image.jpg')\\nimg_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)", "hint": "Use COLOR_BGR2RGB", "rubric": "Correctly specifies cv2.COLOR_BGR2RGB."}
        ]
    },
    "Convolutional Neural Networks": {
        "tier": "Intermediate",
        "aiRubric": "Assess CNN architecture knowledge",
        "lessons": [
            {"title": "Conv2D Layers", "theory": "## Feature Extraction\\nConvolutional layers apply filters to the input image to extract features like edges and textures.", "instructions": "## Task: PyTorch Conv Layer\\nDefine a 2D convolutional layer with 3 input channels (RGB) and 16 output channels.", "starterCode": "import torch.nn as nn\\n\\nconv_layer = nn.___(___, ___, kernel_size=3, stride=1, padding=1)", "solution": "import torch.nn as nn\\n\\nconv_layer = nn.Conv2d(3, 16, kernel_size=3, stride=1, padding=1)", "hint": "Use Conv2d, 3, and 16", "rubric": "Correctly instantiates nn.Conv2d with 3 input and 16 output channels."},
            {"title": "Pooling Layers", "theory": "## Spatial Reduction\\nPooling layers downsample the spatial dimensions (width and height) of the feature maps, reducing computation and controlling overfitting.", "instructions": "## Task: Max Pooling\\nDefine a Max Pooling layer with a kernel size of 2 and a stride of 2.", "starterCode": "pool_layer = nn.___(___, stride=___)", "solution": "pool_layer = nn.MaxPool2d(2, stride=2)", "hint": "Use MaxPool2d, 2, and 2", "rubric": "Correctly uses MaxPool2d with kernel and stride 2."}
        ]
    },
    "Object Detection (YOLO)": {
        "tier": "Intermediate",
        "aiRubric": "Assess object detection concepts",
        "lessons": [
            {"title": "Bounding Boxes", "theory": "## Localization\\nUnlike image classification (which predicts one label for the whole image), object detection predicts bounding boxes (x, y, width, height) and class labels for multiple objects.", "instructions": "## Task: Box Format\\nYOLO predicts coordinates relative to the grid cell. What are the typically predicted 4 values for a bounding box?", "starterCode": "answer = '___, ___, ___, ___'", "solution": "answer = 'x, y, w, h'", "hint": "x, y, w, h (or x, y, width, height)", "rubric": "Mentions x, y, width/w, and height/h."},
            {"title": "Intersection over Union (IoU)", "theory": "## Evaluating Detections\\nIoU is the metric used to measure how much the predicted bounding box overlaps with the ground truth bounding box.", "instructions": "## Task: Perfect Overlap\\nWhat is the IoU value if the predicted box perfectly matches the ground truth box?", "starterCode": "iou_value = ___", "solution": "iou_value = 1.0", "hint": "It is 1.0", "rubric": "Correctly identifies 1.0 (or 1)."}
        ]
    },
    "Generative Adversarial Networks (GANs)": {
        "tier": "Advanced",
        "aiRubric": "Assess GAN architecture",
        "lessons": [
            {"title": "Generator vs Discriminator", "theory": "## The Adversarial Game\\nA GAN consists of two networks: the Generator (tries to create fake images that look real) and the Discriminator (tries to tell fake images from real ones).", "instructions": "## Task: Generator Input\\nWhat does the Generator typically take as input to generate a new, unique image?", "starterCode": "# Options: A real image, Random noise vector, A text prompt\\ninput_type = '___'", "solution": "# Options: A real image, Random noise vector, A text prompt\\ninput_type = 'Random noise vector'", "hint": "Random noise vector", "rubric": "Identifies Random noise vector."},
            {"title": "Loss Functions", "theory": "## Training Equilibrium\\nTraining a GAN is notoriously unstable because you are balancing two loss functions simultaneously.", "instructions": "## Task: Discriminator Goal\\nDoes the Discriminator want to *maximize* or *minimize* the probability of correctly classifying real and fake images?", "starterCode": "goal = '___'", "solution": "goal = 'maximize'", "hint": "It wants to maximize its accuracy.", "rubric": "Identifies maximize."}
        ]
    },
    "Vision Transformers (ViT)": {
        "tier": "Advanced",
        "aiRubric": "Assess Vision Transformers",
        "lessons": [
            {"title": "Image Patches", "theory": "## An Image is Worth 16x16 Words\\nUnlike CNNs that process pixels via convolutions, ViT splits an image into fixed-size patches, linearly embeds them, and treats them like a sequence of words (tokens) in NLP.", "instructions": "## Task: Sequence Length\\nIf a 224x224 image is split into 16x16 patches, how many patches (tokens) will there be in the sequence?", "starterCode": "num_patches = (224 / 16) * (224 / 16)\\nanswer = ___", "solution": "num_patches = (224 / 16) * (224 / 16)\\nanswer = 196", "hint": "14 * 14 = 196", "rubric": "Correctly calculates 196."},
            {"title": "Self-Attention in Vision", "theory": "## Global Context\\nCNNs have a limited receptive field (local context). Transformers use Self-Attention, which allows every patch to attend to every other patch across the entire image in a single layer.", "instructions": "## Task: Receptive Field\\nDoes a Vision Transformer have a *local* or *global* receptive field at the very first layer?", "starterCode": "receptive_field = '___'", "solution": "receptive_field = 'global'", "hint": "It has a global receptive field.", "rubric": "Identifies global."}
        ]
    }
}

def apply_lessons(tracks_dir):
    total = 0
    filepath = os.path.join(tracks_dir, 'computer_vision_deep_learning.json')
    
    # 1. Update computer_vision_deep_learning.json
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            track_data = json.load(f)
            
        updated = False
        
        # Add brand new courses
        for new_course_name, course_info in NEW_COURSES_BATCH42.items():
            if new_course_name not in track_data:
                track_data[new_course_name] = {
                    "aiRubric": course_info["aiRubric"],
                    "lessons": course_info["lessons"]
                }
                updated = True
                total += len(course_info["lessons"])
                
        if updated:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(track_data, f, indent=2, ensure_ascii=False)
                
    # 2. Update index.json
    index_path = os.path.join("curriculum", "index.json")
    if os.path.exists(index_path):
        with open(index_path, 'r', encoding='utf-8') as f:
            index_data = json.load(f)
            
        index_updated = False
        for new_course_name, course_info in NEW_COURSES_BATCH42.items():
            tier = course_info["tier"]
            if "Computer Vision & Deep Learning" in index_data and tier in index_data["Computer Vision & Deep Learning"]:
                if new_course_name not in index_data["Computer Vision & Deep Learning"][tier]:
                    index_data["Computer Vision & Deep Learning"][tier].append(new_course_name)
                    index_updated = True
                    
        if index_updated:
            with open(index_path, 'w', encoding='utf-8') as f:
                json.dump(index_data, f, indent=2, ensure_ascii=False)
                
    print(f'Batch 42: Added {total} lessons to Computer Vision & Deep Learning track')
    os.system('python build_courses.py')

if __name__ == '__main__':
    apply_lessons(os.path.join('curriculum', 'tracks'))
