import pandas as pd

# Вариант 1
#melb_data_ps = pd.read_csv('project_1_Pandas/data/melb_data_ps.csv', sep=',')
#print (melb_data_ps.head())

# Вариант 2
#melb_data_ps = pd.read_csv('https://raw.githubusercontent.com/Yuri-VN/SkillFactory_DATA/main/project_1_Pandas/data/melb_data_ps.csv')
#print (melb_data_ps.head())

# Практика 1.
#citi_bike = pd.read_csv('https://raw.githubusercontent.com/Yuri-VN/SkillFactory_DATA/main/project_1_Pandas/data/citibike-tripdata.csv')
#print(citi_bike.head())

# Практика 2.
#melb_data_fe = pd.read_csv('https://raw.githubusercontent.com/Yuri-VN/SkillFactory_DATA/main/project_1_Pandas/data/melb_data_fe.csv')
#print(melb_data_fe.head())

# Практика 3. Датасет MovieLens
# MovieLens = pd.read_csv('project_1_Pandas/data/movies_data/movies.csv', sep=',')
# print (MovieLens.head())

# Практика 4. Датасет Ratings_MovieLens
# Ratings_MovieLens = pd.read_csv('project_1_Pandas/data/movies_data/ratings_movies.csv', sep=',')
# print (Ratings_MovieLens.head())

# Практика 5. Датасет orders_products
# orders_products = pd.read_csv('project_1_Pandas/data/orders_products/products.csv', sep=';')
# print (orders_products.head())

# Практика 6. Датасет covid_data
#covid_data = pd.read_csv('project_1_Pandas/data/covid_data/covid_data.csv', sep=',')
#print (covid_data.head())

# Практика 7. Датасет churn_data
#churn_data = pd.read_csv('project_1_Pandas/data/churn_data/churn.csv', sep=',')
#print (churn_data.head(3)) 

# Практика 8. Датасет sber_data
#sber_data = pd.read_csv('project_1_Pandas/data/sber_data/sber_data.csv', sep=',')
#print (sber_data.head(3))

# Практика 9. Датасет diabetes_data
#diabetes_data = pd.read_csv('project_1_Pandas/data/diabetes_data/diabetes_data.csv', sep=',')
#print (diabetes_data.head(3)) 

# Практика 10. Датасет hh_data
hh_data = pd.read_csv('project_1_Pandas/data/hh_data/dst-3.0_16_1_hh_database.csv', sep=';')
print (hh_data.shape)
print (hh_data.head(3))