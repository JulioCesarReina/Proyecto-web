#Archivo en Donde se encuentra la parte logica de la pagina
import MySQLdb

try:
  db = MySQLdb.connect("PatientRegistrydb.db")
  
  con = db.cursor()
  
  con.execute("CREATE TABLE IF NOT EXISTS patientRegistry (id INT PRYMARY KEY AUTO_INCREMENT, fisrtName varchar(30),lastname varchar(30), cc INT, phone int, priority varchar(15), time_of_admission Timestamp)")
  
  def add_person(firstName, lastName, cc, phone, priority, time_of_admission):
    con.execute("INSERT INTO patientRegistry VALUES(" + firstname + ", " + lastname + ", " + cc + ", " + phone + ", " + priority + ", " + time_of_admission +  ")")
    print ""
  
  def show_list():
    con.execute("SELECT * FROM patientRegistry")
    print ""
  
  def delete_person(name):
    con.execute("DELETE FROM patientRegistry WHERE name = " + "'" + name + "'")
    con.commit()
    print ""
  
  def update_person(firstName, lastName, cc, phone, priority, time_of_admission):
    con.execute("UPDATE")
    con.commit()
    print ""
  
except MySQLdb, e:
  print "No se pudo realizar conexion con la base de datos"

  

  
  
  
