from QuickProject.Commander import Commander
from . import *

app = Commander(name)


@app.command()
def dl(url: str, _with_content: bool = False):
    """
    下载套图链接里的图片

    :param url: 套图链接
    :param _with_content: 是否下载套图内容 (私有参数)
    """
    urls = get_images_url(url)
    if not urls:
        QproDefaultConsole.print(QproErrorString, "没有找到图片")
        return

    from urllib.parse import unquote

    dir_name = unquote(url.replace(rt_url, ""))

    if not os.path.exists(dir_name):
        os.mkdir(dir_name)

    from QuickStart_Rhy.NetTools.MultiSingleDL import multi_single_dl

    res = multi_single_dl(urls, rt_dir=dir_name + "/")

    if _with_content:
        content_ls = []
        for item in res:
            with open(item, "rb") as f:
                content_ls.append(f.read())
        return content_ls


@app.command()
def preview(
    url: str, concat: bool = False, step: int = 8, _is_urls_content: bool = False
):
    """
    预览套图链接里的图片

    :param url: 套图链接
    :param concat: 是否合并图片
    :param _is_urls_content: 是否是图片内容 (私有参数)
    """
    if _is_urls_content:
        imgs = url
    else:
        from QuickStart_Rhy.NetTools.MultiSingleDL import multi_single_dl_content_ls

        imgs = multi_single_dl_content_ls(get_images_url(url))
    if not imgs:
        QproDefaultConsole.print(QproErrorString, "没有找到图片")
        return

    from QuickStart_Rhy.ImageTools.ImagePreview import image_preview

    if concat:  # 每十张图片合并一次
        for i in range(0, len(imgs), step):
            image_preview(imgsConcat(imgs[i : i + step]))
    else:
        for img in imgs:
            image_preview(img)


@app.command()
def dl_preview(url: str, concat: bool = False, step: int = 8):
    """
    下载并预览套图链接里的图片

    :param url: 套图链接
    :param concat: 是否合并图片
    """
    app.real_call(
        "preview",
        app.real_call("dl", url, _with_content=True),
        concat=concat,
        step=step,
        _is_urls_content=True,
    )


def main():
    """
    注册为全局命令时, 默认采用main函数作为命令入口, 请勿将此函数用作它途.
    When registering as a global command, default to main function as the command entry, do not use it as another way.
    """
    app()


if __name__ == "__main__":
    main()
