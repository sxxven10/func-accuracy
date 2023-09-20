# func-accuracy
python function - Accuracy calculation between predicted and actual numbers.
This function takes actual and predicted values and tells how accurate the model was. You should already have a list of predicted values. The function outputs a table.

About the table:
Predicted name: the column where the values predicted by the model are located.
Actual: actual values from the DataFrame.
Precision: how well the predicted value matches the actual value (pred / actual). The smaller the value, the less the model predicted relative to the actual value. The larger the value, the more the model predicted relative to the actual value.

About the function:
X_test: X_test from splitting the DataFrame into training and test sets.
name: the name of the column.
pred: a list of predicted values.
df: the name of the DataFrame.
