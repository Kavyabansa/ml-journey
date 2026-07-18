# src/utils.py
# Reusable ML utility functions

from sklearn.model_selection import cross_val_score, StratifiedKFold

def evaluate_model(pipeline, X, y, cv=5):
    """
    Evaluates a sklearn pipeline using StratifiedKFold.
    Returns dict with mean accuracy, std, mean F1.
    """
    skfold = StratifiedKFold(n_splits=cv)
    
    acc_scores = cross_val_score(pipeline, X, y,
                                 cv=skfold, scoring='accuracy')
    
    f1_scores  = cross_val_score(pipeline, X, y,
                                 cv=skfold, scoring='f1')
    
    results = {
        'mean_accuracy' : acc_scores.mean(),
        'std_accuracy'  : acc_scores.std(),
        'mean_f1'       : f1_scores.mean()
    }
    
    print("=" * 40)
    print("   MODEL EVALUATION")
    print("=" * 40)
    print(f"  Accuracy : {results['mean_accuracy']:.4f} ± {results['std_accuracy']:.4f}")
    print(f"  F1 Score : {results['mean_f1']:.4f}")
    print("=" * 40)
    
    return results