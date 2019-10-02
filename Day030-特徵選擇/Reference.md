# 參考資料
## Sample Code & 作業內容
請參考範例 Day_030_Feature_Selection.ipynb

作業1 : 鐵達尼生存率預測中，試著變更兩種以上的相關係數門檻值，觀察預測能力是否提升?
作業2 : 續上題，使用 L1 Embedding 做特徵選擇(自訂門檻)，觀察預測能力是否提升?

作業請提交Day_030_HW.ipynb

## Data下載
- [打包下載](http://ai100.cupoy.com/file-download/part02/Part02.7z)
- [house_test.csv.gz](http://ai100.cupoy.com/file-download/part02/house_test.csv.gz)
- [house_train.csv.gz](http://ai100.cupoy.com/file-download/part02/house_train.csv.gz)
- [taxi_data1.csv](http://ai100.cupoy.com/file-download/part02/taxi_data1.csv)
- [taxi_data2.csv](http://ai100.cupoy.com/file-download/part02/taxi_data2.csv)
- [titanic_test.csv](http://ai100.cupoy.com/file-download/part02/titanic_test.csv)
- [titanic_train.csv](http://ai100.cupoy.com/file-download/part02/titanic_train.csv)

## 交叉驗證

[【機器學習】交叉驗證（cross-validation）](https://www.itread01.com/content/1545442603.html)<br>
- 留出法 （holdout cross validation）
在機器學習任務中，拿到資料後，我們首先會將原始資料集分為三部分：訓練集、驗證集和測試集。
- k 折交叉驗證（k-fold cross validation）
k個子集，每個子集均做一次測試集，其餘的作為訓練集。交叉驗證重複k次，每次選擇一個子集作為測試集，並將k次的平均交叉驗證識別正確率作為結果。<br>
通常用在資料量少的時候。

## 正規化迴歸 
- ridge(L2 )
- lasso (L1 )
- Elastice net 增加懲罰項來平滑迴歸曲線，來減少共線性及噪音質的特徵變數，ElasticNet是個神奇的版本，他融合了以上L1跟L2 norm，所以他擁有了篩選特徵跟降低模型複雜度的效果，但是要在兩者間權衡到底要用哪個比較多，或是一樣多。<br>

變數過多時有以下三個問題，所以要減少特徵變數
1. 特微變數(n)若大於測試資料集(m)，使用迴歸時會出現無限多組解，e.g. 資料只有8筆，但是特徵卻有80個
2. 特徵變數共線性問題，另外可能會有OVER FITTING的問題，所謂「共線性」，例如生日和年紀同時取會影響模型，要取一個起來
3. 特徵變數不可解釋性

所以用以下的方式來解決特徵變數過多問題
- Ridge Regression透過將懲罰參數(β平方)λ∑pj=1β2j加入目標函式中。也因為該參數為對係數做出二階懲罰，故又稱為L2 Penalty懲罰參數。
- 懲罰參數(β平方)λ∑pj=1β2j，越大越找不出特徵，λ越大，βj=0的數量越多
- Lasso模型在目標函式中所使用的是一階懲罰式(β絶對值)λ∑pj=1|βj|，故又稱為L1 Penalty懲罰參數。
- 目標函數 LASSO. t = 1/λ ,  minimize{SSE=∑ i=1 n (y i –y ^  i ) 2 } > 0 + λ∑pj=1|βj| > 0，二個是要求最小，所以如果λ->無限大，那y就會變0
- PYTHON LASSO 的 ALPHA 變數是 λ 的標準化.也就是界於0 - 1之間
- ALPHA=0，就是線性迴歸了

這時候我們會想要避免模型複雜度太高，也就是跑到太高次去。我們會加入以下的項<br>
![](http://ithelp.ithome.com.tw/upload/images/20161222/20103529lZhfaMSgBB.png)<br>

後來有人提出了用L1 norm來做regularization。<br>
他跟L2 norm最大的不同就是一個是平方一個是用絕對值，<br>
而L1 norm的效果是讓一些不重要或是影響較小的變數係數為0，如此一來就可以同步達到篩選特徵的效果。<br>
|β1|+|β2|> 0，β1=1,β2=0、β1=-1,β2=0、β1=0,β2=1、β1=0,β2=-1，L1 norm畫出來就像個菱形，<br>
![](http://gerardnico.com/wiki/_media/data_mining/lasso_vs_ridge_regression.png?w=800&tok=f55022)<br>


參考網頁：<br>
[Regularized Regression | 正規化迴歸 – Ridge, Lasso, Elastic Net | R語言](https://www.jamleecute.com/regularized-regression-ridge-lasso-elastic/)<br>
[YOUTUBE:Regularization Part 2: Lasso Regression](https://www.youtube.com/watch?v=NGf0voTMlcs)<br>
[YOUTUBE:Regularization Part 3: Elastice net Regression](https://www.youtube.com/watch?v=1dKRdX9bfIo)<br>



