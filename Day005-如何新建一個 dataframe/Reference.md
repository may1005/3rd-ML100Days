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
## Pandas Foundations : Data ingestion & inspection
[Pandas Foundations](https://www.datacamp.com/courses/pandas-foundations)<br>
第一個 chapter 是免費的，建議可用來預習 pandas，如果覺得英文聽不懂也沒關係，可以按部就班跟著我們後面的課程，也可以學到相關的內容。<br><br>
![](https://ai100-fileentity.cupoy.com/3rd/homework/D5/1566981454012/large)
## 推薦 github repo
馬拉松之後也會有 pandas 操作相關的練習，但若你迫不及待想要更精進自己 pandas 技能，<br>
可以到這個 [github repo](https://github.com/guipsamora/pandas_exercises) 挑戰！<br><br>
![](https://ai100-fileentity.cupoy.com/3rd/homework/D5/1566981467917/large)
## %matplotlib inline
[資料視覺化(Matplotlib, Seaborn, Plotly)](https://medium.com/jameslearningnote/資料分析-機器學習-第2-5講-資料視覺化-matplotlib-seaborn-plotly-75cd353d6d3f)<br>

Python資料視覺化主要有三大套件：
1. Matplotlib
2. Seaborn
3. Plotly<br>

首先要使用matplot的話，跟numpy還有pandas一樣起手式先輸入matplotlib.pyplot as plt。如果要畫折線圖使用 plt.plot，一開始我們先只放一個參數，這樣只會有y的資料，x會是預設的0,1,2,3…。顯示出圖片需要加上.show() 否則只會顯示出這樣的訊息[<matplotlib.lines.Line2D at 0x1100cfe48>]<br>

![](https://miro.medium.com/max/2380/1*409ArBhlxniQ4q657INbpA.png)<br>

如果不想要每次在jupyter notebook顯示都寫.show()，可以在jupyter notebook加上%matplotlib inline<br>
![](https://miro.medium.com/max/2420/1*llN9LEOvTMikRcVHXh7SXw.png)
