# 參考資料
## Data下載
* [打包下載](http://ai100.cupoy.com/file-download/part01/Part01.7z)
* [application_test.csv](http://ai100.cupoy.com/file-download/part01/application_test.csv)
* [application_train.csv](http://ai100.cupoy.com/file-download/part01/application_train.csv)
* [bureau_balance.csv](http://ai100.cupoy.com/file-download/part01/bureau_balance.csv)
* [bureau.csv](http://ai100.cupoy.com/file-download/part01/bureau.csv)
* [credit_card_balance.csv](http://ai100.cupoy.com/file-download/part01/credit_card_balance.csv)
* [example.jpg](http://ai100.cupoy.com/file-download/part01/example.jpg)
* [example.mat](http://ai100.cupoy.com/file-download/part01/example.mat)
* [example.npy](http://ai100.cupoy.com/file-download/part01/example.npy)
* [example.pkl](http://ai100.cupoy.com/file-download/part01/example.pkl)
* [example.txt](http://ai100.cupoy.com/file-download/part01/example.txt)
* [example01.json](http://ai100.cupoy.com/file-download/part01/example01.json)
* [example02.json](http://ai100.cupoy.com/file-download/part01/example02.json)
* [HomeCredit_columns_description.csv](http://ai100.cupoy.com/file-download/part01/HomeCredit_columns_description.csv)
* [installments_payments.csv](http://ai100.cupoy.com/file-download/part01/installments_payments.csv)
* [POS_CASH_balance.csv](http://ai100.cupoy.com/file-download/part01/POS_CASH_balance.csv)
* [previous_application.csv](http://ai100.cupoy.com/file-download/part01/previous_application.csv)
* [sample_submission.csv](http://ai100.cupoy.com/file-download/part01/sample_submission.csv)

## 探索式資料分析簡介
[吳漢銘老師](http://www.hmwu.idv.tw/web/R_AI/AI-D3-1-hmwu_R_EDA.pdf)<br>
這是吳老師講解探索式資料分析(EDA)的內容，比較側重於理論部分，同學可以在這裡看到許多豐富的資料，對照我們後續的課程內容，可以讓您更了解EDA的全貌。
建議同學可以閱讀自己有興趣的部分即可，有必要了解的細節，我們會在後續課程中提到。<br>
![PIC](https://ai100-fileentity.cupoy.com/3rd/homework/D4/1566980173052/large)
## What is Exploratory Data Analysis?
[towards data science Prasad Patil](https://towardsdatascience.com/exploratory-data-analysis-8fc1cb20fd15)<br>
這是另一份 EDA 的教學，比較側重於圖形與對應的程式碼，比較接近我們後續的課程形式
從這些範例中，我們可以看到有分布圖 (左)，蜂窩聯合圖(中)，分類散佈圖(右)，
這些圖形都可以輕鬆藉由 seaborn 套件繪製，所以只要我們在後續課程中學會這些，就可以輕鬆完成資料視覺化。<br>
![PIC](https://ai100-fileentity.cupoy.com/3rd/homework/D4/1566980192493/large)
## ROC曲線
[接收者操作特征曲線(receiver operating characteristic curve)](https://zh.wikipedia.org/wiki/ROC曲线)
1. 選擇`最佳模型`
2. 設定`threshold`，例如血壓以收縮壓140／舒張壓90為閾值<br><br>
![PIC](https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Roccurves.png/440px-Roccurves.png)
## ROC空間
让我们来看在實際有100个阳性和100个阴性的案例時，四種預測方法（可能是四種分類器，或是同一分類器的四種閾值設定）的結果差異：<br>
![](https://upload.cc/i1/2019/08/30/4WQB6U.png)
將這4種结果畫在ROC空间裡：
點與随机猜测线的距離，是預測力的指標：离左上角越近的點預測（診斷）準確率越高。離右下角越近的點，预测越不準。
* 在A、B、C三者當中，最好的結果是`A方法`。
* `B方法`的结果位於随机猜测线（對角線）上，在例子中我们可以看到B的準確度（ACC，定義見前面表格）是50%。
* `C方法`雖然預測準確度最差，甚至劣於隨機分類，也就是低於0.5（低於對角線）。然而，当将C以 (0.5, 0.5) 為中點作一个镜像后，C'的结果甚至要比A还要好。这个作镜像的方法，简单說，不管C（或任何ROC點低於對角線的情況）预测了什么，就做相反的結論。
![](https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/ROC_space-2.png/700px-ROC_space-2.png)
## ROC曲線
同一個`二元分類模型的閾值`可能設定為高或低，每種閾值的設定會得出不同的FPR和TPR
* 當閾值設定為最高時，必得出ROC座標系左下角的點 (0, 0)。
* 當閾值設定為最低時，必得出ROC座標系右上角的點 (1, 1)。
* 隨著閾值調低，ROC點 往右上（或右／或上）移動，或不動；但絕不會往左下(或左／或下)移動。<br><br>
![](https://upload.wikimedia.org/wikipedia/commons/5/5c/ROCfig.PNG)
## 曲線下面積（AUC）
ROC曲線下方的面積 Area under the Curve of ROC (AUC ROC)<br>
* 比較曲線下面積做為`模型優劣`的指標
* 因為是在1x1的方格裡求面積，AUC必在`0~1`之間。
* AUC值越大的分類器，正確率越高。
  - AUC = 1，是完美分類器
  - 0.5 < AUC < 1，優於隨機猜測
  - AUC = 0.5，跟隨機猜測一樣
  - AUC < 0.5，比隨機猜測還差<br><br>
![](https://upload.wikimedia.org/wikipedia/commons/b/b9/Curvas.png)
## Pandas:讀取以及管理理資料
[基礎教材](https://bookdata.readthedocs.io/en/latest/base/01_pandas.html#DataFrame-入门)
```python
df.info()
```
<class 'pandas.core.frame.DataFrame'><br>
RangeIndex: 10 entries, 0 to 9<br>
Data columns (total 4 columns):<br>
A    10 non-null float64<br>
B    10 non-null float64<br>
C    10 non-null float64<br>
D    10 non-null float64br<br>
dtypes: float64(4)<br>
memory usage: 392.0 bytes<br>
