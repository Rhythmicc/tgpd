const completionSpec: Fig.Spec = {
    "name": "tgpd",
    "description": "tgpd",
    "subcommands": [
        {
            "name": "--help",
            "description": "获取帮助"
        },
        {
            "name": "dl",
            "description": "下载套图链接里的图片",
            "args": [
                {
                    "name": "url",
                    "description": "套图链接"
                }
            ],
            "options": []
        },
        {
            "name": "preview",
            "description": "预览套图链接里的图片",
            "args": [
                {
                    "name": "url",
                    "description": "套图链接"
                }
            ],
            "options": [
                {
                    "name": "--concat",
                    "description": "是否合并图片"
                }
            ]
        },
        {
            "name": "dl_preview",
            "description": "下载并预览套图链接里的图片",
            "args": [
                {
                    "name": "url",
                    "description": "套图链接"
                }
            ],
            "options": [
                {
                    "name": "--concat",
                    "description": "是否合并图片"
                }
            ]
        },
        {
            "name": "complete",
            "description": "生成补全脚本并应用至全局",
            "args": [],
            "options": []
        }
    ]
};
export default completionSpec;
