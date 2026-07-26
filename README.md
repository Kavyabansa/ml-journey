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
- Feature importance — permutation vs built-in vs SHAP (all agree: Title #1 on Titanic)
- GridSearchCV vs RandomizedSearchCV — when to use each
- Fit time vs score tradeoff — more trees ≠ better score
- joblib — save and load trained models for production
- Feature engineering — TotalSF ranked #1 by SHAP on House Prices

**StatQuest videos watched:**
- ✅ Decision Trees Part 1 + Part 2
- ✅ Regression Trees
- ✅ Pruning Regression Trees
- ✅ Random Forests Part 1 + Part 2
- ✅ Bagging

---

## 📁 Repository Structure

```
ml-journey/
├── src/
│   └── utils.py               ← reusable evaluate_model() function
├── models/
│   ├── rf_best.pkl            ← best Titanic Random Forest (joblib)
│   └── house_prices_rf.pkl    ← best House Prices Random Forest (joblib)
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
└── week 3/
    ├── week3_day1_decision_trees.ipynb
    ├── week3_day2_overfitting_pruning.ipynb
    ├── week3_day3_random_forests.ipynb
    ├── week3_day4_shap_feature_importance.ipynb
    ├── week3_day5_hyperparameter_tuning.ipynb
    └── week3_day6_house_prices.ipynb
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
| House Prices | v2 | 0.14864 | Week 3 | RF + feature engineering ← top 40% ✅ |

---

## 🛠️ Skills Learned So Far

**Python:** lists, loops, functions, list comprehensions, OOP basics

**NumPy:** arrays, indexing, broadcasting, axis operations, boolean indexing

**Pandas:** DataFrames, groupby, merge, missing values, feature engineering

**Matplotlib + Seaborn:** line, bar, scatter, histogram, subplots, heatmaps

**Sklearn:**
- LinearRegression, Ridge, Lasso, LogisticRegression
- DecisionTreeClassifier, RandomForestClassifier, RandomForestRegressor
- Pipeline, ColumnTransformer
- StandardScaler, OneHotEncoder, SimpleImputer
- cross_val_score, cross_validate, StratifiedKFold, KFold
- GridSearchCV, RandomizedSearchCV
- permutation_importance, confusion matrix, classification report, ROC AUC
- joblib — model saving and loading

**SHAP:** TreeExplainer, summary plot, waterfall plot, feature importance

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
- Hyperparameter tuning — GridSearchCV vs RandomizedSearchCV
- SHAP values — local and global model explanations

---

## 📅 Next Up — Week 4
- SQL for ML workflows
- Window functions
- EDA at scale with ydata-profiling
- Missing data strategies — MCAR, MAR, MNAR
- Outlier detection — IQR, Z-score, IsolationForest
- Melbourne Housing data cleaning project
