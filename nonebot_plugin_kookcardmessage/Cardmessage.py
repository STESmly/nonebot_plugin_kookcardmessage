from typing import Literal
from time import time
from .card_basic import _Card,_CardInitializer

__all__ = ['Card', 'CardModules']


class Card:
    """构造卡片消息"""

    @classmethod
    def card(cls, content:list['_Card']) -> list:
        """组合多个卡片\n\n
           content需使用one_card创建"""
        if not isinstance(content, list):
            content = [content]
        return [item.data if hasattr(item, 'data') else item for item in content]

    @classmethod
    def one_card(cls, size: str = "sm", modules: list = None) -> '_Card':
        """创建单个卡片，返回一个支持+操作的卡片对象，但必须使用card方法组合\n
        :param size: 卡片显示模式 lg是pc端（手机强制使用sm），sm是手机端"""
        if modules is None:
            raise ValueError("modules参数不能为空")
        if not isinstance(modules, list):
            modules = [modules]
        modules = [item.data if hasattr(item, 'data') else item for item in modules]
        
        return _Card({
            "type": "card",
            "theme": "secondary",
            "size": size,
            "modules": modules
        })
    
    @classmethod
    def Initialize_card(cls) -> '_Card':
        """初始化卡片，使用于+=合并无合并头的环境"""
        return _CardInitializer()
    
    @classmethod
    def test_get(cls,data:_Card):
        """如果担心当前结果出现错误，可使用这个方法测试获取未被card包裹的cardmodles的值"""
        if not isinstance(data, list):
            return None if data.__str__() == None else data.data
        return [item.data if hasattr(item, 'data') else item for item in data]


class CardModules:
    """构造卡片模块"""
    @classmethod
    def markdown(cls, content: str, md: bool = True, accessory: '_Card' = Card.Initialize_card(), mode: str = "right") -> '_Card':
        """kMarkdown模块\n
        :param md: 是否使用kmarkdown，false则使用普通字符串\n
        :param accessory: 附件内容，目前仅支持附带一个图片（image）或按钮构（one_button）成1文本+1图片或按钮的布局\n
        :param mode: right或left，默认right，表示附件在文本的右侧或左侧\n
        
        | 功能 | 语法 | 说明 |
        |:------:|:------:|:------:|
        | **加粗文字** | \*\*文字\*\* | markdown加粗 |
        | *斜体文字* | \*文字\* | markdown斜体 |
        | ***加粗斜体*** | \*\*\*文字\*\*\* | markdown加粗斜体 |
        | ~~删除线~~ | \~\~文字\~\~ | markdown删除线 |
        | 链接 | \[文字\]\(地址\) | 仅支持http/https协议，链接文字与地址完全一致时显示缩略图 |
        | 分隔线 | --- | markdown分隔线 |
        | 引用 | > 文字 | 持续到遇到两个(\\n\\n)换行符 |
        | 下划线 | (ins)文字(ins) | 自定义下划线 |
        | 剧透 | (spl)文字(spl) | 点击才显示内容 |
        | emoji | :emoji: | 与emoji shortcode写法一致,[kook表情json文件](https://img.kookapp.cn/assets/emoji.json) |
        | 服务器表情 | (emj)服务器表情名称(emj)[服务器表情id] | 需要服务器发送权限 |
        | 频道提及 | (chn)频道ID(chn) | 提及特定频道 |
        | 用户提及 | (met)用户ID(met) | @用户，可用here（所有在线用户）/all（所有用户） |
        | 角色提及 | (rol)角色ID(rol) | @某角色所有用户 |
        | 行内代码 | \`代码\` | markdown行内代码 |
        | 代码块 | \`\`\`语言\\n\`\`\` | markdown代码块 |
        | 转义字符 | \字符 | 转义特殊字符 |
        | 字体颜色 | (font)文字(font)[theme] | 仅限card使用，支持多种主题色 |
        
        支持的主题色：primary, success, danger, warning, info, secondary, body, tips, pink, purple
        """
        if accessory is not None and (not isinstance(accessory, _Card) or isinstance(accessory, list)):
            raise ValueError("accessory参数必须是单个_Card对象，不能是列表或多个_Card的合并")
        
        # 构建基础卡片结构
        card = {
            "type": "section",
            "text": {
                "type": "kmarkdown" if md else "plain-text",
                "content": content
            }
        }
        
        # 如果有accessory，添加相关字段
        if accessory.__str__() is not None:
            card["mode"] = mode
            card["accessory"] = accessory.data
        
        return _Card(card)
    
    @classmethod
    def button(cls, buttons) -> dict:
        """组合多个按钮\n\n
           由one_button创建按钮对象"""
        if not isinstance(buttons, list):
            buttons = [buttons]
        button_data = [item.data if hasattr(item, 'data') else item for item in buttons]
        # 返回一个包含按钮组数据的字典
        return _Card({
            "type": "action-group",
            "elements": button_data
        })
        

    @classmethod
    def one_button(cls, text: str, value: str= "None",retrun: bool = True) -> dict:
        """创建单个按钮，返回一个支持+操作的按钮对象，但必须被CardModules.button组合\n
        :param text: 按钮文本
        :param value: 按钮按下时返回的值
        :param retrun: 按钮按下时是否返回值
        """
        button = {
            "type": "button",
            "theme": "primary",
            "value": value,
            "text": {
                "type": "plain-text",
                "content": text
            }
        }
        if retrun:
            button["click"] = "return-val"
        return _Card(button)
    
    @classmethod
    def countdown(cls,count_time:int,mode:str="second") -> dict:
        """创建倒计时卡片\n\n
        :param count_time: 倒计时时间，单位为秒
        :param mode: day,hour,second 倒计时类型，不影响count_time参数的单位
        """
        start_time = int(time()*1000)
        end_time = start_time + count_time*1000
        return _Card({
            "type": "countdown",
            "mode": mode,
            "startTime": start_time,
            "endTime": end_time
            })
    
    @classmethod
    def paragraph(cls,cols:Literal[1,2,3],fields:list[dict]) -> dict:
        """创建段落卡片\n\n
        :param cols: 列数
        :param fields: 段落内容可使用markdown
        """
        def process_field(field):
            field = field.data if hasattr(field, 'data') else field
            if (field.get('type') == 'section' and 
                field.get('text', {}).get('type') == 'kmarkdown'):
                return _Card({
                    "type": "kmarkdown",
                    "content": field['text']['content']
                })
            return field

        field_list = [process_field(field) for field in (fields if isinstance(fields, list) else [fields])]
        fields = [item.data if hasattr(item, 'data') else item for item in field_list]
        
        return _Card({
            "type": "section",
            "text": {
                "type": "paragraph",
                "cols": cols,
                "fields": fields
            }
        })
    @classmethod
    def image(cls,url:str) -> '_Card':
        """组成image_list，image_group和备注的重要部分"""
        return _Card({
                "type": "image",
                "src": url
                })

    @classmethod
    def image_list(cls,elements:list[dict]) -> '_Card':
        """竖列image的函数"""
        if not isinstance(elements, list):
            elements = [elements]
        elements = [item.data if hasattr(item, 'data') else item for item in elements]
        return _Card({
            "type": "container",
            "elements": elements
        })
    
    @classmethod
    def image_group(cls,elements:list[dict]) -> '_Card':
        """九宫格image的函数"""
        if not isinstance(elements, list):
            elements = [elements]
        elements = [item.data if hasattr(item, 'data') else item for item in elements]
        return _Card({
            "type": "image-group",
            "elements": elements
      })
    
    @classmethod
    def divider(cls) -> '_Card':
        """分割线"""
        return _Card({
        "type": "divider"
      })
    
    @classmethod
    def header(cls,text:str) -> '_Card':
        """标题"""
        return _Card({
            "type": "header",
            "text": {
                "type": "plain-text",
                "content": text
            }
        })
    
    @classmethod
    def file(cls,title:str,src:str,size:str) -> '_Card':
        """上传txt，zip类文件\n
        :param title: 文件名
        :param src: 文件地址
        :param size: 文件大小，单位kb
        """
        return _Card({
            "type": "file",
            "title": title,
            "src": src,
            "size": size
        })
    
    @classmethod
    def audio(cls,title:str,src:str,cover:str) -> '_Card':
        """上传音频文件\n
        :param title: 音频标题
        :param src: 音频地址
        :param cover: 封面链接
        """
        return _Card({
            "type": "audio",
            "title": title,
            "src": src,
            "cover": cover
        })
    
    @classmethod
    def video(cls,title:str,src:str) -> '_Card':
        """上传视频文件\n
        :param title: 视频标题
        :param src: 视频地址
        """
        return _Card({
            "type": "video",
            "title": title,
            "src": src
        })
    
    @classmethod
    def remarks(cls,remarks:list[_Card]) -> '_Card':
        """备注,可以嵌套其他cardmodles（除了多列文本和markdown1+1模式），甚至可以备注嵌套备注"""
        if not isinstance(remarks, list):
            remarks = [remarks]
        elements = [item.data if hasattr(item, 'data') else item for item in remarks]
        return _Card({
            "type": "context",
            "elements": elements
      })