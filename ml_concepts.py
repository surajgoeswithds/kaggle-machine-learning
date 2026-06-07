# Q1. In notebook 1, you wrote y = home_data.SalePrice. What is y actually representing in the context of the problem? Why do we separate it from X?
#ans:'y' is known as real prices where as 'X' is known as features which is used to determine predictions 
# Q2. You wrote iowa_model.fit(X, y) in notebook 1, then in notebook 2 you wrote iowa_model.fit(train_X, train_y). What is the difference between these two fits, and why does notebook 2 do it differently?
# ans: fit(train_X, train_y) = train only on 75% so the other 25% is a fair test
# Q3. In notebook 2, the setup cell printed this:
#First in-sample predictions: [208500. 181500. 223500. 140000. 250000.]
#Actual target values:        [208500, 181500, 223500, 140000, 250000]
# ans: Perfect in-sample predictions = BAD. Model memorized, didn't learn.
# Q4. Your validation MAE came out as 29,652. What does that number actually mean in plain English — not the formula, what does it mean for this house price problem?
# ans: MAE 29652 = on average my prediction is wrong by $29,652
# Q5. Why did we need random_state=1 in train_test_split? What would happen if you removed it and ran the code twice?
# ans: random_state fixes the shuffle so same split happens every run, without it MAE changes each time because different houses end up in validation