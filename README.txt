The test environment is CentOS7 

The compiler used is Python 3.7

Execution command.

```
python STG.py input1.kiss output1.kiss output1.dot
```

If you want to visualize the output dot file 

Install graphviz in CentOS environment and run command:

```
sudo yum install graphviz
dot -T png output1.dot > output1.png
```
