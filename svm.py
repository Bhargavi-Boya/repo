#https://intellipaat.com/community/20304/a-column-vector-y-was-passed-when-a-1d-array-was-expected
scores = []
C_hyp=[0.001, 0.01 , 0.1, 1, 10, 100, 300]
best_svr = SVR(kernel='rbf',C=1.0)
cv = KFold(n_splits=3, random_state=42, shuffle=False)
for i in C_hyp:
    print("Value of hyper parameter C : ",i)
    for train_index, test_index in cv.split(X_train_scaled_df_imp_feat):
         = SVR(kernel='rbf',C=i)
        X_train, X_test, y_train, y_test = X_train_scaled_df_imp_feat.iloc[train_index],\
        X_train_scaled_df_imp_feat.iloc[test_index], y.iloc[train_index], y.iloc[test_index]

        best_svr.fit(X_train, y_train)
        y_pred=best_svr.predict(X_test)
        scores.append(best_svr.score(X_test, y_test))
        print('\nMAE for SVR: ', round(mean_absolute_error(y_pred, y_test.values.ravel()),3 ))
    print(100*"=")
