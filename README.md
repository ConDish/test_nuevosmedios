## Pergamino del general c-sharp
{
    "id" : "",
    "ruby_rails" : false,
    "armas" : "cuchillos",
    "ubicacion" : "",
    "dinastia" : ""
}


## Contiene las gemas que tiene el soldado
bd/people/apodo/gemas.json

## Contiene la informacion de cada gema [tipo], [poder], [tipo de arma con la que puede ser usada]

bd/gemas/gemaid/gemasinfo.json

## Contiene la informacion de las armas de cada tipo como es nombre del arma, poder, en que posicion puede ser usada. 

bd/arma/tipoarmaid/armasinfo.json

## Contiene la informacion de la posicion dentro de la formacion del ejercito la cual es el poder este puede ser negativo o positivo.

bd/arma/positionid/positioninfo.json



# Numero 1.1
- Inicio
   - Obtener el pergamino
   - Agregar al pergamino campo gem-name de tipo Arreglo
   - Agregar al pergamino campo armas-name de tipo Arreglo
   - Mientras pergamino sea menor a su longitud
   - Entonces 
       - Crear directorio con el nombre del soldado
       - Crear subdirectorio con el nombre de combinaciones
       - Dentro de subdirectorio crear archivo bination.json
       - Si id de soldado esta en bd/people/apodo/gemas.json Obtener la gema
       - Agregar a campo gem-name la gema
       - Agregar a campo armas-name las armas
       - Agregar a bination.json arma
       - Si aram esta en bd/arma/tipoarmaid/armasinfo.json Obtener la posicion
       - Agregar a bination.json posicion
       - Agregar a bination.json gema
       - Agregar a bination.json dinastia
       - Agregar a bination.json poder
- Fin Mientras

- Fin

## Numero 1.2
Inicio
    Crear variable sum
    Mientras directorios sea menor a su longitud
        Entonces
            Entrar a directorio
            Entrar a subdirectorio combinaciones
            Obtener informacion de bination.json
            Sum es igual a informacion de bination.json
        Fin Mientras
    Mostrar sum
Fin

