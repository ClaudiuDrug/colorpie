# -*- coding: UTF-8 -*-

from .core import COLOR, HEX, RGB

# **************************** CSS named colors **************************** #
PINK: dict = {
    "Pink": COLOR(name="Pink", hex=HEX("FF", "C0", "CB"), rgb=RGB(255, 192, 203)),
    "LightPink": COLOR(name="LightPink", hex=HEX("FF", "B6", "C1"), rgb=RGB(255, 182, 193)),
    "HotPink": COLOR(name="HotPink", hex=HEX("FF", "69", "B4"), rgb=RGB(255, 105, 180)),
    "DeepPink": COLOR(name="DeepPink", hex=HEX("FF", "14", "93"), rgb=RGB(255, 20, 147)),
    "PaleVioletRed": COLOR(name="PaleVioletRed", hex=HEX("DB", "70", "93"), rgb=RGB(219, 112, 147)),
    "MediumVioletRed": COLOR(name="MediumVioletRed", hex=HEX("C7", "15", "85"), rgb=RGB(199, 21, 133)),
}

PURPLE: dict = {
    "Lavender": COLOR(name="Lavender", hex=HEX("E6", "E6", "FA"), rgb=RGB(230, 230, 250)),
    "Thistle": COLOR(name="Thistle", hex=HEX("D8", "BF", "D8"), rgb=RGB(216, 191, 216)),
    "Plum": COLOR(name="Plum", hex=HEX("DD", "A0", "DD"), rgb=RGB(221, 160, 221)),
    "Orchid": COLOR(name="Orchid", hex=HEX("DA", "70", "D6"), rgb=RGB(218, 112, 214)),
    "Violet": COLOR(name="Violet", hex=HEX("EE", "82", "EE"), rgb=RGB(238, 130, 238)),
    "Fuchsia": COLOR(name="Fuchsia", hex=HEX("FF", "00", "FF"), rgb=RGB(255, 0, 255)),
    "Magenta": COLOR(name="Magenta", hex=HEX("FF", "00", "FF"), rgb=RGB(255, 0, 255)),
    "MediumOrchid": COLOR(name="MediumOrchid", hex=HEX("BA", "55", "D3"), rgb=RGB(186, 85, 211)),
    "DarkOrchid": COLOR(name="DarkOrchid", hex=HEX("99", "32", "CC"), rgb=RGB(153, 50, 204)),
    "DarkViolet": COLOR(name="DarkViolet", hex=HEX("94", "00", "D3"), rgb=RGB(148, 0, 211)),
    "BlueViolet": COLOR(name="BlueViolet", hex=HEX("8A", "2B", "E2"), rgb=RGB(138, 43, 226)),
    "DarkMagenta": COLOR(name="DarkMagenta", hex=HEX("8B", "00", "8B"), rgb=RGB(139, 0, 139)),
    "Purple": COLOR(name="Purple", hex=HEX("80", "00", "80"), rgb=RGB(128, 0, 128)),
    "MediumPurple": COLOR(name="MediumPurple", hex=HEX("93", "70", "DB"), rgb=RGB(147, 112, 219)),
    "MediumSlateBlue": COLOR(name="MediumSlateBlue", hex=HEX("7B", "68", "EE"), rgb=RGB(123, 104, 238)),
    "SlateBlue": COLOR(name="SlateBlue", hex=HEX("6A", "5A", "CD"), rgb=RGB(106, 90, 205)),
    "DarkSlateBlue": COLOR(name="DarkSlateBlue", hex=HEX("48", "3D", "8B"), rgb=RGB(72, 61, 139)),
    "RebeccaPurple": COLOR(name="RebeccaPurple", hex=HEX("66", "33", "99"), rgb=RGB(102, 51, 153)),
    "Indigo": COLOR(name="Indigo", hex=HEX("4B", "00", "82"), rgb=RGB(75, 0, 130)),
}

RED: dict = {
    "LightSalmon": COLOR(name="LightSalmon", hex=HEX("FF", "A0", "7A"), rgb=RGB(255, 160, 122)),
    "Salmon": COLOR(name="Salmon", hex=HEX("FA", "80", "72"), rgb=RGB(250, 128, 114)),
    "DarkSalmon": COLOR(name="DarkSalmon", hex=HEX("E9", "96", "7A"), rgb=RGB(233, 150, 122)),
    "LightCoral": COLOR(name="LightCoral", hex=HEX("F0", "80", "80"), rgb=RGB(240, 128, 128)),
    "IndianRed": COLOR(name="IndianRed", hex=HEX("CD", "5C", "5C"), rgb=RGB(205, 92, 92)),
    "Crimson": COLOR(name="Crimson", hex=HEX("DC", "14", "3C"), rgb=RGB(220, 20, 60)),
    "Red": COLOR(name="Red", hex=HEX("FF", "00", "00"), rgb=RGB(255, 0, 0)),
    "FireBrick": COLOR(name="FireBrick", hex=HEX("B2", "22", "22"), rgb=RGB(178, 34, 34)),
    "DarkRed": COLOR(name="DarkRed", hex=HEX("8B", "00", "00"), rgb=RGB(139, 0, 0)),
}

ORANGE: dict = {
    "Orange": COLOR(name="Orange", hex=HEX("FF", "A5", "00"), rgb=RGB(255, 165, 0)),
    "DarkOrange": COLOR(name="DarkOrange", hex=HEX("FF", "8C", "00"), rgb=RGB(255, 140, 0)),
    "Coral": COLOR(name="Coral", hex=HEX("FF", "7F", "50"), rgb=RGB(255, 127, 80)),
    "Tomato": COLOR(name="Tomato", hex=HEX("FF", "63", "47"), rgb=RGB(255, 99, 71)),
    "OrangeRed": COLOR(name="OrangeRed", hex=HEX("FF", "45", "00"), rgb=RGB(255, 69, 0)),
}

YELLOW: dict = {
    "Gold": COLOR(name="Gold", hex=HEX("FF", "D7", "00"), rgb=RGB(255, 215, 0)),
    "Yellow": COLOR(name="Yellow", hex=HEX("FF", "FF", "00"), rgb=RGB(255, 255, 0)),
    "LightYellow": COLOR(name="LightYellow", hex=HEX("FF", "FF", "E0"), rgb=RGB(255, 255, 224)),
    "LemonChiffon": COLOR(name="LemonChiffon", hex=HEX("FF", "FA", "CD"), rgb=RGB(255, 250, 205)),
    "LightGoldenRodYellow": COLOR(name="LightGoldenRodYellow", hex=HEX("FA", "FA", "D2"), rgb=RGB(250, 250, 210)),
    "PapayaWhip": COLOR(name="PapayaWhip", hex=HEX("FF", "EF", "D5"), rgb=RGB(255, 239, 213)),
    "Moccasin": COLOR(name="Moccasin", hex=HEX("FF", "E4", "B5"), rgb=RGB(255, 228, 181)),
    "PeachPuff": COLOR(name="PeachPuff", hex=HEX("FF", "DA", "B9"), rgb=RGB(255, 218, 185)),
    "PaleGoldenRod": COLOR(name="PaleGoldenRod", hex=HEX("EE", "E8", "AA"), rgb=RGB(238, 232, 170)),
    "Khaki": COLOR(name="Khaki", hex=HEX("F0", "E6", "8C"), rgb=RGB(240, 230, 140)),
    "DarkKhaki": COLOR(name="DarkKhaki", hex=HEX("BD", "B7", "6B"), rgb=RGB(189, 183, 107)),
}

GREEN: dict = {
    "GreenYellow": COLOR(name="GreenYellow", hex=HEX("AD", "FF", "2F"), rgb=RGB(173, 255, 47)),
    "Chartreuse": COLOR(name="Chartreuse", hex=HEX("7F", "FF", "00"), rgb=RGB(127, 255, 0)),
    "LawnGreen": COLOR(name="LawnGreen", hex=HEX("7C", "FC", "00"), rgb=RGB(124, 252, 0)),
    "Lime": COLOR(name="Lime", hex=HEX("00", "FF", "00"), rgb=RGB(0, 255, 0)),
    "LimeGreen": COLOR(name="LimeGreen", hex=HEX("32", "CD", "32"), rgb=RGB(50, 205, 50)),
    "PaleGreen": COLOR(name="PaleGreen", hex=HEX("98", "FB", "98"), rgb=RGB(152, 251, 152)),
    "LightGreen": COLOR(name="LightGreen", hex=HEX("90", "EE", "90"), rgb=RGB(144, 238, 144)),
    "MediumSpringGreen": COLOR(name="MediumSpringGreen", hex=HEX("00", "FA", "9A"), rgb=RGB(0, 250, 154)),
    "SpringGreen": COLOR(name="SpringGreen", hex=HEX("00", "FF", "7F"), rgb=RGB(0, 255, 127)),
    "MediumSeaGreen": COLOR(name="MediumSeaGreen", hex=HEX("3C", "B3", "71"), rgb=RGB(60, 179, 113)),
    "SeaGreen": COLOR(name="SeaGreen", hex=HEX("2E", "8B", "57"), rgb=RGB(46, 139, 87)),
    "ForestGreen": COLOR(name="ForestGreen", hex=HEX("22", "8B", "22"), rgb=RGB(34, 139, 34)),
    "Green": COLOR(name="Green", hex=HEX("00", "80", "00"), rgb=RGB(0, 128, 0)),
    "DarkGreen": COLOR(name="DarkGreen", hex=HEX("00", "64", "00"), rgb=RGB(0, 100, 0)),
    "YellowGreen": COLOR(name="YellowGreen", hex=HEX("9A", "CD", "32"), rgb=RGB(154, 205, 50)),
    "OliveDrab": COLOR(name="OliveDrab", hex=HEX("6B", "8E", "23"), rgb=RGB(107, 142, 35)),
    "DarkOliveGreen": COLOR(name="DarkOliveGreen", hex=HEX("55", "6B", "2F"), rgb=RGB(85, 107, 47)),
    "MediumAquaMarine": COLOR(name="MediumAquaMarine", hex=HEX("66", "CD", "AA"), rgb=RGB(102, 205, 170)),
    "DarkSeaGreen": COLOR(name="DarkSeaGreen", hex=HEX("8F", "BC", "8F"), rgb=RGB(143, 188, 143)),
    "LightSeaGreen": COLOR(name="LightSeaGreen", hex=HEX("20", "B2", "AA"), rgb=RGB(32, 178, 170)),
    "DarkCyan": COLOR(name="DarkCyan", hex=HEX("00", "8B", "8B"), rgb=RGB(0, 139, 139)),
    "Teal": COLOR(name="Teal", hex=HEX("00", "80", "80"), rgb=RGB(0, 128, 128)),
}

CYAN: dict = {
    "Aqua": COLOR(name="Aqua", hex=HEX("00", "FF", "FF"), rgb=RGB(0, 255, 255)),
    "Cyan": COLOR(name="Cyan", hex=HEX("00", "FF", "FF"), rgb=RGB(0, 255, 255)),
    "LightCyan": COLOR(name="LightCyan", hex=HEX("E0", "FF", "FF"), rgb=RGB(224, 255, 255)),
    "PaleTurquoise": COLOR(name="PaleTurquoise", hex=HEX("AF", "EE", "EE"), rgb=RGB(175, 238, 238)),
    "Aquamarine": COLOR(name="Aquamarine", hex=HEX("7F", "FF", "D4"), rgb=RGB(127, 255, 212)),
    "Turquoise": COLOR(name="Turquoise", hex=HEX("40", "E0", "D0"), rgb=RGB(64, 224, 208)),
    "MediumTurquoise": COLOR(name="MediumTurquoise", hex=HEX("48", "D1", "CC"), rgb=RGB(72, 209, 204)),
    "DarkTurquoise": COLOR(name="DarkTurquoise", hex=HEX("00", "CE", "D1"), rgb=RGB(0, 206, 209)),
}

BLUE: dict = {
    "CadetBlue": COLOR(name="CadetBlue", hex=HEX("5F", "9E", "A0"), rgb=RGB(95, 158, 160)),
    "SteelBlue": COLOR(name="SteelBlue", hex=HEX("46", "82", "B4"), rgb=RGB(70, 130, 180)),
    "LightSteelBlue": COLOR(name="LightSteelBlue", hex=HEX("B0", "C4", "DE"), rgb=RGB(176, 196, 222)),
    "LightBlue": COLOR(name="LightBlue", hex=HEX("AD", "D8", "E6"), rgb=RGB(173, 216, 230)),
    "PowderBlue": COLOR(name="PowderBlue", hex=HEX("B0", "E0", "E6"), rgb=RGB(176, 224, 230)),
    "LightSkyBlue": COLOR(name="LightSkyBlue", hex=HEX("87", "CE", "FA"), rgb=RGB(135, 206, 250)),
    "SkyBlue": COLOR(name="SkyBlue", hex=HEX("87", "CE", "EB"), rgb=RGB(135, 206, 235)),
    "CornflowerBlue": COLOR(name="CornflowerBlue", hex=HEX("64", "95", "ED"), rgb=RGB(100, 149, 237)),
    "DeepSkyBlue": COLOR(name="DeepSkyBlue", hex=HEX("00", "BF", "FF"), rgb=RGB(0, 191, 255)),
    "DodgerBlue": COLOR(name="DodgerBlue", hex=HEX("1E", "90", "FF"), rgb=RGB(30, 144, 255)),
    "RoyalBlue": COLOR(name="RoyalBlue", hex=HEX("41", "69", "E1"), rgb=RGB(65, 105, 225)),
    "Blue": COLOR(name="Blue", hex=HEX("00", "00", "FF"), rgb=RGB(0, 0, 255)),
    "MediumBlue": COLOR(name="MediumBlue", hex=HEX("00", "00", "CD"), rgb=RGB(0, 0, 205)),
    "DarkBlue": COLOR(name="DarkBlue", hex=HEX("00", "00", "8B"), rgb=RGB(0, 0, 139)),
    "Navy": COLOR(name="Navy", hex=HEX("00", "00", "80"), rgb=RGB(0, 0, 128)),
    "MidnightBlue": COLOR(name="MidnightBlue", hex=HEX("19", "19", "70"), rgb=RGB(25, 25, 112)),
}

BROWN: dict = {
    "Cornsilk": COLOR(name="Cornsilk", hex=HEX("FF", "F8", "DC"), rgb=RGB(255, 248, 220)),
    "BlanchedAlmond": COLOR(name="BlanchedAlmond", hex=HEX("FF", "EB", "CD"), rgb=RGB(255, 235, 205)),
    "Bisque": COLOR(name="Bisque", hex=HEX("FF", "E4", "C4"), rgb=RGB(255, 228, 196)),
    "NavajoWhite": COLOR(name="NavajoWhite", hex=HEX("FF", "DE", "AD"), rgb=RGB(255, 222, 173)),
    "Wheat": COLOR(name="Wheat", hex=HEX("F5", "DE", "B3"), rgb=RGB(245, 222, 179)),
    "BurlyWood": COLOR(name="BurlyWood", hex=HEX("DE", "B8", "87"), rgb=RGB(222, 184, 135)),
    "Tan": COLOR(name="Tan", hex=HEX("D2", "B4", "8C"), rgb=RGB(210, 180, 140)),
    "RosyBrown": COLOR(name="RosyBrown", hex=HEX("BC", "8F", "8F"), rgb=RGB(188, 143, 143)),
    "SandyBrown": COLOR(name="SandyBrown", hex=HEX("F4", "A4", "60"), rgb=RGB(244, 164, 96)),
    "GoldenRod": COLOR(name="GoldenRod", hex=HEX("DA", "A5", "20"), rgb=RGB(218, 165, 32)),
    "DarkGoldenRod": COLOR(name="DarkGoldenRod", hex=HEX("B8", "86", "0B"), rgb=RGB(184, 134, 11)),
    "Peru": COLOR(name="Peru", hex=HEX("CD", "85", "3F"), rgb=RGB(205, 133, 63)),
    "Chocolate": COLOR(name="Chocolate", hex=HEX("D2", "69", "1E"), rgb=RGB(210, 105, 30)),
    "Olive": COLOR(name="Olive", hex=HEX("80", "80", "00"), rgb=RGB(128, 128, 0)),
    "SaddleBrown": COLOR(name="SaddleBrown", hex=HEX("8B", "45", "13"), rgb=RGB(139, 69, 19)),
    "Sienna": COLOR(name="Sienna", hex=HEX("A0", "52", "2D"), rgb=RGB(160, 82, 45)),
    "Brown": COLOR(name="Brown", hex=HEX("A5", "2A", "2A"), rgb=RGB(165, 42, 42)),
    "Maroon": COLOR(name="Maroon", hex=HEX("80", "00", "00"), rgb=RGB(128, 0, 0)),
}

WHITE: dict = {
    "White": COLOR(name="White", hex=HEX("FF", "FF", "FF"), rgb=RGB(255, 255, 255)),
    "Snow": COLOR(name="Snow", hex=HEX("FF", "FA", "FA"), rgb=RGB(255, 250, 250)),
    "HoneyDew": COLOR(name="HoneyDew", hex=HEX("F0", "FF", "F0"), rgb=RGB(240, 255, 240)),
    "MintCream": COLOR(name="MintCream", hex=HEX("F5", "FF", "FA"), rgb=RGB(245, 255, 250)),
    "Azure": COLOR(name="Azure", hex=HEX("F0", "FF", "FF"), rgb=RGB(240, 255, 255)),
    "AliceBlue": COLOR(name="AliceBlue", hex=HEX("F0", "F8", "FF"), rgb=RGB(240, 248, 255)),
    "GhostWhite": COLOR(name="GhostWhite", hex=HEX("F8", "F8", "FF"), rgb=RGB(248, 248, 255)),
    "WhiteSmoke": COLOR(name="WhiteSmoke", hex=HEX("F5", "F5", "F5"), rgb=RGB(245, 245, 245)),
    "SeaShell": COLOR(name="SeaShell", hex=HEX("FF", "F5", "EE"), rgb=RGB(255, 245, 238)),
    "Beige": COLOR(name="Beige", hex=HEX("F5", "F5", "DC"), rgb=RGB(245, 245, 220)),
    "OldLace": COLOR(name="OldLace", hex=HEX("FD", "F5", "E6"), rgb=RGB(253, 245, 230)),
    "FloralWhite": COLOR(name="FloralWhite", hex=HEX("FF", "FA", "F0"), rgb=RGB(255, 250, 240)),
    "Ivory": COLOR(name="Ivory", hex=HEX("FF", "FF", "F0"), rgb=RGB(255, 255, 240)),
    "AntiqueWhite": COLOR(name="AntiqueWhite", hex=HEX("FA", "EB", "D7"), rgb=RGB(250, 235, 215)),
    "Linen": COLOR(name="Linen", hex=HEX("FA", "F0", "E6"), rgb=RGB(250, 240, 230)),
    "LavenderBlush": COLOR(name="LavenderBlush", hex=HEX("FF", "F0", "F5"), rgb=RGB(255, 240, 245)),
    "MistyRose": COLOR(name="MistyRose", hex=HEX("FF", "E4", "E1"), rgb=RGB(255, 228, 225)),
}

GREY: dict = {
    "Gainsboro": COLOR(name="Gainsboro", hex=HEX("DC", "DC", "DC"), rgb=RGB(220, 220, 220)),
    "LightGrey": COLOR(name="LightGrey", hex=HEX("D3", "D3", "D3"), rgb=RGB(211, 211, 211)),
    "Silver": COLOR(name="Silver", hex=HEX("C0", "C0", "C0"), rgb=RGB(192, 192, 192)),
    "DarkGrey": COLOR(name="DarkGrey", hex=HEX("A9", "A9", "A9"), rgb=RGB(169, 169, 169)),
    "DimGrey": COLOR(name="DimGrey", hex=HEX("69", "69", "69"), rgb=RGB(105, 105, 105)),
    "Grey": COLOR(name="Grey", hex=HEX("80", "80", "80"), rgb=RGB(128, 128, 128)),
    "LightSlateGrey": COLOR(name="LightSlateGrey", hex=HEX("77", "88", "99"), rgb=RGB(119, 136, 153)),
    "SlateGrey": COLOR(name="SlateGrey", hex=HEX("70", "80", "90"), rgb=RGB(112, 128, 144)),
    "DarkSlateGrey": COLOR(name="DarkSlateGrey", hex=HEX("2F", "4F", "4F"), rgb=RGB(47, 79, 79)),
    "Black": COLOR(name="Black", hex=HEX("00", "00", "00"), rgb=RGB(0, 0, 0)),
}

CSS: dict = {
    key: value
    for group in [
        PINK,
        PURPLE,
        RED,
        ORANGE,
        YELLOW,
        GREEN,
        CYAN,
        BLUE,
        BROWN,
        WHITE,
        GREY,
    ]
    for key, value in group.items()
}

CSS.update(
    DarkGray=COLOR(name="DarkGray", hex=HEX("A9", "A9", "A9"), rgb=RGB(169, 169, 169)),
    DarkSlateGray=COLOR(name="DarkSlateGray", hex=HEX("2F", "4F", "4F"), rgb=RGB(47, 79, 79)),
    DimGray=COLOR(name="DimGray", hex=HEX("69", "69", "69"), rgb=RGB(105, 105, 105)),
    Gray=COLOR(name="Gray", hex=HEX("80", "80", "80"), rgb=RGB(128, 128, 128)),
    LightGray=COLOR(name="LightGray", hex=HEX("D3", "D3", "D3"), rgb=RGB(211, 211, 211)),
    LightSlateGray=COLOR(name="LightSlateGray", hex=HEX("77", "88", "99"), rgb=RGB(119, 136, 153)),
    SlateGray=COLOR(name="SlateGray", hex=HEX("70", "80", "90"), rgb=RGB(112, 128, 144)),
)
# ********************************** END *********************************** #

# foreground: ESC[38;5;{n}m
# background: ESC[48;5;{n}m
__256_color__: dict = {
    # standard:
    0: COLOR(id=0, name="black", hex=HEX("00", "00", "00"), rgb=RGB(0, 0, 0)),
    1: COLOR(id=1, name="maroon", hex=HEX("80", "00", "00"), rgb=RGB(128, 0, 0)),
    2: COLOR(id=2, name="green", hex=HEX("00", "80", "00"), rgb=RGB(0, 128, 0)),
    3: COLOR(id=3, name="olive", hex=HEX("80", "80", "00"), rgb=RGB(128, 128, 0)),
    4: COLOR(id=4, name="navy", hex=HEX("00", "00", "80"), rgb=RGB(0, 0, 128)),
    5: COLOR(id=5, name="purple", hex=HEX("80", "00", "80"), rgb=RGB(128, 0, 128)),
    6: COLOR(id=6, name="teal", hex=HEX("00", "80", "80"), rgb=RGB(0, 128, 128)),
    7: COLOR(id=7, name="silver", hex=HEX("C0", "C0", "C0"), rgb=RGB(192, 192, 192)),

    # high-intensity:
    8: COLOR(id=8, name="grey", hex=HEX("80", "80", "80"), rgb=RGB(128, 128, 128)),
    9: COLOR(id=9, name="red", hex=HEX("FF", "00", "00"), rgb=RGB(255, 0, 0)),
    10: COLOR(id=10, name="lime", hex=HEX("00", "FF", "00"), rgb=RGB(0, 255, 0)),
    11: COLOR(id=11, name="yellow", hex=HEX("FF", "FF", "00"), rgb=RGB(255, 255, 0)),
    12: COLOR(id=12, name="blue", hex=HEX("00", "00", "FF"), rgb=RGB(0, 0, 255)),
    13: COLOR(id=13, name="magenta", hex=HEX("FF", "00", "FF"), rgb=RGB(255, 0, 255)),
    14: COLOR(id=14, name="cyan", hex=HEX("00", "FF", "FF"), rgb=RGB(0, 255, 255)),
    15: COLOR(id=15, name="white", hex=HEX("FF", "FF", "FF"), rgb=RGB(255, 255, 255)),

    # 216 colors:
    16: COLOR(id=16, name="black", hex=HEX("00", "00", "00"), rgb=RGB(0, 0, 0)),
    17: COLOR(id=17, hex=HEX("00", "00", "5F"), rgb=RGB(0, 0, 95)),
    18: COLOR(id=18, hex=HEX("00", "00", "87"), rgb=RGB(0, 0, 135)),
    19: COLOR(id=19, hex=HEX("00", "00", "AF"), rgb=RGB(0, 0, 175)),
    20: COLOR(id=20, hex=HEX("00", "00", "D7"), rgb=RGB(0, 0, 215)),
    21: COLOR(id=21, name="blue", hex=HEX("00", "00", "FF"), rgb=RGB(0, 0, 255)),
    22: COLOR(id=22, hex=HEX("00", "5F", "00"), rgb=RGB(0, 95, 0)),
    23: COLOR(id=23, hex=HEX("00", "5F", "5F"), rgb=RGB(0, 95, 95)),
    24: COLOR(id=24, hex=HEX("00", "5F", "87"), rgb=RGB(0, 95, 135)),
    25: COLOR(id=25, hex=HEX("00", "5F", "AF"), rgb=RGB(0, 95, 175)),
    26: COLOR(id=26, hex=HEX("00", "5F", "D7"), rgb=RGB(0, 95, 215)),
    27: COLOR(id=27, hex=HEX("00", "5F", "FF"), rgb=RGB(0, 95, 255)),
    28: COLOR(id=28, hex=HEX("00", "87", "00"), rgb=RGB(0, 135, 0)),
    29: COLOR(id=29, hex=HEX("00", "87", "5F"), rgb=RGB(0, 135, 95)),
    30: COLOR(id=30, hex=HEX("00", "87", "87"), rgb=RGB(0, 135, 135)),
    31: COLOR(id=31, hex=HEX("00", "87", "AF"), rgb=RGB(0, 135, 175)),
    32: COLOR(id=32, hex=HEX("00", "87", "D7"), rgb=RGB(0, 135, 215)),
    33: COLOR(id=33, hex=HEX("00", "87", "FF"), rgb=RGB(0, 135, 255)),
    34: COLOR(id=34, hex=HEX("00", "AF", "00"), rgb=RGB(0, 175, 0)),
    35: COLOR(id=35, hex=HEX("00", "AF", "5F"), rgb=RGB(0, 175, 95)),
    36: COLOR(id=36, hex=HEX("00", "AF", "87"), rgb=RGB(0, 175, 135)),
    37: COLOR(id=37, hex=HEX("00", "AF", "AF"), rgb=RGB(0, 175, 175)),
    38: COLOR(id=38, hex=HEX("00", "AF", "D7"), rgb=RGB(0, 175, 215)),
    39: COLOR(id=39, hex=HEX("00", "AF", "FF"), rgb=RGB(0, 175, 255)),
    40: COLOR(id=40, hex=HEX("00", "D7", "00"), rgb=RGB(0, 215, 0)),
    41: COLOR(id=41, hex=HEX("00", "D7", "5F"), rgb=RGB(0, 215, 95)),
    42: COLOR(id=42, hex=HEX("00", "D7", "87"), rgb=RGB(0, 215, 135)),
    43: COLOR(id=43, hex=HEX("00", "D7", "AF"), rgb=RGB(0, 215, 175)),
    44: COLOR(id=44, hex=HEX("00", "D7", "D7"), rgb=RGB(0, 215, 215)),
    45: COLOR(id=45, hex=HEX("00", "D7", "FF"), rgb=RGB(0, 215, 255)),
    46: COLOR(id=46, name="lime", hex=HEX("00", "FF", "00"), rgb=RGB(0, 255, 0)),
    47: COLOR(id=47, hex=HEX("00", "FF", "5F"), rgb=RGB(0, 255, 95)),
    48: COLOR(id=48, hex=HEX("00", "FF", "87"), rgb=RGB(0, 255, 135)),
    49: COLOR(id=49, hex=HEX("00", "FF", "AF"), rgb=RGB(0, 255, 175)),
    50: COLOR(id=50, hex=HEX("00", "FF", "D7"), rgb=RGB(0, 255, 215)),
    51: COLOR(id=51, name="cyan", hex=HEX("00", "FF", "FF"), rgb=RGB(0, 255, 255)),

    52: COLOR(id=52, hex=HEX("5F", "00", "00"), rgb=RGB(95, 0, 0)),
    53: COLOR(id=53, hex=HEX("5F", "00", "5F"), rgb=RGB(95, 0, 95)),
    54: COLOR(id=54, hex=HEX("5F", "00", "87"), rgb=RGB(95, 0, 135)),
    55: COLOR(id=55, hex=HEX("5F", "00", "AF"), rgb=RGB(95, 0, 175)),
    56: COLOR(id=56, hex=HEX("5F", "00", "D7"), rgb=RGB(95, 0, 215)),
    57: COLOR(id=57, hex=HEX("5F", "00", "FF"), rgb=RGB(95, 0, 255)),
    58: COLOR(id=58, hex=HEX("5F", "5F", "00"), rgb=RGB(95, 95, 0)),
    59: COLOR(id=59, hex=HEX("5F", "5F", "5F"), rgb=RGB(95, 95, 95)),
    60: COLOR(id=60, hex=HEX("5F", "5F", "87"), rgb=RGB(95, 95, 135)),
    61: COLOR(id=61, hex=HEX("5F", "5F", "AF"), rgb=RGB(95, 95, 175)),
    62: COLOR(id=62, hex=HEX("5F", "5F", "D7"), rgb=RGB(95, 95, 215)),
    63: COLOR(id=63, hex=HEX("5F", "5F", "FF"), rgb=RGB(95, 95, 255)),
    64: COLOR(id=64, hex=HEX("5F", "87", "00"), rgb=RGB(95, 135, 0)),
    65: COLOR(id=65, hex=HEX("5F", "87", "5F"), rgb=RGB(95, 135, 95)),
    66: COLOR(id=66, hex=HEX("5F", "87", "87"), rgb=RGB(95, 135, 135)),
    67: COLOR(id=67, hex=HEX("5F", "87", "AF"), rgb=RGB(95, 135, 175)),
    68: COLOR(id=68, hex=HEX("5F", "87", "D7"), rgb=RGB(95, 135, 215)),
    69: COLOR(id=69, hex=HEX("5F", "87", "FF"), rgb=RGB(95, 135, 255)),
    70: COLOR(id=70, hex=HEX("5F", "AF", "00"), rgb=RGB(95, 175, 0)),
    71: COLOR(id=71, hex=HEX("5F", "AF", "5F"), rgb=RGB(95, 175, 95)),
    72: COLOR(id=72, hex=HEX("5F", "AF", "87"), rgb=RGB(95, 175, 135)),
    73: COLOR(id=73, hex=HEX("5F", "AF", "AF"), rgb=RGB(95, 175, 175)),
    74: COLOR(id=74, hex=HEX("5F", "AF", "D7"), rgb=RGB(95, 175, 215)),
    75: COLOR(id=75, hex=HEX("5F", "AF", "FF"), rgb=RGB(95, 175, 255)),
    76: COLOR(id=76, hex=HEX("5F", "D7", "00"), rgb=RGB(95, 215, 0)),
    77: COLOR(id=77, hex=HEX("5F", "D7", "5F"), rgb=RGB(95, 215, 95)),
    78: COLOR(id=78, hex=HEX("5F", "D7", "87"), rgb=RGB(95, 215, 135)),
    79: COLOR(id=79, hex=HEX("5F", "D7", "AF"), rgb=RGB(95, 215, 175)),
    80: COLOR(id=80, hex=HEX("5F", "D7", "D7"), rgb=RGB(95, 215, 215)),
    81: COLOR(id=81, hex=HEX("5F", "D7", "FF"), rgb=RGB(95, 215, 255)),
    82: COLOR(id=82, hex=HEX("5F", "FF", "00"), rgb=RGB(95, 255, 0)),
    83: COLOR(id=83, hex=HEX("5F", "FF", "5F"), rgb=RGB(95, 255, 95)),
    84: COLOR(id=84, hex=HEX("5F", "FF", "87"), rgb=RGB(95, 255, 135)),
    85: COLOR(id=85, hex=HEX("5F", "FF", "AF"), rgb=RGB(95, 255, 175)),
    86: COLOR(id=86, hex=HEX("5F", "FF", "D7"), rgb=RGB(95, 255, 215)),
    87: COLOR(id=87, hex=HEX("5F", "FF", "FF"), rgb=RGB(95, 255, 255)),

    88: COLOR(id=88, hex=HEX("87", "00", "00"), rgb=RGB(135, 0, 0)),
    89: COLOR(id=89, hex=HEX("87", "00", "5F"), rgb=RGB(135, 0, 95)),
    90: COLOR(id=90, hex=HEX("87", "00", "87"), rgb=RGB(135, 0, 135)),
    91: COLOR(id=91, hex=HEX("87", "00", "AF"), rgb=RGB(135, 0, 175)),
    92: COLOR(id=92, hex=HEX("87", "00", "D7"), rgb=RGB(135, 0, 215)),
    93: COLOR(id=93, hex=HEX("87", "00", "FF"), rgb=RGB(135, 0, 255)),
    94: COLOR(id=94, hex=HEX("87", "5F", "00"), rgb=RGB(135, 95, 0)),
    95: COLOR(id=95, hex=HEX("87", "5F", "5F"), rgb=RGB(135, 95, 95)),
    96: COLOR(id=96, hex=HEX("87", "5F", "87"), rgb=RGB(135, 95, 135)),
    97: COLOR(id=97, hex=HEX("87", "5F", "AF"), rgb=RGB(135, 95, 175)),
    98: COLOR(id=98, hex=HEX("87", "5F", "D7"), rgb=RGB(135, 95, 215)),
    99: COLOR(id=99, hex=HEX("87", "5F", "FF"), rgb=RGB(135, 95, 255)),
    100: COLOR(id=100, hex=HEX("87", "87", "00"), rgb=RGB(135, 135, 0)),
    101: COLOR(id=101, hex=HEX("87", "87", "5F"), rgb=RGB(135, 135, 95)),
    102: COLOR(id=102, hex=HEX("87", "87", "87"), rgb=RGB(135, 135, 135)),
    103: COLOR(id=103, hex=HEX("87", "87", "AF"), rgb=RGB(135, 135, 175)),
    104: COLOR(id=104, hex=HEX("87", "87", "D7"), rgb=RGB(135, 135, 215)),
    105: COLOR(id=105, hex=HEX("87", "87", "FF"), rgb=RGB(135, 135, 255)),
    106: COLOR(id=106, hex=HEX("87", "AF", "00"), rgb=RGB(135, 175, 0)),
    107: COLOR(id=107, hex=HEX("87", "AF", "5F"), rgb=RGB(135, 175, 95)),
    108: COLOR(id=108, hex=HEX("87", "AF", "87"), rgb=RGB(135, 175, 135)),
    109: COLOR(id=109, hex=HEX("87", "AF", "AF"), rgb=RGB(135, 175, 175)),
    110: COLOR(id=110, hex=HEX("87", "AF", "D7"), rgb=RGB(135, 175, 215)),
    111: COLOR(id=111, hex=HEX("87", "AF", "FF"), rgb=RGB(135, 175, 255)),
    112: COLOR(id=112, hex=HEX("87", "D7", "00"), rgb=RGB(135, 215, 0)),
    113: COLOR(id=113, hex=HEX("87", "D7", "5F"), rgb=RGB(135, 215, 95)),
    114: COLOR(id=114, hex=HEX("87", "D7", "87"), rgb=RGB(135, 215, 135)),
    115: COLOR(id=115, hex=HEX("87", "D7", "AF"), rgb=RGB(135, 215, 175)),
    116: COLOR(id=116, hex=HEX("87", "D7", "D7"), rgb=RGB(135, 215, 215)),
    117: COLOR(id=117, hex=HEX("87", "D7", "FF"), rgb=RGB(135, 215, 255)),
    118: COLOR(id=118, hex=HEX("87", "FF", "00"), rgb=RGB(135, 255, 0)),
    119: COLOR(id=119, hex=HEX("87", "FF", "5F"), rgb=RGB(135, 255, 95)),
    120: COLOR(id=120, hex=HEX("87", "FF", "87"), rgb=RGB(135, 255, 135)),
    121: COLOR(id=121, hex=HEX("87", "FF", "AF"), rgb=RGB(135, 255, 175)),
    122: COLOR(id=122, hex=HEX("87", "FF", "D7"), rgb=RGB(135, 255, 215)),
    123: COLOR(id=123, hex=HEX("87", "FF", "FF"), rgb=RGB(135, 255, 255)),

    124: COLOR(id=124, hex=HEX("AF", "00", "00"), rgb=RGB(175, 0, 0)),
    125: COLOR(id=125, hex=HEX("AF", "00", "5F"), rgb=RGB(175, 0, 95)),
    126: COLOR(id=126, hex=HEX("AF", "00", "87"), rgb=RGB(175, 0, 135)),
    127: COLOR(id=127, hex=HEX("AF", "00", "AF"), rgb=RGB(175, 0, 175)),
    128: COLOR(id=128, hex=HEX("AF", "00", "D7"), rgb=RGB(175, 0, 215)),
    129: COLOR(id=129, hex=HEX("AF", "00", "FF"), rgb=RGB(175, 0, 255)),
    130: COLOR(id=130, hex=HEX("AF", "5F", "00"), rgb=RGB(175, 95, 0)),
    131: COLOR(id=131, hex=HEX("AF", "5F", "5F"), rgb=RGB(175, 95, 95)),
    132: COLOR(id=132, hex=HEX("AF", "5F", "87"), rgb=RGB(175, 95, 135)),
    133: COLOR(id=133, hex=HEX("AF", "5F", "AF"), rgb=RGB(175, 95, 175)),
    134: COLOR(id=134, hex=HEX("AF", "5F", "D7"), rgb=RGB(175, 95, 215)),
    135: COLOR(id=135, hex=HEX("AF", "5F", "FF"), rgb=RGB(175, 95, 255)),
    136: COLOR(id=136, hex=HEX("AF", "87", "00"), rgb=RGB(175, 135, 0)),
    137: COLOR(id=137, hex=HEX("AF", "87", "5F"), rgb=RGB(175, 135, 95)),
    138: COLOR(id=138, hex=HEX("AF", "87", "87"), rgb=RGB(175, 135, 135)),
    139: COLOR(id=139, hex=HEX("AF", "87", "AF"), rgb=RGB(175, 135, 175)),
    140: COLOR(id=140, hex=HEX("AF", "87", "D7"), rgb=RGB(175, 135, 215)),
    141: COLOR(id=141, hex=HEX("AF", "87", "FF"), rgb=RGB(175, 135, 255)),
    142: COLOR(id=142, hex=HEX("AF", "AF", "00"), rgb=RGB(175, 175, 0)),
    143: COLOR(id=143, hex=HEX("AF", "AF", "5F"), rgb=RGB(175, 175, 95)),
    144: COLOR(id=144, hex=HEX("AF", "AF", "87"), rgb=RGB(175, 175, 135)),
    145: COLOR(id=145, hex=HEX("AF", "AF", "AF"), rgb=RGB(175, 175, 175)),
    146: COLOR(id=146, hex=HEX("AF", "AF", "D7"), rgb=RGB(175, 175, 215)),
    147: COLOR(id=147, hex=HEX("AF", "AF", "FF"), rgb=RGB(175, 175, 255)),
    148: COLOR(id=148, hex=HEX("AF", "D7", "00"), rgb=RGB(175, 215, 0)),
    149: COLOR(id=149, hex=HEX("AF", "D7", "5F"), rgb=RGB(175, 215, 95)),
    150: COLOR(id=150, hex=HEX("AF", "D7", "87"), rgb=RGB(175, 215, 135)),
    151: COLOR(id=151, hex=HEX("AF", "D7", "AF"), rgb=RGB(175, 215, 175)),
    152: COLOR(id=152, hex=HEX("AF", "D7", "D7"), rgb=RGB(175, 215, 215)),
    153: COLOR(id=153, hex=HEX("AF", "D7", "FF"), rgb=RGB(175, 215, 255)),
    154: COLOR(id=154, hex=HEX("AF", "FF", "00"), rgb=RGB(175, 255, 0)),
    155: COLOR(id=155, hex=HEX("AF", "FF", "5F"), rgb=RGB(175, 255, 95)),
    156: COLOR(id=156, hex=HEX("AF", "FF", "87"), rgb=RGB(175, 255, 135)),
    157: COLOR(id=157, hex=HEX("AF", "FF", "AF"), rgb=RGB(175, 255, 175)),
    158: COLOR(id=158, hex=HEX("AF", "FF", "D7"), rgb=RGB(175, 255, 215)),
    159: COLOR(id=159, hex=HEX("AF", "FF", "FF"), rgb=RGB(175, 255, 255)),

    160: COLOR(id=160, hex=HEX("D7", "00", "00"), rgb=RGB(215, 0, 0)),
    161: COLOR(id=161, hex=HEX("D7", "00", "5F"), rgb=RGB(215, 0, 95)),
    162: COLOR(id=162, hex=HEX("D7", "00", "87"), rgb=RGB(215, 0, 135)),
    163: COLOR(id=163, hex=HEX("D7", "00", "AF"), rgb=RGB(215, 0, 175)),
    164: COLOR(id=164, hex=HEX("D7", "00", "D7"), rgb=RGB(215, 0, 215)),
    165: COLOR(id=165, hex=HEX("D7", "00", "FF"), rgb=RGB(215, 0, 255)),
    166: COLOR(id=166, hex=HEX("D7", "5F", "00"), rgb=RGB(215, 95, 0)),
    167: COLOR(id=167, hex=HEX("D7", "5F", "5F"), rgb=RGB(215, 95, 95)),
    168: COLOR(id=168, hex=HEX("D7", "5F", "87"), rgb=RGB(215, 95, 135)),
    169: COLOR(id=169, hex=HEX("D7", "5F", "AF"), rgb=RGB(215, 95, 175)),
    170: COLOR(id=170, hex=HEX("D7", "5F", "D7"), rgb=RGB(215, 95, 215)),
    171: COLOR(id=171, hex=HEX("D7", "5F", "FF"), rgb=RGB(215, 95, 255)),
    172: COLOR(id=172, hex=HEX("D7", "87", "00"), rgb=RGB(215, 135, 0)),
    173: COLOR(id=173, hex=HEX("D7", "87", "5F"), rgb=RGB(215, 135, 95)),
    174: COLOR(id=174, hex=HEX("D7", "87", "87"), rgb=RGB(215, 135, 135)),
    175: COLOR(id=175, hex=HEX("D7", "87", "AF"), rgb=RGB(215, 135, 175)),
    176: COLOR(id=176, hex=HEX("D7", "87", "D7"), rgb=RGB(215, 135, 215)),
    177: COLOR(id=177, hex=HEX("D7", "87", "FF"), rgb=RGB(215, 135, 255)),
    178: COLOR(id=178, hex=HEX("D7", "AF", "00"), rgb=RGB(215, 175, 0)),
    179: COLOR(id=179, hex=HEX("D7", "AF", "5F"), rgb=RGB(215, 175, 95)),
    180: COLOR(id=180, hex=HEX("D7", "AF", "87"), rgb=RGB(215, 175, 135)),
    181: COLOR(id=181, hex=HEX("D7", "AF", "AF"), rgb=RGB(215, 175, 175)),
    182: COLOR(id=182, hex=HEX("D7", "AF", "D7"), rgb=RGB(215, 175, 215)),
    183: COLOR(id=183, hex=HEX("D7", "AF", "FF"), rgb=RGB(215, 175, 255)),
    184: COLOR(id=184, hex=HEX("D7", "D7", "00"), rgb=RGB(215, 215, 0)),
    185: COLOR(id=185, hex=HEX("D7", "D7", "5F"), rgb=RGB(215, 215, 95)),
    186: COLOR(id=186, hex=HEX("D7", "D7", "87"), rgb=RGB(215, 215, 135)),
    187: COLOR(id=187, hex=HEX("D7", "D7", "AF"), rgb=RGB(215, 215, 175)),
    188: COLOR(id=188, hex=HEX("D7", "D7", "D7"), rgb=RGB(215, 215, 215)),
    189: COLOR(id=189, hex=HEX("D7", "D7", "FF"), rgb=RGB(215, 215, 255)),
    190: COLOR(id=190, hex=HEX("D7", "FF", "00"), rgb=RGB(215, 255, 0)),
    191: COLOR(id=191, hex=HEX("D7", "FF", "5F"), rgb=RGB(215, 255, 95)),
    192: COLOR(id=192, hex=HEX("D7", "FF", "87"), rgb=RGB(215, 255, 135)),
    193: COLOR(id=193, hex=HEX("D7", "FF", "AF"), rgb=RGB(215, 255, 175)),
    194: COLOR(id=194, hex=HEX("D7", "FF", "D7"), rgb=RGB(215, 255, 215)),
    195: COLOR(id=195, hex=HEX("D7", "FF", "FF"), rgb=RGB(215, 255, 255)),

    196: COLOR(id=196, name="red", hex=HEX("FF", "00", "00"), rgb=RGB(255, 0, 0)),
    197: COLOR(id=197, hex=HEX("FF", "00", "5F"), rgb=RGB(255, 0, 95)),
    198: COLOR(id=198, hex=HEX("FF", "00", "87"), rgb=RGB(255, 0, 135)),
    199: COLOR(id=199, hex=HEX("FF", "00", "AF"), rgb=RGB(255, 0, 175)),
    200: COLOR(id=200, hex=HEX("FF", "00", "D7"), rgb=RGB(255, 0, 215)),
    201: COLOR(id=201, name="magenta", hex=HEX("FF", "00", "FF"), rgb=RGB(255, 0, 255)),
    202: COLOR(id=202, hex=HEX("FF", "5F", "00"), rgb=RGB(255, 95, 0)),
    203: COLOR(id=203, hex=HEX("FF", "5F", "5F"), rgb=RGB(255, 95, 95)),
    204: COLOR(id=204, hex=HEX("FF", "5F", "87"), rgb=RGB(255, 95, 135)),
    205: COLOR(id=205, hex=HEX("FF", "5F", "AF"), rgb=RGB(255, 95, 175)),
    206: COLOR(id=206, hex=HEX("FF", "5F", "D7"), rgb=RGB(255, 95, 215)),
    207: COLOR(id=207, hex=HEX("FF", "5F", "FF"), rgb=RGB(255, 95, 255)),
    208: COLOR(id=208, hex=HEX("FF", "87", "00"), rgb=RGB(255, 135, 0)),
    209: COLOR(id=209, hex=HEX("FF", "87", "5F"), rgb=RGB(255, 135, 95)),
    210: COLOR(id=210, hex=HEX("FF", "87", "87"), rgb=RGB(255, 135, 135)),
    211: COLOR(id=211, hex=HEX("FF", "87", "AF"), rgb=RGB(255, 135, 175)),
    212: COLOR(id=212, hex=HEX("FF", "87", "D7"), rgb=RGB(255, 135, 215)),
    213: COLOR(id=213, hex=HEX("FF", "87", "FF"), rgb=RGB(255, 135, 255)),
    214: COLOR(id=214, hex=HEX("FF", "AF", "00"), rgb=RGB(255, 175, 0)),
    215: COLOR(id=215, hex=HEX("FF", "AF", "5F"), rgb=RGB(255, 175, 95)),
    216: COLOR(id=216, hex=HEX("FF", "AF", "87"), rgb=RGB(255, 175, 135)),
    217: COLOR(id=217, hex=HEX("FF", "AF", "AF"), rgb=RGB(255, 175, 175)),
    218: COLOR(id=218, hex=HEX("FF", "AF", "D7"), rgb=RGB(255, 175, 215)),
    219: COLOR(id=219, hex=HEX("FF", "AF", "FF"), rgb=RGB(255, 175, 255)),
    220: COLOR(id=220, name="gold", hex=HEX("FF", "D7", "00"), rgb=RGB(255, 215, 0)),
    221: COLOR(id=221, hex=HEX("FF", "D7", "5F"), rgb=RGB(255, 215, 95)),
    222: COLOR(id=222, hex=HEX("FF", "D7", "87"), rgb=RGB(255, 215, 135)),
    223: COLOR(id=223, hex=HEX("FF", "D7", "AF"), rgb=RGB(255, 215, 175)),
    224: COLOR(id=224, hex=HEX("FF", "D7", "D7"), rgb=RGB(255, 215, 215)),
    225: COLOR(id=225, hex=HEX("FF", "D7", "FF"), rgb=RGB(255, 215, 255)),
    226: COLOR(id=226, name="yellow", hex=HEX("FF", "FF", "00"), rgb=RGB(255, 255, 0)),
    227: COLOR(id=227, hex=HEX("FF", "FF", "5F"), rgb=RGB(255, 255, 95)),
    228: COLOR(id=228, hex=HEX("FF", "FF", "87"), rgb=RGB(255, 255, 135)),
    229: COLOR(id=229, hex=HEX("FF", "FF", "AF"), rgb=RGB(255, 255, 175)),
    230: COLOR(id=230, hex=HEX("FF", "FF", "D7"), rgb=RGB(255, 255, 215)),
    231: COLOR(id=231, name="white", hex=HEX("FF", "FF", "FF"), rgb=RGB(255, 255, 255)),

    # greyscale:
    232: COLOR(id=232, hex=HEX("08", "08", "08"), rgb=RGB(8, 8, 8)),
    233: COLOR(id=233, hex=HEX("12", "12", "12"), rgb=RGB(18, 18, 18)),
    234: COLOR(id=234, hex=HEX("1C", "1C", "1C"), rgb=RGB(28, 28, 28)),
    235: COLOR(id=235, hex=HEX("26", "26", "26"), rgb=RGB(38, 38, 38)),
    236: COLOR(id=236, hex=HEX("30", "30", "30"), rgb=RGB(48, 48, 48)),
    237: COLOR(id=237, hex=HEX("3A", "3A", "3A"), rgb=RGB(58, 58, 58)),
    238: COLOR(id=238, hex=HEX("44", "44", "44"), rgb=RGB(68, 68, 68)),
    239: COLOR(id=239, hex=HEX("4E", "4E", "4E"), rgb=RGB(78, 78, 78)),
    240: COLOR(id=240, hex=HEX("58", "58", "58"), rgb=RGB(88, 88, 88)),
    241: COLOR(id=241, hex=HEX("62", "62", "62"), rgb=RGB(98, 98, 98)),
    242: COLOR(id=242, hex=HEX("6C", "6C", "6C"), rgb=RGB(108, 108, 108)),
    243: COLOR(id=243, hex=HEX("76", "76", "76"), rgb=RGB(118, 118, 118)),
    244: COLOR(id=244, name="grey", hex=HEX("80", "80", "80"), rgb=RGB(128, 128, 128)),
    245: COLOR(id=245, hex=HEX("8A", "8A", "8A"), rgb=RGB(138, 138, 138)),
    246: COLOR(id=246, hex=HEX("94", "94", "94"), rgb=RGB(148, 148, 148)),
    247: COLOR(id=247, hex=HEX("9E", "9E", "9E"), rgb=RGB(158, 158, 158)),
    248: COLOR(id=248, hex=HEX("A8", "A8", "A8"), rgb=RGB(168, 168, 168)),
    249: COLOR(id=249, hex=HEX("B2", "B2", "B2"), rgb=RGB(178, 178, 178)),
    250: COLOR(id=250, hex=HEX("BC", "BC", "BC"), rgb=RGB(188, 188, 188)),
    251: COLOR(id=251, hex=HEX("C6", "C6", "C6"), rgb=RGB(198, 198, 198)),
    252: COLOR(id=252, hex=HEX("D0", "D0", "D0"), rgb=RGB(208, 208, 208)),
    253: COLOR(id=253, hex=HEX("DA", "DA", "DA"), rgb=RGB(218, 218, 218)),
    254: COLOR(id=254, hex=HEX("E4", "E4", "E4"), rgb=RGB(228, 228, 228)),
    255: COLOR(id=255, hex=HEX("EE", "EE", "EE"), rgb=RGB(238, 238, 238)),
}
