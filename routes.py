from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User, Zhihu_hot, Weibo_hot

from spider.zhihu_spider import fetch_zhihu_hot
from spider.weibo_spider import fetch_weibo_hot


# 定义蓝图
main_bp = Blueprint("main", __name__)


@main_bp.route("/")
@login_required
def index():
    # 检查并获取知乎数据
    zhihu_data = Zhihu_hot.query.all()
    if not zhihu_data:
        fetch_zhihu_hot()
        zhihu_data = Zhihu_hot.query.all()

    # 微博
    weibo_data = Weibo_hot.query.all()
    if not weibo_data:
        fetch_weibo_hot()
        weibo_data = Weibo_hot.query.all()
    
    return render_template("index.html", zhihu=zhihu_data[:10], weibo=weibo_data[:10])


@main_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = User.query.filter_by(username=username).first()

        print("用户名：", username)
        print("密码：", password)
        print("查到的用户：", user)
        if user:
            print("数据库密码哈希：", user.password)

        if user and check_password_hash(user.password, password):
            print("检查开始")
            login_user(user)
            return redirect(url_for("main.index"))
        flash("用户名或密码错误")
    return render_template("login.html")


@main_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        print("收到注册请求")
        username = request.form.get("username")
        password = generate_password_hash(request.form.get("password"))
        print("用户名：", username)
        print("密码：", password)
        print(f"查找的用户对象: {User.query.filter_by(username=username).first()}")
        if User.query.filter_by(username=username).first():
            flash("用户名已存在")
        else:
            print("开始注册")
            new_user = User(username=username, password=password)
            db.session.add(new_user)
            db.session.commit()
            flash("注册成功，请登录")
            return redirect(url_for("main.login"))
    return render_template("register.html")


@main_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.login"))


@main_bp.route("/refresh_zhihu")
@login_required
def refresh_zhihu():
    """手动刷新知乎热点数据"""
    try:
        fetch_zhihu_hot()
        flash("知乎热点数据已更新")
    except Exception as e:
        flash(f"更新失败: {str(e)}")
    return redirect(url_for("main.index"))


