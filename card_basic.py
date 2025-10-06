class _Card:
    """合成卡片赋予+和*运算符"""
    def __init__(self, card_data):
        self.data = card_data
            
    def __add__(self, other):
        if isinstance(other, _Card):
            return [self.data, other.data]
        elif isinstance(other, list):
            return [self.data] + other
        return NotImplemented
            
    def __radd__(self, other):
        if isinstance(other, list):
            return other + [self.data]
        return NotImplemented
            
    def __mul__(self, other):
        if isinstance(other, int):
            return [self.data] * other
        return NotImplemented
    
class _CardInitializer(_Card):
    """用于初始化卡片的特殊类，不会在+运算中引入空字典"""
    def __init__(self):
        pass
            
    def __add__(self, other):
        if isinstance(other, _Card):
            return [other.data]
        elif isinstance(other, list):
            return other
        return NotImplemented
            
    def __radd__(self, other):
        if isinstance(other, list):
            return other
        return NotImplemented
            
    def __mul__(self, other):
        if isinstance(other, int):
            return []
        return NotImplemented
    
    def __str__(self):
        return None