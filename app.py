#!/usr/bin/env python3
# -*- coding=utf-8 -*-
import tornado.web
from tornado.options import options, define
import tornado.options
import tornado.ioloop

from handlers import main

define('port', default=8000, help="listening port", type=int)


class App(tornado.web.Application):
    def __init__(self):
        handlers = [
            ('/', main.IndexHandler),
            ('/explore', main.ExploreHandler),
            ('/post/(?P<post_id>[0-9]+)', main.PostHandler)

        ]

        settings = dict(
            debug=True,
            template_path='templates'
        )

        super(App, self).__init__(handlers, **settings)


application = App()
if __name__ == "__main__":
    print('Starting Server......')
    tornado.options.parse_command_line()
    application.listen(options.port)
    print('Server  started')
    tornado.ioloop.IOLoop.current().start()



