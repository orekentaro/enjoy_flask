from flask import session, request, redirect, url_for, flash

# LOGIN不要ページリスト
NOT_REQUIRED_LOGIN = [
  'main_route.login',  # ログイン
  'main_route.login_check',  # ログイン処理
  'static',  # 画像、PDFを閲覧
  'system_route.user_add',  # ユーザー仮登録
  'system_route.user_add_complete',  # ユーザー仮登録処理
  'system_route.user_new_add_complete',  # ユーザー新規登録処理
  'system_route.forgot_password',  # パスワードを忘れた際
  'system_route.forgot_password_send'  # パスワードを忘れた際の再設定メール
]


def before_request():
  """ requestの前処理

  Returns:
      Response | None: ログインしていない状態での画面遷移は行えないようにする
  """
  if request.endpoint not in NOT_REQUIRED_LOGIN and 'login_user' not in session:
    flash("ログイン有効期限切れです。", "alert-danger")
    return redirect(url_for('main_route.login'))
