# 參考資料
## Sample Code & 作業內容
你可能聽過 XGBoost/Light-GBM，這些都是資料科學競賽中最常用的機器學習模型，但其實這些演算法背後原理都是基於 Gradient-boosting 進而優化，強烈建議您對本日的課程與補充教材多花點時間閱讀與理解。 核心概念就是透過計算梯度，來讓下一棵生成的樹能夠根據梯度方向，試圖讓 Loss 變得更小！

 本日作業請完整閱讀以下任一文獻即可：
- [Kaggle 大師帶你了解梯度提升機原理 - 英文](http://blog.kaggle.com/2017/01/23/a-kaggle-master-explains-gradient-boosting/)
- [完整的 Ensemble 概念 by 李宏毅教授](https://www.youtube.com/watch?v=tH9FH1DH5n0)
- [深入了解 Gradient-boosting - 英文](https://explained.ai/gradient-boosting/index.html)

完成閱讀後，請記得到下方按下完成作業。

## 梯度提升機

- 使用boosting方法
- 針對「Error分錯的」再加重權限分類
- 可降低Bias

![](https://hackernoon.com/hn-images/1*_OR57AG1IjL2yqYXMTtOGw.png)

![](https://miro.medium.com/max/1700/0*paPv7vXuq4eBHZY7.png)

![](https://static.packt-cdn.com/products/9781788295758/graphics/image_04_046-1.png)

多棵有權重的樹<br>
![](https://miro.medium.com/max/1026/1*q9D2Lr9Uw8xvUjlj7OmMow.png)

## 隨機森林(bagging) & 梯度提升機(boosting)

![](https://miro.medium.com/max/3288/1*GNO2x4yFFhe_Enr_X8wfVw.png)

