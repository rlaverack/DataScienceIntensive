import pandas as pd
from pandas import DataFrame
import pyproj

#Load csv to DataFrame

landslides_df = pd.read_csv('NOSLIDE_SLOPE.csv')

#Define Coordinate Transformation
p1 = pyproj.Proj(init='epsg:4326')
p2 = pyproj.Proj(init='epsg:5070')

#Loop Through Rows in DataFrame
df = DataFrame(columns=['X_new','Y_new'])
i = 0
print('Start Conversion')
for x_i, y_i in zip(landslides_df['X'],landslides_df['Y']):
    #Transform coordinates
    x_rep, y_rep = pyproj.transform(p1, p2, x_i, y_i)
    #Define DataFrame to append to df DataFrame
    df_add = DataFrame([[x_rep, y_rep]],columns=['X_new','Y_new'])
    frames = [df,df_add]
    df = pd.concat(frames,ignore_index=True)
    if i % 500 == 0:
        print(i)
    i+=1
print('Conversion Complete')
#Add df DataFrame onto landslides DataFrame
landslides = [landslides_df,df]
landslides_df = pd.concat(landslides,axis=1)
#export csv with transformed coordinates
print('Saving...')
landslides_df.to_csv('nolandslides_new_coor.csv')
