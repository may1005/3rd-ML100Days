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
