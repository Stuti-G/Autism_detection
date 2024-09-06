# Autism_detection
This project presents an optimized inference pipeline that processes long-duration videos, detecting and predicting the bounding boxes for "Child" and "Therapist" separately. The pipeline also includes strategies to enhance model performance. Below is a detailed explanation of the workflow, along with reasons for each step and the purpose of the corresponding files.

- [Detailed Documentation](https://docs.google.com/document/d/1smNpC3zGS_jY2iwGUR4oedsOje28-7_6LUalLjeHGUE/edit?usp=sharing)
- [Google colab notebook](https://colab.research.google.com/drive/1r650PWtlYWXAOkk6ZSycntrLkr05-_jM?usp=sharing)

## 1. Installation and Dependencies.
To install the package, run the following command:
```
pip install -r requirements.txt
```

## 2. Downloading Required Videos:
To begin, we need videos for training or testing the model. These videos are downloaded using the **Downloading_vid.py** script, which fetches videos from YouTube or other sources based on their URLs. This is an essential step as the videos serve as the dataset for further processing, including frame extraction and labeling.
```
python Downloading_vid.py
```
## 3. Challenges with Direct YOLO Inference:
If we use a pre-trained YOLO model directly, it can only detect both "Child" and "Therapist" under a single class - Person, which is not ideal for this task. The goal is to distinguish between the two, so the model needs to be trained to recognize them as distinct categories.

## 4. Dataset Creation:
To address the above issue, it is crucial to create a custom dataset where "Child" and "Therapist" are treated as separate classes. For this, two key steps are involved:

### a. Frame Extraction:
Two of the downloaded videos are used for training. These videos are located in the folder **Train_autisim** . To create a dataset, we extract frames from these videos using the **Extracting_frames.py** script. This allows us to convert the continuous video into individual image frames, which can later be labeled for object detection.

```
python Extracting_frames.py
```
### b. Labeling the Frames:
Once the frames are extracted, the next step is to label these images by drawing bounding boxes around "Child" and "Therapist". The Labelling_data.py script facilitates this process by specifying both classes:
* Child
* Therapist.

The script automatically generates annotation files for the corresponding image frames, specifying the bounding boxes and class labels.
```
python Labelling_data.py
```

## 4. Dataset Structure:
Refer [this link](https://drive.google.com/drive/folders/1j4CfSbdYilYLs7eoCuCVfpaCJyADdBoT?usp=sharing) to download the dataset.

After labeling, the dataset is organized into two main parts: training and validation sets.
<details open> <summary>Dataset Structure: (click to expand)</summary>
  
```
├── Labelled_dataset
    ├── train (3724)
        ├── images (1862)
        ├── labels (1862)
    ├── valid (932)
        ├── images (466)
        ├── labels (466)
```
</details>
Each image has a corresponding label file, containing the coordinates of bounding boxes and the class ("Child" or "Therapist").


## 5. Training:
Now that the dataset is prepared, we move on to training a YOLOv8 model. This is done using the Train_dino.py script. YOLOv8 is initialized with a configuration file (**data.yaml**) that specifies details about the dataset (paths to images and labels, class names, etc.).

* The model is trained for 200 epochs with a batch size of 16.
* Early stopping is enabled with a patience of 40 epochs, meaning the training will stop if no improvement is observed after 40 epochs.
* The model uses GPU (device 0) for faster training, and validation is performed after every epoch.

All results, including model checkpoints, are saved in **checkpoints** folder.

```
python Train_dino.py
```

## 6. Inference:
Once the model is trained, it can be used to test new videos. This is done using the test_dino.py script, which runs inference on the test videos. The script processes the video frames, applying the trained model to detect and track both "Child" and "Therapist", outputting the bounding boxes for each.
### 6.2 Tesing dataset
The checkpoints for the inference can be downloaded in [this link](https://drive.google.com/drive/folders/1_UKlU57p9oPJttMiVnKQMK_r6XyB_RBD?usp=sharing).
```
python test_dino.py
```

* The above script is tested on the videos which can be found [here](https://drive.google.com/drive/folders/1-6ukRkzlT3IIOdKLtBuLZw1rUdb0o1ze?usp=sharing) 
* The resulted output videos can be found [here](https://drive.google.com/drive/folders/10ke5mmzHe8W7zLB8MCFbBE_cwgH0RVEq?usp=sharing) 

## 7. Run-Time Results:
* All scripts and models are run in the
Jupyter Notebook: [Main.ipynb](https://colab.research.google.com/drive/1r650PWtlYWXAOkk6ZSycntrLkr05-_jM?usp=sharing), which contains run-time results. 
* This notebook shows how the model performs during training and inference, providing logs and visual results for bounding box predictions.
 

#  Strategies to Improve Model Performance:
Several strategies were employed to further enhance the model’s accuracy and generalization abilities:

* **Increase Training Dataset Size:**
To improve the model’s performance, one approach was to increase the number of labeled images. This adds more data for training, improving the model's ability to generalize to unseen videos. However, due to the model's complexity, training with a significantly larger dataset caused crashes during runtime. To mitigate this, the dataset was carefully augmented while maintaining a manageable size.

* **Data Augmentation:**
Data augmentation techniques such as flipping, scaling, rotation, and color jittering were applied to the training images. These techniques artificially increase the diversity of the dataset by altering the original images, helping the model adapt to a variety of conditions (e.g., different lighting, angles, and poses).

* **Refining Confidence Thresholds:**
Lowering or adjusting the confidence thresholds (e.g., BOX_THRESH and TEXT_THRESH) during inference can make the model less strict in its predictions. This increases the number of detected objects, ensuring that both "Child" and "Therapist" are consistently detected.

* **Non-Max Suppression (NMS) Tuning:**
NMS is a technique used to handle multiple overlapping bounding boxes. By fine-tuning the NMS parameters, the model can better handle situations where the "Child" and "Therapist" are close to each other or overlapping, ensuring both are correctly detected.
