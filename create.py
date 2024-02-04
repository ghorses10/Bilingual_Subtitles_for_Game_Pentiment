import json
import chardet

if __name__ == "__main__":
    # 原始英语字幕文件名，无需修改
    # File name for original English subtitle
    file_name_eng = 'text_enus.stringtablebundle'
    # 翻译字幕的文件名，需要修改
    # File name for translated subtitles, needs modification
    file_name_add = 'text_ruru.stringtablebundle'
    # 输出的文件名，默认输出到 output.stringtablebundle 文件中
    # Output file name, default output to output.stringtablebundle
    file_name_out = './out/text_ruru.stringtablebundle'

    with open(file_name_eng, 'r', encoding='utf-8') as file:
        data_eng = json.load(file)

    with open(file_name_add, 'rb') as file:
        raw_data = file.read()
        result = chardet.detect(raw_data)
        encoding = result['encoding']

    with open(file_name_add, 'r', encoding=encoding) as file:
        data_add = json.load(file)

    # 修改 dont_translate ，你可以选择不翻译某些部分
    # You can choose not to translate certain parts by changing list dont_translate
    dont_translate = []
    # 是否翻译界面条目，默认为 False 不翻译
    # Whether to translate gui, default is False
    translate_gui = False

    table_len = len(data_eng["StringTables"])
    for i in range(table_len):
        if(data_eng["StringTables"][i]["Name"] == "game/gui"):
            if (translate_gui):
                for j in range(len(data_eng["StringTables"][i]["Entries"])):
                    if data_eng["StringTables"][i]["Entries"][j]["DefaultText"] == "":
                        continue
                    data_eng["StringTables"][i]["Entries"][j]["DefaultText"] =  data_add["StringTables"][i]["Entries"][j]["DefaultText"]
                continue
            else:
                continue    

        if(data_eng["StringTables"][i]["Name"] in dont_translate):
            continue

        for j in range(len(data_eng["StringTables"][i]["Entries"])):
            if data_eng["StringTables"][i]["Entries"][j]["DefaultText"] == "":
                continue
            data_eng["StringTables"][i]["Entries"][j]["DefaultText"] = data_add["StringTables"][i]["Entries"][j]["DefaultText"] + "\n" + data_eng["StringTables"][i]["Entries"][j]["DefaultText"]


    
    with open(file_name_out, 'w', encoding='utf-8') as output_file:
        json.dump(data_eng, output_file, indent=4, ensure_ascii=False)

