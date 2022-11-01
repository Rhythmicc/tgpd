const completionSpec: Fig.Spec = {
    "name": "tgpd",
    "description": "tgpd",
    "subcommands": [
        {
            "name": "--help",
            "description": "获取帮助",
            "options": [
                {
                    "name": "--hidden",
                    "description": "显示隐藏命令"
                }
            ]
        },
        {
            "name": "complete",
            "description": "获取补全列表",
            "args": [],
            "options": [
                {
                    "name": "--team",
                    "description": "团队名",
                    "isOptional": true,
                    "args": {
                        "name": "team",
                        "description": "团队名"
                    }
                },
                {
                    "name": "--token",
                    "description": "团队token",
                    "isOptional": true,
                    "args": {
                        "name": "token",
                        "description": "团队token"
                    }
                },
                {
                    "name": "--is_script",
                    "description": "是否为脚本"
                }
            ]
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
                },
                {
                    "name": "--step",
                    "description": "<step>",
                    "isOptional": true,
                    "args": {
                        "name": "step",
                        "description": "<step>"
                    }
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
                },
                {
                    "name": "--step",
                    "description": "<step>",
                    "isOptional": true,
                    "args": {
                        "name": "step",
                        "description": "<step>"
                    }
                }
            ]
        }
    ]
};
export default completionSpec;
