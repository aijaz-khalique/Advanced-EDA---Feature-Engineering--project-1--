import pandas as pd                     # importing library
pd.set_option("display.max_columns", None)    #display all columns in the terminal
pd.set_option("display.width", None)          #display all columns in the terminal
Data=pd.read_csv("C:/repository/DecodeLabs-Internship/Advanced EDA & Feature Engineering (project 1 )/DatasetforDataAnalytics.csv")   #load data

print(Data.head(10))                            #  print first 10 rows 
print("rows and columns=\n ",Data.shape)
print("columns names=\n ",Data.columns)
print("Data types of each column=\n ",Data.dtypes)
print("how many missing value in each column=\n ",Data.isnull().sum())
print("General Information about Data=\n ")
Data.info()

print("Statistical information: ",Data.describe())                      #max, min , mean ,std and other statistical info
print(Data["PaymentMethod"].value_counts())                         # count unique values of column
print(Data["OrderStatus"].value_counts())
print(Data["ReferralSource"].value_counts())
print(Data["Product"].value_counts())
print("Duplicate row= ",Data.duplicated().sum())       
print("Datatype of DATE column= ",Data["Date"].dtype)

Data["CouponCode"]=Data["CouponCode"].fillna("Not Applied")                          #replace missing values with Not Applied
print(Data["CouponCode"].isnull().sum())                                              # verifing it


check_outliers=Data[["Quantity","UnitPrice","ItemsInCart","TotalPrice"]]                #now checking outliers i take 4 numerical data columns 
print(check_outliers)                    
print("length of columns= ",len(check_outliers))
columns=check_outliers.columns
print("column names= ",columns)
for column in columns:
    
    print(column)
    Q1=check_outliers[column].quantile(0.25)
    Q3=check_outliers[column].quantile(0.75)
    IQR=Q3-Q1
    lower_limit=Q1-(1.5*IQR)
    upper_limit=Q3+(1.5*IQR)
    print("upper limit= ",upper_limit,"\nlower limit= ",lower_limit) 
    Outliers=Data[(check_outliers[column]<lower_limit) | (check_outliers[column]>upper_limit)]                    #finding outliers through filtering
    print(Outliers)
    print("number of outliers= ",len(Outliers),"\n","-"*50)




Discount_Applied=[]                                                            #first feature is Discount applied or not
for CouponCode in Data["CouponCode"]:
    if CouponCode=="Not Applied":
        Discount_Applied.append("NO")
    else:
        Discount_Applied.append("YES")
Data["Discount Applied"]=Discount_Applied
print(Data[["CouponCode","Discount Applied"]])


Data["Date"]=pd.to_datetime(Data["Date"])                    #second feature month of sale this is help us to analize in which month sales was higher
Data["order month"]=Data["Date"].dt.month_name()
print(Data[["Date","order month"]])

print(Data["TotalPrice"].describe())                     #third feature order value category this will also help us to understand patterns related with months and prices   
OrderValueCategory=[]
for price in Data["TotalPrice"]:
    if price>2000:
        OrderValueCategory.append("High")
    elif price<1000:
        OrderValueCategory.append("Low")
    else:
        OrderValueCategory.append("Medium")
Data["OrderValueCategory"]=OrderValueCategory
print(Data[["TotalPrice","OrderValueCategory"]])


Data.to_csv("cleaned_dataset.csv",index=False)                  # making new csv file in which data is clear and ready for training to model
