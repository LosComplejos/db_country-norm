A cierta gente se le pidió ingresar su países.
Se creo una bd a partir de esto (ademe.db)... sin embargo algunas personas pudieron cometer errores.

Lo que hace el programa es leer los países ingresados por la gente para hacerlos coincidir con el estándar mundial (iso-3166)
Contamos con dos diccionarios:
- El diccionario iso3166 (codigoPais \t nombreOficial)
- El diccionario alternativo (creado manualmente) que se compone de (codigoPais \t nombre1 \t nombre2 ...)
La idea es convertir lo ingresado por la gente a lo estándar!

Para la primera ejecución, se recomienda dejar el parámetro  write=False. Esto imprimirá las excepciones*
*:países ingresados por la gente que no están en ninguno de los dos diccionarios)
Si encuentra excepciones y crees saber a qué país se refieren, añádelas al diccionario alternativo.

Cambiando write=True se escribirá en la BD otra columna para añadir los códigos de país estándar.
