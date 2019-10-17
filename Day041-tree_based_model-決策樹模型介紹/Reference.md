# 參考資料
## Sample Code & 作業內容

閱讀以下兩篇文獻，了解決策樹原理，並試著回答後續的問題

[決策樹 (Decision Tree) - 中文](https://medium.com/@yehjames/資料分析-機器學習-第3-5講-決策樹-decision-tree-以及隨機森林-random-forest-介紹-7079b0ddfbda)<br>
[how decision tree works - 英文](http://dataaspirant.com/2017/01/30/how-decision-tree-algorithm-works/)

作業１：在分類問題中，若沒有任何限制，決策樹有辦法在訓練時將 training loss 完全降成 0 嗎？

作業２：決策樹做分類問題時，資料的相似度比較容易計算 (是否屬於同一個類別)。那如果變成回歸問題，這時切分後的資料不純度該如何計算？樹建置完成後，又該如何進行預測呢？

作業請繳交Day_041_HW.ipynb

## 父節點決定

* 熵資訊量越小越好，
* 資訊增量越大越好，
* Gini資訊量越小越好。

## 熵資訊量

![](https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/Binary_entropy_plot.svg/400px-Binary_entropy_plot.svg.png)

x軸是事件機率，y軸是熵資訊量，<br>
x軸是事件機率 = 0 和 1 的時候，y軸的熵資訊量為0，因為最穩定，<br>
x軸是事件機率 = 0.5 的時候，y軸的熵資訊量為0.5，因為最浮動，<br>
所以熵資訊量越小，越好越穩定，越可以當決策樹父節點。

## 決策樹youtube影片

決策樹判斷父節點、區間之程式實作youtube影片：
https://youtu.be/IgH5kJmIr6s
