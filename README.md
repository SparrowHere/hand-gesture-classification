# Hand Gesture Classification with MediaPipe
Hand gesture classification model that leverages skeleton-based model to extract joint locations from images of hands.

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## Table of Contents
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Data](#data)
6. [Model Training](#model-training)
8. [Results](#results)
9. [Contributing](#contributing)
10. [License](#license)
11. [Acknowledgements](#acknowledgements)

## Features

- Real-time hand gesture detection and classification.
- Supports multiple gestures including `Open Palm`, `Peace Sign`, `Rock On`, `OK Sign`, and `NOK Sign`.
- Utilizes `Mediapipe Hands` for efficient and accurate hand tracking.
- Model is trained with the joint locations extracted from the images of hands
- Easy to extend and customizable for additional gestures.

## Installation

### Prerequisites

- Python 3.7 or higher
- OpenCV
- Mediapipe
- NumPy
- Pandas
- Scikit-learn
- Pickle

### Clone the Repository

```bash
git clone https://github.com/yourusername/hand-gesture-classification.git
cd hand-gesture-classification
```

### Install the Dependencies

Install the necessary libraries.
```bash
pip install -r requirements.txt
```
## Usage
In order to use the program real-time, run the command below on your terminal:
```bash
python src/run.py
```
> For any possible errors, reach out to my socials with details of the issue.

## Model Training
The dataset used for training the hand gesture classifier consists of images of hands performing different gestures.

![Types of Hand Gestures](https://github.com/SparrowHere/hand-gesture-classification/assets/111817817/804ef0a9-4e5d-47c1-aa17-b70f9cbd583b)

Data is organized into their respective directory as shown below:
```
├── data
│   ├── hand_landmarks.csv     <- Joint data extracted from images using `Mediapipe Hands`
│   ├── training               <- Images of hand gestures used for training.
│   │   ├── OK Sign            <- Images of hands belonging to "OK Sign" class.
│   │   ├── NOK Sign           <- Images of hands belonging to "NOK Sign" class.
│   │   ├── Open Palm          <- Images of hands belonging to "Open Palm" class.
│   │   ├── Peace Sign         <- Images of hands belonging to "Peace Sign" class.
│   │   ├── Rock Sign          <- Images of hands belonging to "Rock Sign" class.
```

Joint information is gathered from 21 joints and saved in the `.csv` format. Predictive model is trained using the data that is saved as `.csv`.

Example results are given below:
![Example Results](https://github.com/SparrowHere/hand-gesture-classification/assets/111817817/9690f3ef-b6eb-43f6-ada5-2b8db48545ff)
