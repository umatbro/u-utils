"""
Module containing color utilities and color constants.

Source of colors - Google Material Design
https://material.io/guidelines/style/color.html#color-color-palette
"""
import re


class Color:
    def __init__(self, r: int =0x0, g: int=0x0, b: int =0x0):
        if any(value < 0 or value > 255 for value in (r, g, b)):
            raise ValueError('RGB color values have to be in range 0-255')
        self.r = r
        self.g = g
        self.b = b

    def hex(self, prefix: str=''):
        return hex((self.r, self.g, self.b), prefix)


def hex2rgb(hex_code: str) -> tuple:
    """
    Convert color given in hex code to RGB in ints. Result is returned inside 3-element tuple.

    :param hex_code:
    :return: tuple (R, G, B)
    """
    pattern = re.compile(r'^#?[a-fA-F0-9]{6}$')
    if not re.match(pattern, hex_code):
        raise ValueError('Hex code should have 6 characters')
    h = hex_code.lstrip('#')

    return tuple(int(h[i: i + 2], 16) for i in (0, 2, 4))


def hex(color: tuple, prefix: str='#') -> str:
    """
    Convert RGB to HEX.

    :param color: 3-element tuple with color RGB values
    :param prefix: string prefix
    :return: string with color in hex
    """
    if len(color) is not 3:
        raise ValueError('Color should be a 3 element tuple')
    if not all([0 <= v <= 255 for v in color]):
        raise ValueError('RGB values have to be in range from 0 to 255')
    return '{}{:02x}{:02x}{:02x}'.format(prefix, color[0], color[1], color[2])


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Red
RED = hex2rgb('#F44336')
RED50 = hex2rgb('#FFEBEE')
RED100 = hex2rgb('#FFCDD2')
RED200 = hex2rgb('#EF9A9A')
RED300 = hex2rgb('#E57373')
RED400 = hex2rgb('#EF5350')
RED500 = hex2rgb('#F44336')
RED600 = hex2rgb('#E53935')
RED700 = hex2rgb('#D32F2F')
RED800 = hex2rgb('#C62828')
RED900 = hex2rgb('#B71C1C')
REDA100 = hex2rgb('#FF8A80')
REDA200 = hex2rgb('#FF5252')
REDA400 = hex2rgb('#FF1744')
REDA700 = hex2rgb('#D50000')

# Pink
PINK = hex2rgb('#E91E63')
PINK50 = hex2rgb('#FCE4EC')
PINK100 = hex2rgb('#F8BBD0')
PINK200 = hex2rgb('#F48FB1')
PINK300 = hex2rgb('#F06292')
PINK400 = hex2rgb('#EC407A')
PINK500 = hex2rgb('#E91E63')
PINK600 = hex2rgb('#D81B60')
PINK700 = hex2rgb('#C2185B')
PINK800 = hex2rgb('#AD1457')
PINK900 = hex2rgb('#880E4F')
PINKA100 = hex2rgb('#FF80AB')
PINKA200 = hex2rgb('#FF4081')
PINKA400 = hex2rgb('#F50057')
PINKA700 = hex2rgb('#C51162')

# Purple
PURPLE = hex2rgb('#9C27B0')
PURPLE50 = hex2rgb('#F3E5F5')
PURPLE100 = hex2rgb('#E1BEE7')
PURPLE200 = hex2rgb('#CE93D8')
PURPLE300 = hex2rgb('#BA68C8')
PURPLE400 = hex2rgb('#AB47BC')
PURPLE500 = hex2rgb('#9C27B0')
PURPLE600 = hex2rgb('#8E24AA')
PURPLE700 = hex2rgb('#7B1FA2')
PURPLE800 = hex2rgb('#6A1B9A')
PURPLE900 = hex2rgb('#4A148C')
PURPLEA100 = hex2rgb('#EA80FC')
PURPLEA200 = hex2rgb('#E040FB')
PURPLEA400 = hex2rgb('#D500F9')
PURPLEA700 = hex2rgb('#AA00FF')

# Deep Purple
DEEP_PURPLE = hex2rgb('#673AB7')
DEEP_PURPLE50 = hex2rgb('#EDE7F6')
DEEP_PURPLE100 = hex2rgb('#D1C4E9')
DEEP_PURPLE200 = hex2rgb('#B39DDB')
DEEP_PURPLE300 = hex2rgb('#9575CD')
DEEP_PURPLE400 = hex2rgb('#7E57C2')
DEEP_PURPLE500 = hex2rgb('#673AB7')
DEEP_PURPLE600 = hex2rgb('#5E35B1')
DEEP_PURPLE700 = hex2rgb('#512DA8')
DEEP_PURPLE800 = hex2rgb('#4527A0')
DEEP_PURPLE900 = hex2rgb('#311B92')
DEEP_PURPLEA100 = hex2rgb('#B388FF')
DEEP_PURPLEA200 = hex2rgb('#7C4DFF')
DEEP_PURPLEA400 = hex2rgb('#651FFF')
DEEP_PURPLEA700 = hex2rgb('#6200EA')

# Indigo
INDIGO = hex2rgb('#3F51B5')
INDIGO50 = hex2rgb('#E8EAF6')
INDIGO100 = hex2rgb('#C5CAE9')
INDIGO200 = hex2rgb('#9FA8DA')
INDIGO300 = hex2rgb('#7986CB')
INDIGO400 = hex2rgb('#5C6BC0')
INDIGO500 = hex2rgb('#3F51B5')
INDIGO600 = hex2rgb('#3949AB')
INDIGO700 = hex2rgb('#303F9F')
INDIGO800 = hex2rgb('#283593')
INDIGO900 = hex2rgb('#1A237E')
INDIGOA100 = hex2rgb('#8C9EFF')
INDIGOA200 = hex2rgb('#536DFE')
INDIGOA400 = hex2rgb('#3D5AFE')
INDIGOA700 = hex2rgb('#304FFE')

# Blue
BLUE = hex2rgb('#2196F3')
BLUE50 = hex2rgb('#E3F2FD')
BLUE100 = hex2rgb('#BBDEFB')
BLUE200 = hex2rgb('#90CAF9')
BLUE300 = hex2rgb('#64B5F6')
BLUE400 = hex2rgb('#42A5F5')
BLUE500 = hex2rgb('#2196F3')
BLUE600 = hex2rgb('#1E88E5')
BLUE700 = hex2rgb('#1976D2')
BLUE800 = hex2rgb('#1565C0')
BLUE900 = hex2rgb('#0D47A1')
BLUEA100 = hex2rgb('#82B1FF')
BLUEA200 = hex2rgb('#448AFF')
BLUEA400 = hex2rgb('#2979FF')
BLUEA700 = hex2rgb('#2962FF')

# Light Blue
LIGHT_BLUE = hex2rgb('#03A9F4')
LIGHT_BLUE50 = hex2rgb('#E1F5FE')
LIGHT_BLUE100 = hex2rgb('#B3E5FC')
LIGHT_BLUE200 = hex2rgb('#81D4FA')
LIGHT_BLUE300 = hex2rgb('#4FC3F7')
LIGHT_BLUE400 = hex2rgb('#29B6F6')
LIGHT_BLUE500 = hex2rgb('#03A9F4')
LIGHT_BLUE600 = hex2rgb('#039BE5')
LIGHT_BLUE700 = hex2rgb('#0288D1')
LIGHT_BLUE800 = hex2rgb('#0277BD')
LIGHT_BLUE900 = hex2rgb('#01579B')
LIGHT_BLUEA100 = hex2rgb('#80D8FF')
LIGHT_BLUEA200 = hex2rgb('#40C4FF')
LIGHT_BLUEA400 = hex2rgb('#00B0FF')
LIGHT_BLUEA700 = hex2rgb('#0091EA')

# Cyan
CYAN = hex2rgb('#00BCD4')
CYAN50 = hex2rgb('#E0F7FA')
CYAN100 = hex2rgb('#B2EBF2')
CYAN200 = hex2rgb('#80DEEA')
CYAN300 = hex2rgb('#4DD0E1')
CYAN400 = hex2rgb('#26C6DA')
CYAN500 = hex2rgb('#00BCD4')
CYAN600 = hex2rgb('#00ACC1')
CYAN700 = hex2rgb('#0097A7')
CYAN800 = hex2rgb('#00838F')
CYAN900 = hex2rgb('#006064')
CYANA100 = hex2rgb('#84FFFF')
CYANA200 = hex2rgb('#18FFFF')
CYANA400 = hex2rgb('#00E5FF')
CYANA700 = hex2rgb('#00B8D4')

# Teal
TEAL = hex2rgb('#009688')
TEAL50 = hex2rgb('#E0F2F1')
TEAL100 = hex2rgb('#B2DFDB')
TEAL200 = hex2rgb('#80CBC4')
TEAL300 = hex2rgb('#4DB6AC')
TEAL400 = hex2rgb('#26A69A')
TEAL500 = hex2rgb('#009688')
TEAL600 = hex2rgb('#00897B')
TEAL700 = hex2rgb('#00796B')
TEAL800 = hex2rgb('#00695C')
TEAL900 = hex2rgb('#004D40')
TEALA100 = hex2rgb('#A7FFEB')
TEALA200 = hex2rgb('#64FFDA')
TEALA400 = hex2rgb('#1DE9B6')
TEALA700 = hex2rgb('#00BFA5')

# Green
GREEN = hex2rgb('#4CAF50')
GREEN50 = hex2rgb('#E8F5E9')
GREEN100 = hex2rgb('#C8E6C9')
GREEN200 = hex2rgb('#A5D6A7')
GREEN300 = hex2rgb('#81C784')
GREEN400 = hex2rgb('#66BB6A')
GREEN500 = hex2rgb('#4CAF50')
GREEN600 = hex2rgb('#43A047')
GREEN700 = hex2rgb('#388E3C')
GREEN800 = hex2rgb('#2E7D32')
GREEN900 = hex2rgb('#1B5E20')
GREENA100 = hex2rgb('#B9F6CA')
GREENA200 = hex2rgb('#69F0AE')
GREENA400 = hex2rgb('#00E676')
GREENA700 = hex2rgb('#00C853')

# Light Green
LIGHT_GREEN = hex2rgb('#8BC34A')
LIGHT_GREEN50 = hex2rgb('#F1F8E9')
LIGHT_GREEN100 = hex2rgb('#DCEDC8')
LIGHT_GREEN200 = hex2rgb('#C5E1A5')
LIGHT_GREEN300 = hex2rgb('#AED581')
LIGHT_GREEN400 = hex2rgb('#9CCC65')
LIGHT_GREEN500 = hex2rgb('#8BC34A')
LIGHT_GREEN600 = hex2rgb('#7CB342')
LIGHT_GREEN700 = hex2rgb('#689F38')
LIGHT_GREEN800 = hex2rgb('#558B2F')
LIGHT_GREEN900 = hex2rgb('#33691E')
LIGHT_GREENA100 = hex2rgb('#CCFF90')
LIGHT_GREENA200 = hex2rgb('#B2FF59')
LIGHT_GREENA400 = hex2rgb('#76FF03')
LIGHT_GREENA700 = hex2rgb('#64DD17')

# Lime
LIME = hex2rgb('#CDDC39')
LIME50 = hex2rgb('#F9FBE7')
LIME100 = hex2rgb('#F0F4C3')
LIME200 = hex2rgb('#E6EE9C')
LIME300 = hex2rgb('#DCE775')
LIME400 = hex2rgb('#D4E157')
LIME500 = hex2rgb('#CDDC39')
LIME600 = hex2rgb('#C0CA33')
LIME700 = hex2rgb('#AFB42B')
LIME800 = hex2rgb('#9E9D24')
LIME900 = hex2rgb('#827717')
LIMEA100 = hex2rgb('#F4FF81')
LIMEA200 = hex2rgb('#EEFF41')
LIMEA400 = hex2rgb('#C6FF00')
LIMEA700 = hex2rgb('#AEEA00')

# Yellow
YELLOW = hex2rgb('#FFEB3B')
YELLOW50 = hex2rgb('#FFFDE7')
YELLOW100 = hex2rgb('#FFF9C4')
YELLOW200 = hex2rgb('#FFF59D')
YELLOW300 = hex2rgb('#FFF176')
YELLOW400 = hex2rgb('#FFEE58')
YELLOW500 = hex2rgb('#FFEB3B')
YELLOW600 = hex2rgb('#FDD835')
YELLOW700 = hex2rgb('#FBC02D')
YELLOW800 = hex2rgb('#F9A825')
YELLOW900 = hex2rgb('#F57F17')
YELLOWA100 = hex2rgb('#FFFF8D')
YELLOWA200 = hex2rgb('#FFFF00')
YELLOWA400 = hex2rgb('#FFEA00')
YELLOWA700 = hex2rgb('#FFD600')

# Amber
AMBER = hex2rgb('#FFC107')
AMBER50 = hex2rgb('#FFF8E1')
AMBER100 = hex2rgb('#FFECB3')
AMBER200 = hex2rgb('#FFE082')
AMBER300 = hex2rgb('#FFD54F')
AMBER400 = hex2rgb('#FFCA28')
AMBER500 = hex2rgb('#FFC107')
AMBER600 = hex2rgb('#FFB300')
AMBER700 = hex2rgb('#FFA000')
AMBER800 = hex2rgb('#FF8F00')
AMBER900 = hex2rgb('#FF6F00')
AMBERA100 = hex2rgb('#FFE57F')
AMBERA200 = hex2rgb('#FFD740')
AMBERA400 = hex2rgb('#FFC400')
AMBERA700 = hex2rgb('#FFAB00')

# Orange
ORANGE = hex2rgb('#FF9800')
ORANGE50 = hex2rgb('#FFF3E0')
ORANGE100 = hex2rgb('#FFE0B2')
ORANGE200 = hex2rgb('#FFCC80')
ORANGE300 = hex2rgb('#FFB74D')
ORANGE400 = hex2rgb('#FFA726')
ORANGE500 = hex2rgb('#FF9800')
ORANGE600 = hex2rgb('#FB8C00')
ORANGE700 = hex2rgb('#F57C00')
ORANGE800 = hex2rgb('#EF6C00')
ORANGE900 = hex2rgb('#E65100')
ORANGEA100 = hex2rgb('#FFD180')
ORANGEA200 = hex2rgb('#FFAB40')
ORANGEA400 = hex2rgb('#FF9100')
ORANGEA700 = hex2rgb('#FF6D00')

# Deep Orange
DEEP_ORANGE = hex2rgb('#FF5722')
DEEP_ORANGE50 = hex2rgb('#FBE9E7')
DEEP_ORANGE100 = hex2rgb('#FFCCBC')
DEEP_ORANGE200 = hex2rgb('#FFAB91')
DEEP_ORANGE300 = hex2rgb('#FF8A65')
DEEP_ORANGE400 = hex2rgb('#FF7043')
DEEP_ORANGE500 = hex2rgb('#FF5722')
DEEP_ORANGE600 = hex2rgb('#F4511E')
DEEP_ORANGE700 = hex2rgb('#E64A19')
DEEP_ORANGE800 = hex2rgb('#D84315')
DEEP_ORANGE900 = hex2rgb('#BF360C')
DEEP_ORANGEA100 = hex2rgb('#FF9E80')
DEEP_ORANGEA200 = hex2rgb('#FF6E40')
DEEP_ORANGEA400 = hex2rgb('#FF3D00')
DEEP_ORANGEA700 = hex2rgb('#DD2C00')

# Brown
BROWN = hex2rgb('#795548')
BROWN50 = hex2rgb('#EFEBE9')
BROWN100 = hex2rgb('#D7CCC8')
BROWN200 = hex2rgb('#BCAAA4')
BROWN300 = hex2rgb('#A1887F')
BROWN400 = hex2rgb('#8D6E63')
BROWN500 = hex2rgb('#795548')
BROWN600 = hex2rgb('#6D4C41')
BROWN700 = hex2rgb('#5D4037')
BROWN800 = hex2rgb('#4E342E')
BROWN900 = hex2rgb('#3E2723')

# Grey
GREY = hex2rgb('#9E9E9E')
GREY50 = hex2rgb('#FAFAFA')
GREY100 = hex2rgb('#F5F5F5')
GREY200 = hex2rgb('#EEEEEE')
GREY300 = hex2rgb('#E0E0E0')
GREY400 = hex2rgb('#BDBDBD')
GREY500 = hex2rgb('#9E9E9E')
GREY600 = hex2rgb('#757575')
GREY700 = hex2rgb('#616161')
GREY800 = hex2rgb('#424242')
GREY900 = hex2rgb('#212121')

# Blue Grey
BLUE_GREY = hex2rgb('#607D8B')
BLUE_GREY50 = hex2rgb('#ECEFF1')
BLUE_GREY100 = hex2rgb('#CFD8DC')
BLUE_GREY200 = hex2rgb('#B0BEC5')
BLUE_GREY300 = hex2rgb('#90A4AE')
BLUE_GREY400 = hex2rgb('#78909C')
BLUE_GREY500 = hex2rgb('#607D8B')
BLUE_GREY600 = hex2rgb('#546E7A')
BLUE_GREY700 = hex2rgb('#455A64')
BLUE_GREY800 = hex2rgb('#37474F')
BLUE_GREY900 = hex2rgb('#263238')