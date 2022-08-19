import pymysql
import os

def load_history_weather(input_year):
    print(type(input_year), input_year)
    if(input_year > 2022):
        return "Input year should be a history year"
    
    Host = os.environ["Host"]
    User = os.environ['User']
    Password = os.environ['Password']
    
    con = pymysql.connect(host = Host, user = User, password = Password, database = 'damg', charset = "utf8")
    
    c = con.cursor()

    sql = "select DATE_FORMAT(date,'%%Y-%%m-%%d') dates, DATE_FORMAT(date,'%%m') months,precipitation,temp_max,temp_min,wind \
    from seattle_weather where year(date) = '%d'" % (input_year)

    try: 
        
        c.execute(sql)
        history_year_data = c.fetchall()
        print(f"Loaded history weather of {input_year}!")
        # print(history_year_data)
    except:
        print("Something went wrong")
    finally:
        c.close()
        con.close()
        
        return history_year_data

# load_history_weather(2018)