class JsonWriter:
    @staticmethod
    def write_to_file_including_chinese_character(file_name, target_json):
        with open(file_name, 'w', encoding='utf-8') as out_file:
            out_file.write(target_json)
            out_file.close()
