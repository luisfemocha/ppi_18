Proyecto para la asignatura Programación para Ingeniería 2023-II
Grupo 18 integrado por:
- Daniel Felipe Garzon Acosta
- Luis Felipe Moreno Chamorro

# [APPETITO](https://grupo18ppi.streamlit.app)
https://grupo18ppi.streamlit.app
## Descripción

Aplicación que en base a ingredientes suministrados por el usuario, le recomiende recetas para que pueda aprender y ampliar sus conocimientos en la cocina, promoviendo la cocina creativa y el buen uso de los ingredientes a mano.

## Objetivo del proyecto

### General: 
Facilitar recetas en base a los ingredientes que tenga el usuario.

### Específicos
- **Organizar** las diferentes recetas que le puedan servir al usuario teniendo en cuenta los ingredientes que este tenga.
- **Permitir** al usuario filtrar estas recetas respecto a las preferencias nutricionales o personales que pueda tener.
- **Facilitar** al usuario las recetas que se adecuan a sus necesidades en una interfaz amigable y cómoda para que pueda elegir fácilmente su receta.
- **Incluir** ingredientes opcionales para promover que el usuario personalice su receta aún más y pueda utilizar al máximo sus ingredientes.
- **Categorizar** las comidas (fit, panadería, grasas, comida rápida…) e incluir el label en las recetas al ser mostradas.
- **Asegurar** que la aplicación pueda consumir los datasets de las recetas y realizar un buen proceso de filtrado para el usuario.

## Librerías

Para iniciar el desarrollo del proyecto se cuentan con 3 librerías de las mencionadas en clase, estas son Pandas, Numpy y Matplotlib, a continuación se comenta su uso:
### Pandas:
**Creación de DataFrames:** Utiliza Pandas para crear DataFrames que almacenen información relevante para tus recetas y los ingredientes disponibles. Cada fila del DataFrame de recetas representaría una receta única, y las columnas podrían incluir detalles como el nombre de la receta, los ingredientes necesarios, los pasos de preparación, el tiempo de cocción y otros datos descriptivos. Del mismo modo, puedes crear un DataFrame para los ingredientes disponibles, donde cada fila represente un ingrediente y las columnas incluyan información como el nombre del ingrediente, la cantidad disponible, la fecha de caducidad, etc.

**Manipulación de datos:** Pandas te permite realizar diversas operaciones en tus DataFrames, como la selección, filtrado y agregación de datos. Por ejemplo, puedes usar Pandas para filtrar las recetas que se pueden preparar con los ingredientes disponibles en un momento dado o para ordenar las recetas según diferentes criterios, como el tiempo de cocción.

**Unión de DataFrames:** Se tiene información nutricional para cada ingrediente y deseas calcular la información nutricional total de una receta, puedes unir los DataFrames de recetas e ingredientes en base a los ingredientes necesarios y luego realizar cálculos numéricos.

### Numpy:
**Cálculos numéricos:** Si deseas ajustar las cantidades de ingredientes en función del número de personas para las que estás cocinando, Numpy es útil para realizar cálculos numéricos eficientes. Por ejemplo, puedes multiplicar las cantidades de ingredientes por un factor dado para adaptar la receta a un número diferente de porciones.

**Operaciones con matrices:** Numpy es especialmente útil cuando necesitas realizar operaciones matemáticas en matrices de datos. Si tienes información nutricional en forma de matrices (por ejemplo, calorías, proteínas, carbohidratos), Numpy facilita la realización de cálculos para obtener información nutricional total o realizar análisis específicos.

### Matplotlib:
**Visualización de ingredientes:** Puedes crear gráficos de barras o gráficos de pastel utilizando Matplotlib para mostrar la cantidad de cada ingrediente necesario para una receta en particular. Esto permite a los usuarios comprender rápidamente las proporciones de los ingredientes.

**Visualización de información nutricional:** Matplotlib también es útil para crear gráficos que muestran la descomposición de la información nutricional de una receta. Por ejemplo, un gráfico circular puede mostrar la proporción de calorías, proteínas, carbohidratos, etc., en una receta, lo que ayuda a los usuarios a comprender la composición nutricional.