### BdSL47: A Complete Open-access Depth-based Bangla Sign Alphabet and Digit Dataset

<hr>

#### <b>Paper Abstract</b> : 
Sign Language Recognition (SLR) is a crucial technology that aims to bridge the communication gap between hearing and deaf-mute individuals. By translating sign language into text or speech, SLR enables the deaf-mute population to communicate with the hearing population and vice versa. However, constructing a sign language dataset is challenging due to the complexity and variability in hand gestures. In particular, Bangla Sign Language (BdSL) has a limited number of datasets available, most of which are based on RGB images, which do not capture the depth information. Incorporating depth information in the dataset can improve the accuracy of SLR, especially for recognizing subtle differences in hand gestures. 

In this study, we propose a complete depth-based dataset for 47 one-handed static signs in BdSL using the MediaPipe framework. MediaPipe is an open-source, cross-platform framework that enables developers to build real-time multimedia applications. The proposed dataset includes 10 digits, from ০ to ৯, and 37 letters, from অ to ◌ँ. To construct the dataset, we used a depth camera to capture the hand gestures, which were then processed using the MediaPipe framework to extract the depth information. For classification, we used both baseline classifiers and an Artificial Neural Network (ANN) model. The baseline classifiers achieved an average accuracy of 84.81%, while the ANN model achieved an accuracy of 97.78%. Furthermore, we compared their dataset with an existing benchmark dataset called "Ishara Lipi" using deep learning approaches and achieved a significantly higher accuracy of 98.92%. These results demonstrate the effectiveness of incorporating depth information in the dataset and highlight the potential of using deep learning approaches for SLR.

<hr>

### <b>Dataset</b> : The Complete Dataset is available [here](https://doi.org/10.7910/DVN/EPIC3H)

<hr>

### <b>Codes in Kaggle</b> : 
- Sign Alphabet (37) : [here](https://www.kaggle.com/code/rayeed045/bdsl37-finalized-code/notebook)
- Sign Alphabet & Digits (47) : [here](https://www.kaggle.com/code/rayeed045/bdsl47-finalized-code/notebook)
