# 參考資料
## Sample Code & 作業內容
今日作業：
- 新增一個欄位 customized_age_grp，把 age 分為 (0, 10], (10, 20], (20, 30], (30, 50], (50, 100] 這五組， '(' 表示不包含, ']' 表示包含
- Hints: 執行 ??pd.cut()，了解提供其中 bins 這個參數的使用方式

作業目標：
- 請同學試著查詢 pandas.cut 這個函數還有哪些參數, 藉由改動參數以達成目標
- 藉由查詢與改動參數的過程, 熟悉查詢函數的方法與理解參數性質, 並了解數值的離散化的調整工具

請參考範例程式碼Day_017_discretizing，作業請提交Day_017_HW

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

## 連續型離散化優點
- 不用另外處理outliner
- 非線性迴歸擬合度高

## 迴歸
例如y為人類活動力，a為權重，x1為連續型的年齡1-99歲<br>
將連續行的y=ax1+d，<br>
化解為非線性的y=ax1+bx2+cx3+d，<br>
其中，x1為1-30歲的青年人，x2為31-60的中年人，x3為61-99的老年人，<br>
可再依照權重調配迴歸線。<br><br>

若是一個29歲的人，<br>
則x1=1，x2=0，x3=0。<br>

## Over Fitting vs Under Fitting
- Over Fitting : Training Model的效度太高，但是Test的結果很差
- Under Fitting : Training Model的效度太低

通常Over Fitting都會等Test才會發現，<br>
比較預測值和實際值，求MSE越小越好。

## Pandas.cut 相關API
[Pandas.cut相關參數](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.cut.html#pandas.cut)<br>
[label應用](https://medium.com/@morris_tai/pandas%E7%9A%84cut-qcut%E5%87%BD%E6%95%B8-93c244e34cfc)

