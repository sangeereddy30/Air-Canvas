# Air Canvas - Virtual Drawing with OpenCV

## Overview
The **Air Canvas** project enables users to draw in the air using a colored object (e.g., a blue pen with a sharp tip). The project utilizes OpenCV to detect the object and track its movement, allowing users to draw on a virtual canvas in real time.

## Features
- **Real-time Object Detection**: Detects a blue pen with a sharp tip.
- **Virtual Drawing**: Users can draw by moving the pen in front of the camera.
- **Color Selection**: Switch between different colors using on-screen buttons.
- **Erase Feature**: Clear the canvas by selecting the "CLEAR ALL" option.
- **Webcam-Based Interaction**: Uses a webcam to capture movements and translate them into drawing actions.

## Installation
### Prerequisites
Ensure you have Python and the required dependencies installed:

```sh
pip install opencv-python numpy
```

### Running the Project
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/air-canvas.git
   cd air-canvas
   ```
2. Run the script:
   ```sh
   python air_canvas.py
   ```
3. Use a **blue pen with a sharp tip** to start drawing in the air.

## Usage
- Move the pen to draw on the virtual canvas.
- Select colors using the on-screen buttons.
- Hover over the "CLEAR ALL" button to erase the canvas.
- Press **'q'** to exit the application.

## Project Demo
![Screenshot 2025-03-13 002102](https://github.com/user-attachments/assets/b5a375f0-ac20-439f-bf2d-98a6a919958f)
![Screenshot 2025-03-13 002237](https://github.com/user-attachments/assets/f5752794-541c-4d0a-901e-09c3e18c3561)

## Contributing
Feel free to fork the repository and submit pull requests to improve the project!


