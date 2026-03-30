Sachant la complixité de notre jeu de données Images et les ressemblances qui existent entre les différentes classes, nous avons rapidement opté pour l’utilisation des méthodes d’apprentissage par transfert(transfert learning) avec des modèles  reposant sur les  réseaux de neurones artificiels, capables d’apprentissage profond (Deep Learning). Nous avons ainsi utilisé les modèles les plus adaptés aux images : les  réseau de neurones convolutifs (CNN)
---Insersetion---
#### Choix des modèles pré-entrainés

Parmis la listes des modèles présentés [ici](https://keras.io/api/applications/),
nous avons retenu les modèles qui ont le moins de paramètres afin de réduire les durées d’entrainement et limiter ainsi les contraintes liées au manque de ressources de calcul
---Insersetion---
>-	**Optimiseur** : Adam est un optimiseur adaptatif éprouvé et très populaire
>-	**Fonction de perte**: la « ***Categorical Cross-Entropy*** » adaptée à notre cas de  classification multi-classes
>-	**Batch size** : 32 et 64 ont été testés
>-	**Learning rate (LR)** :  modèles entrainés avec un LR à 0.001 (valeur par défaut), ensuite un de très faible valeur à 0.00001. Et enfin avec les valeurs obenues à l’issu de l’étape de l’optimtisation des Learning Rate

>- **Augmentation de données** appliquée aux images du jeu de données d’entrainement :
>>- Mise à l'échelle des pixels entre 0 et 1 
>>- Étirement de l'image selon un certain angle.  Donne à l’image un aspect plus écrasé ou étiré en diagonale
>>- Plage de rotation à rotation aléatoire [-45, 45]
>>- Mouvement de l'image dans le sens horizontal par rapport à la largeur de l'image
>>- Mouvement de l'image dans le sens vertical par rapport à la hauteur de l'image
>>- Plage de zoom : zoom arrière et zoom avant [-20%, +20%]
>>- Retournement de l'image horizontalement
>>- Retournement de l'image verticalement
---Insersetion---

#### Etape 1 - Sélection des meilleurs modèles

###### Démarche
>>>-&nbsp;Entrainer les modèles selectionnés avec des images d’entrées de diffrérentes tailles, et ce sans augmentation de données ni fine-tuning</br>
>>>-&nbsp;Utiliser le Learning rate(LR) par défaut (0.001)</br>
>>>-&nbsp;Varier le batch size  de 32 à 64</br>
>>>-&nbsp;Varier le nombre d’Epoch de 10, 20 à 40</br>
>>>-&nbsp;Noter les 5 meilleurs modèles selon la mesure F1-score weighted</br>
---Insersetion---
###### Résultats
Les résultats de l'ensemble des modèles testés:
---Insersetion---
Les 5 meilleurs modèles selon F1-score Weighted sont :
---Insersetion---
##### Etape 2 - Augmentation des données avec les meilleurs modèles obtenus à l’Etape 1

###### Démarche
>>>-&nbsp;Entrainer les 5 meilleurs modèles de l’Etape 1 avec augmentation des données (sans fine-tuning  et  LR toujours par défaut à 0.001)
###### Résultats
---Insersetion---


##### Etape 3 - Augmentation des données + fine tuning des modèles 

###### Démarche
>>>-&nbsp;Fine tuning des meilleurs modèles obtenus à l’Etape 1 </br>
>>>-(Décongélation de certaines couches de nos modèles pré-entrainés)
>>>-&nbsp;Utiliser un LR très fabile(0.00001) </br>
>>>-&nbsp;Et augmentation du nombre d’Epochs  de 40 , 50 à 60</br>
###### Résultats
---Insersetion---


##### Etape 4 - Optimisation LR (Sans augmentation des données ni fine-tuning)

###### Démarche
>> Nous avons suivi la méthode décrite dans [cet article](https://towardsdatascience.com/how-to-optimize-learning-rate-with-tensorflow-its-easier-than-you-think-164f980a7c7b) (En utilisant le callback LearningRateScheduler): 
>>>-&nbsp;&nbsp;Commencer l’entrainement avec un très faible LR (0,00001) puis augmenter sa valeur de manière exponentielle au fur à mesure des Epochs jusqu'à atteindre ≈ 2,54</br>
>>>-&nbsp;&nbsp;Etudier les courbes des résultats (perte et accuracy en fonction du LR et des Epochs)</br>
>>>-&nbsp;&nbsp;Identifier le LR qui réalise la plus petite perte (correspond en général à la plus grande accuracy), à condition que les valeurs qui l'entourent ne soient pas trop volatiles</br>
###### Résultats
Voici les LR obtenus pour nos différents modèls: 
---Insersetion---
L'accuracy :
-	L'accuracy augmente lègèrement jusqu'à l'Epoch 30 
-	Commence ensuite à baisser jusqu'à l'Epoch 63 
-	Elle fluctue très légèrement entre l'Epoch 64 et 67
-	S’ aplatie ensuite à partir de l’Epoch 68 et ce juqu'à la fin de l’entrainement
La perte : 
-	L'exact opposé est arrivé à la perte jusqu'à l'Epoch 63 (Ce qui est logique)
-	Fluctue  légèrement entre l'Epoch 64 et 69 
-	S'aplatie  pratiquement entre l’Epoch 70 et 80 
-	Fluctue esnuite significativicement à partir de l'Epoch 80 et jusqu'à la fin del’entrainement
---Insersetion---
Le taux d'apprentissage optimal(avec la plus faible perte) est d'environ 0,0004
---Insersetion---
##### Etape 5 - Augmentation des données, fine-tuning avec les LRs optimisés

###### Démarche
>>>-&nbsp;&nbsp;Ré-entrainer nos 5 modèles avec les LR opitimaux identifiés à l’étape précédente
---Insersetion---
###### Résultats
---Insersetion---
>- Seulement 1% de plus au niveau du F1-score Weighted pour le modèle Xception 
>- 1% de plus en F1-score Weighted et en accuracy pour le modèle InceptionV3
>- Les deux modèles semblent avoir atteint leurs limites avec ce jeu de données Images !
>- Par contre, ils atteignent ces performances beaucoup plus rapidement avec les LRs optimisés
---Insersetion---
#### Conclusion
>	Les 2 meilleurs résultats ont été obtenus avec :
>>-	**Xception**: LR à 0,0004 , F1-score Weighted à **0.66** 
>>-	**InceptionV3**:LR à 0,0003,  F1-score weighted **0.65** 
(Avec augmentation des données et fine-tuning)

Ces résultats dépassent largement ceux annoncés dans le modèle de référence Rakuten pour la classification basée sur les données Images(0.55)
---Insersetion---
