# Hand Gesture Classification with MediaPipe
Hand gesture classification model that leverages skeleton-based model to extract joint locations from images of hands.

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## Features

- Real-time hand gesture detection and classification.
- Supports multiple gestures including `Open Palm`, `Peace Sign`, `Rock On`, `OK Sign`, and `NOK Sign`.
- Utilizes `Mediapipe Hands` for efficient and accurate hand tracking.
- Model is trained with the joint locations extracted from the images of hands
- Extendible and customizable for additional gestures.

## Installation

### Prerequisites

- `Python 3.7` or higher
- `OpenCV`
- `Mediapipe`
- `NumPy`
- `Pandas`
- `Scikit-learn`
- `Pickle`

### Clone the Repository

```bash
git clone https://github.com/SparrowHere/hand-gesture-classification.git
cd hand-gesture-classification
```

### Install the Dependencies

Install the necessary libraries.
```bash
pip install -r requirements.txt
```
## Usage
In order to use the program real-time, run the command below on your terminal.
```bash
python src/run.py
```
https://github.com/SparrowHere/hand-gesture-classification/assets/111817817/b94f2d3d-0476-4331-bb4c-f692d057318a

## Data & Model Training
The dataset used for training the hand gesture classifier consists of images of hands performing different gestures. The data is collected manually using `OpenCV` and `OS` libraries. This process is automated so that it's possible to add new classes and images if needed.

![Types of Hand Gestures](https://github.com/SparrowHere/hand-gesture-classification/assets/111817817/804ef0a9-4e5d-47c1-aa17-b70f9cbd583b)

Data is organized into their respective directory as given below. 
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

Joint information was collected from 21 joints and saved in `.csv` format. The predictive model was trained using this data.

The model was trained using a `RandomForestClassifier` with the following parameters.
```python
RandomForestClassifier(n_estimators=10, random_state=42)
```
## Results
After evaluation, the model achieved **%98** accuracy on the test set.
```
              precision    recall  f1-score   support

           0       0.97      1.00      0.98        28
           1       1.00      1.00      1.00        14
           2       1.00      1.00      1.00        10
           3       1.00      0.92      0.96        24
           4       0.96      1.00      0.98        24

    accuracy                           0.98       100
   macro avg       0.99      0.98      0.98       100
weighted avg       0.98      0.98      0.98       100
```
The confusion matrix of the mentioned test set is given below.
<p align="center">
  <img src="https://github.com/SparrowHere/hand-gesture-classification/assets/111817817/7242f1c1-e601-4912-8d7f-f88b25110f63" alt="Confusion Matrix of the Test Data"/>
</p>
The results were also saved and evaluated in image format. Few of the outputs with their respected results are given below.
![Example Results](https://github.com/SparrowHere/hand-gesture-classification/assets/111817817/9690f3ef-b6eb-43f6-ada5-2b8db48545ff)

## Contributing
Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a new pull request.

## License
This project is licensed under the `MIT License`, see the [LICENSE](https://github.com/SparrowHere/hand-gesture-classification/blob/main/LICENSE) file for details.

## Acknowledgements
I would like to share my appriciation for the project team -- my friends who put in the efforts for the whole process and done their best to help me stay motivated. You guys are the best ✌️
