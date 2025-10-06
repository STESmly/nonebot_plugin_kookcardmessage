<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# nonebot_plugin_kookcardmessage

_✨ NoneBot 插件描述 ✨_

用于适配kook发送卡片消息的插件
</div>


## 消息支持情况说明

| 名称 | 描述 | 支持情况 | 函数（部分函数用法清详见函数备注） |
|:-----:|:----:|:----:|:----:|
| 添加卡片 | 见函数备注 | √ | Card.card |
| 纯文本 | 纯字符串消息 | √ | CardModules.markdown |
| kmarkdown文本 | kook化md语法（详见函数备注） | √ | CardModules.markdown |
| 多列文本 | 无 | √ | CardModules.paragraph |
| 彩色文本 | 详情见函数备注 | √ | CardModules.markdown |
| 文本+图片 | 见函数备注 | √ | CardModules.markdown |
| 文本+按钮 | 见函数备注 | √ | CardModules.markdown |
| 单图 | 其实是图片竖列 | √ | CardModules.image_list(CardModules.image()) |
| 多图 | 类似九宫格的排列 | √ | CardModules.image_group(CardModules.image()) |
| 标题 | 大号纯文本 | √ | CardModules.header |
| 分割线 | 无 | √ | CardModules.divider |
| 按钮 | 见函数备注 | √ | CardModules.button |
| 文件上传 | 见函数备注 | √ | CardModules.file |
| 音频播放器 | 见函数备注 | √ | CardModules.audio |
| 视频播放器 | 见函数备注 | √ | CardModules.video |
| 倒计时 | 见函数备注 | √ | CardModules.countdown |
| 备注 | 见函数备注 | √ | CardModules.remarks |

## 💿 安装

<details open>
<summary>使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install nonebot_plugin_kookcardmessage

</details>

<details>
<summary>使用包管理器安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details>
<summary>pip</summary>

    pip install nonebot_plugin_kookcardmessage
</details>

打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分追加写入

    plugins = ["nonebot_plugin_kookcardmessage"]

</details>

## 示例代码


```bash

from nonebot.adapters.kaiheila import Event,MessageSegment,Bot
from nonebot import on_command
require("nonebot_plugin_kookcardmessage")
from nonebot_plugin_kookcardmessage import Card,CardModules

card_test = on_command("测试按钮")

@card_test.handle()
async def _(bot: Bot, event: Event):
    content = Card.card(
       Card.one_card(
          size='sm',
          modules=CardModules.markdown("md测试")+CardModules.button(
                CardModules.one_button("测试按钮")+CardModules.one_button("测试按钮2")
             )
       )+Card.one_card(
          size='sm',
          modules=CardModules.markdown("md测试1")+CardModules.button(
                Card.Initialize_card()+CardModules.one_button("测试按钮3")+CardModules.one_button("测试按钮4")
             )
       )
    )
    print(Card.test_get(CardModules.remarks(CardModules.markdown("备注测试")+CardModules.button(CardModules.one_button("备注按钮测试")))))
    await card_test.send(MessageSegment.Card(content=content))
```