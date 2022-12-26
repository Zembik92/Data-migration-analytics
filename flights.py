import os
import glob
import pandas as pd
from IPython.display import display



class Datamigration:

    def __init__(self) -> None:
        self.df_list = []
        self.path = r"C:/Users/kambo/Documents/AiCore Data Analytics/data/"
        self.all_files = glob.glob(os.path.join(self.path, "*.csv"))




    def load_clean_data(self):
        '''Method to load all csv files in a dataframe and drop columns that contain all nulls
           and replacing cells containing nulls with zeros, finally appending all dataframes to an empty list'''
        for filename in self.all_files:
            data_frame = pd.read_csv(filename)
            display(data_frame.head())
            num_rows = sum(data_frame.isnull().any(axis=1))
            drop_null_columns = data_frame.dropna(axis=1, how="all")
            replace_with_zeros = drop_null_columns.fillna(0)
            self.df_list.append(replace_with_zeros)
            print("The number of rows containing null values in", filename, "is", num_rows)
            
            

    def data_intergration(self):    
        '''Concatinating all dataframes into one and filling empty columns will zeros, 
           then write it to a csv file'''    
        combined_data_frame = pd.concat(self.df_list, axis=0, ignore_index=True).fillna(0)
        combined_data_frame.to_csv(r"C:\Users\kambo\Documents\AiCore Data Analytics\combined_data.csv", sep=",", header=True, index=False)
        display(combined_data_frame.head())    

    

def load():     
    dataloader = Datamigration()
    dataloader.load_clean_data()
    dataloader.data_intergration()
    



if __name__ == '__main__':
    load()


