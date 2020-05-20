# Action Classification with OpenPose: Violence
## Project for Biometrics class @ Unisa, Summer 2020

###  Abstract
  
The aim of this project is to use a skeleton estimation performed through OpenPose, to classify if there is or not Violence in a given frame. As dataset, we used a subset of [Real Life Violence Situations Dataset](https://www.kaggle.com/mohamedmustafa/real-life-violence-situations-dataset) with exactly two people for each frame, that can be downloaded [here](https://gofile.io/d/bwIIOh). Both folders contains videos of violence/non violence situations, these have been framed (60fps) and each frame processed with OpenPose. Then we process the data in order to check if two people have been detected and save the data in a 100-feature .csv dataset. The feature used are basically X, Y coordinates of each detected body part, with a feature that indicates the distance from the camera, and some features to indicate the distance between body parts of people (eg. Nose of person 1, with hand of person 2). Then the training has been performed with a normal neural network and the achieved accuracy for the main model is around 98%.


### Prerequisites:
Download the dataset [here](https://gofile.io/d/bwIIOh).  
Download the model [here](https://gofile.io/d/Fq1iHY).  
Install requirements file:  
```
conda create --name envName --file requirements_full.txt
```
Otherwise the main requirements are:
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

### Script and Notebooks description:
**- dataset.csv** and **datasetNoZero.csv**: these are the dataset used for training the neural network. In the second file all missing values have been filled with a valid value, while in the first one, missing values have been left untouched.  
**- detect_body_parts.ipynb**: in this notebook has been performed all the operation for extracting body parts coordinates and calculating the distances.  
**- dataset_framing** Folder: contains links for downloading the data and a notebook to perform the framing.   
**- calculateDistance.py**: this scripts contains the implementation of how distance between body parts have been calculated.  
**- openpose_example.ipynb**: this notebook shows the usage of openpose with some grafical examples.  
**- imputation.ipynb**: in this notebook is performed the imputation process, to generate the datasetNoZero file.  
**- model.ipynb**: this is the model of the Neural Network used.  

### References
OpenPose implementation used: [Tensorflow 2.0 Realtime Multi-Person Pose Estimation](https://github.com/michalfaber/tensorflow_Realtime_Multi-Person_Pose_Estimation)
