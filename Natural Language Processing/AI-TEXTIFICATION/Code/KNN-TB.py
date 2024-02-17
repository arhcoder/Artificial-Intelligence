# PARA TOMAR UN DATASET Y CONVERTIRLO EN DATOS LEÍBLES POR UN MODELO:
import nltk
from nltk.tokenize import word_tokenize
from gensim.models import Word2Vec
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import numpy as np

def get_gensim(dataset, embeddings):
  # Obtiene el dataset:
  dataset = pd.read_csv(dataset)

  # Etiquetas "y":
  y = dataset["label"].values

  # Obtiene las palabras únicas en el dataset:
  unique_words = set(" ".join(dataset["text"]).split())

  # Crea un diccionario de embeddings para las palabras únicas:
  word_embeddings = {word: embeddings.wv[word] if word in embeddings.wv else np.zeros(embeddings.vector_size)
                      for word in unique_words}

  # Crear la matriz de características "X":
  Data_type = object
  X = np.array([[word_embeddings[word] for word in sentence.split() if word in word_embeddings]
                for sentence in dataset["text"]], dtype=Data_type)

  return X, y, len(unique_words)
  
def load_embeddings(embeds_model_path, word2Index_path, embeds_csv_path):
  # Cargar embeddings model desde archivo pickle:
  with open(embeds_model_path, "rb") as model_file:
    embeds_model = pickle.load(model_file)

  # Cargar word2Index desde archivo pickle:
  with open(word2Index_path, "rb") as word2Index_file:
    word2Index = pickle.load(word2Index_file)

  # Cargar embeddings desde archivo CSV:
  embeds_df = pd.read_csv(embeds_csv_path)
  embeds = embeds_df.values

  return embeds, word2Index, embeds_model


def get_own(dataset, embeddings):
  # Obtiene el dataset:
  dataset = pd.read_csv(dataset)

  # Obtiene las etiquetas "y":
  y = dataset["label"].values

  # Obtiene las palabras únicas en el dataset:
  unique_words = set(" ".join(dataset["text"]).split())

  # Crea un diccionario de embeddings para las palabras únicas:
  word_embeddings = {word: embeddings.get_embedding_of(word, embeddings.word2Index) if word in embeddings.word2Index else np.zeros(embeddings.embedding_size)
                      for word in unique_words}

  # Crear la matriz de características "X":
  X = np.array([[word_embeddings[word] for word in sentence.split() if word in word_embeddings]
                for sentence in dataset["text"]])

  return X, y, len(unique_words)

from sklearn.utils import shuffle

# Define la función para cargar embeddings y obtener datos de entrenamiento:
def get_data_and_embeddings(dataset_info, size=1):
  if dataset_info["embeddings"]["own"]:
      embeds_model, word2Index, embeds_csv = load_embeddings(
          dataset_info["embeddings"]["model"],
          dataset_info["embeddings"]["word2Index"],
          dataset_info["embeddings"]["dataset"]
      )
      embeddings, word2Index, embeds_model = load_embeddings(embeds_model, word2Index, embeds_csv)
      X, y, unique_words = get_own(dataset_info["test_dataset"], embeds_model)
  else:
    embeddings = Word2Vec.load(str(dataset_info["embeddings"]["path"]))
    X, y, unique_words = get_gensim(dataset_info["test_dataset"], embeddings)


  # Combina X e y antes de la mezcla aleatoria:
  combined = list(zip(X, y))

  # Mezcla aleatoria:
  combined = shuffle(combined, random_state=11)

  # Desempaqueta X e y después de la mezcla aleatoria:
  X, y = zip(*combined)

  # Devuelve X, y y unique_words por separado:
  return X[:int(len(X)*size)], y[:int(len(y)*size)], unique_words

import pandas as pd
from sklearn.utils import shuffle

# Define la función para cargar embeddings y obtener datos de entrenamiento:
def get_data_and_words(dataset_path, size=1):

  # Obtiene un dataset con "text" y "labels":
  dataset = pd.read_csv(dataset_path)

  # Mezcla y obtiene una parte:
  dataset = dataset.sample(frac=size, random_state=11)

  # Separa X, y:
  X = dataset[["text"]].values.tolist()
  y = dataset[["label"]].values.tolist()

  # Obtén todas las palabras únicas:
  uniques_set = set()
  for texto in dataset["text"]:
    palabras = texto.split()
    uniques_set.update(palabras)
  unique_words = len(uniques_set)

  # Devuelve X, y y unique_words por separado:
  return X, y, unique_words
  
# Define la función para cargar embeddings y obtener datos de entrenamiento:
def get_train_data_and_embeddings(dataset_info, size=1):
    if dataset_info["embeddings"]["own"]:
        embeds_model, word2Index, embeds_csv = load_embeddings(
            dataset_info["embeddings"]["model"],
            dataset_info["embeddings"]["word2Index"],
            dataset_info["embeddings"]["dataset"]
        )
        embeddings, word2Index, embeds_model = load_embeddings(embeds_model, word2Index, embeds_csv)
        X, y, unique_words = get_own(dataset_info["test_dataset"], embeds_model)
    else:
        embeddings = Word2Vec.load(str(dataset_info["embeddings"]["path"]))
        X, y, unique_words = get_gensim(dataset_info["test_dataset"], embeddings)

    return X[:int(len(X)*size)], y[:int(len(y)*size)], unique_words

# Define la función para cargar embeddings y obtener datos de entrenamiento:
def get_test_data_and_embeddings(dataset_info, size=1):
    if dataset_info["embeddings"]["own"]:
        embeds_model, word2Index, embeds_csv = load_embeddings(
            dataset_info["embeddings"]["model"],
            dataset_info["embeddings"]["word2Index"],
            dataset_info["embeddings"]["dataset"]
        )
        embeddings, word2Index, embeds_model = load_embeddings(embeds_model, word2Index, embeds_csv)
        X, y, unique_words = get_own(dataset_info["test_dataset"], embeds_model)
    else:
        embeddings = Word2Vec.load(str(dataset_info["embeddings"]["path"]))
        X, y, unique_words = get_gensim(dataset_info["test_dataset"], embeddings)

    return X[:int(len(X)*size)], y[:int(len(y)*size)], unique_words


def knn_taskb():
	import warnings
	warnings.filterwarnings("ignore")

	import pandas as pd
	import numpy as np
	import pickle
	from tqdm import tqdm
	from gensim.models import Word2Vec



	# IMPLEMENTACIÓN:
	from sklearn.neighbors import KNeighborsClassifier
	from sklearn.metrics import confusion_matrix
	from sklearn.metrics import classification_report
	
	taskB_datasets = {
		"A": {
		      "train_dataset": "TaskB-TrainAB.csv",
		      "test_dataset": "TaskB-DevAB.csv",
		      "embeddings": {
			  "own": False,
			  "path": "TaskB_A_gensim_model.bin"
			}
	      }
	}
	dataset_info = taskB_datasets["A"]
	X, y, _ = get_train_data_and_embeddings(dataset_info)
	counts = np.array([len(sentence) for sentence in X])
	avg_pool = np.array([np.mean(sentence, axis=0) for sentence in X])

	counts = counts.reshape(-1, 1)
	counts = StandardScaler().fit_transform(counts)

	X = np.hstack([counts, avg_pool])
	X_train, X_test, y_train, y_test = train_test_split(X, y)

	knn = KNeighborsClassifier(metric='cosine')
	knn.fit(X_train, y_train)
	y_pred = knn.predict(X_test)

	print(classification_report(y_test, y_pred))



if __name__ == "__main__":
    with open("knn_taskb-TEST.txt", "w") as archivo:
        import sys
        sys.stdout = archivo
        
        knn_taskb()
        
        sys.stdout = sys.__stdout__
