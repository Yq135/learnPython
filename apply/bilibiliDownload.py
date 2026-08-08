import subprocess
import re
import requests


def match1(text, *patterns):
    """Scans through a string for substrings matched some patterns (first-subgroups only).

    Args:
        text: A string to be scanned.
        patterns: Arbitrary number of regex patterns.

    Returns:
        When only one pattern is given, returns a string (None if no match found).
        When more than one pattern are given, returns a list of strings ([] if no match found).
    """

    if len(patterns) == 1:
        pattern = patterns[0]
        match = re.search(pattern, text)
        if match:
            return match.group(1)
        else:
            return None
    else:
        ret = []
        for pattern in patterns:
            match = re.search(pattern, text)
            if match:
                ret.append(match.group(1))
        return ret


def format_path(play_url):
    # redirect: watchlater
    # https://www.bilibili.com/list/watchlater/?bvid=BV1V3onBREVq&oid=116461276236409&watchlater_cfg=%7B%22viewed%22%3A0,%22key%22%3A%22%22,%22asc%22%3Afalse%7D&spm_id_from=333.881.0.0&vd_source=1f3105208bfbd552ce66b97a22285ac8
    if re.match(r'https?://(www\.)?bilibili\.com/list/watchlater/\?bvid=(av(\d+)|BV(\S+))', play_url):
        avid = match1(play_url, r'(av\d+)') or match1(play_url, r'(BV\w+)')
        p = int(match1(play_url, r'/p(\d+)') or '1')
        play_url = 'https://www.bilibili.com/video/%s?p=%s' % (avid, p)

    # redirect: video
    # https://www.bilibili.com/video/BV1A1gX6UEb8/?spm_id_from=333.1387.upload.video_card.click&vd_source=1f3105208bfbd552ce66b97a22285ac8
    elif re.match(r'https?://(www\.)?bilibili\.com/video/(av(\d+)|BV(\S+))', play_url):
        avid = match1(play_url, r'(av\d+)') or match1(play_url, r'(BV\w+)')
        play_url = 'https://www.bilibili.com/video/%s' % avid

    # print(play_url)
    return play_url


def extract_audio(input_video, output_file):
    """
    使用 ffmpeg 提取视频的音频文件。

    Args:
        input_video (str): 视频文件路径
        output_file (str): 输出文件路径
    """
    pass


def you_get_download(download_url, output_dir=None, output_name=None):
    """
       使用 you_get 下载b站视频。

       Args:
           download_url (str): 视频路径
           save_name (str): 保存文件的名称
           # cookie (str): 个人cookie文件路径
       """
    # you-get --cookies=bilicookie.txt --playlist https://www.bilibili.com/video/BV1KKZKYjEKr
    # 构建 you-get 命令
    # command = ['you-get', '--debug', '-c', "bilicookie.txt", "-o", "./download/bilibili"]

    # 保存路径
    command = ['you-get', '-c', "bilicookie.txt", "--no-caption"]
    if output_dir:
        command.extend(["-o", output_dir])
    else:
        command.extend(["-o", "./download/bilibili"])

    # 重命名
    if output_name:
        command.extend(["-O", output_name]),  # --output-filename / -O 选项则用于指定下载文件的名称

    # 添加视频 URL
    command.append(format_path(play_url=download_url))

    try:
        print(f"正在尝试下载: {command[-1]}")
        print("执行命令", " ".join(command))
        # 执行命令
        # check=True 会在命令执行失败时抛出 CalledProcessError 异常
        subprocess.run(command, check=True)
        print(f"✅ 视频下载成功")
    except subprocess.CalledProcessError as e:
        print(f"❌ 下载失败，错误代码: {e.returncode}")
        print(f"错误信息: {e.stderr.decode('utf-8', errors='ignore')}")
    except FileNotFoundError:
        print("❌ 错误: 未找到 you-get 命令。请确认已正确安装 you-get 并配置了环境变量。")
    except Exception as e:
        print(f"❌ 发生未知错误: {e}")


def merge_media(input_video, input_audio, output_file):
    """
    使用 ffmpeg 将视频和音频合并为一个文件。

    Args:
        input_video (str): 视频文件路径
        input_audio (str): 音频文件路径
        output_file (str): 输出文件路径
    """
    # 使用列表形式传参，避免 shell 注入风险
    command = [
        "ffmpeg",
        "-y",  # 自动覆盖已存在的输出文件
        "-i", input_video,  # 输入视频流
        "-i", input_audio,  # 输入音频流
        "-c", "copy",  # 直接复制流，不进行重新编码，速度极快
        output_file  # 输出文件
    ]

    try:
        # 执行命令并捕获输出
        result = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True,  # 如果命令返回非零退出码，则抛出异常
            text=True
        )
        print(f"✅ 合并成功: {output_file}")
        return True

    except subprocess.CalledProcessError as e:
        print(f"❌ 合并失败，退出码: {e.returncode}")
        print(f"错误信息:\n{e.stderr}")
        return False
    except FileNotFoundError:
        print("❌ 错误: 未找到 ffmpeg 命令。请确认已安装并添加到系统 PATH。")
        return False


if __name__ == "__main__":
    url = input("粘贴要下载的b站视频链接：")
    rename = input("重命名？：")
    isdefaute = input("默认路径最高画质下载？(y/n)：")
    if 'y' == isdefaute or 'Y' == isdefaute:
        you_get_download(url, None, rename)
    else:
        output_dir = input("保存路径（不传 默认下载到./download/bilibili/）：")
        # todo 调用查询视频信息 返回画质选项 - format: dash-hdflv2_4k-AVC
        format = input("复制选择画质(-format, 传空 只下载音频)：")
        you_get_download(url, output_dir, rename)
    # format_path(url)

    # 假设 you-get 下载后生成了以下两个文件
    # video_path = "downloaded_video.mp4"
    # audio_path = "downloaded_audio.m4a"
    # final_output = "final_video.mp4"
    #
    # merge_media(video_path, audio_path, final_output)
