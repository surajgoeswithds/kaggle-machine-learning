# Intro to Machine Learning

### Building My First Model
* **Dataset:** Iowa Housing Data (Kaggle)
* **Goal:** Predict home sale prices based on spatial and structural features.
* **Model Used:** Scikit-learn `DecisionTreeRegressor`
* **What I Learned:** How to split a dataset into a target vector ($y$) and a feature matrix ($X$), handle missing values using `.dropna()`, and initialize/fit a model using reproducibility anchors (`random_state`).

---

### Model Validation Complete
* **Concept Mastered:** Overfitting, and why testing a model on its training data creates a dangerous "memorization" trap.
* **Metrics Applied:** Calculated Mean Absolute Error (MAE) using `val_y` and `val_predictions` to see the true real-world error.
* **Final Result:** Out-of-sample validation error came out to approximately $29,653.