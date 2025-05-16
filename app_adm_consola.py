from db.Connection import ConnectionSQLite
from db.data_model import CreateTables
from Model.Admin import Admin


# from Model import Cliente
import datetime


def login():
  user = input("Ingrese Usuario:\n")
  passw = input("Ingrese Contraseña:\n")
  user = db_user.login(user, passw)
  if user:
      if user[5] == 1:
          print("Bienvenido")
          print("Usuario Administrador")
          adm = Admin(user[0], user[1], user[2], user[3], user[4], user[5])
          adm.menu()
      else:
          print("*********************************")
          print("Usuario o contraseña incorrectos")
          print("*********************************")
  else:
      print("*********************************")
      print("Usuario o contraseña incorrectos")
      print("*********************************")



def iniciar():
  print("Bienvenido al sistema de Restaurante")
  print("1. Iniciar Sesión")
  print("2. Salir")
  opcion = int(input("Ingrese una opción: "))
  while True:
    if opcion == 1:
      login()
    elif opcion == 2:
      print("Programa finalizado.")
      break
    else:
        print("Opción no válida. Por favor, selecciona una opción válida del menú.")
    print("1. Iniciar Sesión")
    print("2. Salir")
    opcion = int(input("Ingrese una opción: "))


if __name__ == "__main__":
    db_user = ConnectionSQLite()
    ct = CreateTables()
    db_user.execute_query(ct.create_table_user())
    db_user.execute_query(ct.create_table_category())
    db_user.execute_query(ct.create_table_order())
    db_user.execute_query(ct.create_table_product())
    db_user.execute_query(ct.create_table_detail())
    db_user.execute_query(ct.create_table_qualification())
    db_user.execute_query(ct.create_table_shipment())
    db_user.execute_query(ct.create_table_mylikes())

    iniciar()
