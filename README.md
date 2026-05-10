# CS5481 Topic 2: Automated Topic Summary Generator

## 项目简介
本项目是一个全自动化的新闻摘要生成管道，专注于“第十五届全运会”。
包含三个步骤：数据爬取 -> LLM 深度分析 -> 静态网页生成。

## 安装依赖
在终端运行：
pip install -r requirements.txt

## 运行步骤

### 1. 爬取数据
python crawler.py
> 输出: national_games.json

### 2. 模型分析
python process.py
> 输出: processed_data.json

### 3. 生成网页
python visualization.py
> 读取 template.html 和 processed_data.json
> 输出: index.html (最终成品)

接入LLM的时候有一个API key，我随便注册了一个QWEN的用了
其他好像都要付费，QWEN有一定的免费额度T^T.
要是大家有别的API可以用也可以把它换掉，生成新的文件之后运行就可以了