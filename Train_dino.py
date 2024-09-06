from ultralytics import YOLO

def main():
    
    model = YOLO("yolov8l.yaml")
    
    config_file_path = "/content/drive/MyDrive/Autisim_Detection/Dataset/Labelled_dataset/data.yaml"
    
    project = "/content/drive/MyDrive/Autisim_Detection/checkpoints"
    experiment = "My-Large-Model-epochs200"
    
    batch_size = 16
    
    results = model.train(data = config_file_path,
                          epochs = 200,
                          project = project,
                          name = experiment,
                          batch = batch_size,
                          device = 0,
                          patience = 40,
                          imgsz = 640,
                          verbose = True,
                          val = True   
    )
    
if __name__ == "__main__":
    main()