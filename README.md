### BdSL47: A Complete Open-access Depth-based Bangla Sign Alphabet and Digit Dataset

<hr>

#### <b>Paper Abstract</b> : 
Sign Language Recognition (SLR) is crucial for enabling communication between the deaf-mute and hearing communities. Nevertheless, the development of a comprehensive sign language dataset is a challenging task due to the complexity and variations in hand gestures. This challenge is particularly evident in the case of Bangla Sign Language (BdSL), where the limited availability of depth datasets impedes accurate recognition. To address this issue, we propose BdSL47, an open-access depth dataset for 47 one-handed static signs (10 digits, from ০ to ৯; and 37 letters, from অ to  ँ ) of BdSL. The dataset was created using the MediaPipe framework for extracting depth information. To classify the signs, we developed an Artificial Neural Network (ANN) model with a 63-node input layer, a 47-node output layer, and 4 hidden layers that included dropout in the last two hidden layers, an Adam optimizer, and a ReLU activation function. Based on the selected hyperparameters, the proposed ANN model effectively learns the spatial relationships and patterns from the depth-based gestural input features and gives an F1 score of 97.84% , indicating the effectiveness of the approach compared to the baselines provided. Additionally, we compared the BdSL47 dataset with an existing benchmark dataset 'Ishara Lipi' using the Convolutional Neural Network (CNN) model and achieved 98.92% recognition accuracy, which is significantly higher than that of the Ishara Lipi dataset. The availability of BdSL47 as a comprehensive dataset can have an impact on improving the accuracy of SLR for BdSL using more advanced deep-learning models.

<hr>

### <b>Dataset</b> : The Complete Dataset is available [here](https://doi.org/10.7910/DVN/EPIC3H)

<hr>

### <b>Codes in Kaggle</b> : 
- Sign Alphabet (37) : [here](https://www.kaggle.com/code/rayeed045/bdsl37-finalized-code/notebook)
- Sign Alphabet & Digits (47) : [here](https://www.kaggle.com/code/rayeed045/bdsl47-finalized-code/notebook)
