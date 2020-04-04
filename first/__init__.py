import pymysql

pymysql.install_as_MySQLdb()

db = pymysql.connect("localhost", "root", "", "django_mysql")

cursor = db.cursor()

cursor.execute("SELECT VERSION()")

db.close()
