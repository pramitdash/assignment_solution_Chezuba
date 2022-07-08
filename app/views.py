from app import app, pd


@app.route("/1/queries/count/<DATE_PREFIX>", methods = ['GET'])
def fetch_data(DATE_PREFIX):
    prefix = DATE_PREFIX

    #creating the dataframe from the .tsv file and add the columns name
    df = pd.read_csv('hn_logs.tsv',sep = '\t', names=['date_time','url'])
    
    #converting the string date_time column to Date_time format by creating a new column
    df['Date'] = pd.to_datetime(df['date_time'])

    #setting the Date column as index of the dataframe
    df.set_index('Date', inplace=True)
      
    #counting the numbers of record according to our given date_time range  
    count = len(df[prefix].index)

    #adding the count value to the json object 
    result = {
        "count" : count
    }
    

    return result