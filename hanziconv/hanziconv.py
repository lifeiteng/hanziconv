# -*- coding: utf-8 -*-
#
# Copyright 2014 Bernard Yue
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from __future__ import unicode_literals

__doc__ = """
Hanzi Converter 繁簡轉換器 | 繁简转换器

This module provides functions converting chinese text between simplified and
traditional characters.  It returns unicode represnetation of the text.

Class HanziConv is the main entry point of the module, you can import the
class by doing:

    >>> from hanziconv import HanziConv
"""

import os
from .charmap import simplified_charmap, traditional_charmap


class HanziConv(object):
    """This class supports hanzi (漢字) convention between simplified and
    traditional format"""
    __traditional_to_simplified_charmap = dict([(traditional_charmap[i], simplified_charmap[i]) for i in range(len(traditional_charmap))])
    __simplified_to_traditional_charmap = dict([(simplified_charmap[i], traditional_charmap[i]) for i in range(len(traditional_charmap))])


    @classmethod
    def __convert(cls, text, toTraditional=True):
        """Convert `text` to Traditional characters if `toTraditional` is
        True, else convert to simplified characters

        :param text:           data to convert
        :param toTraditional:  True -- convert to traditional text
                               False -- covert to simplified text
        :returns:              converted 'text`
        """
        if isinstance(text, bytes):
            text = text.decode('utf-8')

        charMap = cls.__simplified_to_traditional_charmap if toTraditional else cls.__traditional_to_simplified_charmap
        final = [charMap.get(c, c) for c in text]
        return ''.join(final)

    @classmethod
    def toSimplified(cls, text):
        """Convert `text` to simplified character string.  Assuming text is
        traditional character string

        :param text:  text to convert
        :returns:     converted UTF-8 characters

        >>> from hanziconv import HanziConv
        >>> print(HanziConv.toSimplified('繁簡轉換器'))
        繁简转换器
        """
        return cls.__convert(text, toTraditional=False)

    @classmethod
    def toTraditional(cls, text):
        """Convert `text` to traditional character string.  Assuming text is
        simplified character string

        :param text:  text to convert
        :returns:     converted UTF-8 characters

        >>> from hanziconv import HanziConv
        >>> print(HanziConv.toTraditional('繁简转换器'))
        繁簡轉換器
        """
        return cls.__convert(text, toTraditional=True)

    @classmethod
    def same(cls, text1, text2):
        """Return True if text1 and text2 meant literally the same, False
        otherwise

        :param text1: string to compare to ``text2``
        :param text2: string to compare to ``text1``
        :returns:     **True**  -- ``text1`` and ``text2`` are the same in meaning,
                      **False** -- otherwise

        >>> from hanziconv import HanziConv
        >>> print(HanziConv.same('繁简转换器', '繁簡轉換器'))
        True
        """
        t1 = cls.toSimplified(text1)
        t2 = cls.toSimplified(text2)
        return t1 == t2


del traditional_charmap, simplified_charmap
