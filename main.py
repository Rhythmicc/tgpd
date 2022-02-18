from QuickStart_Rhy.NetTools.NormalDL import normal_dl
from QuickStart_Rhy.ImageTools.ImagePreview import image_preview
from QuickProject.Commander import Commander
from QuickProject import QproDefaultConsole
from urllib.parse import unquote
from inspect import isfunction
import pyperclip
import requests
import re
import os

app = Commander()

rt_url = 'https://telegra.ph/'


def funcWrapper(func, url, *args, **kwargs):
    try:
        os.chdir('./img')
        dir_name = unquote(url.replace(rt_url, ''))
        if not (os.path.exists(dir_name) and os.path.isdir(dir_name)):
            os.mkdir(dir_name)
        os.chdir(dir_name)

        for item in re.findall('<img.*?src="(.*?)".*?>', requests.get(url).text):
            item = item.strip('/')
            if isfunction(func):
                func(rt_url + item, *args, **kwargs)
            elif isinstance(func, list):
                _fs = [i[0] for i in func]
                if normal_dl in _fs:
                    imgName = normal_dl(rt_url + item, **func[_fs.index(normal_dl)][1])
                    has_dl = True
                else:
                    imgName = ''
                    has_dl = False

                for f in func:
                    if f[0] == normal_dl:
                        continue
                    if has_dl:
                        f[0](imgName, **f[1])
                    else:
                        f[0](rt_url + item, **f[1])
    except KeyboardInterrupt:
        exit(0)
    except:
        QproDefaultConsole.print_exception()


@app.command()
def dl(url: str = pyperclip.paste()):
    """
    下载telegra.ph的图片

    :param url: the url like https://telegra.ph/*
    """
    funcWrapper(normal_dl, url)


@app.command()
def preview(url: str = pyperclip.paste()):
    """
    在iTerm2中预览telegra.ph的图片(不下载)

    :param url: the url like https://telegra.ph/*
    """
    funcWrapper(image_preview, url)


@app.command()
def dl_preview(url: str = pyperclip.paste()):
    """
    下载并在iTerm2中预览telegra.ph的图片

    :param url: the url like https://telegra.ph/*
    """
    funcWrapper(
        [
            (normal_dl, {'exit_if_exist': True}),
            (image_preview, {})
        ], url
    )


if __name__ == '__main__':
    app()
