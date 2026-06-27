"""
Batch 62: Deep Dive into Computer Vision (Diffusion Models Masterclass)
"""
import json, os

NEW_COURSES_BATCH62 = {
    "Diffusion Models Masterclass": {
        "tier": "Advanced",
        "aiRubric": "Assess deep understanding of Diffusion Models and Generative AI",
        "lessons": [
            {"title": "The Forward Process", "theory": "## Adding Noise\\nDiffusion models work by learning how to reverse noise. The 'Forward Process' (or diffusion process) takes a clean image and incrementally adds Gaussian noise to it over many time steps until it becomes pure static.", "instructions": "## Task: The End State\\nIf you run the forward diffusion process for an infinite number of steps, what does the image eventually become?", "starterCode": "# Options: A black image, A white image, Pure Gaussian noise\\nend_state = '___'", "solution": "# Options: A black image, A white image, Pure Gaussian noise\\nend_state = 'Pure Gaussian noise'", "hint": "Pure Gaussian noise", "rubric": "Identifies Pure Gaussian noise."},
            {"title": "The Reverse Process", "theory": "## Denoising with UNet\\nThe 'Reverse Process' is the actual AI generation. A neural network (typically a U-Net) is trained to predict the noise that was added at each step, so it can subtract that noise to recover a clean image.", "instructions": "## Task: Network Architecture\\nWhat neural network architecture is traditionally used in Diffusion models to predict and remove noise?", "starterCode": "# Options: ResNet50, U-Net, LSTM\\narchitecture = '___'", "solution": "# Options: ResNet50, U-Net, LSTM\\narchitecture = 'U-Net'", "hint": "U-Net", "rubric": "Identifies U-Net."},
            {"title": "Latent Diffusion", "theory": "## Saving VRAM\\nOperating on 1024x1024 images pixel-by-pixel is extremely slow and requires massive GPUs. 'Latent Diffusion' (used by Stable Diffusion) solves this by compressing the image into a smaller 'Latent Space' using a VAE, doing the diffusion there, and then decoding it.", "instructions": "## Task: The Compressor\\nWhat component compresses the pixel image into the smaller latent space before the diffusion process begins?", "starterCode": "# Options: The CLIP text encoder, The VAE Encoder, The U-Net\\ncompressor = 'The ___'", "solution": "# Options: The CLIP text encoder, The VAE Encoder, The U-Net\\ncompressor = 'The VAE Encoder'", "hint": "VAE Encoder", "rubric": "Identifies VAE Encoder."},
            {"title": "Text Encoders", "theory": "## Cross-Attention\\nTo generate images from text (like 'A cat on a moon'), the text must be converted into numerical embeddings. A text encoder like OpenAI's CLIP is used to create embeddings that the U-Net uses as a guide during denoising.", "instructions": "## Task: Guiding the Image\\nIn Stable Diffusion, what specific mechanism inside the U-Net injects the text embeddings into the image generation process?", "starterCode": "# Options: Max Pooling, Cross-Attention, Softmax\\nmechanism = '___'", "solution": "# Options: Max Pooling, Cross-Attention, Softmax\\nmechanism = 'Cross-Attention'", "hint": "Cross-Attention", "rubric": "Identifies Cross-Attention."},
            {"title": "Classifier-Free Guidance", "theory": "## Following the Prompt\\nClassifier-Free Guidance (CFG) controls how strictly the model should follow your text prompt. The model generates two images simultaneously (one with the prompt, one unconditionally) and extrapolates the difference.", "instructions": "## Task: CFG Scale Effect\\nIf you set the CFG Scale extremely high (e.g., 20), what is the most likely outcome?", "starterCode": "# Options: The image ignores the prompt entirely, The image strictly follows the prompt but may look fried/oversaturated\\noutcome = '___'", "solution": "# Options: The image ignores the prompt entirely, The image strictly follows the prompt but may look fried/oversaturated\\noutcome = 'The image strictly follows the prompt but may look fried/oversaturated'", "hint": "It strictly follows the prompt but may look fried", "rubric": "Identifies strict following but fried/oversaturated."},
            {"title": "Schedulers and Samplers", "theory": "## Taking Steps\\nThe scheduler (or sampler) determines how the noise is removed over time. Euler is very fast (good images in 20 steps), while DDIM might take longer but offers different stylistic convergences.", "instructions": "## Task: Sampler Speed\\nWhy are modern samplers like Euler Ancestral or DPM++ preferred over the original DDPM sampler?", "starterCode": "# Options: They generate higher resolution images, They require far fewer steps to converge to a good image\\nreason = '___'", "solution": "# Options: They generate higher resolution images, They require far fewer steps to converge to a good image\\nreason = 'They require far fewer steps to converge to a good image'", "hint": "They require far fewer steps", "rubric": "Identifies fewer steps."},
            {"title": "Inpainting", "theory": "## Modifying Regions\\nInpainting allows you to mask out a specific part of an image (like a person's hat) and run the diffusion process *only* on that masked area, seamlessly blending the new generation with the original image.", "instructions": "## Task: Required Inputs\\nTo perform Inpainting, you must provide the model with a text prompt, the original image, and what else?", "starterCode": "# Options: A 3D model, A binary mask image, An audio file\\nthird_input = '___'", "solution": "# Options: A 3D model, A binary mask image, An audio file\\nthird_input = 'A binary mask image'", "hint": "A binary mask image", "rubric": "Identifies binary mask image."},
            {"title": "ControlNet", "theory": "## Spatial Guidance\\nText prompts are bad at dictating exact spatial layouts. ControlNet solves this by locking the main diffusion model and feeding it a spatial guide image (like a Canny edge map or OpenPose skeleton).", "instructions": "## Task: Pose Guidance\\nIf you want the generated person to stand in a very specific martial arts stance, which ControlNet preprocessor should you use?", "starterCode": "# Options: Depth Map, Canny Edge, OpenPose\\npreprocessor = '___'", "solution": "# Options: Depth Map, Canny Edge, OpenPose\\npreprocessor = 'OpenPose'", "hint": "OpenPose extracts human skeletons", "rubric": "Identifies OpenPose."}
        ]
    }
}

def apply_lessons(tracks_dir):
    total = 0
    filepath = os.path.join(tracks_dir, 'computer_vision_deep_learning.json')
    
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            track_data = json.load(f)
            
        updated = False
        
        for new_course_name, course_info in NEW_COURSES_BATCH62.items():
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
                
    index_path = os.path.join("curriculum", "index.json")
    if os.path.exists(index_path):
        with open(index_path, 'r', encoding='utf-8') as f:
            index_data = json.load(f)
            
        index_updated = False
        for new_course_name, course_info in NEW_COURSES_BATCH62.items():
            tier = course_info["tier"]
            if "Computer Vision & Deep Learning" in index_data and tier in index_data["Computer Vision & Deep Learning"]:
                if new_course_name not in index_data["Computer Vision & Deep Learning"][tier]:
                    index_data["Computer Vision & Deep Learning"][tier].append(new_course_name)
                    index_updated = True
                    
        if index_updated:
            with open(index_path, 'w', encoding='utf-8') as f:
                json.dump(index_data, f, indent=2, ensure_ascii=False)
                
    print(f'Batch 62: Added {total} lessons to Computer Vision & Deep Learning track')
    os.system('python fix_newlines.py')

if __name__ == '__main__':
    apply_lessons(os.path.join('curriculum', 'tracks'))
