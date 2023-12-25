# Car Insurance Claim Prediction with ML Algorithms and Imbalanced Dataset Handling

The Car Insurance Claim Prediction project aimed to develop a robust machine learning model capable of predicting whether a customer is likely to file an insurance claim based on various features. To address the challenge of an imbalanced dataset, I employed oversampling techniques, and hyperparameter tuning was performed to optimize the performance of five different classification algorithms: KNeigboursClassifiers, RandomForestClassifier, AdaboostClassifier, GaussianNB, and DecisionTreeClassifier.

# Key Components:

Dataset: The dataset used for this project contained information about customers, including vehicle information, policyholder information and historical claim data. The imbalanced nature of the dataset presented a challenge, as the number of positive (claim filed) instances was significantly lower than the negative instances.

Imbalanced Dataset Handling: To tackle the imbalance, oversampling techniques were applied to artificially increase the number of positive instances. This ensures that the machine learning models are trained on a more balanced dataset, preventing bias towards the majority class and improving the model's ability to accurately predict positive instances.

# Machine Learning Algorithms:

KNeigboursClassifiers: Utilized for its ability to classify instances based on the similarity of their neighbours.
RandomForest Classifier: Employed for its ensemble learning capability, combining multiple decision trees for improved accuracy and robustness.
Adaboost Classifier: Applied to boost the performance of weak learners, enhancing overall model accuracy.
GaussianNB: Leveraged for its simplicity and efficiency in handling continuous features.
DecisionTreeClassifier: Used to create a tree-like model of decisions, providing interpretability and insights into feature importance.
Hyperparameter Tuning: Each algorithm's hyperparameters were fine-tuned using techniques like grid search or random search to optimize the model's performance. This process aimed to find the best set of hyperparameters that maximizes predictive accuracy.

# Results and Evaluation:

The models were evaluated using standard classification metrics such as accuracy, precision, recall, and F1 score. This comprehensive evaluation helped in understanding the strengths and weaknesses of each algorithm in the context of car insurance claim prediction.

# Future Enhancements:

Feature Engineering: Explore additional features or engineer new ones to enhance the model's predictive power.

Ensemble Methods: Investigate the potential of creating ensemble models that combine the strengths of multiple algorithms for even better performance.

Continuous Monitoring: Implement a continuous monitoring system to ensure the model's effectiveness over time and adapt to changes in the data distribution.

# Conclusion:

The Car Insurance Claim Prediction project successfully addressed the challenges of imbalanced datasets and leveraged multiple machine learning algorithms. Through oversampling and hyperparameter tuning, the models achieved improved accuracy and robustness. This project sets the stage for further refinement and potential deployment in real-world scenarios to aid insurance companies in assessing and managing claim risks effectively.

# colab notebook link :
[https://colab.research.google.com/drive/1GoMg3NQYejfB2-C0u7B7Z7miYFBVWhbk?authuser=1#scrollTo=fak7bAcbVXno](https://colab.research.google.com/drive/1GoMg3NQYejfB2-C0u7B7Z7miYFBVWhbk?usp=sharing)https://colab.research.google.com/drive/1GoMg3NQYejfB2-C0u7B7Z7miYFBVWhbk?usp=sharing
