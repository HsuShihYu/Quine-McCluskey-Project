測試環境為 CentOS 

使用的編譯器為 Python3.7

執行方法：

ex: python STG.py input1.kiss output1.kiss output1.dot


如果想視覺化 該output dot檔 

在 CentOS 環境安裝 graphviz:
  
指令: sudo yum install graphviz

執行方法： dot -T png output1.dot > output1.png
