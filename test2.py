# pip install faster_whisper
import argparse
import os

from faster_whisper import WhisperModel

model = WhisperModel("faster-whisper-medium/pengzhendong/faster-whisper-medium",local_files_only=True, device="cuda")

def asr(path):
    # segments, info = model.transcribe("/data/coding/whisper_inference/岁不寒.mp4")
    segments, info = model.transcribe(path)
    name='./'+ path +'.txt'
    with open(name,"a+") as f:
        f.write("----{path}---- ")  # 自带文件关闭功能，不需要再写f.close()
        for segment in segments:
            # print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))
            s,e,t=segment.start, segment.end, segment.text
            f.write("\n[%.2fs -> %.2fs] %s" % (s,e,t))
    print("生成完成")

def main(file_path):
    if os.path.exists(file_path):
        print("文件路径有效")
    else:
        print("文件路径无效，请检查后重试！")
        return
    output = asr(file_path)
    print(output)

if __name__=="__main__":

    # 我希望能够通过命令行直接提供文件路径，这样便于远程传输文件后直接执行脚本。
    # 命令：python test2.py 岁不寒.mp4
    # /data/coding/whisper_inference/test2.py
    #  

    # 创建解析器
    parser = argparse.ArgumentParser(description='Process an audio file.')
    parser.add_argument('file_path', type=str) # 添加位置参数，这是必须提供的
    args = parser.parse_args()
    main(args.file_path)
    



