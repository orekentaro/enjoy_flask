from models.base_model import BaseModel
from flask import render_template, request, flash, redirect, session, url_for, jsonify
from werkzeug.security import check_password_hash


class MainModel(BaseModel):
  def login(self):
    """ログイン画面表示"""
    return render_template('main/login.html')
