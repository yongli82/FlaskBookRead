#!/usr/bin/env python
# -*- coding:utf-8 -*-

import json
from flask import render_template, Blueprint, flash, redirect, url_for, abort, request, g
from werkzeug.contrib.atom import AtomFeed
from ..models.book import Book,BookChapter
from ..utils.permissions import AdminPermission, UserPermission

bp = Blueprint('book', __name__)


@bp.route('/books', defaults={'page': 1})
@bp.route('/books/page/<int:page>')
def books(page):
    book_list = Book.query.order_by(Book.created_at.desc()).paginate(page, 20)
    return render_template('book/books.html', book_list=book_list)

@bp.route('/book/<int:book_id>')
def book_view(book_id):
    book = Book.query.get_or_404(book_id)
    book_chapters = BookChapter.query.filter(BookChapter.book_id == book_id).order_by(BookChapter.id.asc())
    return render_template('book/book.html', book=book, book_chapters=book_chapters)

@bp.route('/chapter/<int:chapter_id>')
def chapter_view(chapter_id):
    book_chapter = BookChapter.query.get_or_404(chapter_id)
    return render_template('book/chapter.html', book_chapter=book_chapter)