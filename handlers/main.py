#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import tornado.web


class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('index.html')


class ExploreHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('explore.html')


class PostHandler(tornado.web.RequestHandler):
    def get(self, post_id):
        self.render('post.html', post_id=post_id)


class UploadHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('upload.html')

    def post(self, *args, **kwargs):
        # files={'newimg':[{'body':content','content-type':'abc','filename':'build1.txt'}], [{'body':content','content-type':'bcd','filename':'build2.txt'}]}
        img_files = self.request.files.get('newimg', None)
        for img in img_files:
            with open('./static/uploads/{}'.format(img['filename']), 'wb') as f:
                f.write(img['body'])
        self.write('upload Done.')
