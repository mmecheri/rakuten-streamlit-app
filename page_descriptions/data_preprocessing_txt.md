#### Text Data

>**Variables**
>>- The **designation** column: does not contain any missing values  
>>- The **description** column provides more details about the products, but has many missing values (35%)

For the text data, we:
>>>- used only the **designation** column  
>>>- then **combined** the two variables **description** and **designation** into a single column named **text**

>**Text Cleaning**
>>>- Convert all words to lowercase  
>>>- Remove accents and HTML tags  
>>>- Remove stopwords (French, English, and German)  
>>>- Remove words with less than two letters  </br>

>**Vector Representation**
>>- **Machine Learning**: each text sample is converted into vectors using ***TfidfVectorizer***, with ***max_features*** set to 5000.  </br>
>>- **Deep Learning**: the text is split into tokens using ***Tokenizer*** from *tf.keras.preprocessing.text*, with a maximum number of words (***num_words***) of 20,000. The maximum sequence length was set to 200.


#### Image Data

> We used a data generator (***ImageDataGenerator***, from *tensorflow.keras.preprocessing.image*).  
The data generator helps us:
>>- Enrich the training set  
>>- Reduce overfitting  
>>- Handle resource limitations during training

---Insersetion---
