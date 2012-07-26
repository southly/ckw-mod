#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
from string import Template
from xml.sax.saxutils import escape

##  m_colors[0]  = RGB(0x00, 0x00, 0x01);
##  m_colors[1]  = RGB(0x00, 0x00, 0x80);
##  m_colors[2]  = RGB(0x00, 0x80, 0x00);
##  m_colors[3]  = RGB(0x00, 0x80, 0x80);
##  m_colors[4]  = RGB(0x80, 0x00, 0x00);
##  m_colors[5]  = RGB(0x80, 0x00, 0x80);
##  m_colors[6]  = RGB(0x80, 0x80, 0x00);
##  m_colors[7]  = RGB(0xC0, 0xC0, 0xC0);
##  m_colors[8]  = RGB(0x80, 0x80, 0x80);
##  m_colors[9]  = RGB(0x00, 0x00, 0xFF);
##  m_colors[10] = RGB(0x00, 0xFF, 0x00);
##  m_colors[11] = RGB(0x00, 0xFF, 0xFF);
##  m_colors[12] = RGB(0xFF, 0x00, 0x00);
##  m_colors[13] = RGB(0xFF, 0x00, 0xFF);
##  m_colors[14] = RGB(0xFF, 0xFF, 0x00);
##  m_colors[15] = RGB(0xFF, 0xFF, 0xFF);
##  m_colorFg    = RGB(0xC0, 0xC0, 0xC0); // cursor fg
##  m_colorBg    = RGB(0x00, 0x00, 0x01); // cursor bg
##  m_colorCursor = RGB(0xC0, 0xC0, 0x80);
##  m_colorCursorIme = RGB(0xC0, 0x00, 0x00);

default_colors = {
    "Ckw*foreground": "#C0C0C0",
    "Ckw*background": "#000001",
    "Ckw*cursorColor": "#C0C080",
    "Ckw*cursorImeColor": "#C00000",
    "Ckw*color0":  "#000001",
    "Ckw*color1":  "#000080",
    "Ckw*color2":  "#008000",
    "Ckw*color3":  "#008080",
    "Ckw*color4":  "#800000",
    "Ckw*color5":  "#800080",
    "Ckw*color6":  "#808000",
    "Ckw*color7":  "#C0C0C0",
    "Ckw*color8":  "#808080",
    "Ckw*color9":  "#0000FF",
    "Ckw*color10": "#00FF00",
    "Ckw*color11": "#00FFFF",
    "Ckw*color12": "#FF0000",
    "Ckw*color13": "#FF00FF",
    "Ckw*color14": "#FFFF00",
    "Ckw*color15": "#FFFFFF",
}


def RGB(r, g, b):
    return "#{0:02x}{1:02x}{2:02x}".format(r, g, b)


named_colors = {
    "alice blue":             RGB(0xF0, 0xF8, 0xFF),
    "AliceBlue":              RGB(0xF0, 0xF8, 0xFF),
    "antique white":          RGB(0xFA, 0xEB, 0xD7),
    "AntiqueWhite":           RGB(0xFA, 0xEB, 0xD7),
    "AntiqueWhite1":          RGB(0xFF, 0xEF, 0xDB),
    "AntiqueWhite2":          RGB(0xEE, 0xDF, 0xCC),
    "AntiqueWhite3":          RGB(0xCD, 0xC0, 0xB0),
    "AntiqueWhite4":          RGB(0x8B, 0x83, 0x78),
    "aquamarine":             RGB(0x7F, 0xFF, 0xD4),
    "aquamarine1":            RGB(0x7F, 0xFF, 0xD4),
    "aquamarine2":            RGB(0x76, 0xEE, 0xC6),
    "aquamarine3":            RGB(0x66, 0xCD, 0xAA),
    "aquamarine4":            RGB(0x45, 0x8B, 0x74),
    "azure":                  RGB(0xF0, 0xFF, 0xFF),
    "azure1":                 RGB(0xF0, 0xFF, 0xFF),
    "azure2":                 RGB(0xE0, 0xEE, 0xEE),
    "azure3":                 RGB(0xC1, 0xCD, 0xCD),
    "azure4":                 RGB(0x83, 0x8B, 0x8B),
    "beige":                  RGB(0xF5, 0xF5, 0xDC),
    "bisque":                 RGB(0xFF, 0xE4, 0xC4),
    "bisque1":                RGB(0xFF, 0xE4, 0xC4),
    "bisque2":                RGB(0xEE, 0xD5, 0xB7),
    "bisque3":                RGB(0xCD, 0xB7, 0x9E),
    "bisque4":                RGB(0x8B, 0x7D, 0x6B),
    "black":                  RGB(0x00, 0x00, 0x01),
    "blanched almond":        RGB(0xFF, 0xEB, 0xCD),
    "BlanchedAlmond":         RGB(0xFF, 0xEB, 0xCD),
    "blue":                   RGB(0x00, 0x00, 0xFF),
    "blue violet":            RGB(0x8A, 0x2B, 0xE2),
    "blue1":                  RGB(0x00, 0x00, 0xFF),
    "blue2":                  RGB(0x00, 0x00, 0xEE),
    "blue3":                  RGB(0x00, 0x00, 0xCD),
    "blue4":                  RGB(0x00, 0x00, 0x8B),
    "BlueViolet":             RGB(0x8A, 0x2B, 0xE2),
    "brown":                  RGB(0xA5, 0x2A, 0x2A),
    "brown1":                 RGB(0xFF, 0x40, 0x40),
    "brown2":                 RGB(0xEE, 0x3B, 0x3B),
    "brown3":                 RGB(0xCD, 0x33, 0x33),
    "brown4":                 RGB(0x8B, 0x23, 0x23),
    "burlywood":              RGB(0xDE, 0xB8, 0x87),
    "burlywood1":             RGB(0xFF, 0xD3, 0x9B),
    "burlywood2":             RGB(0xEE, 0xC5, 0x91),
    "burlywood3":             RGB(0xCD, 0xAA, 0x7D),
    "burlywood4":             RGB(0x8B, 0x73, 0x55),
    "cadet blue":             RGB(0x5F, 0x9E, 0xA0),
    "CadetBlue":              RGB(0x5F, 0x9E, 0xA0),
    "CadetBlue1":             RGB(0x98, 0xF5, 0xFF),
    "CadetBlue2":             RGB(0x8E, 0xE5, 0xEE),
    "CadetBlue3":             RGB(0x7A, 0xC5, 0xCD),
    "CadetBlue4":             RGB(0x53, 0x86, 0x8B),
    "chartreuse":             RGB(0x7F, 0xFF, 0x00),
    "chartreuse1":            RGB(0x7F, 0xFF, 0x00),
    "chartreuse2":            RGB(0x76, 0xEE, 0x00),
    "chartreuse3":            RGB(0x66, 0xCD, 0x00),
    "chartreuse4":            RGB(0x45, 0x8B, 0x00),
    "chocolate":              RGB(0xD2, 0x69, 0x1E),
    "chocolate1":             RGB(0xFF, 0x7F, 0x24),
    "chocolate2":             RGB(0xEE, 0x76, 0x21),
    "chocolate3":             RGB(0xCD, 0x66, 0x1D),
    "chocolate4":             RGB(0x8B, 0x45, 0x13),
    "coral":                  RGB(0xFF, 0x7F, 0x50),
    "coral1":                 RGB(0xFF, 0x72, 0x56),
    "coral2":                 RGB(0xEE, 0x6A, 0x50),
    "coral3":                 RGB(0xCD, 0x5B, 0x45),
    "coral4":                 RGB(0x8B, 0x3E, 0x2F),
    "cornflower blue":        RGB(0x64, 0x95, 0xED),
    "CornflowerBlue":         RGB(0x64, 0x95, 0xED),
    "cornsilk":               RGB(0xFF, 0xF8, 0xDC),
    "cornsilk1":              RGB(0xFF, 0xF8, 0xDC),
    "cornsilk2":              RGB(0xEE, 0xE8, 0xCD),
    "cornsilk3":              RGB(0xCD, 0xC8, 0xB1),
    "cornsilk4":              RGB(0x8B, 0x88, 0x78),
    "cyan":                   RGB(0x00, 0xFF, 0xFF),
    "cyan1":                  RGB(0x00, 0xFF, 0xFF),
    "cyan2":                  RGB(0x00, 0xEE, 0xEE),
    "cyan3":                  RGB(0x00, 0xCD, 0xCD),
    "cyan4":                  RGB(0x00, 0x8B, 0x8B),
    "dark goldenrod":         RGB(0xB8, 0x86, 0x0B),
    "dark green":             RGB(0x00, 0x64, 0x00),
    "dark khaki":             RGB(0xBD, 0xB7, 0x6B),
    "dark olive green":       RGB(0x55, 0x6B, 0x2F),
    "dark orange":            RGB(0xFF, 0x8C, 0x00),
    "dark orchid":            RGB(0x99, 0x32, 0xCC),
    "dark salmon":            RGB(0xE9, 0x96, 0x7A),
    "dark sea green":         RGB(0x8F, 0xBC, 0x8F),
    "dark slate blue":        RGB(0x48, 0x3D, 0x8B),
    "dark slate gray":        RGB(0x2F, 0x4F, 0x4F),
    "dark slate grey":        RGB(0x2F, 0x4F, 0x4F),
    "dark turquoise":         RGB(0x00, 0xCE, 0xD1),
    "dark violet":            RGB(0x94, 0x00, 0xD3),
    "DarkGoldenrod":          RGB(0xB8, 0x86, 0x0B),
    "DarkGoldenrod1":         RGB(0xFF, 0xB9, 0x0F),
    "DarkGoldenrod2":         RGB(0xEE, 0xAD, 0x0E),
    "DarkGoldenrod3":         RGB(0xCD, 0x95, 0x0C),
    "DarkGoldenrod4":         RGB(0x8B, 0x65, 0x08),
    "DarkGreen":              RGB(0x00, 0x64, 0x00),
    "DarkKhaki":              RGB(0xBD, 0xB7, 0x6B),
    "DarkOliveGreen":         RGB(0x55, 0x6B, 0x2F),
    "DarkOliveGreen1":        RGB(0xCA, 0xFF, 0x70),
    "DarkOliveGreen2":        RGB(0xBC, 0xEE, 0x68),
    "DarkOliveGreen3":        RGB(0xA2, 0xCD, 0x5A),
    "DarkOliveGreen4":        RGB(0x6E, 0x8B, 0x3D),
    "DarkOrange":             RGB(0xFF, 0x8C, 0x00),
    "DarkOrange1":            RGB(0xFF, 0x7F, 0x00),
    "DarkOrange2":            RGB(0xEE, 0x76, 0x00),
    "DarkOrange3":            RGB(0xCD, 0x66, 0x00),
    "DarkOrange4":            RGB(0x8B, 0x45, 0x00),
    "DarkOrchid":             RGB(0x99, 0x32, 0xCC),
    "DarkOrchid1":            RGB(0xBF, 0x3E, 0xFF),
    "DarkOrchid2":            RGB(0xB2, 0x3A, 0xEE),
    "DarkOrchid3":            RGB(0x9A, 0x32, 0xCD),
    "DarkOrchid4":            RGB(0x68, 0x22, 0x8B),
    "DarkSalmon":             RGB(0xE9, 0x96, 0x7A),
    "DarkSeaGreen":           RGB(0x8F, 0xBC, 0x8F),
    "DarkSeaGreen1":          RGB(0xC1, 0xFF, 0xC1),
    "DarkSeaGreen2":          RGB(0xB4, 0xEE, 0xB4),
    "DarkSeaGreen3":          RGB(0x9B, 0xCD, 0x9B),
    "DarkSeaGreen4":          RGB(0x69, 0x8B, 0x69),
    "DarkSlateBlue":          RGB(0x48, 0x3D, 0x8B),
    "DarkSlateGray":          RGB(0x2F, 0x4F, 0x4F),
    "DarkSlateGray1":         RGB(0x97, 0xFF, 0xFF),
    "DarkSlateGray2":         RGB(0x8D, 0xEE, 0xEE),
    "DarkSlateGray3":         RGB(0x79, 0xCD, 0xCD),
    "DarkSlateGray4":         RGB(0x52, 0x8B, 0x8B),
    "DarkSlateGrey":          RGB(0x2F, 0x4F, 0x4F),
    "DarkTurquoise":          RGB(0x00, 0xCE, 0xD1),
    "DarkViolet":             RGB(0x94, 0x00, 0xD3),
    "deep pink":              RGB(0xFF, 0x14, 0x93),
    "deep sky blue":          RGB(0x00, 0xBF, 0xFF),
    "DeepPink":               RGB(0xFF, 0x14, 0x93),
    "DeepPink1":              RGB(0xFF, 0x14, 0x93),
    "DeepPink2":              RGB(0xEE, 0x12, 0x89),
    "DeepPink3":              RGB(0xCD, 0x10, 0x76),
    "DeepPink4":              RGB(0x8B, 0x0A, 0x50),
    "DeepSkyBlue":            RGB(0x00, 0xBF, 0xFF),
    "DeepSkyBlue1":           RGB(0x00, 0xBF, 0xFF),
    "DeepSkyBlue2":           RGB(0x00, 0xB2, 0xEE),
    "DeepSkyBlue3":           RGB(0x00, 0x9A, 0xCD),
    "DeepSkyBlue4":           RGB(0x00, 0x68, 0x8B),
    "dim gray":               RGB(0x69, 0x69, 0x69),
    "dim grey":               RGB(0x69, 0x69, 0x69),
    "DimGray":                RGB(0x69, 0x69, 0x69),
    "DimGrey":                RGB(0x69, 0x69, 0x69),
    "dodger blue":            RGB(0x1E, 0x90, 0xFF),
    "DodgerBlue":             RGB(0x1E, 0x90, 0xFF),
    "DodgerBlue1":            RGB(0x1E, 0x90, 0xFF),
    "DodgerBlue2":            RGB(0x1C, 0x86, 0xEE),
    "DodgerBlue3":            RGB(0x18, 0x74, 0xCD),
    "DodgerBlue4":            RGB(0x10, 0x4E, 0x8B),
    "firebrick":              RGB(0xB2, 0x22, 0x22),
    "firebrick1":             RGB(0xFF, 0x30, 0x30),
    "firebrick2":             RGB(0xEE, 0x2C, 0x2C),
    "firebrick3":             RGB(0xCD, 0x26, 0x26),
    "firebrick4":             RGB(0x8B, 0x1A, 0x1A),
    "floral white":           RGB(0xFF, 0xFA, 0xF0),
    "FloralWhite":            RGB(0xFF, 0xFA, 0xF0),
    "forest green":           RGB(0x22, 0x8B, 0x22),
    "ForestGreen":            RGB(0x22, 0x8B, 0x22),
    "gainsboro":              RGB(0xDC, 0xDC, 0xDC),
    "ghost white":            RGB(0xF8, 0xF8, 0xFF),
    "GhostWhite":             RGB(0xF8, 0xF8, 0xFF),
    "gold":                   RGB(0xFF, 0xD7, 0x00),
    "gold1":                  RGB(0xFF, 0xD7, 0x00),
    "gold2":                  RGB(0xEE, 0xC9, 0x00),
    "gold3":                  RGB(0xCD, 0xAD, 0x00),
    "gold4":                  RGB(0x8B, 0x75, 0x00),
    "goldenrod":              RGB(0xDA, 0xA5, 0x20),
    "goldenrod1":             RGB(0xFF, 0xC1, 0x25),
    "goldenrod2":             RGB(0xEE, 0xB4, 0x22),
    "goldenrod3":             RGB(0xCD, 0x9B, 0x1D),
    "goldenrod4":             RGB(0x8B, 0x69, 0x14),
    "gray":                   RGB(0xBE, 0xBE, 0xBE),
    "gray0":                  RGB(0x00, 0x00, 0x01),
    "gray1":                  RGB(0x03, 0x03, 0x03),
    "gray10":                 RGB(0x1A, 0x1A, 0x1A),
    "gray100":                RGB(0xFF, 0xFF, 0xFF),
    "gray11":                 RGB(0x1C, 0x1C, 0x1C),
    "gray12":                 RGB(0x1F, 0x1F, 0x1F),
    "gray13":                 RGB(0x21, 0x21, 0x21),
    "gray14":                 RGB(0x24, 0x24, 0x24),
    "gray15":                 RGB(0x26, 0x26, 0x26),
    "gray16":                 RGB(0x29, 0x29, 0x29),
    "gray17":                 RGB(0x2B, 0x2B, 0x2B),
    "gray18":                 RGB(0x2E, 0x2E, 0x2E),
    "gray19":                 RGB(0x30, 0x30, 0x30),
    "gray2":                  RGB(0x05, 0x05, 0x05),
    "gray20":                 RGB(0x33, 0x33, 0x33),
    "gray21":                 RGB(0x36, 0x36, 0x36),
    "gray22":                 RGB(0x38, 0x38, 0x38),
    "gray23":                 RGB(0x3B, 0x3B, 0x3B),
    "gray24":                 RGB(0x3D, 0x3D, 0x3D),
    "gray25":                 RGB(0x40, 0x40, 0x40),
    "gray26":                 RGB(0x42, 0x42, 0x42),
    "gray27":                 RGB(0x45, 0x45, 0x45),
    "gray28":                 RGB(0x47, 0x47, 0x47),
    "gray29":                 RGB(0x4A, 0x4A, 0x4A),
    "gray3":                  RGB(0x08, 0x08, 0x08),
    "gray30":                 RGB(0x4D, 0x4D, 0x4D),
    "gray31":                 RGB(0x4F, 0x4F, 0x4F),
    "gray32":                 RGB(0x52, 0x52, 0x52),
    "gray33":                 RGB(0x54, 0x54, 0x54),
    "gray34":                 RGB(0x57, 0x57, 0x57),
    "gray35":                 RGB(0x59, 0x59, 0x59),
    "gray36":                 RGB(0x5C, 0x5C, 0x5C),
    "gray37":                 RGB(0x5E, 0x5E, 0x5E),
    "gray38":                 RGB(0x61, 0x61, 0x61),
    "gray39":                 RGB(0x63, 0x63, 0x63),
    "gray4":                  RGB(0x0A, 0x0A, 0x0A),
    "gray40":                 RGB(0x66, 0x66, 0x66),
    "gray41":                 RGB(0x69, 0x69, 0x69),
    "gray42":                 RGB(0x6B, 0x6B, 0x6B),
    "gray43":                 RGB(0x6E, 0x6E, 0x6E),
    "gray44":                 RGB(0x70, 0x70, 0x70),
    "gray45":                 RGB(0x73, 0x73, 0x73),
    "gray46":                 RGB(0x75, 0x75, 0x75),
    "gray47":                 RGB(0x78, 0x78, 0x78),
    "gray48":                 RGB(0x7A, 0x7A, 0x7A),
    "gray49":                 RGB(0x7D, 0x7D, 0x7D),
    "gray5":                  RGB(0x0D, 0x0D, 0x0D),
    "gray50":                 RGB(0x7F, 0x7F, 0x7F),
    "gray51":                 RGB(0x82, 0x82, 0x82),
    "gray52":                 RGB(0x85, 0x85, 0x85),
    "gray53":                 RGB(0x87, 0x87, 0x87),
    "gray54":                 RGB(0x8A, 0x8A, 0x8A),
    "gray55":                 RGB(0x8C, 0x8C, 0x8C),
    "gray56":                 RGB(0x8F, 0x8F, 0x8F),
    "gray57":                 RGB(0x91, 0x91, 0x91),
    "gray58":                 RGB(0x94, 0x94, 0x94),
    "gray59":                 RGB(0x96, 0x96, 0x96),
    "gray6":                  RGB(0x0F, 0x0F, 0x0F),
    "gray60":                 RGB(0x99, 0x99, 0x99),
    "gray61":                 RGB(0x9C, 0x9C, 0x9C),
    "gray62":                 RGB(0x9E, 0x9E, 0x9E),
    "gray63":                 RGB(0xA1, 0xA1, 0xA1),
    "gray64":                 RGB(0xA3, 0xA3, 0xA3),
    "gray65":                 RGB(0xA6, 0xA6, 0xA6),
    "gray66":                 RGB(0xA8, 0xA8, 0xA8),
    "gray67":                 RGB(0xAB, 0xAB, 0xAB),
    "gray68":                 RGB(0xAD, 0xAD, 0xAD),
    "gray69":                 RGB(0xB0, 0xB0, 0xB0),
    "gray7":                  RGB(0x12, 0x12, 0x12),
    "gray70":                 RGB(0xB3, 0xB3, 0xB3),
    "gray71":                 RGB(0xB5, 0xB5, 0xB5),
    "gray72":                 RGB(0xB8, 0xB8, 0xB8),
    "gray73":                 RGB(0xBA, 0xBA, 0xBA),
    "gray74":                 RGB(0xBD, 0xBD, 0xBD),
    "gray75":                 RGB(0xBF, 0xBF, 0xBF),
    "gray76":                 RGB(0xC2, 0xC2, 0xC2),
    "gray77":                 RGB(0xC4, 0xC4, 0xC4),
    "gray78":                 RGB(0xC7, 0xC7, 0xC7),
    "gray79":                 RGB(0xC9, 0xC9, 0xC9),
    "gray8":                  RGB(0x14, 0x14, 0x14),
    "gray80":                 RGB(0xCC, 0xCC, 0xCC),
    "gray81":                 RGB(0xCF, 0xCF, 0xCF),
    "gray82":                 RGB(0xD1, 0xD1, 0xD1),
    "gray83":                 RGB(0xD4, 0xD4, 0xD4),
    "gray84":                 RGB(0xD6, 0xD6, 0xD6),
    "gray85":                 RGB(0xD9, 0xD9, 0xD9),
    "gray86":                 RGB(0xDB, 0xDB, 0xDB),
    "gray87":                 RGB(0xDE, 0xDE, 0xDE),
    "gray88":                 RGB(0xE0, 0xE0, 0xE0),
    "gray89":                 RGB(0xE3, 0xE3, 0xE3),
    "gray9":                  RGB(0x17, 0x17, 0x17),
    "gray90":                 RGB(0xE5, 0xE5, 0xE5),
    "gray91":                 RGB(0xE8, 0xE8, 0xE8),
    "gray92":                 RGB(0xEB, 0xEB, 0xEB),
    "gray93":                 RGB(0xED, 0xED, 0xED),
    "gray94":                 RGB(0xF0, 0xF0, 0xF0),
    "gray95":                 RGB(0xF2, 0xF2, 0xF2),
    "gray96":                 RGB(0xF5, 0xF5, 0xF5),
    "gray97":                 RGB(0xF7, 0xF7, 0xF7),
    "gray98":                 RGB(0xFA, 0xFA, 0xFA),
    "gray99":                 RGB(0xFC, 0xFC, 0xFC),
    "green":                  RGB(0x00, 0xFF, 0x00),
    "green yellow":           RGB(0xAD, 0xFF, 0x2F),
    "green1":                 RGB(0x00, 0xFF, 0x00),
    "green2":                 RGB(0x00, 0xEE, 0x00),
    "green3":                 RGB(0x00, 0xCD, 0x00),
    "green4":                 RGB(0x00, 0x8B, 0x00),
    "GreenYellow":            RGB(0xAD, 0xFF, 0x2F),
    "grey":                   RGB(0xBE, 0xBE, 0xBE),
    "grey0":                  RGB(0x00, 0x00, 0x01),
    "grey1":                  RGB(0x03, 0x03, 0x03),
    "grey10":                 RGB(0x1A, 0x1A, 0x1A),
    "grey100":                RGB(0xFF, 0xFF, 0xFF),
    "grey11":                 RGB(0x1C, 0x1C, 0x1C),
    "grey12":                 RGB(0x1F, 0x1F, 0x1F),
    "grey13":                 RGB(0x21, 0x21, 0x21),
    "grey14":                 RGB(0x24, 0x24, 0x24),
    "grey15":                 RGB(0x26, 0x26, 0x26),
    "grey16":                 RGB(0x29, 0x29, 0x29),
    "grey17":                 RGB(0x2B, 0x2B, 0x2B),
    "grey18":                 RGB(0x2E, 0x2E, 0x2E),
    "grey19":                 RGB(0x30, 0x30, 0x30),
    "grey2":                  RGB(0x05, 0x05, 0x05),
    "grey20":                 RGB(0x33, 0x33, 0x33),
    "grey21":                 RGB(0x36, 0x36, 0x36),
    "grey22":                 RGB(0x38, 0x38, 0x38),
    "grey23":                 RGB(0x3B, 0x3B, 0x3B),
    "grey24":                 RGB(0x3D, 0x3D, 0x3D),
    "grey25":                 RGB(0x40, 0x40, 0x40),
    "grey26":                 RGB(0x42, 0x42, 0x42),
    "grey27":                 RGB(0x45, 0x45, 0x45),
    "grey28":                 RGB(0x47, 0x47, 0x47),
    "grey29":                 RGB(0x4A, 0x4A, 0x4A),
    "grey3":                  RGB(0x08, 0x08, 0x08),
    "grey30":                 RGB(0x4D, 0x4D, 0x4D),
    "grey31":                 RGB(0x4F, 0x4F, 0x4F),
    "grey32":                 RGB(0x52, 0x52, 0x52),
    "grey33":                 RGB(0x54, 0x54, 0x54),
    "grey34":                 RGB(0x57, 0x57, 0x57),
    "grey35":                 RGB(0x59, 0x59, 0x59),
    "grey36":                 RGB(0x5C, 0x5C, 0x5C),
    "grey37":                 RGB(0x5E, 0x5E, 0x5E),
    "grey38":                 RGB(0x61, 0x61, 0x61),
    "grey39":                 RGB(0x63, 0x63, 0x63),
    "grey4":                  RGB(0x0A, 0x0A, 0x0A),
    "grey40":                 RGB(0x66, 0x66, 0x66),
    "grey41":                 RGB(0x69, 0x69, 0x69),
    "grey42":                 RGB(0x6B, 0x6B, 0x6B),
    "grey43":                 RGB(0x6E, 0x6E, 0x6E),
    "grey44":                 RGB(0x70, 0x70, 0x70),
    "grey45":                 RGB(0x73, 0x73, 0x73),
    "grey46":                 RGB(0x75, 0x75, 0x75),
    "grey47":                 RGB(0x78, 0x78, 0x78),
    "grey48":                 RGB(0x7A, 0x7A, 0x7A),
    "grey49":                 RGB(0x7D, 0x7D, 0x7D),
    "grey5":                  RGB(0x0D, 0x0D, 0x0D),
    "grey50":                 RGB(0x7F, 0x7F, 0x7F),
    "grey51":                 RGB(0x82, 0x82, 0x82),
    "grey52":                 RGB(0x85, 0x85, 0x85),
    "grey53":                 RGB(0x87, 0x87, 0x87),
    "grey54":                 RGB(0x8A, 0x8A, 0x8A),
    "grey55":                 RGB(0x8C, 0x8C, 0x8C),
    "grey56":                 RGB(0x8F, 0x8F, 0x8F),
    "grey57":                 RGB(0x91, 0x91, 0x91),
    "grey58":                 RGB(0x94, 0x94, 0x94),
    "grey59":                 RGB(0x96, 0x96, 0x96),
    "grey6":                  RGB(0x0F, 0x0F, 0x0F),
    "grey60":                 RGB(0x99, 0x99, 0x99),
    "grey61":                 RGB(0x9C, 0x9C, 0x9C),
    "grey62":                 RGB(0x9E, 0x9E, 0x9E),
    "grey63":                 RGB(0xA1, 0xA1, 0xA1),
    "grey64":                 RGB(0xA3, 0xA3, 0xA3),
    "grey65":                 RGB(0xA6, 0xA6, 0xA6),
    "grey66":                 RGB(0xA8, 0xA8, 0xA8),
    "grey67":                 RGB(0xAB, 0xAB, 0xAB),
    "grey68":                 RGB(0xAD, 0xAD, 0xAD),
    "grey69":                 RGB(0xB0, 0xB0, 0xB0),
    "grey7":                  RGB(0x12, 0x12, 0x12),
    "grey70":                 RGB(0xB3, 0xB3, 0xB3),
    "grey71":                 RGB(0xB5, 0xB5, 0xB5),
    "grey72":                 RGB(0xB8, 0xB8, 0xB8),
    "grey73":                 RGB(0xBA, 0xBA, 0xBA),
    "grey74":                 RGB(0xBD, 0xBD, 0xBD),
    "grey75":                 RGB(0xBF, 0xBF, 0xBF),
    "grey76":                 RGB(0xC2, 0xC2, 0xC2),
    "grey77":                 RGB(0xC4, 0xC4, 0xC4),
    "grey78":                 RGB(0xC7, 0xC7, 0xC7),
    "grey79":                 RGB(0xC9, 0xC9, 0xC9),
    "grey8":                  RGB(0x14, 0x14, 0x14),
    "grey80":                 RGB(0xCC, 0xCC, 0xCC),
    "grey81":                 RGB(0xCF, 0xCF, 0xCF),
    "grey82":                 RGB(0xD1, 0xD1, 0xD1),
    "grey83":                 RGB(0xD4, 0xD4, 0xD4),
    "grey84":                 RGB(0xD6, 0xD6, 0xD6),
    "grey85":                 RGB(0xD9, 0xD9, 0xD9),
    "grey86":                 RGB(0xDB, 0xDB, 0xDB),
    "grey87":                 RGB(0xDE, 0xDE, 0xDE),
    "grey88":                 RGB(0xE0, 0xE0, 0xE0),
    "grey89":                 RGB(0xE3, 0xE3, 0xE3),
    "grey9":                  RGB(0x17, 0x17, 0x17),
    "grey90":                 RGB(0xE5, 0xE5, 0xE5),
    "grey91":                 RGB(0xE8, 0xE8, 0xE8),
    "grey92":                 RGB(0xEB, 0xEB, 0xEB),
    "grey93":                 RGB(0xED, 0xED, 0xED),
    "grey94":                 RGB(0xF0, 0xF0, 0xF0),
    "grey95":                 RGB(0xF2, 0xF2, 0xF2),
    "grey96":                 RGB(0xF5, 0xF5, 0xF5),
    "grey97":                 RGB(0xF7, 0xF7, 0xF7),
    "grey98":                 RGB(0xFA, 0xFA, 0xFA),
    "grey99":                 RGB(0xFC, 0xFC, 0xFC),
    "honeydew":               RGB(0xF0, 0xFF, 0xF0),
    "honeydew1":              RGB(0xF0, 0xFF, 0xF0),
    "honeydew2":              RGB(0xE0, 0xEE, 0xE0),
    "honeydew3":              RGB(0xC1, 0xCD, 0xC1),
    "honeydew4":              RGB(0x83, 0x8B, 0x83),
    "hot pink":               RGB(0xFF, 0x69, 0xB4),
    "HotPink":                RGB(0xFF, 0x69, 0xB4),
    "HotPink1":               RGB(0xFF, 0x6E, 0xB4),
    "HotPink2":               RGB(0xEE, 0x6A, 0xA7),
    "HotPink3":               RGB(0xCD, 0x60, 0x90),
    "HotPink4":               RGB(0x8B, 0x3A, 0x62),
    "indian red":             RGB(0xCD, 0x5C, 0x5C),
    "IndianRed":              RGB(0xCD, 0x5C, 0x5C),
    "IndianRed1":             RGB(0xFF, 0x6A, 0x6A),
    "IndianRed2":             RGB(0xEE, 0x63, 0x63),
    "IndianRed3":             RGB(0xCD, 0x55, 0x55),
    "IndianRed4":             RGB(0x8B, 0x3A, 0x3A),
    "ivory":                  RGB(0xFF, 0xFF, 0xF0),
    "ivory1":                 RGB(0xFF, 0xFF, 0xF0),
    "ivory2":                 RGB(0xEE, 0xEE, 0xE0),
    "ivory3":                 RGB(0xCD, 0xCD, 0xC1),
    "ivory4":                 RGB(0x8B, 0x8B, 0x83),
    "khaki":                  RGB(0xF0, 0xE6, 0x8C),
    "khaki1":                 RGB(0xFF, 0xF6, 0x8F),
    "khaki2":                 RGB(0xEE, 0xE6, 0x85),
    "khaki3":                 RGB(0xCD, 0xC6, 0x73),
    "khaki4":                 RGB(0x8B, 0x86, 0x4E),
    "lavender":               RGB(0xE6, 0xE6, 0xFA),
    "lavender blush":         RGB(0xFF, 0xF0, 0xF5),
    "LavenderBlush":          RGB(0xFF, 0xF0, 0xF5),
    "LavenderBlush1":         RGB(0xFF, 0xF0, 0xF5),
    "LavenderBlush2":         RGB(0xEE, 0xE0, 0xE5),
    "LavenderBlush3":         RGB(0xCD, 0xC1, 0xC5),
    "LavenderBlush4":         RGB(0x8B, 0x83, 0x86),
    "lawn green":             RGB(0x7C, 0xFC, 0x00),
    "LawnGreen":              RGB(0x7C, 0xFC, 0x00),
    "lemon chiffon":          RGB(0xFF, 0xFA, 0xCD),
    "LemonChiffon":           RGB(0xFF, 0xFA, 0xCD),
    "LemonChiffon1":          RGB(0xFF, 0xFA, 0xCD),
    "LemonChiffon2":          RGB(0xEE, 0xE9, 0xBF),
    "LemonChiffon3":          RGB(0xCD, 0xC9, 0xA5),
    "LemonChiffon4":          RGB(0x8B, 0x89, 0x70),
    "light blue":             RGB(0xAD, 0xD8, 0xE6),
    "light coral":            RGB(0xF0, 0x80, 0x80),
    "light cyan":             RGB(0xE0, 0xFF, 0xFF),
    "light goldenrod":        RGB(0xEE, 0xDD, 0x82),
    "light goldenrod yellow": RGB(0xFA, 0xFA, 0xD2),
    "light gray":             RGB(0xD3, 0xD3, 0xD3),
    "light grey":             RGB(0xD3, 0xD3, 0xD3),
    "light pink":             RGB(0xFF, 0xB6, 0xC1),
    "light salmon":           RGB(0xFF, 0xA0, 0x7A),
    "light sea green":        RGB(0x20, 0xB2, 0xAA),
    "light sky blue":         RGB(0x87, 0xCE, 0xFA),
    "light slate blue":       RGB(0x84, 0x70, 0xFF),
    "light slate gray":       RGB(0x77, 0x88, 0x99),
    "light slate grey":       RGB(0x77, 0x88, 0x99),
    "light steel blue":       RGB(0xB0, 0xC4, 0xDE),
    "light yellow":           RGB(0xFF, 0xFF, 0xE0),
    "LightBlue":              RGB(0xAD, 0xD8, 0xE6),
    "LightBlue1":             RGB(0xBF, 0xEF, 0xFF),
    "LightBlue2":             RGB(0xB2, 0xDF, 0xEE),
    "LightBlue3":             RGB(0x9A, 0xC0, 0xCD),
    "LightBlue4":             RGB(0x68, 0x83, 0x8B),
    "LightCoral":             RGB(0xF0, 0x80, 0x80),
    "LightCyan":              RGB(0xE0, 0xFF, 0xFF),
    "LightCyan1":             RGB(0xE0, 0xFF, 0xFF),
    "LightCyan2":             RGB(0xD1, 0xEE, 0xEE),
    "LightCyan3":             RGB(0xB4, 0xCD, 0xCD),
    "LightCyan4":             RGB(0x7A, 0x8B, 0x8B),
    "LightGoldenrod":         RGB(0xEE, 0xDD, 0x82),
    "LightGoldenrod1":        RGB(0xFF, 0xEC, 0x8B),
    "LightGoldenrod2":        RGB(0xEE, 0xDC, 0x82),
    "LightGoldenrod3":        RGB(0xCD, 0xBE, 0x70),
    "LightGoldenrod4":        RGB(0x8B, 0x81, 0x4C),
    "LightGoldenrodYellow":   RGB(0xFA, 0xFA, 0xD2),
    "LightGray":              RGB(0xD3, 0xD3, 0xD3),
    "LightGrey":              RGB(0xD3, 0xD3, 0xD3),
    "LightPink":              RGB(0xFF, 0xB6, 0xC1),
    "LightPink1":             RGB(0xFF, 0xAE, 0xB9),
    "LightPink2":             RGB(0xEE, 0xA2, 0xAD),
    "LightPink3":             RGB(0xCD, 0x8C, 0x95),
    "LightPink4":             RGB(0x8B, 0x5F, 0x65),
    "LightSalmon":            RGB(0xFF, 0xA0, 0x7A),
    "LightSalmon1":           RGB(0xFF, 0xA0, 0x7A),
    "LightSalmon2":           RGB(0xEE, 0x95, 0x72),
    "LightSalmon3":           RGB(0xCD, 0x81, 0x62),
    "LightSalmon4":           RGB(0x8B, 0x57, 0x42),
    "LightSeaGreen":          RGB(0x20, 0xB2, 0xAA),
    "LightSkyBlue":           RGB(0x87, 0xCE, 0xFA),
    "LightSkyBlue1":          RGB(0xB0, 0xE2, 0xFF),
    "LightSkyBlue2":          RGB(0xA4, 0xD3, 0xEE),
    "LightSkyBlue3":          RGB(0x8D, 0xB6, 0xCD),
    "LightSkyBlue4":          RGB(0x60, 0x7B, 0x8B),
    "LightSlateBlue":         RGB(0x84, 0x70, 0xFF),
    "LightSlateGray":         RGB(0x77, 0x88, 0x99),
    "LightSlateGrey":         RGB(0x77, 0x88, 0x99),
    "LightSteelBlue":         RGB(0xB0, 0xC4, 0xDE),
    "LightSteelBlue1":        RGB(0xCA, 0xE1, 0xFF),
    "LightSteelBlue2":        RGB(0xBC, 0xD2, 0xEE),
    "LightSteelBlue3":        RGB(0xA2, 0xB5, 0xCD),
    "LightSteelBlue4":        RGB(0x6E, 0x7B, 0x8B),
    "LightYellow":            RGB(0xFF, 0xFF, 0xE0),
    "LightYellow1":           RGB(0xFF, 0xFF, 0xE0),
    "LightYellow2":           RGB(0xEE, 0xEE, 0xD1),
    "LightYellow3":           RGB(0xCD, 0xCD, 0xB4),
    "LightYellow4":           RGB(0x8B, 0x8B, 0x7A),
    "lime green":             RGB(0x32, 0xCD, 0x32),
    "LimeGreen":              RGB(0x32, 0xCD, 0x32),
    "linen":                  RGB(0xFA, 0xF0, 0xE6),
    "magenta":                RGB(0xFF, 0x00, 0xFF),
    "magenta1":               RGB(0xFF, 0x00, 0xFF),
    "magenta2":               RGB(0xEE, 0x00, 0xEE),
    "magenta3":               RGB(0xCD, 0x00, 0xCD),
    "magenta4":               RGB(0x8B, 0x00, 0x8B),
    "maroon":                 RGB(0xB0, 0x30, 0x60),
    "maroon1":                RGB(0xFF, 0x34, 0xB3),
    "maroon2":                RGB(0xEE, 0x30, 0xA7),
    "maroon3":                RGB(0xCD, 0x29, 0x90),
    "maroon4":                RGB(0x8B, 0x1C, 0x62),
    "medium aquamarine":      RGB(0x66, 0xCD, 0xAA),
    "medium blue":            RGB(0x00, 0x00, 0xCD),
    "medium orchid":          RGB(0xBA, 0x55, 0xD3),
    "medium purple":          RGB(0x93, 0x70, 0xDB),
    "medium sea green":       RGB(0x3C, 0xB3, 0x71),
    "medium slate blue":      RGB(0x7B, 0x68, 0xEE),
    "medium spring green":    RGB(0x00, 0xFA, 0x9A),
    "medium turquoise":       RGB(0x48, 0xD1, 0xCC),
    "medium violet red":      RGB(0xC7, 0x15, 0x85),
    "MediumAquamarine":       RGB(0x66, 0xCD, 0xAA),
    "MediumBlue":             RGB(0x00, 0x00, 0xCD),
    "MediumOrchid":           RGB(0xBA, 0x55, 0xD3),
    "MediumOrchid1":          RGB(0xE0, 0x66, 0xFF),
    "MediumOrchid2":          RGB(0xD1, 0x5F, 0xEE),
    "MediumOrchid3":          RGB(0xB4, 0x52, 0xCD),
    "MediumOrchid4":          RGB(0x7A, 0x37, 0x8B),
    "MediumPurple":           RGB(0x93, 0x70, 0xDB),
    "MediumPurple1":          RGB(0xAB, 0x82, 0xFF),
    "MediumPurple2":          RGB(0x9F, 0x79, 0xEE),
    "MediumPurple3":          RGB(0x89, 0x68, 0xCD),
    "MediumPurple4":          RGB(0x5D, 0x47, 0x8B),
    "MediumSeaGreen":         RGB(0x3C, 0xB3, 0x71),
    "MediumSlateBlue":        RGB(0x7B, 0x68, 0xEE),
    "MediumSpringGreen":      RGB(0x00, 0xFA, 0x9A),
    "MediumTurquoise":        RGB(0x48, 0xD1, 0xCC),
    "MediumVioletRed":        RGB(0xC7, 0x15, 0x85),
    "midnight blue":          RGB(0x19, 0x19, 0x70),
    "MidnightBlue":           RGB(0x19, 0x19, 0x70),
    "mint cream":             RGB(0xF5, 0xFF, 0xFA),
    "MintCream":              RGB(0xF5, 0xFF, 0xFA),
    "misty rose":             RGB(0xFF, 0xE4, 0xE1),
    "MistyRose":              RGB(0xFF, 0xE4, 0xE1),
    "MistyRose1":             RGB(0xFF, 0xE4, 0xE1),
    "MistyRose2":             RGB(0xEE, 0xD5, 0xD2),
    "MistyRose3":             RGB(0xCD, 0xB7, 0xB5),
    "MistyRose4":             RGB(0x8B, 0x7D, 0x7B),
    "moccasin":               RGB(0xFF, 0xE4, 0xB5),
    "navajo white":           RGB(0xFF, 0xDE, 0xAD),
    "NavajoWhite":            RGB(0xFF, 0xDE, 0xAD),
    "NavajoWhite1":           RGB(0xFF, 0xDE, 0xAD),
    "NavajoWhite2":           RGB(0xEE, 0xCF, 0xA1),
    "NavajoWhite3":           RGB(0xCD, 0xB3, 0x8B),
    "NavajoWhite4":           RGB(0x8B, 0x79, 0x5E),
    "navy":                   RGB(0x00, 0x00, 0x80),
    "navy blue":              RGB(0x00, 0x00, 0x80),
    "NavyBlue":               RGB(0x00, 0x00, 0x80),
    "old lace":               RGB(0xFD, 0xF5, 0xE6),
    "OldLace":                RGB(0xFD, 0xF5, 0xE6),
    "olive drab":             RGB(0x6B, 0x8E, 0x23),
    "OliveDrab":              RGB(0x6B, 0x8E, 0x23),
    "OliveDrab1":             RGB(0xC0, 0xFF, 0x3E),
    "OliveDrab2":             RGB(0xB3, 0xEE, 0x3A),
    "OliveDrab3":             RGB(0x9A, 0xCD, 0x32),
    "OliveDrab4":             RGB(0x69, 0x8B, 0x22),
    "orange":                 RGB(0xFF, 0xA5, 0x00),
    "orange red":             RGB(0xFF, 0x45, 0x00),
    "orange1":                RGB(0xFF, 0xA5, 0x00),
    "orange2":                RGB(0xEE, 0x9A, 0x00),
    "orange3":                RGB(0xCD, 0x85, 0x00),
    "orange4":                RGB(0x8B, 0x5A, 0x00),
    "OrangeRed":              RGB(0xFF, 0x45, 0x00),
    "OrangeRed1":             RGB(0xFF, 0x45, 0x00),
    "OrangeRed2":             RGB(0xEE, 0x40, 0x00),
    "OrangeRed3":             RGB(0xCD, 0x37, 0x00),
    "OrangeRed4":             RGB(0x8B, 0x25, 0x00),
    "orchid":                 RGB(0xDA, 0x70, 0xD6),
    "orchid1":                RGB(0xFF, 0x83, 0xFA),
    "orchid2":                RGB(0xEE, 0x7A, 0xE9),
    "orchid3":                RGB(0xCD, 0x69, 0xC9),
    "orchid4":                RGB(0x8B, 0x47, 0x89),
    "pale goldenrod":         RGB(0xEE, 0xE8, 0xAA),
    "pale green":             RGB(0x98, 0xFB, 0x98),
    "pale turquoise":         RGB(0xAF, 0xEE, 0xEE),
    "pale violet red":        RGB(0xDB, 0x70, 0x93),
    "PaleGoldenrod":          RGB(0xEE, 0xE8, 0xAA),
    "PaleGreen":              RGB(0x98, 0xFB, 0x98),
    "PaleGreen1":             RGB(0x9A, 0xFF, 0x9A),
    "PaleGreen2":             RGB(0x90, 0xEE, 0x90),
    "PaleGreen3":             RGB(0x7C, 0xCD, 0x7C),
    "PaleGreen4":             RGB(0x54, 0x8B, 0x54),
    "PaleTurquoise":          RGB(0xAF, 0xEE, 0xEE),
    "PaleTurquoise1":         RGB(0xBB, 0xFF, 0xFF),
    "PaleTurquoise2":         RGB(0xAE, 0xEE, 0xEE),
    "PaleTurquoise3":         RGB(0x96, 0xCD, 0xCD),
    "PaleTurquoise4":         RGB(0x66, 0x8B, 0x8B),
    "PaleVioletRed":          RGB(0xDB, 0x70, 0x93),
    "PaleVioletRed1":         RGB(0xFF, 0x82, 0xAB),
    "PaleVioletRed2":         RGB(0xEE, 0x79, 0x9F),
    "PaleVioletRed3":         RGB(0xCD, 0x68, 0x89),
    "PaleVioletRed4":         RGB(0x8B, 0x47, 0x5D),
    "papaya whip":            RGB(0xFF, 0xEF, 0xD5),
    "PapayaWhip":             RGB(0xFF, 0xEF, 0xD5),
    "peach puff":             RGB(0xFF, 0xDA, 0xB9),
    "PeachPuff":              RGB(0xFF, 0xDA, 0xB9),
    "PeachPuff1":             RGB(0xFF, 0xDA, 0xB9),
    "PeachPuff2":             RGB(0xEE, 0xCB, 0xAD),
    "PeachPuff3":             RGB(0xCD, 0xAF, 0x95),
    "PeachPuff4":             RGB(0x8B, 0x77, 0x65),
    "peru":                   RGB(0xCD, 0x85, 0x3F),
    "pink":                   RGB(0xFF, 0xC0, 0xCB),
    "pink1":                  RGB(0xFF, 0xB5, 0xC5),
    "pink2":                  RGB(0xEE, 0xA9, 0xB8),
    "pink3":                  RGB(0xCD, 0x91, 0x9E),
    "pink4":                  RGB(0x8B, 0x63, 0x6C),
    "plum":                   RGB(0xDD, 0xA0, 0xDD),
    "plum1":                  RGB(0xFF, 0xBB, 0xFF),
    "plum2":                  RGB(0xEE, 0xAE, 0xEE),
    "plum3":                  RGB(0xCD, 0x96, 0xCD),
    "plum4":                  RGB(0x8B, 0x66, 0x8B),
    "powder blue":            RGB(0xB0, 0xE0, 0xE6),
    "PowderBlue":             RGB(0xB0, 0xE0, 0xE6),
    "purple":                 RGB(0xA0, 0x20, 0xF0),
    "purple1":                RGB(0x9B, 0x30, 0xFF),
    "purple2":                RGB(0x91, 0x2C, 0xEE),
    "purple3":                RGB(0x7D, 0x26, 0xCD),
    "purple4":                RGB(0x55, 0x1A, 0x8B),
    "red":                    RGB(0xFF, 0x00, 0x00),
    "red1":                   RGB(0xFF, 0x00, 0x00),
    "red2":                   RGB(0xEE, 0x00, 0x00),
    "red3":                   RGB(0xCD, 0x00, 0x00),
    "red4":                   RGB(0x8B, 0x00, 0x00),
    "rosy brown":             RGB(0xBC, 0x8F, 0x8F),
    "RosyBrown":              RGB(0xBC, 0x8F, 0x8F),
    "RosyBrown1":             RGB(0xFF, 0xC1, 0xC1),
    "RosyBrown2":             RGB(0xEE, 0xB4, 0xB4),
    "RosyBrown3":             RGB(0xCD, 0x9B, 0x9B),
    "RosyBrown4":             RGB(0x8B, 0x69, 0x69),
    "royal blue":             RGB(0x41, 0x69, 0xE1),
    "RoyalBlue":              RGB(0x41, 0x69, 0xE1),
    "RoyalBlue1":             RGB(0x48, 0x76, 0xFF),
    "RoyalBlue2":             RGB(0x43, 0x6E, 0xEE),
    "RoyalBlue3":             RGB(0x3A, 0x5F, 0xCD),
    "RoyalBlue4":             RGB(0x27, 0x40, 0x8B),
    "saddle brown":           RGB(0x8B, 0x45, 0x13),
    "SaddleBrown":            RGB(0x8B, 0x45, 0x13),
    "salmon":                 RGB(0xFA, 0x80, 0x72),
    "salmon1":                RGB(0xFF, 0x8C, 0x69),
    "salmon2":                RGB(0xEE, 0x82, 0x62),
    "salmon3":                RGB(0xCD, 0x70, 0x54),
    "salmon4":                RGB(0x8B, 0x4C, 0x39),
    "sandy brown":            RGB(0xF4, 0xA4, 0x60),
    "SandyBrown":             RGB(0xF4, 0xA4, 0x60),
    "sea green":              RGB(0x2E, 0x8B, 0x57),
    "SeaGreen":               RGB(0x2E, 0x8B, 0x57),
    "SeaGreen1":              RGB(0x54, 0xFF, 0x9F),
    "SeaGreen2":              RGB(0x4E, 0xEE, 0x94),
    "SeaGreen3":              RGB(0x43, 0xCD, 0x80),
    "SeaGreen4":              RGB(0x2E, 0x8B, 0x57),
    "seashell":               RGB(0xFF, 0xF5, 0xEE),
    "seashell1":              RGB(0xFF, 0xF5, 0xEE),
    "seashell2":              RGB(0xEE, 0xE5, 0xDE),
    "seashell3":              RGB(0xCD, 0xC5, 0xBF),
    "seashell4":              RGB(0x8B, 0x86, 0x82),
    "sienna":                 RGB(0xA0, 0x52, 0x2D),
    "sienna1":                RGB(0xFF, 0x82, 0x47),
    "sienna2":                RGB(0xEE, 0x79, 0x42),
    "sienna3":                RGB(0xCD, 0x68, 0x39),
    "sienna4":                RGB(0x8B, 0x47, 0x26),
    "sky blue":               RGB(0x87, 0xCE, 0xEB),
    "SkyBlue":                RGB(0x87, 0xCE, 0xEB),
    "SkyBlue1":               RGB(0x87, 0xCE, 0xFF),
    "SkyBlue2":               RGB(0x7E, 0xC0, 0xEE),
    "SkyBlue3":               RGB(0x6C, 0xA6, 0xCD),
    "SkyBlue4":               RGB(0x4A, 0x70, 0x8B),
    "slate blue":             RGB(0x6A, 0x5A, 0xCD),
    "slate gray":             RGB(0x70, 0x80, 0x90),
    "slate grey":             RGB(0x70, 0x80, 0x90),
    "SlateBlue":              RGB(0x6A, 0x5A, 0xCD),
    "SlateBlue1":             RGB(0x83, 0x6F, 0xFF),
    "SlateBlue2":             RGB(0x7A, 0x67, 0xEE),
    "SlateBlue3":             RGB(0x69, 0x59, 0xCD),
    "SlateBlue4":             RGB(0x47, 0x3C, 0x8B),
    "SlateGray":              RGB(0x70, 0x80, 0x90),
    "SlateGray1":             RGB(0xC6, 0xE2, 0xFF),
    "SlateGray2":             RGB(0xB9, 0xD3, 0xEE),
    "SlateGray3":             RGB(0x9F, 0xB6, 0xCD),
    "SlateGray4":             RGB(0x6C, 0x7B, 0x8B),
    "SlateGrey":              RGB(0x70, 0x80, 0x90),
    "snow":                   RGB(0xFF, 0xFA, 0xFA),
    "snow1":                  RGB(0xFF, 0xFA, 0xFA),
    "snow2":                  RGB(0xEE, 0xE9, 0xE9),
    "snow3":                  RGB(0xCD, 0xC9, 0xC9),
    "snow4":                  RGB(0x8B, 0x89, 0x89),
    "spring green":           RGB(0x00, 0xFF, 0x7F),
    "SpringGreen":            RGB(0x00, 0xFF, 0x7F),
    "SpringGreen1":           RGB(0x00, 0xFF, 0x7F),
    "SpringGreen2":           RGB(0x00, 0xEE, 0x76),
    "SpringGreen3":           RGB(0x00, 0xCD, 0x66),
    "SpringGreen4":           RGB(0x00, 0x8B, 0x45),
    "steel blue":             RGB(0x46, 0x82, 0xB4),
    "SteelBlue":              RGB(0x46, 0x82, 0xB4),
    "SteelBlue1":             RGB(0x63, 0xB8, 0xFF),
    "SteelBlue2":             RGB(0x5C, 0xAC, 0xEE),
    "SteelBlue3":             RGB(0x4F, 0x94, 0xCD),
    "SteelBlue4":             RGB(0x36, 0x64, 0x8B),
    "tan":                    RGB(0xD2, 0xB4, 0x8C),
    "tan1":                   RGB(0xFF, 0xA5, 0x4F),
    "tan2":                   RGB(0xEE, 0x9A, 0x49),
    "tan3":                   RGB(0xCD, 0x85, 0x3F),
    "tan4":                   RGB(0x8B, 0x5A, 0x2B),
    "thistle":                RGB(0xD8, 0xBF, 0xD8),
    "thistle1":               RGB(0xFF, 0xE1, 0xFF),
    "thistle2":               RGB(0xEE, 0xD2, 0xEE),
    "thistle3":               RGB(0xCD, 0xB5, 0xCD),
    "thistle4":               RGB(0x8B, 0x7B, 0x8B),
    "tomato":                 RGB(0xFF, 0x63, 0x47),
    "tomato1":                RGB(0xFF, 0x63, 0x47),
    "tomato2":                RGB(0xEE, 0x5C, 0x42),
    "tomato3":                RGB(0xCD, 0x4F, 0x39),
    "tomato4":                RGB(0x8B, 0x36, 0x26),
    "turquoise":              RGB(0x40, 0xE0, 0xD0),
    "turquoise1":             RGB(0x00, 0xF5, 0xFF),
    "turquoise2":             RGB(0x00, 0xE5, 0xEE),
    "turquoise3":             RGB(0x00, 0xC5, 0xCD),
    "turquoise4":             RGB(0x00, 0x86, 0x8B),
    "violet":                 RGB(0xEE, 0x82, 0xEE),
    "violet red":             RGB(0xD0, 0x20, 0x90),
    "VioletRed":              RGB(0xD0, 0x20, 0x90),
    "VioletRed1":             RGB(0xFF, 0x3E, 0x96),
    "VioletRed2":             RGB(0xEE, 0x3A, 0x8C),
    "VioletRed3":             RGB(0xCD, 0x32, 0x78),
    "VioletRed4":             RGB(0x8B, 0x22, 0x52),
    "wheat":                  RGB(0xF5, 0xDE, 0xB3),
    "wheat1":                 RGB(0xFF, 0xE7, 0xBA),
    "wheat2":                 RGB(0xEE, 0xD8, 0xAE),
    "wheat3":                 RGB(0xCD, 0xBA, 0x96),
    "wheat4":                 RGB(0x8B, 0x7E, 0x66),
    "white":                  RGB(0xFF, 0xFF, 0xFF),
    "white smoke":            RGB(0xF5, 0xF5, 0xF5),
    "WhiteSmoke":             RGB(0xF5, 0xF5, 0xF5),
    "yellow":                 RGB(0xFF, 0xFF, 0x00),
    "yellow green":           RGB(0x9A, 0xCD, 0x32),
    "yellow1":                RGB(0xFF, 0xFF, 0x00),
    "yellow2":                RGB(0xEE, 0xEE, 0x00),
    "yellow3":                RGB(0xCD, 0xCD, 0x00),
    "yellow4":                RGB(0x8B, 0x8B, 0x00),
    "YellowGreen":            RGB(0x9A, 0xCD, 0x32),
}


html_template = '''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html lang="ja">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<meta http-equiv="Content-Style-Type" content="text/css">
<title>ckw colortest</title>
<style type="text/css">
<!-- /**/
  body { color: ${foreground}; background-color: ${background}; }
  table, td, th { border: solid 1px ${foreground}; }
  col { width: 150px; }
  .fg { font-family: monospace; }
  .f00 { color: ${foreground}; }
  .f01 { color: ${background}; }
  .f02 { color: ${cursorColor}; }
  .f03 { color: ${cursorImeColor}; }
  .f04 { color: ${color0}; }
  .f05 { color: ${color1}; }
  .f06 { color: ${color2}; }
  .f07 { color: ${color3}; }
  .f08 { color: ${color4}; }
  .f09 { color: ${color5}; }
  .f10 { color: ${color6}; }
  .f11 { color: ${color7}; }
  .f12 { color: ${color8}; }
  .f13 { color: ${color9}; }
  .f14 { color: ${color10}; }
  .f15 { color: ${color11}; }
  .f16 { color: ${color12}; }
  .f17 { color: ${color13}; }
  .f18 { color: ${color14}; }
  .f19 { color: ${color15}; }

  .b00 { background-color: ${foreground}; }
  .b01 { background-color: ${background}; }
  .b02 { background-color: ${cursorColor}; }
  .b03 { background-color: ${cursorImeColor}; }
  .b04 { background-color: ${color0}; }
  .b05 { background-color: ${color1}; }
  .b06 { background-color: ${color2}; }
  .b07 { background-color: ${color3}; }
  .b08 { background-color: ${color4}; }
  .b09 { background-color: ${color5}; }
  .b10 { background-color: ${color6}; }
  .b11 { background-color: ${color7}; }
  .b12 { background-color: ${color8}; }
  .b13 { background-color: ${color9}; }
  .b14 { background-color: ${color10}; }
  .b15 { background-color: ${color11}; }
  .b16 { background-color: ${color12}; }
  .b17 { background-color: ${color13}; }
  .b18 { background-color: ${color14}; }
  .b19 { background-color: ${color15}; }
/**/ -->
</style>
</head>
<body>
  <p>${config}</p>
  <table>
    <col><col><col>
    <tbody>
    <tr><td>Ckw*foreground</td><td class="f00 fg">${foreground}</td><td class="b00"></td></tr>
    <tr><td>Ckw*background</td><td class="f01 fg">${background}</td><td class="b01"></td></tr>
    <tr><td>Ckw*cursorColor</td><td class="f02 fg">${cursorColor}</td><td class="b02"></td></tr>
    <tr><td>Ckw*cursorImeColor</td><td class="f03 fg">${cursorImeColor}</td><td class="b03"></td></tr>

    <tr><td>Ckw*color0</td><td class="f04 fg">${color0}</td><td class="b04"></td></tr>
    <tr><td>Ckw*color1</td><td class="f05 fg">${color1}</td><td class="b05"></td></tr>
    <tr><td>Ckw*color2</td><td class="f06 fg">${color2}</td><td class="b06"></td></tr>
    <tr><td>Ckw*color3</td><td class="f07 fg">${color3}</td><td class="b07"></td></tr>
    <tr><td>Ckw*color4</td><td class="f08 fg">${color4}</td><td class="b08"></td></tr>
    <tr><td>Ckw*color5</td><td class="f09 fg">${color5}</td><td class="b09"></td></tr>
    <tr><td>Ckw*color6</td><td class="f10 fg">${color6}</td><td class="b10"></td></tr>
    <tr><td>Ckw*color7</td><td class="f11 fg">${color7}</td><td class="b11"></td></tr>

    <tr><td>Ckw*color8</td> <td class="f12 fg">${color8}</td> <td class="b12"></td></tr>
    <tr><td>Ckw*color9</td> <td class="f13 fg">${color9}</td> <td class="b13"></td></tr>
    <tr><td>Ckw*color10</td><td class="f14 fg">${color10}</td><td class="b14"></td></tr>
    <tr><td>Ckw*color11</td><td class="f15 fg">${color11}</td><td class="b15"></td></tr>
    <tr><td>Ckw*color12</td><td class="f16 fg">${color12}</td><td class="b16"></td></tr>
    <tr><td>Ckw*color13</td><td class="f17 fg">${color13}</td><td class="b17"></td></tr>
    <tr><td>Ckw*color14</td><td class="f18 fg">${color14}</td><td class="b18"></td></tr>
    <tr><td>Ckw*color15</td><td class="f19 fg">${color15}</td><td class="b19"></td></tr>
    </tbody>
  </table>
</body>
</html>
'''


def read_config(filename):
    colors = dict(default_colors)
    if os.path.exists(filename) and os.path.isfile(filename):
        with open(filename, "r") as f:
            for line in f.readlines():
                line = line.strip()
                if line.startswith("!") or len(line) == 0:
                    pass
                else:
                    k, v = line.split(":", 1)
                    k = k.strip()
                    v = v.strip()
                    if k in colors:
                        colors[k] = v

    return colors


def update_named_colors():
    for k, v in named_colors.items():
        named_colors[k.upper()] = v


def make_params(config="ckw.cfg", colors=default_colors):
    update_named_colors()

    params = {"config": config}
    for k, v in colors.items():
        key = k[4:] if k.startswith("Ckw*") else k
        val = named_colors[v.upper()] if v.upper() in named_colors else v
        if val.startswith("#"):
            val = val.upper()

        params[key] = val

    return params


def template_substitute(template, params):
    for k, v in params.items():
        params[k] = escape(v)

    return template.substitute(params)


def write_html(filename='colors.html', params={}):
    with open(filename, "w") as f:
        t = Template(html_template)
        f.write(template_substitute(t, params))


def main():
    cfg = sys.argv[1] if len(sys.argv) > 1 else "ckw.cfg"
    if len(sys.argv) > 2:
        f = sys.argv[2]
    else:
        t = os.path.split(cfg)
        f = os.path.join(t[0],
                         t[1].lstrip(".").replace(".", "-") + "-colors.html")

    colors = read_config(cfg)
    params = make_params(cfg, colors)
    write_html(f, params)


if __name__ == '__main__':
    main()
