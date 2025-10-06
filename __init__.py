from .Cardmessage import *
from nonebot.plugin import PluginMetadata

__plugin_meta__ = PluginMetadata(
    name="kook卡片消息编写适配插件",
    description="该插件为用户提供类MessageSegment的卡片消息编写方式，以简化用户kook卡片消息的编辑和方便用户的维护",
    usage="参考项目的readme",

    type="library",
    # 发布必填，当前有效类型有：`library`（为其他插件编写提供功能），`application`（向机器人用户提供功能）。

    homepage="https://github.com/STESmly/nonebot_plugin_kookcardmessage",
    # 发布必填。

    supported_adapters={"nonebot.adapters.kaiheila"},
    # 支持的适配器集合，其中 `~` 在此处代表前缀 `nonebot.adapters.`，其余适配器亦按此格式填写。
    # 若插件可以保证兼容所有适配器（即仅使用基本适配器功能）可不填写，否则应该列出插件支持的适配器。
)