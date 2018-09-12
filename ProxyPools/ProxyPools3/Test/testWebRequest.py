# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     testWebRequest
   Description :   test class WebRequest
   Author :        xcl
   date：          2018/7/31
-------------------------------------------------
   Change Activity:
                   2018/7/31: function testWebRequest
-------------------------------------------------
"""
__author__ = 'xcl'

from Util.WebRequest import WebRequest


# noinspection PyPep8Naming
def testWebRequest():
    """
    test class WebRequest in Util/WebRequest.py
    :return:
    """
    wr = WebRequest()
    request_object = wr.get('https://www.baidu.com/')
    assert request_object.status_code == 200


if __name__ == '__main__':
    testWebRequest()
