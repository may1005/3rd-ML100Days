# Reference

## Data Scientist、Data Analyst、Data Engineer 的區別是什麼？

[原始連結(英文)](https://www.datacamp.com/community/blog/data-scientist-vs-data-engineer)
[後續討論(簡中)](https://www.zhihu.com/question/23946233)

各位同學第一天開始這些課程，想必在之前多少聽過這些名詞，也帶有不少疑惑，就讓我們看看在業內的專家們怎麼說吧。簡單來說 : 
資料科學家 (Data Scientist) 需要擅長的是數字的敏感度與資料分析工具，訓練偏重統計，也就是本課程想要帶給各位同學的內容。而資料工程師 (Data Engineer) 需要對計算機本身較為熟悉，訓練偏重資料工程，往往需要透過實務的親身經歷來成長，這部分比較難以線上課程的方式提供。

![PIC](https://ai100-fileentity.cupoy.com/3rd/homework/D1/1564482186539/large)

![PIC](https://ai100-fileentity.cupoy.com/3rd/homework/D1/1564482201488/large)

## R or Python for Data Science?

[kdnuggets](https://www.kdnuggets.com/2015/05/r-vs-python-data-science.html)
"學 Python 還是 R 語言好?"  想必這個經典問題, 也曾是不少同學的煩惱吧?
這個網站的回答雖然也很經典，但是製表的日期已經是2014年了，以老師現在(2019年)的觀察來說，R語言雖然在機器學習上比 Python 略為好用，可是在深度學習上，Python 可以說壓著R語言打呢，所以還是建議同學先學 Python 比較穩當。
此外，R語言的另一個好處，是由大量碩博士生貢獻的套件，這個學界霸主的地位已經逐步被 PyTorch 所取代，而業界因為生態系完整的關係，還是以 TensorFlow / Keras 為主，後兩者都是在 Python 上的套件，所以怎麼看，先學 Python 還是比較不虧的。

![PIC](https://ai100-fileentity.cupoy.com/3rd/homework/D1/1564482270812/large)

## [其他參考連結]

[Why Data Scientist Must Focus on Developing Product Sense](https://www.kdnuggets.com/2018/04/data-scientists-product-sense.html)
資料科學家需要目標的領域知識

[Why so many data scientist leaving their jobs](https://www.kdnuggets.com/2018/04/why-data-scientists-leaving-jobs.html)
想當資料科學家 : 三思而後行
 
## Mean Absolute Error(MAE) 平均絕對誤差

* 是絕對誤差的平均值（絕對值後所求的平均值）
* 能更好地反映預測值誤差的實際情況（幫助測量）
* 數字小於1，且越小越好
* 參考：[什麼是平均絕對誤差](http://staruphackers.com/什麼是平均絕對誤差-mean-absolute-error-mae？/)、[常見機器學習評估指標](https://zhuanlan.zhihu.com/p/65663148)
![PIC](https://upload.cc/i1/2019/08/22/1oavtH.png)
![PIC](https://pic4.zhimg.com/80/v2-55462c20cce263774454dfe8f059bd9b_hd.jpg)

## Mean Absolute Error(MAE) 平均絕對誤差

* 是各測量值誤差的平方和取平均值的平方根（均方根誤差的平方）
* 可以評價數據的變化程度
* 數學特性很好，使計算梯度變得更容易
* 參考：[什麼是均方誤差](http://staruphackers.com/什麼是均方誤差-mean-square-error-mse？/)

![PIC](http://staruphackers.com/wp-content/uploads/2019/04/image-6.png)
  
## 深度學習指標

參考：
 [深度學習中](https://www.twblogs.net/a/5c8416bcbd9eee35fc13e15f)、
 [TP FP FN TN precision Recall Accuracy](https://www.twblogs.net/a/5b8e7ef72b71771883459e91)

![PIC](https://pic1.xuehuaimg.com/proxy/csdn/https://img-blog.csdn.net/20180131133832714?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvU3VwZXJZUl8yMTA=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

 * True Positive（TP）：預測爲正例，實際爲正例
 * False Positive（FP）：預測爲正例，實際爲負例
 * True Negative（TN）：預測爲負例，實際爲負例
 * False Negative（FN）：預測爲負例，實際爲正例
 
 ![PIC](https://pic1.xuehuaimg.com/proxy/csdn/https://img-blog.csdnimg.cn/20190307201742301.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2JhbnhpYTE5OTU=,size_16,color_FFFFFF,t_70)
 
 * accuracy : 正確預測的樣本數佔總預測樣本數的比值，它不考慮預測的樣本是正例還是負例。考慮全部樣本。
 * precision : 正確預測的正樣本數佔所有預測爲正樣本的數量的比值，也就是說所有預測爲正樣本的樣本中有多少是真正的正樣本。只關注預測爲正樣本的部份。
 * Recall : 正確預測的正樣本數佔真實正樣本總數的比值，也就是從這些樣本中能夠正確找出多少個正樣本。
 * F-score : 相當於precision和recall的調和平均，recall和precision任何一個數值減小，F-score都會減小，反之，亦然。
 * specificity : 相對於sensitivity（recall）而言的，指的是正確預測的負樣本數佔真實負樣本總數的比值，也就是我能從這些樣本中能夠正確找出多少個負樣本。
 
 
## MAE vs MSE

參考：[如何選擇回歸損失函數？](https://mp.weixin.qq.com/s/Xbi5iOh3xoBIK5kVmqbKYA)<br>
評估實際值和預測值的距離，例如「問我們預測出來的排名，距離實際的排名差了多少」

|    |MAE|MSE|
|---|---|---|
|特性|較同原資料|容易被放大|
|離群值|不適|適合|
|用途||適合商業模型|
|準確|數字越小|數字越小|
|迴歸|收斂慢，次數多|收斂快，次數少|
|梯形|較平|較陡|

## Kaggle
- 包含大量資料科學數據的平台
- 提供「競賽」解題，可上傳Modle和答案來取得排名
- 透過大量「資料集」來發想並解決問題
- Overview介紹資料和來源
- Data資料字典
- Karnel欲解決的問題

範例：[[機器學習專案] Kaggle競賽-鐵達尼號生存預測(Top 3%)](https://medium.com/@yulongtsai/https-medium-com-yulongtsai-titanic-top3-8e64741cc11f)
- 使用探索性分析(EDA)，取出多個資料因子，通常若有過多「空值」較不適合，預先進行「資料清洗」(合併欄位、補空值等)。
- 本篇文章最後用5個特徵(性別、艙等、票價、是否成年、連結)來達到Top3%的公開排名(301/11455)，來預測鐵達尼號的存活率。

範例：[[資料分析&機器學習] 第4.1講 : Kaggle競賽-鐵達尼號生存預測(前16%排名)](https://medium.com/jameslearningnote/資料分析-機器學習-第4-1講-kaggle競賽-鐵達尼號生存預測-前16-排名-a8842fea7077)
- 較初階的文章
- 結合Kaggle討論區文章以及參考閱讀獲得前10%的成績甚至是前5%
- 以正式比賽來說前10%就可以獲得一個銅牌成就

範例：[[機器學習專案]Kaggle競賽-kkbox顧客流失預測(Top5%)](https://medium.com/@yulongtsai/kaggle-kkbox-churn-prediction-top5-c0ea4c9b3f1a)
- 未來可能運用，預測和分群客人是否買單？並可回傳檢查。

範例：[新手玩Kaggle入門](http://terrence.logdown.com/posts/1224642-introduction-to-novice-kaggle)
- 在Kaggle送出第一個submission

範例：[Kaggle-MoneyBall](https://www.kaggle.com/wduckett/moneyball-mlb-stats-19622012)
- 分析大聯盟資料，創建「低預算的明星球隊」
- 評估上壘率(OBP)和打擊率(SLG)
- 來源baseball-reference.com

## Uber

### 核心問題為何？
參考 : [[譯]解密 Uber 資料科學團隊路徑選擇演算法的優化之路](https://codertw.com/程式語言/119643/)
- 找出最短路徑，提升載客率
- 使用ETA推算特性

### 資料從何而來？
[Uber Movement](https://movement.uber.com/explore/taipei/travel-times/query?si=34&ag=taz&dt[tpb]=ALL_DAY&dt[dr][sd]=2018-12-01&dt[dr][ed]=2018-12-31&dt[wd;]=1,2,3,4,5,6,7&cd=&sa;=&sdn=&lng.=121.5244378&z.=12&lat.=25.0735791&ti=77&ta;=&tdn=&lang=en-US)
- 路段行駛時間
- 每週路段平均時間
- 各時段行駛時間

[氣象開放資料平台](https://opendata.cwb.gov.tw/index)
- 台灣未來1週天氣預報
- 過去1小時雨量觀測資料

[交通部即時路況資訊](https://www.motc.gov.tw/ch/home.jsp?id=817&parentpath=0,4)
- 各路段行駛時間

### 蒐集而來的資料型態為何？

字串、數字(結構性資料)

### 你要回答的問題，其如何評估？

建立對照組和實驗組，評估優化和無優化的結果，可能會有些bias(遊行、路障)

 
