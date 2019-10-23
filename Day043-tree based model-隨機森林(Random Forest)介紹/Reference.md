# 參考資料
## Sample Code & 作業內容
閱讀以下兩篇文獻，了解隨機森林原理，並試著回答後續的思考問題<br>
[隨機森林 (random forest) - 中文](http://hhtucode.blogspot.com/2013/06/ml-random-forest.html)<br>
[how random forest works - 英文](https://medium.com/@Synced/how-random-forest-algorithm-works-in-machine-learning-3c0fe15b6674)<br>

1. 隨機森林中的每一棵樹，是希望能夠<br>
沒有任何限制，讓樹可以持續生長 (讓樹生成很深，讓模型變得複雜)<br>
不要過度生長，避免 Overfitting<br>

2. 假設總共有 N 筆資料，每棵樹用取後放回的方式抽了總共 N 筆資料生成，請問這棵樹大約使用了多少 % 不重複的原資料生成?<br>
hint: 0.632 bootstrap<br>

作業請提交Day_043_HW.ipynb

## 隨機森林 

- 多棵決策樹組成
- Bagging : 多次隨機抽取再放回組成多顆的Subset Tree
- 因為隨機，權重1:1
- 多個Subset Tree做成的多個Model，最後決定用「平均數\投票」
- 可減少variance：使分散程度更集中

![](https://img.itw01.com/images/2018/10/20/16/0744_F0KU6a_QO86TEH.jpg)

## Variance & Bias

- Variance : 分散程度，通常Bagging可降低
- Bias : 正中位置，通常Boosting可降低

![](https://miro.medium.com/max/936/1*xwtSpR_zg7j7zusa4IDHNQ.png)

Overfitting擁有High Variance和Low Bias
![](https://miro.medium.com/max/1660/1*9hPX9pAO3jqLrzt0IE3JzA.png)

實務上，因為無法找到最低的Variance和最低的Bias，所以只能找相對低點 
![](https://miro.medium.com/max/1124/1*RQ6ICt_FBSx6mkAsGVwx8g.png)

## 为什么说bagging是减少variance，而boosting是减少bias?

Bagging相当于对训练数据做一定程度的扰动，造成基分类器的多样性，<br>
由于基分类器优化的目标本质上是一致的，<br>
因此variance会随着集成过程的进行而降低，<br>
但是无法降低bias。<br>

Boosting的理论保证了其本质上是一个优化算法，<br>
集成分类器整体具有一个优化目标，<br>
即Boosting的训练过程最终可以使集成分类器收敛到最优贝叶斯决策，<br>
因此降低了bias，而这个性质是Bagging不具有的。<br>

