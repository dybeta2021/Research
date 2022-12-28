#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project  : Date20221228 指数成分股重叠和相关性 
# @File     : task.py 
# @Author   : Gavin
# @Time     : 2022/12/28 19:26
# @Desc     :

import re
from os import getcwd, sep

from pandas import read_excel


def get_weight_from_zz(index_symbol: str):
    """
    中证指数

    :param index_symbol:
    :return:
    """
    weight = getcwd() + sep + r"data" + sep + r"{}closeweight.xls".format(index_symbol)
    weight = read_excel(io=weight, dtype=str)
    weight.columns = [''.join(re.findall(re.compile(u'[\u4e00-\u9fa5]'), i)) for i in weight.columns]
    weight["权重"] = weight["权重"].astype(float)
    weight.sort_values("权重", inplace=True, ascending=False)
    weight = weight.set_index("成分券代码")
    weight.index.name = "symbol"
    return weight


def get_weight_from_gz(file_name: str):
    """
    国证指数
    :param file_name:
    :return:
    """
    weight = getcwd() + sep + r"data" + sep + r"{}.xls".format(file_name)
    weight = read_excel(io=weight, dtype=str)
    weight.columns = [''.join(re.findall(re.compile(u'[\u4e00-\u9fa5]'), i)) for i in weight.columns]
    weight["权重"] = weight["权重"].astype(float)
    weight.sort_values("权重", inplace=True, ascending=False)
    weight = weight.set_index("样本代码")
    weight.index.name = "symbol"
    return weight
