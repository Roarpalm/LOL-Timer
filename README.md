# 召唤师技能计时器
无读取游戏数据，一切手动

进入游戏点击开始，开始计时

看到对方交技能后点击对应技能，自动计算CD并复制到粘贴板，可在游戏中CTRL+V告知队友

点击重置可清空文本和计时

![Instructions](img.png?raw=true)

打包命令：
```python
pyinstaller -w -F -c 召唤师技能计时器.pyw  --hidden-import PySide2.QtXml
```

## 2020年3月29日更新：
增加更多的召唤师技能

打包了一个.exe文件