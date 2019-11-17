# 參考資料
## Sample Code & 作業內容
在精簡深度學習的方式上：卷積類神經 (CNN) 採用像素遠近，而遞歸類神經 (RNN) 採用著則是時間遠近
作業１：那麼，既然有著類似的設計精神，兩者是否有可能互換應用呢?
作業請提交Day_63_HW<br>

由於從機器學習跨到NN的知識領域範圍較大，有鑑於此，陪跑專家們提供一份補充教材，針對深度學習的基本概念作一個簡要說明，請至範例程式碼內下載「深度學習補充教材」。

## 類神經網路
1. 透過輸入層、隱藏層和輸出層結合，將Ｘi * Wi + B合計再帶入active function中，以"前向傳遞"推測出^Y
2. 再類似監督式學習，會用Loss function計算Y和^Y的誤差。
3. 再以"後向傳遞"tunning出Ｂ和Ｗ，其中W反推新的W會使用到Learning Rate
4. 多次迭代前後傳遞，算出Loss最小收斂

參考[類神經網路 -- Backward Propagation 詳細推導過程](http://cpmarkchang.logdown.com/posts/277349-neural-network-backward-propagation)，

### Forward Phase
![](http://lh3.googleusercontent.com/-jL2GyLqhwVo/VWbfk9q6PwI/AAAAAAAABZI/QojhPNfCpak/w583-h386-no/n1.png)

### Derivation of Backward Propagation
![](http://lh5.googleusercontent.com/-SXvapzxY9Ts/VWb2Yth41wI/AAAAAAAABak/3sPSuiM8jk8/w657-h382-no/bp0.png)
