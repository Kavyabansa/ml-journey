# ML Journey — Kavya Bansal

## 🎯 Goal
Get a 25+ LPA ML/AI job by 2028.
Currently: 3rd year B.Tech CSE (AI) student at NIET, Greater Noida.

---

## 📊 Progress Overview

| Phase | Status | Duration |
|-------|--------|----------|
| Phase 0 — Python Foundation | ✅ Complete | Jul 1–5, 2026 |
| Phase 1 — ML Fundamentals | 🔄 In Progress | Jul 6, 2026 – |
| Phase 2 — Deep Learning | ⏳ Upcoming | |
| Phase 3 — GenAI + LLMs | ⏳ Upcoming | |
| Phase 4 — MLOps + Deployment | ⏳ Upcoming | |

---

## ✅ Phase 0 — Python Foundation (Complete)

**What I learned:**
- Kaggle Learn Python — all 7 lessons
- NumPy — arrays, indexing, broadcasting, axis operations
- Pandas — all 6 lessons (groupby, merge, missing values)
- Matplotlib — line, bar, scatter, histogram, subplots

---

## 🔄 Phase 1 — ML Fundamentals (In Progress)

### Week 1 — Core ML Concepts ✅

| Day | Topic | Status |
|-----|-------|--------|
| Day 1 | Train/test split, cross validation from scratch | ✅ |
| Day 2 | NumPy, confusion matrix from scratch | ✅ |
| Day 3 | Titanic EDA — 5 visualizations, data cleaning | ✅ |
| Day 4 | Linear regression from scratch + sklearn verify | ✅ |
| Day 5 | Logistic regression + gradient descent from scratch | ✅ |
| Day 6 | Titanic baseline project — Kaggle submission | ✅ |

**Week 1 Kaggle Score: 0.782**

**Key projects:**
- Linear regression from scratch — R² matches sklearn exactly
- Logistic regression with gradient descent — 1000 epochs
- Titanic baseline — 81.48% CV accuracy, 0.782 Kaggle score

---

### Week 2 — Sklearn Pipelines + Evaluation ✅

| Day | Topic | Status |
|-----|-------|--------|
| Day 1 | Ridge, Lasso regularization, alpha tuning | ✅ |
| Day 2 | sklearn Pipeline, cross_val_score | ✅ |
| Day 3 | Data leakage demonstration — 1.6% inflation proved | ✅ |
| Day 4 | cross_validate, StratifiedKFold, evaluate_model() | ✅ |
| Day 5 | Evaluation metrics, ROC AUC, imbalanced data | ✅ |
| Day 6 | Titanic v2 — full ColumnTransformer Pipeline | ✅ |

**Week 2 Kaggle Score: 0.775**

**Key concepts mastered:**
- Ridge (L2) vs Lasso (L1) — when to use each
- Pipeline prevents data leakage automatically
- StratifiedKFold for reliable classification evaluation
- Overfitting demo — Val RMSE 129.88 → 1.52 with Ridge
- Multicollinearity — AveRooms & AveBedrms correlated 0.7+
- AUC-ROC better than accuracy for imbalanced data

**Kaggle Learn completed:**
- ✅ Intermediate ML — all 6 lessons

**StatQuest videos watched:**
- ✅ Ridge Regression
- ✅ Lasso Regression
- ✅ ElasticNet
- ✅ Multiple Regression
- ✅ Ridge vs Lasso Visualized
- ✅ Odds and Log Odds

---

### Week 3 — Decision Trees, Random Forests, SHAP ✅

| Day | Topic | Status |
|-----|-------|--------|
| Day 1 | Decision Trees from scratch — Gini, info gain | ✅ |
| Day 2 | Overfitting + pruning — max_depth, ccp_alpha | ✅ |
| Day 3 | Random Forests + bagging + OOB score | ✅ |
| Day 4 | SHAP values + feature importance | ✅ |
| Day 5 | GridSearchCV + RandomizedSearchCV + joblib | ✅ |
| Day 6 | House Prices Kaggle competition | ✅ |

**Kaggle Scores:**
- Titanic v4 (RF constrained depth=5) : 0.78468 ← best Titanic score
- House Prices v2 (RF + feature engineering) : 0.14864 ← top 40% globally

**Key concepts mastered:**
- Gini impurity and information gain from scratch
- Overfitting — visualized train vs val curve across depths 1–20
- Bagging — simulated manually with bootstrap samples
- Random Forest — decorrelated trees via random feature subset at each split
- OOB score — free validation without separate val set
- SHAP values — explained individual predictions with waterfall plot
- Feature importance — permutation vs built-in vs SHAP
- GridSearchCV vs RandomizedSearchCV — when to use each
- joblib — save and load trained models for production
- Feature engineering — TotalSF ranked #1 by SHAP on House Prices

**StatQuest videos watched:**
- ✅ Decision Trees Part 1 + Part 2
- ✅ Regression Trees
- ✅ Pruning Regression Trees
- ✅ Random Forests Part 1 + Part 2
- ✅ Bagging

---

### Week 4 — SQL + Data Engineering ✅

| Day | Topic | Status |
|-----|-------|--------|
| Day 1 | SQL foundations — SELECT, WHERE, GROUP BY, JOINs | ✅ |
| Day 2 | Window functions — ROW_NUMBER, RANK, LAG, LEAD | ✅ |
| Day 3 | EDA at scale — ydata-profiling, distributions, Q-Q plot | ✅ |
| Day 4 | Missing data — MCAR/MAR/MNAR, imputation comparison | ✅ |
| Day 5 | Outlier detection — IQR, Z-score, IsolationForest | ✅ |
| Day 6 | Melbourne Housing — full data cleaning pipeline | ✅ |

**Key concepts mastered:**
- SQL — SELECT, WHERE, GROUP BY, HAVING, ORDER BY, LIMIT
- SQL JOINs — INNER vs LEFT JOIN with real examples
- Window functions — ROW_NUMBER, RANK, DENSE_RANK, LAG, LEAD, running totals
- SQLite in Python — pd.read_sql(), to_sql()
- ydata-profiling — automated EDA report generation
- Skewness and kurtosis — log transformation fixes both
- Q-Q plot — checking normality of distributions
- Missing data types — MCAR, MAR, MNAR classification
- Imputation comparison — Drop < Simple < KNN < Iterative (best)
- Missingness indicators — binary flags capture MNAR signal
- IQR outlier detection from scratch
- Z-score outlier detection from scratch
- IsolationForest — multivariate outlier detection
- Outlier removal impact — IsoForest cleaning improved RMSE by 9.8%

**Reusable functions added to src/utils.py:**
- ✅ evaluate_model() — cross-validated accuracy + F1
- ✅ eda_summary() — quick dataset overview
- ✅ report_missing() — missing value analysis with strategy

**SQL key finding:**
Female 1st class → 96.81% survival vs Male 3rd class → 13.54%
Gap of 83.27% — found in one SQL query, verified with Pandas ✅

---

### Week 5 — XGBoost + LightGBM 🔄

| Day | Topic | Status |
|-----|-------|--------|
| Day 1 | XGBoost — first model, Titanic + House Prices | ✅ |
| Day 2 | XGBoost tuning — early stopping, hyperparameters | 🔄 |
| Day 3 | LightGBM — faster gradient boosting | ⏳ |
| Day 4 | Advanced feature engineering | ⏳ |
| Day 5 | Model stacking + ensembling | ⏳ |
| Day 6 | House Prices v3 — full pipeline | ⏳ |

**Kaggle Scores (Week 5 so far):**
- House Prices v4 (XGBoost) : 0.12930 ← new best 🏆

---

## 📁 Repository Structure

```
ml-journey/
├── src/
│   └── utils.py               ← evaluate_model(), eda_summary(), report_missing()
├── models/
│   ├── rf_best.pkl            ← best Titanic Random Forest
│   └── house_prices_rf.pkl    ← best House Prices Random Forest
├── week1/
│   ├── week1_day1_ml_intro.ipynb
│   ├── week1_day2_numpy.ipynb
│   ├── week1_day3_titanic_eda.ipynb
│   ├── week1_day4_linear_regression.ipynb
│   ├── week1_day5_logistic_regression.ipynb
│   └── week1_day6_titanic_baseline.ipynb
├── week 2/
│   ├── week2_day1_regularization.ipynb
│   ├── week2_day3_cross_validation.ipynb
│   ├── week2_day4_cross_validation_deep.ipynb
│   ├── week2_day4_evaluation_metrics.ipynb
│   └── week2_day6_titanic_v2_pipeline.ipynb
├── week 3/
│   ├── week3_day1_decision_trees.ipynb
│   ├── week3_day2_overfitting_pruning.ipynb
│   ├── week3_day3_random_forests.ipynb
│   ├── week3_day4_shap_feature_importance.ipynb
│   ├── week3_day5_hyperparameter_tuning.ipynb
│   └── week3_day6_house_prices.ipynb
├── week 4/
│   ├── week4_day1_sql_for_ml.ipynb
│   ├── week4_day2_window_functions.ipynb
│   ├── week4_day3_eda_at_scale.ipynb
│   ├── week4_day4_missing_data.ipynb
│   ├── week4_day5_outlier_detection.ipynb
│   └── week4_day6_melbourne_cleaning.ipynb
└── week 5/
    ├── week5_day1_xgboost.ipynb
    └── week5_day2_xgboost_tuning.ipynb
```

---

## 🏆 Kaggle Scores

| Competition | Version | Score | Week | Notes |
|-------------|---------|-------|------|-------|
| Titanic | v1 | 0.78229 | Week 1 | Logistic Regression |
| Titanic | v2 | 0.77511 | Week 2 | ColumnTransformer Pipeline |
| Titanic | v3 | 0.76794 | Week 3 | RF depth=None (overfit) |
| Titanic | v4 | 0.78468 | Week 3 | RF depth=5 ← best ✅ |
| House Prices | v1 | 0.15197 | Week 3 | Basic Random Forest |
| House Prices | v2 | 0.14864 | Week 3 | RF + feature engineering |
| House Prices | v3 | 0.12930 | Week 5 | XGBoost ← new best 🏆 |

---

## 🛠️ Skills Learned So Far

**Python:** lists, loops, functions, list comprehensions, OOP basics

**NumPy:** arrays, indexing, broadcasting, axis operations, boolean indexing

**Pandas:** DataFrames, groupby, merge, missing values, feature engineering

**Matplotlib + Seaborn:** line, bar, scatter, histogram, subplots, heatmaps, pairplots

**SQL:** SELECT, WHERE, GROUP BY, HAVING, ORDER BY, JOINs, Window Functions

**Sklearn:**
- LinearRegression, Ridge, Lasso, LogisticRegression
- DecisionTreeClassifier, RandomForestClassifier, RandomForestRegressor
- Pipeline, ColumnTransformer
- StandardScaler, OneHotEncoder, OrdinalEncoder, SimpleImputer, KNNImputer
- cross_val_score, cross_validate, StratifiedKFold, KFold
- GridSearchCV, RandomizedSearchCV
- IsolationForest, permutation_importance
- confusion matrix, classification report, ROC AUC
- joblib — model saving and loading

**Gradient Boosting:** XGBoost (classifier + regressor), early stopping

**SHAP:** TreeExplainer, summary plot, waterfall plot

**ML Concepts:**
- Bias-variance tradeoff
- Train/val/test split — 70/15/15
- Cross validation — KFold, StratifiedKFold
- Data leakage — what it is and how to prevent it
- Regularization — Ridge (L2), Lasso (L1), ElasticNet
- Evaluation metrics — accuracy, precision, recall, F1, AUC-ROC, RMSE, MAE, R²
- Feature engineering — FamilySize, IsAlone, Title, TotalSF, HouseAge
- Multicollinearity detection
- Decision trees — Gini impurity, information gain, pruning
- Ensemble methods — bagging, random forests, OOB score
- Gradient boosting — XGBoost sequential tree learning
- Hyperparameter tuning — GridSearchCV vs RandomizedSearchCV
- SHAP values — local and global model explanations
- Missing data — MCAR, MAR, MNAR classification
- Outlier detection — IQR, Z-score, IsolationForest
- SQL for data analysis — window functions, JOINs, aggregations

---

## 📅 Next Up — Week 5 (continuing)
- XGBoost early stopping + tuning
- LightGBM — faster gradient boosting
- Advanced feature engineering — target encoding
- Model stacking + ensembling
- House Prices below 0.13 (top 20%)
