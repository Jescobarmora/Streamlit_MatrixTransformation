# API en Streamlit para Transformaciones de Matrices

Este repositorio contiene el código de una aplicación desarrollada en **Streamlit** que permite aplicar diversas transformaciones de matrices basadas en un archivo `pixeles.xlsx`. El usuario puede interactuar con la aplicación a través de un menú de opciones que permite cargar el archivo y realizar las siguientes transformaciones: Convolución, Padding, Stride, Stacking y Max Pooling.

## Funciones Implementadas

### 1. Convolución
La función de convolución permite aplicar un kernel de 3x3 para la detección de bordes en la matriz de píxeles. El usuario puede elegir entre un kernel horizontal o vertical, y la aplicación calculará los bordes correspondientes en la imagen.

- **Argumentos:**
  - Tipo de kernel: Horizontal o Vertical.
  - Matriz original cargada desde el archivo `pixeles.xlsx`.

- **Resultado:** 
  - Una nueva matriz donde se destacan los bordes detectados según el tipo de kernel seleccionado.

### 2. Padding
La función de padding permite agregar filas y columnas de ceros alrededor de la matriz original, incrementando su tamaño. El usuario puede especificar la cantidad de filas/columnas de ceros que se añadirán.

- **Argumentos:**
  - Tamaño de padding: Cantidad de filas/columnas de ceros a añadir.
  - Matriz original cargada desde el archivo `pixeles.xlsx`.

- **Resultado:** 
  - Una matriz más grande con ceros agregados alrededor de la matriz original.

### 3. Stride
La función de stride permite aplicar un kernel de 3x3 para detección de bordes, pero esta vez desplazándose en saltos (stride) de 2 o más posiciones. El usuario puede seleccionar el tamaño del stride y el tipo de kernel (horizontal o vertical).

- **Argumentos:**
  - Tipo de kernel: Horizontal o Vertical.
  - Tamaño de stride: Cantidad de posiciones que saltará el kernel al recorrer la matriz.
  - Matriz original cargada desde el archivo `pixeles.xlsx`.

- **Resultado:** 
  - Una matriz reducida generada por la aplicación del kernel con el stride especificado.

### 4. Stacking
La función de stacking genera varios mapas de características (feature maps) a partir de la matriz original, utilizando kernels aleatorios de 3x3. El usuario puede especificar cuántos mapas de características desea generar.

- **Argumentos:**
  - Número de mapas de características: Cantidad de mapas que se generarán.
  - Matriz original cargada desde el archivo `pixeles.xlsx`.

- **Resultado:** 
  - Múltiples mapas de características que representan diferentes transformaciones de la matriz original.

### 5. Max Pooling
La función de max pooling permite recorrer la matriz con un kernel de 2x2 y calcular el valor máximo en cada bloque. El usuario puede especificar el tamaño del stride para ajustar el desplazamiento del kernel sobre la matriz.

- **Argumentos:**
  - Tamaño de stride: Cantidad de posiciones que saltará el kernel al recorrer la matriz.
  - Matriz original cargada desde el archivo `pixeles.xlsx`.

- **Resultado:** 
  - Una matriz reducida donde cada valor representa el máximo de un bloque 2x2 de la matriz original.

## Instrucciones de Uso

1. Cargar el archivo `pixeles.xlsx` en la interfaz de Streamlit.
2. Seleccionar una de las transformaciones disponibles en el menú desplegable.
3. Ingresar los parámetros requeridos (kernel, stride, tamaño de padding, etc.).
4. Presionar el botón "Calcular" para ver el resultado de la transformación.
