calification = input ("Introduce tu calificación de la AZ 900: ")

#sino añadimos esta variable nos dará error porque nos pide un string y nosotros daremos un int, así que lo convertimos 
calification = int (calification)

#en lugar de abrir llaves en el if "{}" utilizamos dos puntos ":"
if calification < 700 : 
    print ("veees por no estudiar")
#elif se utiliza para poner otra condicional pero que no es un else
elif calification > 1000:
    print ("mientes no puedes sacar más de 1000")
else :
    print ("felicidades pasa por tu certificado")

edad = input ("introduce tu edad")
edad = int (edad)

if edad >= 18 and edad <= 100 : #lo que en java sería &&
    print ("bienvenido al manitas")
elif edad > 100 :
    print ("si vienes acompañado de tus abuelitos, si te podemos fiar")
