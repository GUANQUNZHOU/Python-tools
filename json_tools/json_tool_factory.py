from json_tools.json_generator import JsonGenerator
from json_tools.json_writer import JsonWriter


class JsonToolFactor:
    class_mapping = {"generator": JsonGenerator, "writer": JsonWriter}
    method_mapping = {"generate_json_as_list_of_value_and_key": JsonGenerator.generate_json_as_list_of_value_and_key,
                      "generate_json_as_key_and_list_of_values": JsonGenerator.generate_json_as_key_and_list_of_values,
                      "write_to_file_including_chinese_character": JsonWriter.write_to_file_including_chinese_character}

    def get_target_tool(self, name):
        return self.class_mapping[name]

    def get_tool_methods(self, name):
        return self.method_mapping[name]
