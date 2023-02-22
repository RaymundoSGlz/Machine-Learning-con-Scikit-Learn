Repositorio de seguimiento para el [Curso Profesional de Machine Learning con Scikit-Learn](https://platzi.com/cursos/scikitlearn/)

Las librerías utilizadas se encuentran en el archivo requirements.txt, pude instalarlas con el comando:

```bash
pip install -r requirements.txt
```
Los Notebooks se encuentran en la carpeta notebooks, cada uno representa una parte del curso, pero en la mayoría solo se encuentra el código, no el texto explicativo.

Para finalizar el curso se desarrollo un proyecto con Flask para el despliegue de un modelo de Machine Learning, el cual se encuentra en la carpeta `project`.
Para verificar que todo este funcionando correctamente, se puede ejecutar el siguiente comando:

```bash
python app.py
```
y después realizar una petición con el comando:

```bash
python request_test.py
```

Este ejemplo devolverá la predicción del score de Felicidad de un país, `request_test.py` contiene una lista que contiene los datos de  `GDP per capita,Social support,Healthy life expectancy,Freedom to make life choices,Generosity,Perceptions of corruption`.



> Para el seguimiento del curso se utilizo la version 3.10.9 de Python y Visual Studio Code, por lo que algunos comandos pueden variar si estas utilizando otra version de **Python** o un IDE diferente.