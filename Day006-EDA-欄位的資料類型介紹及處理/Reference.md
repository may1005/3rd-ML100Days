# 參考資料
## Sample Code & 作業內容
1. 在初步 EDA 的過程，我們無可避免會想問的問題
    * 不同資料類型各有多少個欄位？
    * 類別型欄位 (pandas 中的 object) 的類別數量?
    * 模型怎麼處理類別型的資料？有什麼表示方法？

2. 這三個問題在參考程式碼範例(請點選下方檢視範例Day_006_column_data_type.ipynb)都會實現，第三個問題會更為複雜一些，簡單來說我們有兩種方法來處理類別型資料 
   * Label encoding: 把每個類別 mapping 到某個整數，不會增加新欄位
   * One Hot encoding: 為每個類別新增一個欄位，用 0/1 表示是否

![](https://ai100-fileentity.cupoy.com/3rd/homework/D6/1566981613434/large)

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

## Label Encoder vs. One Hot Encoder
[Label Encoder vs. One Hot Encoder In ML](https://medium.com/@contactsunny/label-encoder-vs-one-hot-encoder-in-machine-learning-3fc273365621)<br><br>
為了讓機器分析數據，所以要將「字串」轉為電腦看得懂的「數字」，<br>
一般都是使用Label Encoder，如下範例將第一欄「國家」轉為「0、1、2」，<br>
但是這樣容易誤解成「有順序性」的資料。<br><br>
![](https://miro.medium.com/max/800/1*eWtGdqsEXCnX_ZiVw2Ba0g.png)<br><br>
![](https://miro.medium.com/max/634/1*zS-7qHEGhZ7tX6aamc3RpQ.png)<br><br>
所以衍生出One Hot Encoder分類，將一個欄位依「資料種類數」拆分多欄位呈現，<br>
如下0欄是France、1欄是Germny、2欄是Spain：<br><br>
![](https://miro.medium.com/max/1038/1*HMAPmcCtGwZSjSvgS4MKGw.png)

## Pandas 數據類型 csdn - Claroja
[Pandas 數據類型 csdn - Claroja](https://blog.csdn.net/claroja/article/details/72622375)<br>
這邊完整的列舉了 Pandas 所有的類別型態，同學大概知道有哪些即可，若有需要深入了解的，我們在後面的課程會再提及。<br>
![](https://ai100-fileentity.cupoy.com/3rd/homework/D6/1566981660551/large)

