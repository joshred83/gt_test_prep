

monzersaleh_data_wrangling_question_1 = {
    'question': "What is the purpose of cross-validation in model evaluation?",
    'options_list': [
        'To increase the size of the training dataset.',
        'To estimate the prediction error and avoid overfitting.',
        'To remove outliers from the dataset.',
        'To perform hyperparameter tuning.'
    ],
    'correct_answer': 'To estimate the prediction error and avoid overfitting.',
    'explanation': "Cross-validation is used to estimate the prediction error of a model and help prevent overfitting by using different subsets of the data for training and testing.",
    'chapter_information': 'Monzersaleh Notes on Data Wrangling'
}

monzersaleh_data_wrangling_question_2 = {
    'question': "Which method can be used to handle class imbalance in a dataset?",
    'options_list': [
        'Dropping the minority class.',
        'Using the SMOTE technique.',
        'Ignoring the imbalance and proceeding with training.',
        'Removing all duplicate samples from the majority class.'
    ],
    'correct_answer': 'Using the SMOTE technique.',
    'explanation': "SMOTE (Synthetic Minority OverSampling Technique) is a method used to handle class imbalance by generating synthetic samples for the minority class.",
    'chapter_information': 'Monzersaleh Notes on Data Wrangling'
}

monzersaleh_data_wrangling_question_3 = {
    'question': "What is the main goal of data pre-processing in deep learning?",
    'options_list': [
        'To increase the dimensionality of the dataset.',
        'To improve model convergence by scaling and normalizing data.',
        'To create new features from the existing dataset.',
        'To decrease the model’s computational complexity.'
    ],
    'correct_answer': 'To improve model convergence by scaling and normalizing data.',
    'explanation': "Data pre-processing, such as scaling and normalizing, helps improve model convergence and stability during training.",
    'chapter_information': 'Monzersaleh Notes on Data Wrangling'
}

monzersaleh_data_wrangling_question_4 = {
    'question': "What does the term 'missing at random' imply in the context of missing data?",
    'options_list': [
        'The likelihood of a data observation being missing depends on other observed data features.',
        'The likelihood of a data observation being missing is completely random.',
        'The missing data is related to unobserved outcomes.',
        'The missing data can be ignored without any consequences.'
    ],
    'correct_answer': 'The likelihood of a data observation being missing depends on other observed data features.',
    'explanation': "'Missing at random' means that the likelihood of a data observation being missing depends on other observed features, which can guide the imputation process.",
    'chapter_information': 'Monzersaleh Notes on Data Wrangling'
}

monzersaleh_data_wrangling_question_5 = {
    'question': "What is the key advantage of using Focal Loss over Cross Entropy in classification tasks?",
    'options_list': [
        'It simplifies the model architecture.',
        'It down-weights easy examples, focusing more on hard examples.',
        'It reduces the size of the training dataset.',
        'It improves model interpretability.'
    ],
    'correct_answer': 'It down-weights easy examples, focusing more on hard examples.',
    'explanation': "Focal Loss is designed to down-weight easy examples, which allows the model to focus more on difficult and rare examples during training.",
    'chapter_information': 'Monzersaleh Notes on Data Wrangling'
}

lesson_4_1_data_cleaning_mpc_question_1 = {
    'question': "Which of the following best describes Missing Not at Random (MNAR) data?",
    'options_list': [
        "A) Data missing completely without any identifiable pattern",
        "B) Data missing due to observed characteristics like gender or age",
        "C) Data missing due to unobserved features, such as a respondent not answering a question based on their depression level",
        "D) Data missing randomly due to technical issues"
    ],
    'correct_answer': 'C',
    'explanation': "Missing Not at Random (MNAR) refers to data missing based on unobserved features, such as depression affecting someone's likelihood to answer a question.",
    'chapter_information': 'Lesson 4.1: Data Cleaning'
}

lesson_4_1_data_cleaning_mpc_question_2 = {
    'question': "What is one major drawback of handling missing data by dropping rows?",
    'options_list': [
        "A) It introduces bias into the model",
        "B) It is computationally expensive",
        "C) It results in the loss of valuable data",
        "D) It requires complex algorithms to execute"
    ],
    'correct_answer': 'C',
    'explanation': "Dropping rows with missing values is simple, but it can result in a significant loss of data, reducing the size and value of the dataset.",
    'chapter_information': 'Lesson 4.1: Data Cleaning'
}

lesson_4_1_data_cleaning_mpc_question_3 = {
    'question': "Which data transformation would be appropriate for an image dataset used in a neural network model?",
    'options_list': [
        "A) Converting images from RGB to grayscale",
        "B) Tokenizing text using bag-of-words",
        "C) Normalizing text data using TF-IDF",
        "D) Imputing missing values with the median"
    ],
    'correct_answer': 'A',
    'explanation': "Converting RGB images to grayscale is a transformation that reduces data size and is often used for image-based machine learning models.",
    'chapter_information': 'Lesson 4.1: Data Cleaning'
}

lesson_4_1_data_cleaning_tf_question_1 = {
    'question': "Normalization ensures that each feature has a mean of zero.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'False',
    'explanation': "Normalization scales data to a specific range (e.g., 0 to 1), whereas mean subtraction is the process that zero-centers the data.",
    'chapter_information': 'Lesson 4.1: Data Cleaning'
}

lesson_4_1_data_cleaning_tf_question_2 = {
    'question': "Using inverse depth normalization improves numerical stability for depth estimation models.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'True',
    'explanation': "Inverse depth normalization is used in depth estimation tasks to improve the model's numerical stability and error distribution.",
    'chapter_information': 'Lesson 4.1: Data Cleaning'
}


lesson_4_2_managing_bias_mpc_question_1 = {
    'question': "Which of the following is an example of classification parity in fairness?",
    'options_list': [
        "A) A model that avoids using protected attributes like race and gender",
        "B) A model where the false positive rates are similar across different demographic groups",
        "C) A model that predicts outcomes independently of race or gender",
        "D) A model that uses a standardized dataset for training"
    ],
    'correct_answer': 'B',
    'explanation': "Classification parity refers to ensuring similar performance metrics, such as false positive rates, across different groups.",
    'chapter_information': 'Lesson 4.2: Managing Bias'
}

lesson_4_2_managing_bias_mpc_question_2 = {
    'question': "What is calibration in the context of fairness in machine learning?",
    'options_list': [
        "A) Ensuring the model has similar false positive rates for all groups",
        "B) Ensuring the predicted risk estimate is independent of protected attributes like race",
        "C) Ensuring the model is trained on balanced datasets",
        "D) Ensuring that protected attributes are not used in the training process"
    ],
    'correct_answer': 'B',
    'explanation': "Calibration refers to ensuring that given a predicted risk estimate, the outcomes are independent of protected attributes like race or gender.",
    'chapter_information': 'Lesson 4.2: Managing Bias'
}

lesson_4_2_managing_bias_mpc_question_3 = {
    'question': "Which of the following describes anti-classification in fairness?",
    'options_list': [
        "A) Ensuring that models have similar performance across different groups",
        "B) Ensuring that protected attributes like race or gender are not used directly in making predictions",
        "C) Ensuring the model has a high level of accuracy",
        "D) Ensuring that false positive rates are minimized"
    ],
    'correct_answer': 'B',
    'explanation': "Anti-classification prevents models from directly using protected attributes like race or gender in predictions to avoid explicit bias.",
    'chapter_information': 'Lesson 4.2: Managing Bias'
}

lesson_4_2_managing_bias_tf_question_1 = {
    'question': "Bias testing is important in products like video calling devices to ensure fairness across all users.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'True',
    'explanation': "Bias testing ensures that devices like video calling products perform equally well for all users, regardless of characteristics such as skin tone or lighting conditions.",
    'chapter_information': 'Lesson 4.2: Managing Bias'
}

lesson_4_2_managing_bias_tf_question_2 = {
    'question': "The goal of fairness in machine learning is to make sure models only work well for the majority group of users.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'False',
    'explanation': "The goal of fairness in machine learning is to create inclusive products that work well for all users, reducing bias and ensuring equitable performance.",
    'chapter_information': 'Lesson 4.2: Managing Bias'
}

lesson_4_4_cross_validation_mpc_question_1 = {
    'question': "Which of the following methods is appropriate for addressing class imbalance?",
    'options_list': [
        "A) Under-sampling the majority class",
        "B) Adding more layers to the model",
        "C) Normalizing the dataset",
        "D) Using grid search for hyperparameter tuning"
    ],
    'correct_answer': 'A',
    'explanation': "Under-sampling the majority class is a method to balance class distributions, often used alongside other methods like oversampling the minority class.",
    'chapter_information': 'Lesson 4.4: Cross-Validation and Class Imbalance'
}

lesson_4_4_cross_validation_mpc_question_2 = {
    'question': "In K-Fold Cross-Validation, how many times is the model trained and evaluated?",
    'options_list': [
        "A) Once, using a test set",
        "B) Twice, using a validation set",
        "C) K times, each time on a different partition of the data",
        "D) K-1 times, ignoring one fold"
    ],
    'correct_answer': 'C',
    'explanation': "In K-Fold Cross-Validation, the dataset is split into K parts, and the model is trained and evaluated K times, each time using a different fold for testing.",
    'chapter_information': 'Lesson 4.4: Cross-Validation and Class Imbalance'
}

lesson_4_4_cross_validation_mpc_question_3 = {
    'question': "Which of the following best describes the goal of Focal Loss in object detection models?",
    'options_list': [
        "A) To focus the model on easy examples to improve training speed",
        "B) To down-weight easy examples and focus on harder examples, reducing bias toward the majority class",
        "C) To balance the loss function by emphasizing background pixels",
        "D) To encourage the model to focus more on the background of images"
    ],
    'correct_answer': 'B',
    'explanation': "Focal Loss is used to down-weight easy examples and focus on harder-to-classify examples, which helps address class imbalance in object detection tasks.",
    'chapter_information': 'Lesson 4.4: Cross-Validation and Class Imbalance'
}

lesson_4_4_cross_validation_tf_question_1 = {
    'question': "When addressing class imbalance, oversampling the minority class before splitting the dataset can lead to data leakage.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'True',
    'explanation': "Oversampling the minority class before splitting the data can cause data leakage, where the same observations appear in both training and test sets, leading to overly optimistic model performance estimates.",
    'chapter_information': 'Lesson 4.4: Cross-Validation and Class Imbalance'
}

lesson_4_4_cross_validation_tf_question_2 = {
    'question': "Time-Series Cross-Validation ensures that testing is done on future data and training on historical data, avoiding look-ahead bias.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'True',
    'explanation': "Time-Series Cross-Validation ensures that models are trained on historical data and tested on future data, preventing look-ahead bias, which is crucial in time-sensitive datasets.",
    'chapter_information': 'Lesson 4.4: Cross-Validation and Class Imbalance'
}

lesson_4_3_data_wrangling_mpc_question_1 = {
    'question': "Which of the following is a key challenge during data wrangling?",
    'options_list': [
        "A) Hyperparameter tuning",
        "B) Addressing class imbalance",
        "C) Selecting a neural network architecture",
        "D) Data augmentation for image datasets"
    ],
    'correct_answer': 'B',
    'explanation': "Addressing class imbalance is a common challenge during data wrangling, especially in binary classification problems.",
    'chapter_information': 'Lesson 4.3: Data Wrangling'
}

lesson_4_3_data_wrangling_mpc_question_2 = {
    'question': "Which sampling technique divides the population into groups (strata) and randomly samples from each group?",
    'options_list': [
        "A) Simple Random Sampling",
        "B) Systematic Sampling",
        "C) Stratified Random Sampling",
        "D) Cluster Sampling"
    ],
    'correct_answer': 'C',
    'explanation': "Stratified Random Sampling divides the population into groups and ensures that each group is represented by sampling from each stratum.",
    'chapter_information': 'Lesson 4.3: Data Wrangling'
}

lesson_4_3_data_wrangling_mpc_question_3 = {
    'question': "Which of the following is an example of a data wrangling error that could lead to incorrect conclusions?",
    'options_list': [
        "A) Mislabeling treatment and control groups in an experiment",
        "B) Using a smaller learning rate during training",
        "C) Implementing batch normalization incorrectly",
        "D) Using dropout in convolutional layers"
    ],
    'correct_answer': 'A',
    'explanation': "Mislabeling treatment and control groups is a critical error that can lead to incorrect conclusions during data analysis.",
    'chapter_information': 'Lesson 4.3: Data Wrangling'
}

lesson_4_3_data_wrangling_tf_question_1 = {
    'question': "Data wrangling involves transforming and preparing data, ensuring that it is suitable for cross-validation and model evaluation.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'True',
    'explanation': "Data wrangling includes cleaning, transforming, and preparing data for reliable cross-validation and model evaluation.",
    'chapter_information': 'Lesson 4.3: Data Wrangling'
}

lesson_4_3_data_wrangling_tf_question_2 = {
    'question': "Simple random sampling ensures that each observation has an equal chance of being selected.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'True',
    'explanation': "Simple Random Sampling ensures that every observation in the population has an equal probability of being selected.",
    'chapter_information': 'Lesson 4.3: Data Wrangling'
}

lesson_4_5_prediction_evaluation_mpc_question_1 = {
    'question': "Which of the following is an evaluation metric used to determine if a model is well-calibrated in binary classification?",
    'options_list': [
        "A) Confusion Matrix",
        "B) Calibration Plot",
        "C) Mean-Squared Error",
        "D) ROC Curve"
    ],
    'correct_answer': 'B',
    'explanation': "Calibration plots compare predicted probabilities with the actual fraction of positives to determine if the model's predictions align with real outcomes, ensuring the model is well-calibrated.",
    'chapter_information': 'Lesson 4.5: Model Prediction and Evaluation'
}

lesson_4_5_prediction_evaluation_mpc_question_2 = {
    'question': "What type of prediction task would you be solving if the goal is to predict a continuous value?",
    'options_list': [
        "A) Binary classification",
        "B) Multi-class classification",
        "C) Regression",
        "D) Clustering"
    ],
    'correct_answer': 'C',
    'explanation': "Regression involves predicting continuous values, while classification focuses on assigning an observation to discrete categories.",
    'chapter_information': 'Lesson 4.5: Model Prediction and Evaluation'
}

lesson_4_5_prediction_evaluation_mpc_question_3 = {
    'question': "Which of the following is NOT a component of the confusion matrix?",
    'options_list': [
        "A) True Positives (TP)",
        "B) False Positives (FP)",
        "C) Mean-Squared Error (MSE)",
        "D) True Negatives (TN)"
    ],
    'correct_answer': 'C',
    'explanation': "Mean-Squared Error (MSE) is a metric used in regression tasks, not a component of the confusion matrix, which is used to evaluate classification performance.",
    'chapter_information': 'Lesson 4.5: Model Prediction and Evaluation'
}

lesson_4_5_prediction_evaluation_mpc_question_4 = {
    'question': "When ensuring reproducibility in machine learning, which of the following is the purpose of Model Cards?",
    'options_list': [
        "A) To document the training data, performance metrics, and evaluation procedures for a model.",
        "B) To summarize the architecture of neural networks used in deep learning.",
        "C) To describe the hyperparameters used in training neural networks.",
        "D) To record how missing data is handled in the dataset."
    ],
    'correct_answer': 'A',
    'explanation': "Model Cards are designed to document important details such as the training data, performance metrics, and evaluation methods for a trained model to ensure transparency and reproducibility.",
    'chapter_information': 'Lesson 4.5: Model Prediction and Evaluation'
}

lesson_4_5_prediction_evaluation_tf_question_1 = {
    'question': "Reproducibility is particularly challenging in AI due to the large number of factors like hyperparameter tuning and data choices that can affect model outcomes.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'True',
    'explanation': "AI models are sensitive to various factors, including hyperparameters and data preprocessing steps, which can make reproducibility more challenging.",
    'chapter_information': 'Lesson 4.5: Model Prediction and Evaluation'
}

lesson_4_5_prediction_evaluation_tf_question_2 = {
    'question': "A confusion matrix compares predicted probabilities with actual outcomes to evaluate the calibration of a model.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'False',
    'explanation': "A confusion matrix compares predicted class labels to actual class labels, while a calibration plot evaluates predicted probabilities against actual outcomes.",
    'chapter_information': 'Lesson 4.5: Model Prediction and Evaluation'
}

lesson_4_5_prediction_evaluation_tf_question_3 = {
    'question': "Baseline comparisons help contextualize model performance by providing a reference point, such as random guessing or existing models.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'True',
    'explanation': "Baseline comparisons, such as random guessing or performance from existing models, are crucial for understanding the value of a new model.",
    'chapter_information': 'Lesson 4.5: Model Prediction and Evaluation'
}




KC_MPC_QUESTIONS = []
global_items = list(globals().items())
# print(global_items)

for name, value in global_items:
    if not name.startswith('_'):
        KC_MPC_QUESTIONS.append(value)

WEEK_4_MPC = KC_MPC_QUESTIONS[:-1]
