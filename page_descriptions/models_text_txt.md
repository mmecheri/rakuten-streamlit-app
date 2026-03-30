#### Machine learning 
Below is a summary comparing training results when using only the **“designation”** column first, and then both the **“designation”** and **“description”** columns combined into a single **“text”** column:
---Insersetion---
The machine learning models showed limited performance, so we moved on to deep learning models.

#### Deep learning 

Here are the models we used and the results obtained:
---Insersetion---
Parameter choices:
>- Batch size: 200</br>
>- Epochs: 5</br>
>- Learning Rate: 0.001</br>
>- Optimizer: “adam”</br>

---Insersetion---
The least well-predicted product classes were mostly the same for both Conv1D and Simple DNN models, except for classes: 300, 200, 6604, and 3330, which were better predicted by the Simple DNN model.

---Insersetion---
#### Conclusion
The Conv1D and DNN (Deep Neural Network) models achieved the best scores. The LinearSVC model also gave interesting results. In fact, we noticed that the Conv1D model is much faster to train.

---Insersetion---
#### Demo - Predictions
For predictions, we focus only on the two best models: **Conv1D** and **DNN**
---Insersetion---
