# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JsnSgP13hSKWNSHmvu5_Nq0A2J7FqSFA

IMPORTS
"""

#imports
import tensorflow
from tensorflow import keras
import matplotlib.pyplot as plt
import numpy as np

"""Loads Datasets"""

#load_dataset
dataset = keras.datasets.fashion_mnist
((imagens_treino, identificacoes_treino), (imagens_teste, identificacoes_teste)) = dataset.load_data()

"""Explore Data"""

#Explore data
len(imagens_treino)
imagens_treino.shape
imagens_teste.shape
len(identificacoes_teste)
identificacoes_treino.min()
identificacoes_treino.max()

"""Data Exibition"""

#Data_Exibition
total_de_identificacoes = 10
nomes_de_classificacao = ['Camiseta', 'Calça', 'PullOver', ' Vestido', 'Casaco', 'Sandália', 'Camisa', 'Tenis', 'Bolsa', 'Bota']

'''
plt.imshow(imagens_treino[0])
plt.title(identificacoes_treino[0])

for imagem in range(10):
  plt.subplot(2, 5, imagem+1)
  plt.imshow(imagens_treino[imagem])
  plt.title(nomes_de_classificacao[identificacoes_treino[imagem]])
'''
plt.imshow(imagens_treino[0])
plt.colorbar()

"""Normalizando as Imagens"""

#Normalização
imagens_treino = imagens_treino/255.0

modelo = keras.Sequential([
  keras.layers.Flatten(input_shape=(28, 28)),
  keras.layers.Dense(272, activation=tensorflow.nn.relu),
  keras.layers.Dropout(0.2),
  keras.layers.Dense(10, activation=tensorflow.nn.softmax)
])
modelo.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
print("Os testes estão se iniciando... Há 32 ciclos de teste, AGUARDE!")
historico = modelo.fit(imagens_treino, identificacoes_treino, epochs=32, validation_split=0.2)
print(".................................")
print(".................................")
print(".................................")
print(".................................")
print(".................................")
print(".................................")
print(".................................")
print("OS TESTE DE 32 CICLOS")
print(".................................")
print(".................................")
print(".................................")

"""# Nova seção"""

import tensorflow
from tensorflow.keras.models import load_model

modelo.save('Model.h5')

plt.plot(historico.history['accuracy'])
plt.plot(historico.history['val_accuracy'])
plt.title('Acuracia Por Épocas')
plt.xlabel('epochs')
plt.ylabel('acurracy')
plt.legend(['Treino', 'Validação'])

plt.plot(historico.history['loss'])
plt.plot(historico.history['val_loss'])
plt.title('Acuracia Por Épocas')
plt.xlabel('epochs')
plt.ylabel('loss')
plt.legend(['Treino', 'Validação'])

teste = modelo.predict(imagens_teste)
np.argmax(teste[0])
print('Resultado do Teste:', np.argmax(teste[1]))
print('Número da Imagem Teste:', identificacoes_teste[1])

perda_teste, acuracia_teste = modelo.evaluate(imagens_teste, identificacoes_teste)
print('Perda do Teste:', perda_teste)
print('Acurácia Tetse:', acuracia_teste)