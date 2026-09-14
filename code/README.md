# 代码目录

`demo.py` 用于统计文本词频。它会识别连续的英文、数字、下划线和中文文本片段；英文会统一转换为小写。中文若需要严格按词切分，需进一步接入中文分词工具。

运行示例：

```powershell
python code\demo.py path\to\text.txt
python code\demo.py path\to\text.txt --top 10
```
