# 參考資料
## Sample Code & 作業內容
請觀看李宏毅教授以神奇寶貝進化 CP 值預測的範例，解說何謂機器學習與過擬合。<br>
影片連結：[ML Lecture 1: Regression - Case Study](https://www.youtube.com/watch?v=fegAeph9UaA)

看完影片請回答以下問題：
1. 模型的泛化能力 (generalization) 是指什麼？
2. 分類問題與回歸問題分別可用的目標函數有哪些？

請點擊檢視範例，作業請提交Day_033_HW.ipynb

## 模型的泛化能力 (generalization)

- 這是機器學習中最佳化（optimization）和泛化（generalization）之間的 trade-off 。
- 最佳化（optimization） 的目的是找到最小化訓練集損失的最佳參數。
- 泛化（generalization） 則是說明了模型對看不見的數據的行為。

本文介紹了六種避免 Overfitting 的方法：
1. 搜集更多資料
資料的收集可以降低 Overfitting 的風險。在資料分析任務中，更多的數據往往能提高模型的準確性，且減少過度擬合的可能性。
客戶無法提供大量資料，或是資料本身是 skewed distribution(左偏或右偏的分佈)。
2. Dropout
透過減少神經網絡的層數、神經元個數等方式，可以限制神經網絡的擬合能力
3. Early Stopping
在每一個 epoch 結束時計算驗證集（validation data）的準確率，當準確率不再提高就停止訓練。
4. Data augmentation
如果是圖片相關任務的話，我通常會用到 Data augmentation 的方式，它會增加本身數據的多樣性。
5. Weight Decay
原理是在 cost function 的後面增加一個懲罰項（代表對某些參數做一些限制），如果一個權重太大，將導致代價過大，因此在反向傳播後就會對該權重進行懲罰，使其保持在一個較小的值。
6. 簡化模型複雜
Overfitting 某方面是呈現出目前模型太強大了，已知具有太多層和隱藏單元的神經網絡非常複雜，所以另一個避免 Overfitting 的方法是直接是減小模型的大小。

## 分類問題與回歸問題分別可用的目標函數有哪些？
目標函數基本上都是「損失函數(loss function)」
[機器/深度學習: 基礎介紹-損失函數(loss function)](https://medium.com/@chih.sheng.huang821/機器-深度學習-基礎介紹-損失函數-loss-function-2dcac5ebb6cb)
