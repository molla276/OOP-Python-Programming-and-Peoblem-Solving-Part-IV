import pandas as pd
data = pd.read_csv('HR_comma_sep.csv')
# print(data.size)
#step1: missing data for any row any column
# print(data.isnull().values.any())
# step2: check data type
# print(data.dtypes)

# step3: Clean data
clean_up_values = {
    'salary' : {
        'low' : 1,
        'medium' : 2,
        'high' : 3
    }
}

data.replace(clean_up_values, inplace=True)
# print(data)

# step4: get dummies for the Department
dummies = pd.get_dummies(data.Department)
# print(dummies)

# step5: merge dummies (dummy columns) with the original data)
merged = pd.concat([data, dummies], axis='columns')
# print(merged)

# step6: Drop unnecessary columns
final_data = merged.drop(['Department', 'technical'], axis = 'columns')
print('Department' in list(merged.columns))