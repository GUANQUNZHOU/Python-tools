import inspect
import typing

from json_tools.json_tool_factory import JsonToolFactor

if __name__ == '__main__':
    # generator = JsonGenerator()
    # jsonObject = generator.generate_json_as_list_of_value_and_key(
    #     ["银行", "证券", "保险", "信托", "期货", "基金", "资管", "金融科技", "科技", "咨询", "服务", "架构", "业务",
    #      "数据", "流程"], "keyword")
    # writer = JsonWriter()
    # writer.write_to_file_including_chinese_character("/Users/guanqun.zhou/Downloads/postman_script.json", jsonObject)

    # 选取哪一个领域的tool
    tools_box = {"Json tools": ["generator", "writer"]}
    options = ["Json tools"]
    numbers = [1]
    for i in range(len(options)):
        print(f"{i + 1}. {options[i]}")
    selected_number = int(input("请选择一个数字："))
    selected_value = options[selected_number - 1]

    # 在领域内选取目标功能的tool
    selected_pack = tools_box[selected_value]
    for j in range(len(selected_pack)):
        print(f"{j + 1}. {selected_pack[j]}")

    selected_tool_name = selected_pack[int(input("请选择一个数字：")) - 1]
    selected_tool = JsonToolFactor().get_target_tool(name=selected_tool_name)
    # 选择目标tool中提供的方法
    all_methods = [method for method in dir(selected_tool) if callable(getattr(selected_tool, method))]
    methods_in_tool = [method for method in all_methods if not method.startswith("__")]

    for j in range(len(methods_in_tool)):
        print(f"{j + 1}. {methods_in_tool[j]}")

    selected_method_name = methods_in_tool[int(input("请选择一个数字：")) - 1]

    # 对于选定的method，列出所需参数，让用户传入
    selected_method = JsonToolFactor().get_tool_methods(selected_method_name)
    parameters = inspect.signature(selected_method).parameters
    arguments = {}
    for name, param in parameters.items():
        if param.annotation == typing.List:
            input_value = input(f'Input value for parameter: {name} whose type is {param.annotation},please '
                                f'use comma to separate the values: ').split(',')

        else:
            input_value = input(f'Input value for parameter: {name} whose type is {param.annotation}: ')

        arguments[name] = input_value
    result = selected_method(**arguments)
    print(result)
