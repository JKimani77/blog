from . import main
from ..models import User, Articlez, Comment
from .forms import FormBlog, FormComment
from flask import render_template, request, redirect, url_for, abort, flash
from flask_login import login_required, current_user
from datetime import datetime, timezone
from .. import db


#landing page
@main.route('/')
def index():
    title = 'Home'
    postr = Articlez.get_posts()
    print(postr)
    return render_template('index.html', title=title, postr=postr)

#blogs page
@main.route('/post/<int:id>', methods=['GET', 'POST'])
def single_line(id):
    article = Articlez.query.get(id)
    title = "Blogz"
    comments = Comment.get_usercomments(id)

    return render_template('blog.html', article=article, title=title, comments=comments)


#create new blog page
@main.route('/new/blog', methods=['GET', 'POST'])
def new_blog():
    form = FormBlog()
    if form.validate_on_submit():
        title = form.title.data
        blog = form.articles.data
        new_blog = Articlez(title=title, blog=blog)
        new_blog.save_blog()
        return redirect(url_for('main.index'))
    return render_template('newpost.html', form=form)

#delete blog
@main.route('/delete/blog/<int:id>', methods=['GET', 'POST'])
def delete_blog(id):
    article = Articlez.query.filter_by(id=id).first()

    if article is None:
        abort(404)

    article.delete_blog()
    return redirect(url_for('main.index'))

#create comment, have to be logged in
@main.route('/post/comment/new/<int:id>', methods=['GET', 'POST'])
@login_required
def new_comment(id):
    post = Articlez.query.filter_by(id=id).first()

    if post is None:
        abort(404)

    form = FormComment()

    if form.validate_on_submit():
        opinion = form.opinion.data
        new_comment = Comment(
            opinion=opinion, articles_id=id, user_id=current_user.id)
        new_comment.save_usercomment()

        return redirect(url_for('main.index'))

    title = 'New Comment'
    return render_template('comment.html', title=title, comment_form=form)

#delete comment
@main.route('/delete/comment/<int:id>', methods=['GET', 'POST'])
def delete_selected_comment(id):
    comment = Comment.query.get(id)
    comment.del_comment(id)

    return redirect(url_for('main.index'))
