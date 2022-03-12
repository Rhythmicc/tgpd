from QuickStart_Rhy.NetTools.MultiSingleDL import multi_single_dl
from QuickStart_Rhy.ImageTools.ImagePreview import image_preview
from QuickProject.Commander import Commander
from QuickProject import QproDefaultConsole, QproInfoString
from urllib.parse import unquote
from inspect import isfunction
import pyperclip
import requests
import time
import re
import os

app = Commander()

rt_url = 'https://telegra.ph/'


def funcWrapper(func, url, *args, **kwargs):
    try:
        if (isfunction(func) and func == multi_single_dl) or (isinstance(func, dict) and multi_single_dl in func):
            os.chdir('./img')
            dir_name = unquote(url.replace(rt_url, ''))
            if not (os.path.exists(dir_name) and os.path.isdir(dir_name)):
                os.mkdir(dir_name)
            os.chdir(dir_name)
        
        urls = [i.strip('/') for i in re.findall('<img.*?src="(.*?)".*?>', requests.get(url).text)]
        flag = func == multi_single_dl if isfunction(func) else multi_single_dl in func
        if flag:
            if (isinstance(func, dict) and multi_single_dl in func):
                func.pop(multi_single_dl)
            files = multi_single_dl([rt_url + i.strip('/') for i in urls])
            if isinstance(func, dict):
                for item in files:
                    for f in func:
                        f(item, **func[f])
                        time.sleep(1)
        else:
            [f(rt_url + url, **func[f]) for url in urls for f in func] if isinstance(func, dict) else [func(rt_url + url, *args, **kwargs) for url in urls]

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
    funcWrapper(multi_single_dl, url)


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
        {
            multi_single_dl: {'exit_if_exist': True},
            image_preview: {}
        }, url
    )


if __name__ == '__main__':
    app()
