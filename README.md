# Object_Tracker
This project is a real-time object tracker designed to accurately track selected objects from a live camera feed with high efficiency and minimal latency. 

---

## Project Details
### In this project I have used:
1. **OpenCV** to accuratly capture and process the video from **Webcam**.
2. **selectROI** from **OpenCV** to draw box arround the selected object.
3. **TrackerCSRT** from **OpenCV** to accurately track selected object from **Webcam** in real-time.

---

### Project Structure
1. **ObjectTracker** (Class) - Manages the entire object tracking process, including selection and real-time tracking.
2. **select_object** (Function) - Opens the camera, allowing users to manually select the most suitable frame for object selection instead of using the first frame. Press **S** to capture the desired frame.
3. **run_tracker** (Function) - Tracks the selected object in real time through the camera and stops when the user presses **Q**.

---

### Run Project Workflow
1. Open the webcam using the ```cv2.VideoCapture(0)``` function.
2. Display the frames until user press on **S** key to annotated the object he want to track.
3. Annotated the object which we want to track using ```cv2.selectROI()``` function.
4. Pass the anntation to tracking object and track the object until the object disappear or user quit by pressing on **Q** key.

---

### Demo
[![Object Tracker](https://img.youtube.com/vi/Dqc9c8Rdv0w/0.jpg)](https://www.youtube.com/watch?v=Dqc9c8Rdv0w)

---
---

## Project Setup & Deployment

### Clone The Repo
To clone the repo, run:

```bash
git clone https://github.com/walid404/Object_Tracker.git
cd Object_Tracker
```

---

### Install Requirements

To install the required dependencies, run:

```bash
pip install -r requirements.txt
```

---

### run the script
To run the script, run:
```bash
python Object_Tracker
```

---

## 📩 Contact  
If you have any questions, suggestions, or responses, feel free to reach out:  
📧 Email: [walid.max28@gmail.com](mailto:walid.max28@gmail.com)  

---

## 📌 Stay Connected  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?logo=linkedin)](https://www.linkedin.com/in/waleed-shaban-17170924a/)  


---

## ⭐ Show Your Support  
If you found this project helpful, please ⭐ the repository!  
