# Prueba Tecnica de EasyBroker
Este repositorio es para la prueba técnica para Software Developer Intern en EasyBroker.

El proyecto  consiste  un sitio web conectado a una cuenta de EasyBroker con todas sus propiedades publicadas. El sitio web consta de dos páginas principales: la página del listado de propiedades y la página de propiedades.

Utilizo la API de EasyBroker para obtener toda la información necesaria para construir el sitio web utilizando el framework Django.

## ¿Cómo correr este proyecto?


### Requisitos:
                
* Acceso a la terminal de línea de comandos.
* Python3.
* Git.
                
### Pasos a seguir:
#### 1. Clonar Repositorio desde GitHub.
`$ git clone https://github.com/IrvingReyes/PruebaTecnicaEasyBroker.git`
#### 2. Moverse a la carpeta 'PruebaTecnicaEasyBroker'.
`$ cd PruebaTecnicaEasyBroker/`
#### 3. Crear entorno virtual (opcional).
`python3 -m venv venv`
#### 4. Activar el ambiente virtual (opcional).
`source venv/bin/activate`
#### 5. Instalar los requisitos del proyecto.
`pip install -r requirements.txt`
#### 6. Moverse a la carpeta 'prueba_tecnica'
`cd prueba_tecnica/`
#### 7. Correr el servidor de Django
`python3 manage.py runserver`

## Sección de Notas:
Aquí están las notas  sobre mis decisiones de diseño o las mejoras que habría hecho si tuviera más tiempo.

### Diseño
Se diseñó una *clase* para interactuar con la API,  creo que es la mejor manera para no repqetir código. Dicha clase solo obtiene el *token* de autenticación en el *constructor*,  así no es necesario enviarlo cada vez que se manda a llamar a un método, trate de dejar solo los parámetros necesarios. Para crear la clase utilicé la librería *requests*, que es una librería  de Python sencilla pero efectiva  para poder enviar solicitudes HTTP, me gusta porque permite enviar los headers de la petición como *dictionaries* de python.

Para hacer la paginación de las propiedades usé la propia API para hacerlo, creo que es la mejor manera, pues se aprovecha bien la API, el resto solo fue crear URL's con la información que se requiriera para cada vista en concreto. La información de las peticiones la obtengo mediante el método GET para obtener las vistas de las propiedades y el método POST para enviar los datos del formulario, ya que estos no se mandan mediante el URL, hacen a POST la opcíon más segura.

Como *framework* decidí utilizar Django, que, además de ya estar familiarizado con él, es una solución ya probada  que lleva muchísimo tiempo funcionando y que ha pasado por numerosas pruebas que lo han vuelto muy robusto y confiable. También Django incluye ciertas utilidades que se encargan de mitigar la mayoría de los ataques comunes como CSRF para los formularios. Aunado a lo anterior, considero que su manera para crear plantillas y vistas también es muy práctica y no muy complicada de implementar.

### Pruebas
Quizás esta parte fue la que más me resultó complicada, pues fue en la que aprendí a utilizar los *mocks*. Gracias a las observaciones que me realizaron, supe que consumir la API directamente en las pruebas tiene ciertas desventajas, como que un cambio temporal en el comportamiento de la API externa puede provocar fallos intermitentes en el conjunto de pruebas.

Por lo anterior, comprendí que una de las razones para utilizar *mock Objects* de Python es para controlar el comportamiento del código durante la ejecución pruebas. Entonces podemos probar el código en un entorno controlado, sustituyendo la solicitud real por un objeto simulado para obtener respuestas predecibles.

Un objeto *mock* sustituye e imita a un objeto real dentro de un entorno de pruebas. Me gusto la analogía del articulo que me pasaron y me sirivio para comprender mejor que es un *mock*: “El uso de un mock me recuerda a un tropo clásico de las películas en el que el héroe agarra a un esbirro, se pone el uniforme y se mete en una fila de enemigos en marcha. Nadie se da cuenta del impostor y todo el mundo sigue avanzando, como siempre.”

Entonces definí algunas pruebas utilizando mocks y una librería llamada *nose*, que extiende el módulo incorporado de u*nittest* de Python para facilitar las pruebas. Dichas pruebas validan que la respuesta de los métodos de la clase al solicitar las propiedades es la respuesta esperada.

La pruebas se pueden ejecutar desde la primera carpeta ‘prueba_tecnica’ con el comando siguiente:

`$ nosetests --verbosity=2 prueba_tecnica/`

### Cosas que me gustaría mejorar
Creo que mi código pudo ser un poco más limpio en las vistas y pruebas, quizás declaro  más de las variables necesarias y hay algunas líneas que podrían omitirse. También creo que pude haber creado más validaciones con los parámetros y considerar más casos para excepciones. Puede que esas partes hayan sido las menos limpias.

Por otro lado, considero que podría haberle sacado más provecho al *framework*, quizás pude haber creado una aplicación  para tener mi código ahí. También Django proporciona un marco de prueba con una pequeña jerarquía de clases que se basan en la librería *unittest* estándar Python, me hubiera gustado explorar más de eso.

Creo que mi cobertura de pruebas pudo tener más pruebas y estas pudieron ser más sustanciosas.

