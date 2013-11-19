#Archivo en Donde se encuentra la parte logica de la pagina
import MySQLdb

try:
  db = MySQLdb.connect(host = "localhost", user = "root", passwd = "", db = "PatientRegistrydb")
  
  con = db.cursor()
  
  cur.execute("CREATE TABLE IF NOT EXISTS patientRegistry (id INT PRYMARY KEY AUTO_INCREMENT, fisrtName varchar(30),lastname varchar(30), cc INT, priority varchar(15
  
except MySQLdb, e:
  print "No se pudo realizar conexion con la base de datos"

def add_person(firstName, lastName, cc, phone, priority, time_of_admission):
  print ""
  
def show_list():
  print ""
  
def delete_person():
  print ""
  
def update_person():
  print ""
  

  
  
  
