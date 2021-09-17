def model(a,b,c,d,e):
    
    # Importing the necessary libraries
    import pandas as pd
    # import numpy as np
    from sklearn import linear_model

    # defining the data
    df = pd.read_csv("clean1.csv")
    x = df.iloc[:,1:6]
    y = df.iloc[:,7]

    # Model fitting
    model = linear_model.LinearRegression()
    model.fit(x,y)

    # Trying to correct some cofficient values
    # model.coef_[0] = 0.4
    # model.coef_[3] = 0.2
    # model.coef_[2] = 0.2
    # print(model.coef_[0],model.coef_[1],model.coef_[2],model.coef_[3],model.coef_[4])

    # Taking input
    modelInput = model.predict([[a,b,c,d,e]])

    return (modelInput * 100 / 2)

# if __name__ == "__main__":
#     a = int(input("Do you suffer from any kind of breathing issues?"))
#     b = int(input("Cold/Cough?"))
#     c = int(input("Fever?"))
#     d = int(input("Shortness of breath?"))
#     e = int(input("Taste disorders?"))
#     print(model(a,b,c,d,e))