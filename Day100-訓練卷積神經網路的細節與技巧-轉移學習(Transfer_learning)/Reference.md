# 參考資料
## Sample Code & 作業內容
請參考範例程式碼Day100_transfer_learning.ipynb與resnet_builder.py檔，作業請提交Day100_transfer_learning_HW.ipynb

礙於不是所有同學都有 GPU ，今日程式碼範例使用的是簡化版本的 ResNet，確保所有同學都能夠訓練!最後一天的作業請先參考這篇![非常詳盡的文章](https://blog.gtwang.org/programming/keras-resnet-50-pre-trained-model-build-dogs-cats-image-classification-system/)，基本上已經涵蓋了所有訓練CNN 常用的技巧，只要能夠妥善運用這些技巧 (資料增強、遷移學習、調整學習率)，即使簡單的模型也能帶來很高的基準點，再以此基準點微調參數，達到最佳的結果。

另外這些技巧在 Kaggle 上也會被許多人使用，更有人會開發一些新的技巧，例如使把預訓練在 ImageNet 上的模型當成 feature extractor 後，再拿擷取出的特徵重新訓練新的模型，這些技巧再進階的課程我們會在提到，有興趣的同學也可以![參考](https://www.kaggle.com/insaff/img-feature-extraction-with-pretrained-resnet
