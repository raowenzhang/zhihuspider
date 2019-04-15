# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html


class ZhihuMiddleware(object):

    def process_response(self, request, response, spider):
        if response.status in [408, 404]:
            return request

        return response
