from autodistill.detection import CaptionOntology
from autodistill_grounding_dino import GroundingDINO
import os



ontology = CaptionOntology({
    "Child" : "Child",
    "Therapist" : "Therapist"
})

IMG_PATH = "/content/drive/MyDrive/Autisim_Detection/Dataset/New_images"
DATASET_DIR_PATH = "/content/drive/MyDrive/Autisim_Detection/Dataset/Labelled_dataset/"

BOX_THRESH = 0.6
TEXT_THRESH = 0.50

base_model = GroundingDINO(ontology= ontology,
                           box_threshold= BOX_THRESH,
                           text_threshold= TEXT_THRESH)

dataset = base_model.label(
    input_folder= IMG_PATH,
    extension= ".png",
    output_folder= DATASET_DIR_PATH
)

# # Ensure the output directory exists
# os.makedirs(DATASET_DIR_PATH, exist_ok=True)
# # Get the list of all images to process
# image_files = [f for f in os.listdir(IMG_PATH) if f.endswith('.png')]

# # Initialize counter
# count = 0

# # Process each image individually, up to 3 images
# for image_file in image_files:
#     if count >= 3:
#         break  # Stop processing after 3 images

#     try:
#         input_image_path = os.path.join(IMG_PATH, image_file)
#         output_image_path = os.path.join(DATASET_DIR_PATH, image_file)

#         # Label the image and save the result incrementally
#         dataset = base_model.label(
#             input_folder=IMG_PATH,
#             extension=".png",
#             output_folder=DATASET_DIR_PATH
#         )
        
#         print(f"Successfully labeled and saved: {output_image_path}")

#         # Increment counter
#         count += 1
#     except Exception as e:
#         print(f"An error occurred while processing {image_file}: {e}")

# import torch
# from pathlib import Path

# # Load the YOLOv5 model
# model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# # Define paths
# IMG_PATH = Path("C:/Users/Stuti/Downloads/Autisim_Detection/Dataset/All_images")
# OUTPUT_DIR = Path("C:/Users/Stuti/Downloads/Autisim_Detection/Dataset/Dataset/Labelled_dataset")
# OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# # Run detection and save annotated images
# for img_path in IMG_PATH.glob("*.png"):
#     results = model(img_path)
#     results.save(OUTPUT_DIR)
