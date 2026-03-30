#### Image Data

Knowing the complexity of our image dataset and the similarities between the different classes, we quickly decided to use transfer learning methods with models based on artificial neural networks capable of deep learning. We focused on models best suited for image data: Convolutional Neural Networks (CNNs).

---Insersetion---

#### Choice of Pre-trained Models

Among the models listed [here](https://keras.io/api/applications/), we chose those with fewer parameters to reduce training time and avoid the limitations of computational resources.

---Insersetion---

>- **Optimizer**: Adam, a proven and widely-used adaptive optimizer  
>- **Loss Function**: “**Categorical Cross-Entropy**” is suited for our multi-class classification task  
>- **Batch size**: we tested both 32 and 64  
>- **Learning Rate (LR)**: models were trained using the default value of 0.001, then with a smaller value of 0.00001, and finally with optimized values obtained through LR tuning  

>- **Data Augmentation** applied to training images:  
>>- Scale pixel values between 0 and 1  
>>- Stretch the image at an angle, making it look squashed or stretched diagonally  
>>- Random rotation between -45° and +45°  
>>- Horizontal shift relative to image width  
>>- Vertical shift relative to image height  
>>- Zoom range between -20% and +20%  
>>- Horizontal flip  
>>- Vertical flip  

---Insersetion---

#### Step 1 - Selecting the Best Models

###### Approach
>>>-&nbsp;Train selected models with input images of different sizes, without data augmentation or fine-tuning  
>>>-&nbsp;Use the default learning rate (0.001)  
>>>-&nbsp;Try different batch sizes: 32 and 64  
>>>-&nbsp;Try different epoch counts: 10, 20, 40  
>>>-&nbsp;Track the top 5 models based on weighted F1-score  

---Insersetion---

###### Results  
The scores for all tested models:  

---Insersetion---

Top 5 models based on weighted F1-score:

---Insersetion---

##### Step 2 - Data Augmentation with the Best Models from Step 1

###### Approach  
>>>-&nbsp;Train the top 5 models from Step 1 with data augmentation (no fine-tuning, LR = 0.001)  

###### Results  
---Insersetion---

##### Step 3 - Data Augmentation + Fine-Tuning of the Models

###### Approach  
>>>-&nbsp;Fine-tune the top models from Step 1  
>>>-(Unfreeze certain layers of the pre-trained models)  
>>>-&nbsp;Use a very small LR (0.00001)  
>>>-&nbsp;Increase the number of epochs to 40, 50, 60  

###### Results  
---Insersetion---

##### Step 4 - LR Optimization (No Data Augmentation, No Fine-Tuning)

###### Approach  
>> We followed the method described in [this article](https://towardsdatascience.com/how-to-optimize-learning-rate-with-tensorflow-its-easier-than-you-think-164f980a7c7b) (using the LearningRateScheduler callback):  
>>>-&nbsp;&nbsp;Start training with a very small LR (0.00001), then increase exponentially up to ≈ 2.54  
>>>-&nbsp;&nbsp;Analyze plots of loss and accuracy over epochs and LR  
>>>-&nbsp;&nbsp;Identify the LR with the lowest loss (generally matches highest accuracy), ensuring values around it are not too unstable  

###### Results  
The optimized LRs for each model:  

---Insersetion---

Accuracy:  
- Slightly increases until Epoch 30  
- Then decreases until Epoch 63  
- Small fluctuations between Epoch 64 and 67  
- Stabilizes from Epoch 68 onward  

Loss:  
- Shows the opposite trend up to Epoch 63 (which makes sense)  
- Small fluctuations between Epoch 64 and 69  
- Mostly flat from Epoch 70 to 80  
- Fluctuates again from Epoch 80 to the end of training  

---Insersetion---

The optimal learning rate (with the lowest loss) is approximately 0.0004  

---Insersetion---

##### Step 5 - Data Augmentation and Fine-Tuning with Optimized LRs

###### Approach  
>>>-&nbsp;&nbsp;Retrain the 5 best models using the optimized LRs from Step 4  

---Insersetion---

###### Results  
---Insersetion---

>- Xception improved by 1% in weighted F1-score  
>- InceptionV3 improved by 1% in both weighted F1-score and accuracy  
>- Both models may have reached their limits with this dataset  
>- However, they reached these scores faster using the optimized LRs  

---Insersetion---

#### Conclusion  

>	The best results were obtained with:  
>>-	**Xception**: LR = 0.0004, weighted F1-score = **0.66**  
>>-	**InceptionV3**: LR = 0.0003, weighted F1-score = **0.65**  
(With data augmentation and fine-tuning)

These scores clearly outperform the reference Rakuten model for image classification (0.55)

---Insersetion---

Reminder - Best scores so far (**Step 1**)  
(No data augmentation, LR = 0.001)  
| Model  | Weighted F1-score |  
| :--------------- |:---------------:|  
|InceptionResNetV2|**0.61**|  
|Xception| **0.60** |  
|DenseNet121| **0.61**|  
|InceptionV3| **0.59** |  
|MobileNetV2| **0.59** |  

---Insersetion---

Reminder - Best scores so far (**Step 1**)  
(No data augmentation, LR = 0.001)  
| Model  | Weighted F1-score |  
| :--------------- |:---------------:|  
|Xception| **0.60** |  
|InceptionV3| **0.59** |  
|MobileNetV2| **0.59** |  
|InceptionResNetV2|**0.61**|  
|DenseNet121| **0.61**|  

---Insersetion---

Reminder - Best scores so far (**Step 3**)  
(Data augmentation + fine-tuning, LR = 0.00001)  
| Model  | Weighted F1-score |  
| :--------------- |:---------------:|  
|Xception| **0.65** |  
|InceptionV3| **0.64** |  
|InceptionResNetV2|**0.63**|  
|DenseNet121| **0.59**|  
|MobileNetV2| **0.63** |  
