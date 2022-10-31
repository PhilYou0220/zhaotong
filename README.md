> 参考文章
> https://blog.csdn.net/chen__an/article/details/102681701
> https://zhuanlan.zhihu.com/p/130882819

# 总述

## 手工测试的缺点
    创造未来的最好方法就是重述历史,研究历史不是为了延续过去,而是从过去中解放出来。--《未来简史》
    我们来简单回顾下手工测试的缺点
    1.回归BUG方面:重复的手工回归测试，代价昂贵、容易出错，由于没有及时回归会推迟上线时间 开发人员不知道BUG是否修改正确 在那里苦苦等待 想下班却不能下班 
    2.软件质量：软件测试质量依赖于测试工程师的能力（经验，思维） 测试人员的更替对软件质量影响明显 
    3.在原有模块的测试进行额外开发 如视频巡检增加巡检餐饮 要考虑是否影响原有的功能 没有对原有功能进行测试
## 自动化的好处
    1.可重复（复用）性：自动化测试可以替代大量的手工机械重复性操作，相同模块
    2.时间选择性：自动化测试可以更好地利用无人值守时间，去更频繁地执行测试，特别适合现在非工作时间执行测试，工作时间分析失败用例的工作模式；
    3.高效率性：一个字--快！代码执行时间和手工验证时间相比，代码执行时间非常短，可以大幅提升回归测试的效率
    4.可信任性：自动化测试一旦发现问题，在排除测试代码、测试数据、对需求误解的错误外，其结果还是可以信任的，因为它里面没有人的主观意识的参与，代码不会骗人的
    5.固化资产：固化公司资产，自动化测试会留下代码，即使有人员离职，下一个人也可以快速接手 如同研发组人员更替一样
    6.提升技术：搞自动化的过程中可以提高个人和团队的技术，为公司更上一层楼打好基础、做好准备
##自动化的成本
    1.自动化测试比起手工测试对测试人员的技术有一定要求，那么公司用人成本会增加
    2.自动化测试用例的开发工作量远大于单次的手工测试，所以只有当开发完成的测试用例的有效执行次数大于等于5次时，才能收回自动化测试的成本。

## 哪些项目适合自动化
    1.接口自动化要求：项目为前后端分离的项目
    2.稳定的项目(或者叫做产品)： 短期的一次性项目，就算从技术上讲自动化测试的可行性很高，但从投入产出比（ROI）的角度看并不建议实施自动化，因为千辛万苦开发完成的自动化用例可能执行一两次，项目就结束了。

## 自动化能否取代手工测试？
    1.自动化测试并不能取代手工测试，它只能替代手工测试中执行频率高、机械化的重复步骤
    2.自动测试远比手动测试脆弱，无法应对被测系统的变化，业界一直有句玩笑话“开发手一抖，测试忙一宿”，这也从侧面反映了自动化测试用例的维护成本一直居高不下的事实。
    3.测试的效率很大程度上依赖自动化测试用例的设计以及实现质量，不稳定的自动化测试用例实现比没有自动化更糟糕
    4.代码本身并没有想象力，人才有，无法发挥人的主观能动性



## 设计模式
```python
page object UI自动化
公共（工具）层  （初始化浏览器 打开 关闭浏览器 ，log日志的记录）
元素定位层      定位各种元素
操作层         操作各种元素（如输入，点击） 
用例层         根据具体需求 操作各种元素（如先打开某个页面，再点击某个按钮）
数据层         各种定位数据 输入数据
```

```python
api object  接口自动化
公共（工具）层  （数据库操作  日志处理）
接口层         请求接口
业务层         根据业务注入不同请求参数去请求接口 
用例层         组合接口（或不组合） 实现用例
数据层         各种请求参数
```
单个接口 整体思路 用例数据-->请求接口(api_level)(包括读取用例数据(read_config)，组装用例数据(parse_data)，请求接口(auth_requests))-->断言用例(testcase_api)
关联接口 整体思路 用例数据-->请求接口(api_level)(包括读取用例数据(read_config)，组装用例数据(parse_data)，请求接口(auth_requests))-->设计场景-->断言用例(testcase_api)
### api_level
    api_level 包括api层和业务数据层 完成业务数据的组装和请求接口和在测试报告里测试步骤的呈现 
### test_case
    用例层，会调用API层 选择合适的用例数据、查询数据库、更新数据库、更新用例数据、进行场景设计和断言，判断用例是否通过
### tools
    工具层 包括数据库连接、日志记录、更新数据表字段等方法和工具
### 数据层
    位于数据库中存储用例数据（包括请求方式、url、请求参数、预期结果等）
### 测试报告生成
    通过三方插件工具allure生成精美的报告
    
## pytest.ini的使用

命令行的参数，用空格分隔 这里写了，命令行或者 pytest.main(["-sv", "test_001.py"])就不用写-sv了

    addopts = -sv
测试用例的路径

    testpaths = scripts

模块名的规则

    python_files = test_parametrize.py

类名的规则 类里一定不包含 __init__ 方法

    python_classes = Test*


方法名的规则

    python_functions = test*


测试用例中添加了 @pytest.mark.webtest 装饰器，如果不添加marks选项的话，就会报warnings

**

    markers =
        smoke: smoke test
        uint: uint test
        system: system test**

设置xfail_strict = True可以让那些标记为@pytest.mark.xfail但实际通过显示XPASS的测试用例被报告为失败

    xfail_strict = True

;控制台实时输出日志 True 打开 False 关闭

    log_cli=True

pytest 收集测试用例时，会递归遍历所有子目录，包括某些你明知道没必要遍历的目录，遇到这种情况，可以使用 norecursedirs 参数简化 pytest 的搜索工作【还是挺有用的！！！】

    norecursedirs = .* build dist CVS _darcs {arch} *.e**__**gg venv src resources log report util


    

# 一些插件的使用
## pytest_check
``pytest_check 断言插件``

为什么使用 pytest_check 进行断言？

    原先使用if 条件语句进行断言
```python
if dict_expect_return_data == dict_return_data and status_code == real_status_code and result1:
    pass
else:
    pass
```
    上图有三个条件 若走到else里 不直观不知道哪个条件出问题了
    不使用 原生断言 assert 是因为不能进行连续断言 一但某个条件出错将不会执行下面的断言
    不选用pytest-assume可以连续断言 但不会显示 变量的实际值  如 pytest.assume(status_code == real_status_code)有问题我们只知道它出问题了 而不知道值是多少
    因此我们选用pytest_check 连续断言 可以知道断言变量的实际值 利于排查问题 减少了代码量

```python
"""官方用例+笔者执行方法"""
import pytest_check as check
import pytest
def test_example():
    a = 1
    b = 2
    c = [2, 4, 6]
    check.equal(1, 3)
    check.greater(a, b)
    check.less_equal(b, a)
    check.is_in(b, c, "Is 1 in the list")
    check.is_not_in(b, c, "make sure 2 isn't in list")
if __name__ == '__main__':
    pytest.main(["-sv", "test_1.py"])
```
**其余方法**

    check.equal - a == b
    check.not_equal - a != b
    check.is_ - a is b
    check.is_not - a is not b
    check.is_true - bool(x) is True
    check.is_false - bool(x) is False
    check.is_none - x is None
    check.is_not_none - x is not None
    check.is_in - a in b
    check.is_not_in - a not in b
    check.is_instance - isinstance(a, b)
    check.is_not_instance - not isinstance(a, b)
    check.almost_equal - a == pytest.approx(b, rel, abs) see at: pytest.approx
    check.not_almost_equal - a != pytest.approx(b, rel, abs) see at: pytest.approx
    check.greater - a > b
    check.greater_equal - a >= b
    check.less - a < b
    check.less_equal - a <= b
## jsonpath库
```用于json路径获取及过滤json```
```python
from jsonpath import jsonpath

data1 = {"data": [{"areaName": "青白江区", "day": "2022-04-14", "count": 3}, {"areaName": "青白江区", "day": "2022-04-15", "count": 3}], "dayCount": 1}

result = jsonpath(data1, "$.data[0].areaName")  # 根节点data下的第0个值，查找他的areaName

result1 = jsonpath(data1, "$..areaName")  # 模糊查询.两个点是搜索所有的层级的。返回的是一个list 全部添加到列表中去
print(result)
print(result1)
```
    注意jsonpath取出来是个列表，若想用里面的数据记得记得用索引或其他方式取出来用
## allure 
新建项目时不要管report目录 运行下面命令时会自动生成目录及目录下的数据
```python
os.system(
        "allure generate  ../report/temp_jsonreport -o ../report/html --clean")
```
## config.yml
    配置文件，接口前缀，日志级别，数据库等配置都在这个文件改，数据库先写死吧

## 在linux（腾讯云centos 7.9）上运行pytest,allure
    tips：云服务器上不能使用局域网接口和数据库 如以 192.168开头的
    查看安装了哪些包
    pip3 list
### 在linux服务器上安装python 3.9.2
- 1 创建目录 


    mkdir -p /usr/local/python3.9.2
- 2 将下载好的Python-3.9.2.tgz包移到Linux下，然后解压 


    tar -zxvf Python-3.9.2.tgz
- 3 进入解压后的目录 cd Python-3.9.2 编译安装 


    ./configure --prefix=/usr/local/python3.9.2
- 4 编译：


    make
- 5 编译成功后，编译安装：


    make install
- 6 环境变量配置 


    vi /etc/profile 
- 在最下边输入 


    export PYTHON_HOME=/usr/local/python3.9.2
    export PATH=${PYTHON_HOME}/bin:$PATH
- 7 使得配置的环境变量立即生效： 


    source /etc/profile
- 8 检查 应为3.9.2版本的解释器


    python3 --version


### requirements.txt 安装所需要的第三方库
    pip批量导出包含环境中所有组件的requirements.txt文件
    pip3 freeze > requirements.txt

    pip批量安装requirements.txt文件中包含的组件依赖
    pip3 install -r requirements.txt
### 在服务器上安装allure
#### 首先安装JDK
- 1 检查服务器上有没得JDK
- java -version
- javac -version
- 2 安装jdk1.8


    yum install -y java-1.8.0-openjdk

- 3 检查是否安装好


    java -version
    javac -version

- 4 设置环境变量
- vim /etc/profile
- 按“i”进入编辑模式，在文件末尾添加一下内容：


    export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.332.b09-1.el7_9.x86_64
    export JRE_HOME=${JAVA_HOME}/jre
    export CLASSPATH=.:${JAVA_HOME}/lib:${JRE_HOME}/lib
    export PATH=${JAVA_HOME}/bin:$PATH

- 5 保存后用source命令是配置立即生效


    source /etc/profile

-6 如果linux7.x下javac:未找到命令的问题，说明环境没有安装
执行命令


    yum install java-devel
- 7 验证java是否安装成功


    javac -version
#### 然后安装allure
- 1 为allure创建目录


    mkdir  /usr/local/allure
- 2 在此目录下解压


    tar -zxvf allure-2.18.0.tgz
- 3 设置环境变量


    vim /etc/profile
- 按“i”进入编辑模式，在文件末尾添加一下内容


    export PATH=$PATH:/usr/local/allure/allure-2.18.1/bin
- 4 保存后用source命令是配置立即生效


    source /etc/profile
- 5  验证allure是否成功


    allure --version
- 6 浏览器打开 allure 报告的两种方式
   
allure serve 标准写法

    # 执行 pytest，指定 allure 结果目录
    pytest -sq --alluredir=./allure
    
    # 打开 allure 报告
    allure serve ./allure

allure generate + allure open 标准写法
    
    # 执行 pytest，指定 allure 结果目录 ./allure是指临时的json文件爆出地址
    pytest -sq --alluredir=./allure
    
    # 生成 allure 的 html 报告 allure-report是指报告的目录 
    allure generate -c -o ./allure-report ./allure
    
    # 打开 allure 报告
    allure open ./allure-report
### 生成公网地址的测试报告，
- 1 生成报告的html文件
```python
os.system(
    "allure generate  ../report/temp_jsonreport -o ../report/html --clean")

```
- 2 生成一个公网地址的测试报告 笔者用的腾讯云服务器 因此绑定的是 0.0.0.0地址 访问的时候替换成服务器的公网IP即可 端口不用替换 端口在腾讯云后台要先开出来
- 这样全公司的人都可以查看测试报告了
# 生成一个网址来访问测试报告 当然浏览器直接访问 html/index.html文件也是可以的

```python
os.system("allure open html -h 0.0.0.0 -p 8889")
```






