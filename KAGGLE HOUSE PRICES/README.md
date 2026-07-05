# House Prices - Advanced Regression Techniques

- **Competition:** Kaggle House Prices (Baseline Submission)
- **Model:** RandomForestRegressor (n_estimators=100)
- **Features Used:** Numeric columns only — dropped all categorical 
  features (Neighborhood, HouseStyle, SaleCondition, etc.)
- **Preprocessing:** Dropped high-null columns (PoolQC, MiscFeature, 
  Alley, Fence, FireplaceQu), filled remaining nulls with median, 
  dropped Id column
- **Score:** 0.15366 RMSLE (public leaderboard)
- **Key Learning:** RMSLE penalizes underestimating expensive houses 
  more than raw RMSE. Correlation analysis showed GarageCars and 
  GarageArea are redundant — both proxy for house size/quality already 
  captured by OverallQual and GrLivArea.
- **Known Limitation:** Dropping all categorical features leaves 
  significant accuracy on the table — Neighborhood alone is typically 
  a top-5 predictor in this dataset. Next iteration needs 
  OneHotEncoder/ColumnTransformer to include them.