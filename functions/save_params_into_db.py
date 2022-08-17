import pymysql
import os
# from functions.dbconfig import funct

def save_params_into_db(id, tdatetime, precipitation, temp_max, temp_min, wind, real_weather):
    # 上传数据到本地库
    # Host, User, Password = funct()
    Host = os.environ['Host']
    User = os.environ['User']
    Password = os.environ['Password']
    con = pymysql.connect(host = Host, user = User, password = Password, database = 'damg', charset = "utf8")
    c = con.cursor()
    id = id + "-airflow"
    
    precipitation = float(precipitation)
    temp_max = float(temp_max)
    temp_min = float(temp_min)
    wind = float(wind)

    sql = "insert into seattle_weather (id, date, precipitation, temp_max, temp_min, wind, real_weather)\
                values('%s','%s','%f','%f','%f','%f','%s')" % \
                (id, tdatetime, precipitation, temp_max, temp_min, wind, real_weather)
    
    try: 
        print("Prepare to insert")
        c.execute(sql)
        # print(c.fetchall())
        con.commit() # 若操作为增删改则需要提交数据
        print("Inserted!")
        
    except:
        print("Something went wrong")
    finally:
        c.close()
        con.close()

# utctimenow = dt.datetime.utcnow()
# save_params_into_db('test01', utctimenow, 0.3, 27, 16, 10, 'clean')