# un diccionario para asignar los valores de meses con los dias de cada mes.
month = {"January" : "31", "February" : "28", "March" : "31", "April" : "30", "May" : "31", "June" : "30", "July" :"31", "August" : "31", "September" : "30", "October" : "31", "November" : "30", "December" :"31"}
# una entrada de datos para el año.
year = int(input("Insert a year to check: "))
# una entrada de datos para el mes.
months = str(input("Now, insert a month to check: "))
# transformamos la inicial en mayusculas para que coincida con la clave del diccionario de arriba.
months = months.capitalize()

def days_calc(year, months): #definimos la funcion con los argumentos que se introducen.

    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        month["February"] = "29"
        print(f"The year {year}, has {month[months]} days.")
    else:
        print(f"The year {year}, has {month[months]} days.")

days_calc(year, months)