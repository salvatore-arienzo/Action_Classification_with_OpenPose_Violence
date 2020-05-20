# Action Classification with OpenPose: Violence
## Project for Biometrics class @ Unisa, Summer 2020

###  Abstract
  
The aim of this project is to use a skeleton estimation performed through OpenPose, to classify if there is or not Violence in a given frame. As dataset, we used a subset of [Real Life Violence Situations Dataset](https://www.kaggle.com/mohamedmustafa/real-life-violence-situations-dataset) with exactly two people for each frame, that can be downloaded [here](https://gofile.io/d/bwIIOh). Both folders contains videos of violence/non violence situations, these have been framed (60fps) and each frame processed with OpenPose. Then we process the data in order to check if two people have been detected and save the data in a 100-feature .csv dataset. The feature used are basically X, Y coordinates of each detected body part, with a feature that indicates the distance from the camera, and some features to indicate the distance between body parts of people (eg. Nose of person 1, with hand of person 2). Then the training has been performed with a normal neural network and the achieved accuracy for the main model is around 98%.


### To install requirements full requirements:
```
conda create --name envName --file requirements_full.txt
```
Main requirements: 
```
cudatoolkit==10.0.130-0
keras=2.3.1
opencv=4.1.2
numpy=1.18.1
pandas=1.0.3
scikit-learn=0.22.2
scipy=1.3.3
tensorflow=2.0.0

```
### References
OpenPose implementation used: [Tensorflow 2.0 Realtime Multi-Person Pose Estimation](https://github.com/michalfaber/tensorflow_Realtime_Multi-Person_Pose_Estimation)
