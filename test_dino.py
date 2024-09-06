# import cv2
# from ultralytics import YOLO
# import os

# # Paths
# video_path = "/content/drive/MyDrive/Autisim_Detection/test_vids/ABA Therapy - Play.mp4"
# model_path = os.path.join("/content/drive/MyDrive/Autisim_Detection/checkpoints", "My-Large-Model-epochs200", "weights", "last.pt")
# output_video_path = "/content/drive/MyDrive/Autisim_Detection/output/My-Large-Model200best_vid3.mp4"

# # Load the model
# model = YOLO(model_path)
# threshold = 0.25

# # Open the input video file
# cap = cv2.VideoCapture(video_path)

# # Get the width, height, and frame rate of the input video
# frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# fps = int(cap.get(cv2.CAP_PROP_FPS))

# # Define the codec and create a VideoWriter object
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Specify the codec
# out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))

# while True:
#     ret, frame = cap.read()
    
#     if not ret:
#         break
    
#     # Perform detection
#     results = model(frame)[0]
    
#     # Process each detection result
#     for result in results.boxes.data.tolist():
#         x1, y1, x2, y2, score, class_id = result
        
#         x1 = int(x1)
#         x2 = int(x2)
#         y1 = int(y1)
#         y2 = int(y2)
        
#         if score > threshold:
#             cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 1)
#             cv2.putText(frame, results.names[int(class_id)].upper(), (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
    
#     # Write the frame into the output video file
#     out.write(frame)

# # Release the video capture and writer objects
# cap.release()
# out.release()

# print("Processed video saved as:", output_video_path)


import cv2
from ultralytics import YOLO
import os

# Paths
video_folder_path = "/content/drive/MyDrive/Autisim_Detection/test_videos/"
model_path = os.path.join("/content/drive/MyDrive/Autisim_Detection/checkpoints", "My-Large-Model-epochs200", "weights", "last.pt")
output_folder_path = "/content/drive/MyDrive/Autisim_Detection/Output/"

# Load the model
model = YOLO(model_path)
threshold = 0.25

# Ensure output folder exists
if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

# Loop over each video file in the folder
for video_file in os.listdir(video_folder_path):
    video_path = os.path.join(video_folder_path, video_file)
    
    # Ensure it's a video file (you can add more extensions if needed)
    if not video_file.endswith(('.mp4', '.avi', '.mkv', '.mov')):
        continue
    
    # Open the input video file
    cap = cv2.VideoCapture(video_path)

    # Get the width, height, and frame rate of the input video
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    # Define the codec and create a VideoWriter object
    output_video_path = os.path.join(output_folder_path, f"processed_{video_file}")
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Specify the codec
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        # Perform detection
        results = model(frame)[0]

        # Process each detection result
        for result in results.boxes.data.tolist():
            x1, y1, x2, y2, score, class_id = result

            x1 = int(x1)
            x2 = int(x2)
            y1 = int(y1)
            y2 = int(y2)

            if score > threshold:
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 1)
                cv2.putText(frame, results.names[int(class_id)].upper(), (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

        # Write the frame into the output video file
        out.write(frame)

    # Release the video capture and writer objects
    cap.release()
    out.release()

    print(f"Processed video saved as: {output_video_path}")
