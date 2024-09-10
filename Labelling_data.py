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
