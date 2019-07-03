import codecs

# 函数：获取配置文件里的数据
def GetConfigData(path):
    '''
    获取配置文件的数据
    :return: 字典类型的数据
    '''
    # 定义一个字典存放文件里的数据
    configdata_dict = {}
    # 打开文件，参数：路径，只读，编码方式
    fileContent = codecs.open(path,'r','utf-8')
    # 获取每行数据进行处理，并存放到字典里
    for line in fileContent:
        # print(line)
        # 读取每行数据，根据'='进行分割，res为一个列表
        res = line.split('=')
        # print(res)
        # 返回的res列表每个数据后面有换行符，进行处理
        res[1] = res[1].strip()
        # print(res)
        # 将res列表类型转换成字典类型
        res_dict = {}
        res_dict[res[0]] = res[1]
        # print(res_dict)
        # 追加到字典
        configdata_dict.update(res_dict)
        # print(configdata_dict)
    # 返回数据字典
    return configdata_dict

# 测试函数功能
# data = GetConfigData()
# print(data)