# 參考資料
## Sample Code & 作業內容
請參考範例程式碼 Day_007_Feature_Types.ipynb: 房價預測<br>
執行作業範例Day_007_HW.ipynb：鐵達尼生存預測

* 作業1 : <br>
試著執行作業程式，觀察三種類型的欄位分別進行( 平均 mean / 最大值 Max / 相異值 nunique ) 中的九次操作會有那些問題? 並試著解釋那些發生Error的程式區塊的原因?

* 作業2 : <br>
思考一下，試著舉出今天五種類型以外的一種或多種資料類型，你舉出的新類型是否可以歸在三大類中的某些大類? 所以三大類特徵中，哪一大類處理起來應該最複雜?

作業請提交Day_007_HW.ipynb

## Data下載
* [打包下載](http://ai100.cupoy.com/file-download/part02/Part02.7z)
* [house_test.csv.gz](http://ai100.cupoy.com/file-download/part02/house_test.csv.gz)
* [house_train.csv.gz](http://ai100.cupoy.com/file-download/part02/house_train.csv.gz)
* [taxi_data1.csv](http://ai100.cupoy.com/file-download/part02/taxi_data1.csv)
* [taxi_data2.csv](http://ai100.cupoy.com/file-download/part02/taxi_data2.csv)
* [titanic_test.csv](http://ai100.cupoy.com/file-download/part02/titanic_test.csv)
* [titanic_train.csv](http://ai100.cupoy.com/file-download/part02/itanic_train.csv)

## drop用法

[Python中pandas dataframe删除一行或一列：drop函数](https://blog.csdn.net/songyunli1111/article/details/79306639)<br>

用法：DataFrame.drop(labels=None,axis=0, index=None, columns=None, inplace=False)

参数说明：<br>
- labels 就是要删除的行列的名字，用列表给定
- axis 默认为0，指删除行，因此删除columns时要指定axis=1；
- index 直接指定要删除的行
- columns 直接指定要删除的列
- inplace=False，默认该删除操作不改变原数据，而是返回一个执行删除操作后的新dataframe；
- inplace=True，则会直接在原数据上进行删除操作，删除后无法返回。

因此，删除行列有两种方式：
1. labels=None,axis=0 的组合
2. index或columns直接指定要删除的行或列

## concat 用法
[pandas.concat用法詳解](https://www.itread01.com/content/1545045061.html)

![](https://img-blog.csdnimg.cn/20181205152000631.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0FzaGVyMTE3,size_16,color_FFFFFF,t_70)

pd.concat([df1,df2,df3]),預設axis=0，在0軸上合併。

![](https://img-blog.csdnimg.cn/20181205152220793.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0FzaGVyMTE3,size_16,color_FFFFFF,t_70)


