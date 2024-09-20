import pandas as pd

#function to load json data into pandas dataframe
def load_data(filepath):
    df = pd.read_json(filepath)
    return df

#Function to convert duration fields into seconds
def convert_duration(strings):
    splitted = strings.split(":")
    day_hour = splitted[0].split(".")
    day = 0
    if len(day_hour)>1:
        day = float(day_hour[0])
        hour = float(day_hour[1])
    else:
        hour = float(day_hour[0])
    minutes = float(splitted[1])
    seconds = float(splitted[2])
    total_seconds = (day*86400)+(hour*3600)+(minutes*60)+seconds
    return total_seconds

#Apply field conversion and change data types of columns
def data_transform(df):
    columns = df.columns.tolist()
    #find duration columns
    duration_columns = [col for col in columns if "duration" in col.lower()]
    for col in duration_columns:
        df[col] = df[col].apply(lambda x: convert_duration(x))
    #Change datatype of datetime columns
    datetime_columns = ["nextTripStart", "start", "stop"]
    for col in datetime_columns:
        df[col] = pd.to_datetime(df[col], format = "ISO8601")

    #Additional step to drop duplicate values(not required for given json file)
    df.drop_duplicates(inplace = True)
    return df

#Save cleaned data in parquet file
def save_output(df, output_path):
    df.to_parquet(output_path, index = False)

if __name__ == "__main__":
    input_file_path = "./input/trip_data.json"
    output_path = "./output/trip_data.parquet"
    
    data = load_data(input_file_path)
    output_data = data_transform(data)
    print(output_data)
    save_output(output_data, output_path)


 