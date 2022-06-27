import yaml
class yaml_open:
    @staticmethod
    def read_yaml(yaml_path,node_name):
        '''

        :param yaml_path:路径哈
        :param node_name:节点名字
        :return:
        '''
        with open(yaml_path,'r',encoding="utf-8") as file:
            data = yaml.safe_load(file)
            print(data)
            data_dict = data[node_name]
            #拿到values 转成list
            print(list(data_dict.values()))
            return list(data_dict.values())
if __name__ == '__main__':
    yaml_open.read_yaml("../data/data.yaml",'test_data')
