# predict_flower_species

1.Problem_Statement:

This data set consists of the physical parameters of three species of flower — Versicolor, Setosa and Virginica.
The numeric parameters which the dataset contains are Sepal width, Sepal length, Petal width and Petal length. 
In this data we will be predicting the classes of the flowers based on these parameters.
The data consists of continuous numeric values which describe the dimensions of the respective features.
We will be training the model based on these features.

    

2.Dataset:

    The dataset was downloade from kaggle website
["IRIS_DATASET"](https://www.kaggle.com/datasets/uciml/iris/download?datasetVersionNumber=2)

3.Packages_Required:

    All the packages required for model building are mentioned in requirement.txt file

4.Dataset_Reading:

    Done using pandas library as follows:

        df = pd.read_csv('Iris_data.csv')

        df

5.Model_Building:

    Algorithm used : Logistic Regression

    Steps:

    Following steps involved in model building

    1.Exploratory_Data_Analysis

    2.Feature_Engineering

    3.Feature_selection

    4.Data_Splitting

    5.Model_Training

    6.Model_Evaluation

    7.Single_Row_Check

    8.Pickle file_Creation

    9.Json file_Creation

6.API_Writing:

    API writing for builded model was done in VS Code with help of flask web framework, along with HTML code.

    Model data required for writing api importted through pickle file and json file

    It was then tested using Postman app.

    command to run flask app in vs code:

    flask run

    or

    python app.py

7.GIT_Repository:

    All the project related file are uploded to Git hub cloud by making it's repository.

    Mainly three commands are used for this purpose:
    git add
    git commit
    git push


8.Deployment_On_Cloud:

    Build model was deployed on cloud using Amazon web services's EC2 instance and Git Bash terminal

    command to run app in Git Bash

    python3 app.py