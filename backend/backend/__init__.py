import sys
import pymysql

# if you want to add module/function from different folder
# use sys.path.append("< path to the folder that contains the module >")
sys.path.append("../common")

# problem with MySQLdb, use pymysql instead
pymysql.install_as_MySQLdb()
