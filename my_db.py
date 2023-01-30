# import MySQLdb
import mysql.connector as MySQLdb


def get_connection(database_info):
    host_name, user_name, passw_name, db_name = database_info.split('#')
    dataBase = MySQLdb.connect(
        host=host_name,
        user=user_name,
        passwd=passw_name,
        database=db_name)   # host_name, user_name, paasw_name, db_name, charset="utf8")

    cur_obj = dataBase.cursor()
    return dataBase, cur_obj


def insert_data(database_info, details_dict):
    dataBase, cur_obj = get_connection(database_info)
    i_sql = "insert into deta_table(Name, Guardian, DOB, Gender, Aadhar_No, Passport_No, Pancard_No) values (%s, %s, %s, %s, %s, %s, %s)"

    val = (details_dict["Name"], details_dict["Guardian"], details_dict["DOB"], details_dict["Gender"],
           details_dict["Aadhar no"], details_dict["Passport No"], details_dict["Pancard no"])

    cur_obj.execute(i_sql, val)

    dataBase.commit()
    cur_obj.close()
    dataBase.close()
    return


def get_data(database_info):
    dataBase, cur_obj = get_connection(database_info)
    get_sql = "select * from deta_table"
    cur_obj.execute(get_sql)
    # res = cur.fetchone()
    res = cur_obj.fetchall()
    cur_obj.close()
    dataBase.close()
    if res:
        return res
    else:
        res = []
