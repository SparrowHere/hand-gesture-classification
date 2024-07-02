# Hand Gesture Classification with MediaPipe
Hand gesture classification model that leverages skeleton-based model to extract joint locations from images of hands.

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## Table of Contents
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Data](#data)
6. [Model Training](#model-training)
7. [Model Inference](#model-inference)
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
