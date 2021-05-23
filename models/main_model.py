from models.base_model import BaseModel
from flask import render_template, request, flash, redirect, session, url_for, jsonify
from werkzeug.security import check_password_hash


class MainModel(BaseModel):
  def login(self):
    """ログイン画面表示"""
    return render_template('main/login.html')

  def login_check(self):
    email = request.form['email']
    password = request.form['password']

    with self.start_transaction() as tx:
      sql = """
            SELECT
              password
            FROM
              admin_user
            WHERE
              email=%s
            """
      password_result = tx.find_one(sql, [email])

    if password_result is None:
      """メールアドレスが登録されていない場合"""
      flash("アドレスが登録されていません。")
      return redirect('main_route.login')

    if password_result['password'] != password:
      """パスワードが違う場合"""
      flash("パスワードが間違っています")
      return redirect('main_route.login')
    return redirect(url_for('main_route.top_page'))

  def top_page(self):
    return render_template('main/top_page.html')