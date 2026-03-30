
In this section, we address the **main challenge** of the Rakuten competition, which is **multimodal classification**, based on **Text** and **Image** data.

The idea is to combine multiple models into one to achieve better predictive performance than each model taken separately. This ensemble learning approach includes many techniques, such as Voting and Stacking, widely discussed in the literature.

#### Approach

For our classification problem, we chose the Voting approach (Max Voting and Weighted Average Voting) as follows:
- **Max Voting**: choose the prediction with the highest probability among the combined models
- **Weighted Average**: assign a weight to each model based on its F1-score
---Insersetion---
#### Selection of the Best Models

Among all the tested Text and Image models, the best performances were obtained with the following models:
---Insersetion---
**Text Models**:
>- Embedding + Conv1D: F1-score Weighted and accuracy of 0.80
>- Simple DNN: F1-score Weighted and accuracy of 0.81
---Insersetion---
**Image Models**:
>- Xception: F1-score Weighted and accuracy of 0.66
>- InceptionV3: F1-score Weighted and accuracy of 0.64
---Insersetion---
#### Voting Combinations - Text and Image
We used two combinations for the voting system:
---Insersetion---
>>- **Simple DNN**, **Conv1D**, and **Xception**
>>- **Simple DNN**, **Conv1D**, and **InceptionV3**
---Insersetion---
The weights used in the Weighted Average Voting for each model were:
>>- Simple DNN: **0.81**, Conv1D: **0.80**
>>- Xception: **0.66**, InceptionV3: **0.65**
---Insersetion---

#### Results

##### Simple DNN, Conv1D and Xception
---Insersetion---

##### Simple DNN, Conv1D and InceptionV3
---Insersetion---

##### Analysis of Results from Both Combinations
---Insersetion---
We also submitted our predictions to the challenge website (over 13,000 observations) using both voting combinations and achieved the following results:

>>- Conv1D, Simple DNN, and Xception: submitted on February 21, 2022, with a score of **0.8333**, ranking **27th out of 83**
>>- Conv1D, Simple DNN, and InceptionV3: submitted on March 19, 2022, with a score of **0.8349**, ranking **25th out of 83**
