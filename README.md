# CnkiSpider使用指南（by@zemengchuan）
GitHub链接：https://github.com/zemengchuan/CnkiSpider

## 用途：

CnkiSpider可以通过简单的代码实现高效的知网文章信息爬取，主要爬取的内容包括：【**标题、作者、发表时间、来源、链接**】，并将爬取的结果保存为CSV格式。经测试，某作者在知网上的821篇文章只需要2-4s即可全部获取（不同设备及网络情况可能会出现差异），效率相对而言比较高。

CnkiSpider的高效来自于采用了多线程的方式进行爬取。目前实现了**知网常规的所有搜索方式**进行查询，将来还会持续更新通过其他缩小范围的方式（如发表年度、研究层次等）方式，还计划实现相关的图表分析功能，现在先将实现的部分上传供大家使用

## 安装方式

```python
pip install CnkiSpider
```

## 优势

- 能够在较短时间内爬取大量数据
- 能够实现知网的基本搜索功能

## 缺点

- 目前不能使用更精细的方式（如发表年度、研究层次等）
- 保存的方式较为单一，目前只能保存为csv

## 使用方式

### 1、参数介绍

CnkiSpider的核心函数是`CnkiSpider(search_mode, search_content,author_code='', institution='')`，其中，`searchmode`是搜索模式，可选内容如下表所示：

| 模式 | 描述     |
| ---- | -------- |
| SU   | 主题     |
| TKA  | 篇关摘   |
| KY   | 关键词   |
| TI   | 篇名     |
| FT   | 全文     |
| FU   | 基金     |
| AB   | 摘要     |
| CO   | 小标题   |
| RF   | 参考文献 |
| CLC  | 分类号   |
| LY   | 文献来源 |
| DOI  | DOI      |
| AU   | 作者     |
| FI   | 第一作者 |
| RP   | 通讯作者 |

`search_content`是搜索内容，填入您需要搜索的内容即可；`author_code`和`institution`是使用通过作者查询时的可选参数，为作者代码和作者第一机构，如果不需要通过作者查询或不知道这两个内容，可以不填。

### 2、属性介绍

CnkiSpider对象有以下几个属性供用户调用：

- `.info`返回CnkiSpider对象的基本信息，包含搜索模式、搜索内容和保存路径
- `.path`返回CnkISpider对象的保存路径，可以通过修改该对象将文件保存到自定义的路径
- `.session`返回CnkiSpider的Session对象，供有需求的用户使用

### 3、方法介绍

CnkiSpider对象目前有两个方法：

- `.get_overview(save=True)`获取搜索信息概览，默认保存概览文件overview.csv，可以修改`save=False`不保存文件，函数会返回一个DataFrame对象。使用方法如下：

  ```python
  from CnkiSpider import CnkiSpider
  
  """
  这里使用搜索模式为”第一作者“，且没有作者的代码和机构
  此时函数会自动指引您获得相关信息
  """
  search_mode = 'FI'
  search_content = '钟南山'
  cs = CnkiSpider(
           search_mode=search_mode, 
           search_content=search_content,
  )
  
  df = cs.get_overview()
  ```

  输出结果：

  ```python
  """
  作者              机构
  0  钟南山           中国工程院
  1  钟南山                
  2  钟南山                
  3  钟南山      南昌大学第一附属医院
  4  钟南山   共信医药科技股份有限公司;
  5  钟南山          南风窗杂志社
  6  钟南山         扎木县人民医院
  7  钟南山                
  8  钟南山                
  9  钟南山  上海明品医学数据科技有限公司
  请选择需要查询的作者序号(输入exit退出，输入re再次获取)：0
  "钟南山"在知网上共有记录137条，详细情况如下：
  总库:137篇
  学术期刊:122篇
  特色期刊:8篇
  学术辑刊:0篇
  学位论文:0篇
  博士:0篇
  硕士:0篇
  会议:3篇
  国内会议:3篇
  国际会议:0篇
  会议视频:0篇
  报纸:4篇
  年鉴:0篇
  专利:0篇
  中国专利:0篇
  海外专利:0篇
  图书:0篇
  外文图书:0篇
  中文图书:0篇
  标准:0篇
  国家标准:0篇
  行业标准:0篇
  标准题录:0篇
  成果:0篇
  古籍:0篇
  视频:0篇
  """
  ```

- `.get_result()`返回搜索内容在知网上的所有反馈，并且保存在result.csv文件中。函数会返回一个DataFrame对象。使用方法如下：

  ```python
  from CnkiSpider import CnkiSpider
  
  """
  这里使用搜索模式为”作者“，且提供了作者的代码和机构
  此时函数会自动指引您获得相关信息
  """
  
  search_mode = 'AU'
  author_code = '000039348927'
  institution = '四川大学'
  search_content = '王红宁'
  cs = CnkiSpider(
      search_mode=search_mode, 
      search_content=search_content,
      author_code=author_code,
      institution=institution)
  
  df = cs.get_result()
  ```

  输出结果：

  ```python
  """
  一共有文章428篇
  共需要爬取9页
  ====================================================================================================
  正在爬取第2页……
  正在爬取第3页……
  正在爬取第4页……
  正在爬取第5页……
  正在爬取第6页……
  正在爬取第7页……
  正在爬取第8页……
  正在爬取第9页……
  第9页爬取成功！第9页有28条数据
  第7页爬取成功！第7页有50条数据
  第4页爬取成功！第4页有50条数据
  第6页爬取成功！第6页有50条数据
  第5页爬取成功！第5页有50条数据
  第3页爬取成功！第3页有50条数据
  第2页爬取成功！第2页有50条数据
  第8页爬取成功！第8页有50条数据
  ====================================================================================================
  爬取完成，已将结果保存至./王红宁-AU/
  """
  ```

### 4、使用举例

```python
from CnkiSpider import CnkiSpider

"""
这里使用搜索模式为”篇名“，且没有作者的代码和机构
此时函数会自动指引您获得相关信息
"""
search_mode = 'TI'
search_content = '粘质沙雷氏菌'
cs = CnkiSpider(
         search_mode=search_mode, 
         search_content=search_content,
)

overview_df = cs.get_overview()

result_df = cs.get_result()
```

输出结果：

```python
"""
"粘质沙雷氏菌"在知网上共有记录628条，详细情况如下：
总库:628篇
学术期刊:457篇
特色期刊:0篇
学术辑刊:0篇
学位论文:139篇
博士:19篇
硕士:120篇
会议:28篇
国内会议:27篇
国际会议:1篇
会议视频:0篇
报纸:0篇
年鉴:0篇
专利:0篇
中国专利:0篇
海外专利:0篇
图书:0篇
外文图书:0篇
中文图书:0篇
标准:0篇
国家标准:0篇
行业标准:0篇
标准题录:0篇
成果:4篇
古籍:0篇
视频:0篇
一共有文章628篇
共需要爬取13页
====================================================================================================
正在爬取第2页……
正在爬取第3页……
正在爬取第4页……
正在爬取第5页……
正在爬取第6页……
正在爬取第7页……
正在爬取第8页……
正在爬取第9页……
正在爬取第10页……
正在爬取第11页……
正在爬取第12页……
正在爬取第13页……
第13页爬取成功！第13页有28条数据
第2页爬取成功！第2页有50条数据
第11页爬取成功！第11页有50条数据
第8页爬取成功！第8页有50条数据
第12页爬取成功！第12页有50条数据
第5页爬取成功！第5页有50条数据
第4页爬取成功！第4页有50条数据
第3页爬取成功！第3页有50条数据
第6页爬取成功！第6页有50条数据
第7页爬取成功！第7页有50条数据
第9页爬取成功！第9页有50条数据
第10页爬取成功！第10页有50条数据
====================================================================================================
爬取完成，已将结果保存至./粘质沙雷氏菌-TI/
"""
```

文件预览：

![image-20230220165718595](C:\Users\pc\AppData\Roaming\Typora\typora-user-images\image-20230220165718595.png)

## 计划

- 知网上所有缩小范围方式爬取文献
- 知网上所有文献信息可视化获取
- 设计将数据存储至数据库的函数
- ……