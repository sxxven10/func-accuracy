#Accuracy calculation between predicted and actual numbers.
#Go to README
def return_result(X_test, name, pred, df):
    y_pred = pred
    y_actual = df.loc[X_test.index, name]
    result = pd.DataFrame({f'Predicted {name}': np.round(y_pred, 1), f'Actual {name}': y_actual, "Precision": y_pred / y_actual})
    return result
