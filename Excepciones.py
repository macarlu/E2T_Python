def caculadora():
    
    try:
        x = int(input("introduzca un múmero: "))
        y = int(input("Introduzca otro: "))
        print(x/y)
        
    except ZeroDivisionError:
        print("No se puede dividir entre cero")

    except Exception as e:
        print(f"Ha ocurrido un error: {e}")

    finally:
        caculadora()

caculadora()