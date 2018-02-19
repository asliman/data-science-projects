# Titanic Data Science 
### questions:

In this project, I train a model to determine whether passengers are survived or not during the tragic shipwreck, based on the features provided such as gender, cabin class, age and etc. 
### Workflow
1. Question or problem definition.
2. Acquire training and testing data.
3. Wrangle, prepare, cleanse the data.
4. Analyze, identify patterns, and explore the data.
5. Model, predict and solve the problem.
6. Visualize, report, and present the problem solving steps and final solution.
7. Supply or submit the results.


* I look at each features and decide which features to keep for the training of model.
* I drop PassengerId,Name,Ticket as they do not predict survival.
* Cabin is dropped because too many NaN.
* Survival rate is higher when Fare is higher.
* Embark: survival rate: C>Q>S. we should keep the feature.
* I combine Parch and SibSp into Family size. Having family the survival rate is higher.
* Sex is the strongest feature in deciding survival rate.
* Pclass also a good indicator.

I train several algorithms ( decision tree, SVM and SGDClassifier) and use precision/recall to examine the models.



