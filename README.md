# Heart Disease Prediction

Simple project to determine the degree of narrowing blood vessel walls based on the features of the patient

## Tools used:
**Language:** Python<br>
**Libraries:** Numpy, Pandas, Seaborn<br>
**Frameworks:** Tensorflow, Keras, Scikit-Learn, Flask<br>

## Dataset:
The dataset is taken from [UCI](https://archive.ics.uci.edu/ml/datasets/heart+disease)<br>
**Features:**
* **age:** age in years
* **sex:** sex (1 = male; 0 = female)
* **cp:** chest pain type (1 = typical angina; 2 = atypical angina; 3 = non-anginal pain; 4 = asymptomatic)
* **trestbps:** resting blood pressure (in mm Hg on admission to the hospital)
* **chol:** serum cholestoral in mg/dl
* **fbs:** fasting blood sugar > 120 mg/dl (1 = true; 0 = false)
* **restecg:** resting electrocardiographic results (0 = normal; 1 = having ST-T wave abnormality; 2 = showing probable or definite left ventricular hypertrophy by Estes' criteria)
* **thalach:** maximum heart rate achieved
* **exang:** exercise induced angina (1 = yes; 0 = no)
* **oldpeak:** ST depression induced by exercise relative to rest
* **slope:** the slope of the peak exercise ST segment (1 = upsloping; 2 = flat; 3 = downsloping)
* **ca:** number of major vessels (0-3) colored by flourosopy
* **thal:** (3 = normal; 6 = fixed defect; 7 = reversable defect)
* **target:** diagnosis of heart disease (angiographic disease status) (0 = < 50% diameter narrowing; 1 = > 50% diameter narrowing)

## Analysis:
* [SOURCE](Analysis/Analysis.ipynb)
* The dataset has 13 features. The target variable is the last one
* There are 1025 entities in the dataset, each with their own feature values. Each entity represents a patient
* The dataset is already cleaned, with no null values
* Using the pandas correlation matrix and seaborn heatmap, we see:
    * oldpeak and exang are negatively correlated
    * cp and thalach are positively correlated
* From the above observation, it becomes clear that:
    * The chance of diameter narrowing reduces with exercise
    * Higher heart rate and chest pain indicates diameter narrowing
* Exercising regularly and maintaining a healthy heart rate can clearly reduce the chances of diameter narrowing

## Training:
* [SOURCE](Training/tf_model.ipynb)
* We drop the target variable from the dataset and use the remaining features to predict the target variable
* We will use 80% of the dataset for training the neural network
* The model we used is a simple sequential model, consisting of only 1 hidden layer
* The structure of the model is as follows:
    * Input layer: 64 neurons, ReLU activation
    * Hidden layer: 32 neurons, ReLU activation
    * Output layer: 1 neuron, Sigmoid activation
* Since the target is binary, we have used Sigmoid as the activation function of the output layer, and the optimizer is Adam
* Since the dataset is relatively small, we have created this simple NN structure and also are dropping 10% training data while leaving each layer. All this has been done to avoid overfitting
* Training accuracy is 83%
* Validation accuracy is 78%
* I have tried tweaking the hyper-parameters multiple times, but this seems to be the most optimal. I did not increase the complexity of the model just  for the sake of improving it's accuracy, since it will come at a cost of overfitting
* The model is saved in the file [heart_model.h5](model)
* As shown in the notebook, we can load the model and use it to predict the target variable for any new entity
* The model throws result in floating point numbers, while the target should be integer (binary)
* We converted the output to integer and then tested against an unseen dataset. The accuracy was 78%
* The model seems to have been properly trained

## Deployment:
* [SOURCE](app.py)
* We use Flask to deploy the model
* The HTML templates used have been stored in [templates](templates) directory
* The steps to use the model is as follows:
    * Run the Flask app:
  ```bash
    python app.py
  ```
    * Open the link (shown in the terminal) in the browser
    * Upload the .csv file containing the features of the patient (except the target variable ofcourse)
    * Click on the `Predict` button
    * You will be redirected to a new webpage that contains the result
    * **NOTE:** The predicted csv file is displayed in the webpage, i.e., in HTML form. You can manually download the predicted csv file by using pandas to convert the `data` dataframe present in `app.py` to a csv file and then saving it

