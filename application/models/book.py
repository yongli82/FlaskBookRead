#!/usr/bin/env python
# -*- coding:utf-8 -*-

from datetime import datetime

from ._base import db


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    author = db.Column(db.String(20))
    coverImage = db.Column(db.String(200), default='default.png')
    description = db.Column(db.Text())
    updated_at = db.Column(db.DateTime, default=datetime.now)
    created_at = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return '<Book %s>' % self.name


class BookChapter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    book = db.relationship('Book', backref=db.backref('book_chapters', lazy='dynamic',
                                                      order_by='desc(BookChapter.created_at)',
                                                      cascade="all, delete, delete-orphan"))
    name = db.Column(db.String(200))
    content = db.Column(db.Text())
    updated_at = db.Column(db.DateTime, default=datetime.now)
    created_at = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return '<BookChapter %s>' % self.name
