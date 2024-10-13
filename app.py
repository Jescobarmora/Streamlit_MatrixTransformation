import streamlit as st
import pandas as pd
import numpy as np

def apply_convolution(matrix, kernel):
    matrix_height, matrix_width = matrix.shape
    kernel_height, kernel_width = kernel.shape
    output_matrix = np.zeros((matrix_height - 2, matrix_width - 2))
    for i in range(matrix_height - 2):
        for j in range(matrix_width - 2):
            region = matrix[i:i + kernel_height, j:j + kernel_width]
            output_matrix[i, j] = np.sum(region * kernel)
    return output_matrix

def apply_padding(matrix, padding_size):
    original_height, original_width = matrix.shape
    padded_matrix = np.zeros((original_height + 2 * padding_size, original_width + 2 * padding_size))
    padded_matrix[padding_size:padding_size + original_height, padding_size:padding_size + original_width] = matrix
    return padded_matrix

def apply_stride(matrix, kernel, stride):
    matrix_height, matrix_width = matrix.shape
    kernel_height, kernel_width = kernel.shape
    output_height = (matrix_height - kernel_height) // stride + 1
    output_width = (matrix_width - kernel_width) // stride + 1
    output_matrix = np.zeros((output_height, output_width))
    for i in range(0, matrix_height - kernel_height + 1, stride):
        for j in range(0, matrix_width - kernel_width + 1, stride):
            region = matrix[i:i + kernel_height, j:j + kernel_width]
            output_matrix[i // stride, j // stride] = np.sum(region * kernel)
    return output_matrix

def apply_stacking(matrix, n):
    kernels = [np.random.randint(-1, 2, (3, 3)) for _ in range(n)]
    feature_maps = [apply_convolution(matrix, kernel) for kernel in kernels]
    return feature_maps

def max_pooling(matrix, stride):
    matrix_height, matrix_width = matrix.shape
    output_height = (matrix_height - 2) // stride + 1
    output_width = (matrix_width - 2) // stride + 1
    pooled_matrix = np.zeros((output_height, output_width))
    for i in range(0, matrix_height - 1, stride):
        for j in range(0, matrix_width - 1, stride):
            region = matrix[i:i + 2, j:j + 2]
            pooled_matrix[i // stride, j // stride] = np.max(region)
    return pooled_matrix

st.title('Transformaciones de Matrices')

uploaded_file = st.file_uploader("Sube tu archivo pixeles.xlsx", type=["xlsx"])

if uploaded_file is not None:
    # Cargar la matriz del archivo Excel subido
    matrix_data = pd.read_excel(uploaded_file, sheet_name=0, header=None)
    matrix = matrix_data.values
    
    option = st.selectbox(
        "Selecciona una transformación",
        ("Convolución", "Padding", "Stride", "Stacking", "Max Pooling")
    )

    if option == "Convolución":
        kernel_type = st.selectbox("Tipo de Kernel", ("Horizontal", "Vertical"))
        kernel = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]]) if kernel_type == "Horizontal" else np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
        if st.button("Calcular"):
            result = apply_convolution(matrix, kernel)
            st.write("Matriz resultante (Convolución):")
            st.write(result)
    
    elif option == "Padding":
        padding_size = st.number_input("Introduce el tamaño de padding (número de filas/columnas de ceros a añadir)", min_value=1, max_value=10, value=1)
        if st.button("Calcular"):
            result = apply_padding(matrix, padding_size)
            st.write("Matriz resultante (Padding):")
            st.write(result)
    
    elif option == "Stride":
        kernel_type = st.selectbox("Tipo de Kernel", ("Horizontal", "Vertical"))
        stride = st.number_input("Introduce el valor del stride", min_value=1, max_value=5, value=2)
        kernel = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]]) if kernel_type == "Horizontal" else np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
        if st.button("Calcular"):
            result = apply_stride(matrix, kernel, stride)
            st.write("Matriz resultante (Stride):")
            st.write(result)
    
    elif option == "Stacking":
        n = st.number_input("Introduce la cantidad de mapas de características a generar", min_value=1, max_value=10, value=5)
        if st.button("Calcular"):
            feature_maps = apply_stacking(matrix, n)
            for idx, fmap in enumerate(feature_maps):
                st.write(f"Mapa de Características {idx+1}:")
                st.write(fmap)
    
    elif option == "Max Pooling":
        stride = st.number_input("Introduce el valor del stride", min_value=1, max_value=5, value=2)
        if st.button("Calcular"):
            result = max_pooling(matrix, stride)
            st.write("Matriz resultante (Max Pooling):")
            st.write(result)