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

---

### Underfitting and Overfitting Complete
* **Concept Mastered:** How tree depth controls the underfitting/overfitting tradeoff
* **Key Tool:** `max_leaf_nodes` parameter to control tree size
* **Method:** Looped through candidate values [5, 25, 50, 100, 250, 500], calculated MAE for each, selected best
* **Final Result:** Identified optimal `max_leaf_nodes` value using validation MAE

---

### Random Forests Complete
* **Concept Mastered:** Random Forest builds many trees and averages predictions, canceling out individual tree errors
* **Model Used:** `RandomForestRegressor` from `sklearn.ensemble`
* **Result:** Validation MAE of 21,857 vs Decision Tree's 29,652 — same data, better model, zero extra tuning
* **Key Insight:** More trees = errors cancel out = better predictions than any single tree