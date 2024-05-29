#print函数
print("hello world!")
print("您好" + " 这是一句代码" + " 哈哈") #字符串连接
print('Let\' go!')  #单双引号转义
print("我是第一行\n我是第二行") #换行
print("\n") #空行
print("""第一行
第二行
第三行""") #多行换行
mylove = "13570346789" #赋值操作：给变量一个值的操作;python从上到下使用，先对变量赋值才能使用
print("拨打："+ mylove) #赋值后可以通过变量名获取值，重复使用
myex = mylove #前面的mylove变成myex
mylove = "12345566778" #重新对mylove赋值
print("当前mylove的值:" + mylove) #print的一个作用：在程序逻辑复杂的时候，用print打印出变量的值
greet = "你好，吃饭了吗？" #变量值可发生替换
print(greet + "张三")
print(greet + "李四")

#变量命名
#1.硬性规则：只能由文字、数字、下划线组成；不能有下划线以外的符号；不能有空格；不能数字开头
#2.变量应尽量取得易于理解与记忆
#3.主流是用英文单词做变量名，中文可能会出现不兼容
#4.约定俗成：使用下划线命名法，字母全部小写，不同单词用下划线分隔。如user_name
#5.驼峰命名法：单词用首字母大写分隔；如UserName
#6.注意点：大小写敏感，大小写会被就看作两个不同的变量；不要占用python关键字(30多个)，如print

#用代码写数字运算
#python的整数是直接的数字，和字符串不同的类型，不要用引号包裹
#字符串"6"、整数6、浮点数（带小数点）6.0
#数学运算：加减乘除；运算顺序：（）、**乘方、*\乘除、+-加减
#函数库，将每个函数库想象成一个工具箱，每个函数是一个工具，负责一个功能。math是一个专门提供数学运算函数的库
#内置函数。print是内置函数，已经默认存放了
import math #安装math库
print(math.sin(1)) #打印出运算结果
#math.sqrt()返回平方根
#求一元二次函数的根
a = -1
b = -2
c = 3
print((-b + math.sqrt(b ** 2 - 4 * a * c))/(2 * a)) #求根公式
print((-b - math.sqrt(b ** 2 - 4 * a * c))/(2 * a))

#注释
#单行注释 control+/同时多行单行注释 再一次取消
#多行注释，用三引号包裹注释

#python数据类型
#数据类型：字符串str、整数int、浮点数float、布尔类型bool（是否）、空值类型NoneType（None）、列表、字典等

#字符串str：表示文本内容，被双引号或单引号包裹 
#len("hello")得到字符串长度；完整的转义符占一个长度
print(len("12345"))

#提取字符串某一位置上的单个字符 "Hello"[3]从0开始数，所以索引值为3提取的是第4个字符
print("Hello"[2])

#布尔类型bool 真True 假False 用于逻辑判断
b1 = True
b2 = False
#空值类型NoneType表示完全没有值；需要某个变量但还不知道该变量的值，可以定义为None
c = None

#不确定某个对象类型用type函数，会返回该对象的类型
#数据类型的重要性：决定能在该对象身上运用哪些函数
print(type(c))
print(type(b1))

#python交互模式：读一行执行一行
#两种执行模式：命令行模式、交互模式
#命令行模式：写好代码后，保存并运行整个文件
#交互模式：解释器不读完整个文件就执行某个命令；输入一行后立马执行并展示运行结果
#交互模式特点：不需创建新文件，只需进入交互式环境；不需要用print就可以看到返回结果；所有输入的指令不会被保存

#input函数
#input("给用户的提示信息")
input("请输入你的年龄")
user_age = input("请输入你的年龄") #字符串类型，如做数学运算，会报错
print("知道了，你今年" + user_age + "岁了")
#将其它数据类型转化为整数int类型/浮点数float/字符串str(整数转化为字符串就可以一起打印)
int("555") #转化的内容应能被转化为整数类型

#例子：计算年龄
user_age = int(input("请输入你的年龄:"))
user_age_after_ten_year = user_age + 10
print("您十年后会是" + str(user_age_after_ten_year) + "岁") 

#计算BMI指数：BMI = 体重 / (身高**2)
user_weight = float(input("请输入你的体重(单位:kg):"))
user_height = float(input("请输入你的身高(单位:米):"))
user_BMI = user_weight / (user_height ** 2)
print("你的BMI值为:" + str(user_BMI))

#条件语句
#if [条件]:
#   [执行语句] （每行前面要有缩进）
#   [执行语句]
#else:
#   [执行语句] 
#   [执行语句]
#比较运算符：==(等于)、!=(不等于)、>=、<=
#例子
mood_index = int(input("今天的心情指数是:"))
if mood_index >= 80:
    print("可以出去玩!")
else:
    print("不可以出去玩")

#elif 

#逻辑运算 与或非 优先级排序：not、and、or

#数据列表
#需要定义变量多时，需一个个赋值，比较麻烦。为了解决，需要一个数据结构，把相关联的数据整合在一起
#定义列表 如shopping_list = ["键盘"，"键帽"，"显示器"] 方括号
#往列表中加东西，使用append，如shopping_list.append("手机") 列表的内容发生改变，不需要重新赋值
#移除列表中的东西，使用remove，如shopping_list.remove("显示器")
#列表可存放不同类型的数据，如文本、浮点数、布尔
#同字符串一样，可通过len函数求长度，len函数会返回列表里元素的数量；针对列表，可通过索引获得某个位置的元素，位置从0开始数
#shopping_list[1] = "音响" 索引为1的元素被更改
#python有针对列表的内置函数，如最大值max、最小值min、排序sorted，如print（max（num_list)）
#将原字符串变成大写，比如print（s.upper())

#字典 
#定义电话号码，人名+号码，数据列表只能存储一方面的信息，不适用于两方对应信息，用字典可以将人名与号码绑定
#字典dictionary，用于储存键（key）值（value）对，键有对应的值，键用于查找值
#创建字典：contacts = {"小明"："137","小花"："167"} 往字典中添加键值对:contacts["小样"] = "189"
#获取某个键的值，在字典名后跟方括号，contacts["小明"]
#注意点：键的类型不可变。列表属于可变数据类型，字符串、整数、浮点数、布尔类型属于不可变数据类型
# 需要两个元素作为键，用不可变但很像列表的数据结构 元组tuple（可以放多个元素），example_tuple = ("键盘"，"键帽") 圆括号
# 元组 不可变，不能删除、添加元素
# 元组作为键 contacts = {("张伟", 23):"178",("张伟"，34)："156"}
#字典与列表都是可变的，可以添加（append）和删除（del）键值对
#查询某个键是否存在，"小明" in contacts ,会返回布尔值
contacts = {"小明":"137","小花":"167"}
contacts["小样"] = "189"
query = input("请输入名字")
if query in contacts :
    print(query + "尾号是" + contacts[query])
else:
    print("无")

#for 迭代
#迭代的对象：列表、字典、字符串
#语句：for 变量名 in 可迭代对象
#     对每个变量做一些事情
#temperature_list = [36.4,36.6,36.2,37.8,39,40]
#    for temp >= 38:
#    print(temp)
#    print("发烧了")
#改进：需要知道是谁发烧。有工号为键，体温为值的字典
#temp_dic = {"1":36,"2":37,"3":37.8,"4"=38.8}
#temp_dic.keys() 返回所有键
#temp_dic.values() 返回所有值
#temp_dic.items()  返回所有键值对
temp_dic = {"11":36,"12":37,"13":37.8,"14":38.8}
for id,temp in temp_dic.items():
    if temp >= 38:
        print(id)
#forx循环结合range，range表示整数序列，如range(5,10)表示从5到9，结束值不在序列范围内；range(1,100,5),5表示步长
#计算1到100相加之和
total = 0
for i in range(1,101):
    total = total + i
print(total) #在循环之外，打印最终结果

#while循环 （捕捉日落，持续拍照直到天空亮度小于500）
#measure_brightness函数返回当前测量的天空亮度
#方法1：if函数 但只会判断一次
#if measure_brightness() >= 500
#   take_photo() #拍照

#方法2：加入for函数进行循环,如循环100次，但计算机运行很快，100次很快循环完了
#for i in range(100)
#  if measure_brightness() >= 500
#     take_photo() #拍照

#方法3：while 循环
#while 条件A：
#    行动B  #条件A为真则行动B，为假则结束

#for 与 while 可以相互转化
#如list1 = ["你","好","吗"] 打印出列表的元素
#方法1
#for char in list1:
#   print(char)
#方法2
#for i in range(len(list1))
#    print(list1[i])
#方法3
#i = 0
#while i < len(list1):
#    print(list1[])
#    i = i+1 #忘写这行会进行无限循环

#for循环：有明确循环对象或次数；while循环：循环次数未知

#while循环写一个对用户输入数字求平均值的计算器，用户可以输入任意数量的数字，最后输入q，表示所有数字输入完成，程序给出平均值计算结果
print("这是一个求平均值的程序")
total = 0
count = 0 #赋值的意思
user_input = input("请输入数字（完成所有数字输入后,请输入q终止程序):")
while user_input != "q":
    num = float(user_input) #float将字符串转化为浮点数
    total += num #+=是自加的意思，total = total + num
    count += 1 #count = count +1
    user_input = input("请输入数字（完成所有数字输入后,请输入q终止程序):")
if count == 0: #==是比较运算符，如果两个对象具有相同的值，则相等运算符==返回true
    result = 0
else:
    result = total/count
print("你输入的数字平均值为" + str(result)) #str将数字转化为字符串类型

#格式化字符 群发春节短信
#contacts = ["1","2","3","4"]
for name in contacts:
    massage_content = name + ":岁始之乐，点翠画柳喜开颜。\
                 云开雾散，良辰美景共团圆。祝福" + name +\
                 "及家人新年快乐，平安顺遂，虎年大吉！"
#send_masssge(name,massage_content)  发送短信的函数
#简化格式化字符串的方法1：format方法
#message_content = """
#{0}岁始之乐，点翠画柳喜开颜。
#{1}新年快乐！""".format(year,name)

#简化格式化字符串的方法2：f-字符串
#name = "老林"
#year = "虎"
#message_content = f """
#{year}岁始之乐，点翠画柳喜开颜。
#{name}新年快乐！

#数字对字符串进行格式化
#gpa_dict = {"小明":3.3,"小花":3.8,"小丽":4.2,"小张":3.9}
#for name,gpa in gpa_dict.items():
#   print("{0}你好，你的当前绩点为：{1}".format(name,gpa)) #虽然绩点是浮点数，无需转化为字符串便可打印出 {1:2f} 绩点保留2位小数

#函数，不做复读机 计算扇形的面积并打印
#定做函数，制作一个负责某一特定任务的机器，定义好后，直接用函数，无需反复定义
def calculate_sector(central_angle, radius):
    sector_area = central_angle / 360 * 3.14 * radius ** 2
    print(f"此扇形面积为：{sector_area}")

calculate_sector(160,30)

#改进：在上述程序中并没有任何变量来储存计算结果，无法进行后续使用
#sector_area被赋值计算结果，但在函数里面定义的变量是局部变量，只能在函数内部访问到，在外部无法访问到
#return语句
def func():
    a = 3
    print(a)
    return a #在函数完成调用后，返回变量a的值，即整数3，在函数外部可以使用
#函数没有return语句，默认为return None
def calculate_sector(central_angle, radius):
    sector_area = central_angle / 360 * 3.14 * radius ** 2
    print(f"此扇形面积为：{sector_area}")
    return sector_area
sector_area_1 = calculate_sector(160,34)
sector_area_2 = calculate_sector(180,38) #变量储存不同扇形的面积，可以拿去进行更多后续操作

def calculate_BMI(weight,height): #将if写在内部
    BMI =weight / height ** 2
    if BMI <= 18.5:
        print("您的BMI分类为:偏瘦")
    elif BMI <= 25:
        print("您的BMI分类为:正常")
    elif BMI <= 30:
        print("您的BMI分类为:偏胖")
    else:
        print("您的BMI分类为:肥胖")
    return BMI 
calculate_BMI(50,1.63)

BMI_1 = calculate_BMI(50,1.63)
BMI_2 = calculate_BMI(75,1.78)

if BMI_1 <= 18.5:
    print("您的BMI分类为:偏瘦")
elif 18.5 < BMI_1 <= 25:
    print("您的BMI分类为:正常")
elif 25 < BMI_1 <= 30:
    print("您的BMI分类为:偏胖")
else:
    print("您的BMI分类为:肥胖")

#BMI = calculate_BMI(input("您的体重为:"),input("您的身高为:")) 有问题
#if BMI <= 18.5:
#    print("您的BMI分类为:偏瘦")
#elif 18.5 < BMI <= 25:
#    print("您的BMI分类为:正常")
#elif 25 < BMI <= 30:
#    print("您的BMI分类为:偏胖")
#else:
#    print("您的BMI分类为:肥胖")

#引入模块 python标准库
#定义求中位数的函数
def median(num_list): 
    sorted_list = sorted(num_list)
    n = len(sorted_list)
    #如果一共有奇数个数字，取中间那个
    if n % 2 == 1:
        return sorted_list[n//2] #n//2是向下取整的意思，比如3//2=1
    #如果一共有偶数个数字，取中间两个的平均值
    else:
        return (sorted_list[n//2-1] + sorted_list[n//2]) / 2
print(median([68,23,34,67]))

#引入python模块中的函数，比如python有个模块叫statistics帮助进行统计相关的计算，其中有median用于计算中位数的函数
import statistics #引入模块
print(statistics.median([56,23,22,33,44])) #使用模块中的函数

#引入模块的方法
#1.import语句 import+模块 模块名.函数名 推荐
#2.from...import...语句
#   from statistics import median,mean 引入某个模块中的函数
#   print(median([18,23])) 不需带上模块名
#   print(mean([18,22,33]))
#3.from...import * 将模块中全部函数引入，不需跟上前面的模块名 不推荐，引入多个模块可能会有冲突
#   print(median([18,23])) 不需带上模块名

#python标准库，点进模块就可以看到里面包含的函数和变量介绍
#查看模块源代码，按住ctrl键点击函数名

#引入第三方库（其它程序员提供）的模块，python标准库不能满足使用时
#引入模块方法一样，但引入之前需先安装，从互联网下载别人写好的模块 安装+引入
#pip install 用于安装的命令
#网站：pypi.org 对第三方库进行搜索
#安装AKshare 去到终端，pip install AKshare ,安装成功后用import引进来，引入后可以使用模块中的函数

#面向对象编程 Object Oriented Programming  面向过程是编年体，面向对象是纪传体
#面向过程编程。过程是负责完成某个具体任务的代码，基本可以理解为函数。把要实现的事情拆分成一个个步骤，依次完成。一步步指导执行各个步骤
#面向对象编程，核心是对象，首先并不会聚焦于第一步，而是模拟真实世界，先考虑各个对象有什么性质、能做什么事情
     #提取信息，定义类，用类创建对象。类与对象之间的关系是，类是创建对象的模板，对象是类的实例
#定义ATM类 制造具体对象的图纸 创建对象，封装数据
class ATM:
   def __init__(self , 编号 , 银行 , 支行) :  #self是什么意思
        self.编号 = 编号
        self.银行 = 银行
        self.支行 = 支行
#创建两个ATM对象 不同ATM对象各自的属性
atm1 = ATM("001","招商银行","南园支行") #self不需要手动传入
atm2 = ATM("001","中国银行","北园支行")

#创建对象后可以直接作为参数，传入函数中。参数变少，但多了两大定义类的代码
#面向对象可以让参数变少，用对象把相关属性绑定在一起，有利于让程序逻辑更加清晰，信息更加集中
print(atm1.编号) #可以清楚看到性质所属的对象

#与对象绑定的有属性(attribute)，如颜色、大小、体积、编号；与对象绑定的还有方法(method)，如移动、放大、变色、打印
#类中属性为特征（放在类里面的变量），类中方法为功能（放在类中的函数）

#面向过程
# def 放（被放的物品，放入的物品） 放（"衣服","洗衣机"） 放("洗衣粉","洗衣机")
# def 开机（机器）  开机("洗衣机")
# def 清洗（需清洗物品） 清洗("衣服")
# def 烘干（需烘干物品） 烘干("衣服")

#面向对象 人和洗衣机都是执行的对象 人能放东西和开机，洗衣机能清洗和烘干，可以作为类的方法（放在类里面的函数）
#class 人：
#    def 放（self,被放的物品,放入的物品）
#    def 开机（self,机器）
#class 洗衣机：
#    def 清洗（self，需清洗物品）
#    def 烘干（self，需烘干物品）
#定义好类之后通过类来创建对象
# 我 = 人() 我的洗衣机 = 洗衣机()
#我.放("衣服"，我的洗衣机)
#我.放("洗衣粉"，我的洗衣机)
#我.开机(我的洗衣机)
#我的洗衣机.清洗("衣服")
#我的洗衣服.烘干("衣服")
#总结：把事务分解到事物身上，描述各个对象的作用，然后才是它们之间的交互。

#面向对象3个被反复提及的特性：封装、继承、多态
#封装：写类的人将内部实现细节隐藏起来，使用类的人只通过外部接口访问和使用。可减少对不必要细节的精力投入
#继承：面向对象编程允许创建有层次的类，类有子类、父类来表示从属关系。如创建出学生父类，小学生、大学生为子类，父类的属性、方法都可以被子类继承，不需要反复定义
#多态：同样的接口，因为对象具体类的不同而有不同的表现。小、大学生都要写作业，但作业难度不一样。写作业的方法不能直接定义在父类中，需分别定义在子类里面，否则大、小学生用的是同一个方法写作业
#     如大学生.写作业、小学生.写作业，不用类的话需要用if函数判断类型，手动调动写作业函数。面向对象的多态无需判断，统一调用统一名称的方法
#C语言：纯面向过程 Java：纯面向对象

#类是创建对象的模板，对象是类的实例，类定义了对象有何种属性和方法，对象拥有的具体属性则可以不尽相同
# class NameOfClass（Pascal命名法）:
#       def _init_():   #命名必须是_init_，括号里可以放任意的参数，第一个参数永远被占用，得用于表示对象自身self，帮助把属性的值绑定在实例对象上
#       定义类的代码
#定义类的属性（对象有什么属性）
class CuteCat:
    def __init__(self,cat_name,cat_age,cat_color):
        self.name = cat_name
        self.age = cat_age
        self.color = cat_color
cat1 = CuteCat("jj",2,"白色")
print(cat1.name)
print(f"小猫{cat1.name}的年龄是{cat1.age}岁，花色是{cat1.color}")
#定义类的方法（对象有什么方法）

#定义一个学生类
#要求：
# 1.属性包括学生姓名、学号，以及语数英三科的成绩
# 2.能够设置学生某科目的成绩
# 3.能够打印出该学生的所有科目成绩

class Student:
    def __init__(self, name, number,score_chinese,score_math,score_en):
        self.name = name
        self.number = number
        self.score_chinese = score_chinese
        self.score_math = score_math
        self.score_en = score_en
student1 = Student("小叶","2017",140,136,142) 
print(f"姓名为{student1.name}的同学的语文成绩是{student1.score_chinese},数学成绩是{student1.score_math},英语成绩是{student1.score_en}")