# import os
# import random
# import matplotlib.pyplot as plt
# import cv2

# label_names = ['Child','Therapist']

# def get_annotations(original_img , label_file):
    
#     with open(label_file , 'r') as file:
#         lines = file.readlines()
        
#     annotations = []
    
#     for line in lines:
#         values = line.split()
#         label = values[0]
#         x,y,w,h = map(float, values[1:])
#         annotations.append((label, x, y, w, h))
        
#     return annotations
    
    
    
# def put_annotations_in_image(image, annotations):
#     H, W, _ = image.shape
        
#     for annotation in annotations:
#         label, x, y, w, h = annotation
#         print(label,x,y,w,h)
#         label_name = label_names[int(label)]
            
            
#         x1 = int((x - w / 2) * W)
#         x2 = int((y - h / 2) * H)
#         y1 = int((x + w / 2) * W)
#         y2 = int((y + h / 2) * W)
            
#         cv2.rectangle(image, (x1, y1), (x2 , y2), (200, 200,0 ), 1)
            
#         cv2.putText(image, label_name, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200,200,0), 2)
            
#     return image 
    
# def display_random_images(folder_path, num_images , label_folder):
        
#     image_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        
#     selected_images = random.sample(image_files, num_images)
        
#     for i, image_file in enumerate(selected_images):
            
#         img = cv2.imread(os.path.join(folder_path, image_file))     
            
#         label_file = os.path.splitext(image_file)[0] + ".txt"
#         label_file_path = os.path.join(label_folder, label_file)
            
#         annotations_Yolo_format = get_annotations(img , label_file_path)
            
#         image_with_annotations = put_annotations_in_image(img, annotations_Yolo_format)
#         print(image_with_annotations)
#         cv2.imshow("img no. " + str(i), image_with_annotations)
#         cv2.waitKey(0) 
            
            
# image_path = "/content/drive/MyDrive/Autisim_Detection/Dataset/Labelled_dataset/train/images"
# label_folder = "/content/drive/MyDrive/Autisim_Detection/Dataset/Labelled_dataset/train/labels"
    
# num_images = 8 
    
# display_random_images(image_path, num_images , label_folder)
        
import os
import random
import matplotlib.pyplot as plt
import cv2

label_names = ['Child', 'Therapist']

def get_annotations(original_img, label_file):
    with open(label_file, 'r') as file:
        lines = file.readlines()
        
    annotations = []
    for line in lines:
        values = line.split()
        label = values[0]
        x, y, w, h = map(float, values[1:])
        annotations.append((label, x, y, w, h))
        
    return annotations

def put_annotations_in_image(image, annotations):
    H, W, _ = image.shape
        
    for annotation in annotations:
        label, x, y, w, h = annotation
        label_name = label_names[int(label)]
        
        x1 = int((x - w / 2) * W)
        y1 = int((y - h / 2) * H)
        x2 = int((x + w / 2) * W)
        y2 = int((y + h / 2) * H)
        
        cv2.rectangle(image, (x1, y1), (x2, y2), (200, 200, 0), 1)
        cv2.putText(image, label_name, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 0), 2)
            
    return image

def display_random_images(folder_path, num_images, label_folder):
    image_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        
    selected_images = random.sample(image_files, num_images)
        
    for i, image_file in enumerate(selected_images):
        img_path = os.path.join(folder_path, image_file)
        img = cv2.imread(img_path)
        
        # Debugging: Check if the image is loaded correctly
        if img is None:
            print(f"Error loading image: {img_path}")
            continue
        
        label_file = os.path.splitext(image_file)[0] + ".txt"
        label_file_path = os.path.join(label_folder, label_file)
        
        # Debugging: Check if the label file exists
        if not os.path.exists(label_file_path):
            print(f"Label file not found: {label_file_path}")
            continue
            
        annotations_Yolo_format = get_annotations(img, label_file_path)
        image_with_annotations = put_annotations_in_image(img, annotations_Yolo_format)
        
        # Convert BGR image (OpenCV) to RGB (Matplotlib)
        image_with_annotations = cv2.cvtColor(image_with_annotations, cv2.COLOR_BGR2RGB)
        
        # Display the image using Matplotlib
        plt.figure(figsize=(10, 10))
        plt.imshow(image_with_annotations)
        plt.title(f"Image {i+1}: {image_file}")
        plt.axis('off')
        plt.show()

image_path = "/content/drive/MyDrive/Autisim_Detection/Dataset/Labelled_dataset/train/images"
label_folder = "/content/drive/MyDrive/Autisim_Detection/Dataset/Labelled_dataset/train/labels"
    
num_images = 8
    
display_random_images(image_path, num_images, label_folder)
 
            