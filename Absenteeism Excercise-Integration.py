from absenteeism_module import *
import pymysql

# print(pd.read_csv('Absenteeism_new_data.csv'))
model = absenteeism_model('model', 'scaler')
model.load_and_clean_data('Absenteeism_new_data.csv')
model.predicted_outputs()
