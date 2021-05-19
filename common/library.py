"""共通で使用する処理のlibrary

時間のフォーマットや料金のフォーマットなど
各ページで同じ表記をする為のメソッドを作成
"""

from flask import session
import datetime
from models.base_model import BaseModel
from werkzeug.security import check_password_hash
import re


def date_format(hiduke):
  """日付のフォーマット（%Y/%m/%d %H:%M or %Y/%m/%d）
    Args:
      hiduke(datetime.date か datetime.datetime型):主にnow()やtoday()で持ってきた時間か、ＤＢ内の時間に使用
    Returns:
      True:
        datetime.date(2021, 3, 10) => 例 2021/03/10
        datetime.datetime(2021, 3, 10, 20, 17, 46, 726575) => 例 2021/03/10 20:17
      False:
        型が上記の2つ以外のものだったらexceptでエラーを出す。
    Examples:
      引数にdatetime.date か datetime.datetime型を入れるだけでフォーマット完了
  """
  try:
    if type(hiduke) is datetime.datetime:
      return hiduke.strftime("%Y/%m/%d %H:%M")
    elif type(hiduke) is datetime.date:
      return hiduke.strftime("%Y/%m/%d")
    elif hiduke is None:
      return None
  except Exception:
    raise Exception("日付の形式が正しくありません")


def date_format_j(hiduke):
  """時間のフォーマット（%Y年%m月%d日）
    Args:
      hiduke(datetime.datetime型):開始時間等日付が含まれるが時間のみ必要な場合
    Returns:
      True:
        datetime.date(2021, 3, 10) => 例) 2021月03月10日
        datetime.datetime(2021, 3, 10, 20, 17, 46, 726575) => 例) 2021月03月10日
      False:
        型が上記の2つ以外のものだったらexceptでエラーを出す。
    Examples:
      引数にdatetime.date か datetime.datetime型を入れるだけでフォーマット完了
  """
  return hiduke.strftime("%Y年%m月%d日")


def date_format_j2(hiduke):
  """時間のフォーマット（%m月%d日）
    Args:
      hiduke(datetime.datetime型):開始時間等日付が含まれるが時間のみ必要な場合
    Returns:
      True:
        datetime.date(2021, 3, 10) => 例) 03月10日
        datetime.datetime(2021, 3, 10, 20, 17, 46, 726575) => 例) 03月10日
      False:
        型が上記の2つ以外のものだったらexceptでエラーを出す。
    Examples:
      引数にdatetime.date か datetime.datetime型を入れるだけでフォーマット完了
  """
  return hiduke.strftime("%m月%d日")


def date_format2(hiduke):
  """時間のフォーマット（%m/%d/）
    Args:
      hiduke(datetime.datetime型):開始時間等日付が含まれるが時間のみ必要な場合
    Returns:
      True:
        datetime.date(2021, 3, 10) => 例) 03/10
        datetime.datetime(2021, 3, 10, 20, 17, 46, 726575) => 例) 03/10
      False:
        型が上記の2つ以外のものだったらexceptでエラーを出す。
    Examples:
      引数にdatetime.date か datetime.datetime型を入れるだけでフォーマット完了
  """
  return hiduke.strftime("%m/%d")


def time_format(hiduke):
  """時間のフォーマット（%H:%M）
    Args:
      hiduke(datetime.datetime型):開始時間等日付が含まれるが時間のみ必要な場合
    Returns:
      True:
        datetime.datetime(2021, 3, 10, 20, 17, 46, 726575) => 例) 20:17
      False:
        datetime.datetime型を引数に指定しないとexceptでエラーを出す。
    Examples:
      引数にdatetime.datetime型を入れるだけでフォーマット完了
  """
  try:
    return hiduke.strftime("%H:%M")
  except Exception:
    raise Exception("日付の形式が正しくありません")


def str_date(hiduke):
  """日付を年からスラッシュで区切り、時間はhh:㎜表記に"""
  return datetime.datetime.strptime(hiduke, '%Y/%m/%d %H:%M')


def str_day(hiduke):
  """年月日をスラッシュで区切る"""
  hiduke = datetime.datetime.strptime(hiduke, '%Y/%m/%d')
  return datetime.date(hiduke.year, hiduke.month, hiduke.day)


def nendo_format(hiduke):
  """西暦の数字を年度表記する"""
  hiduke = hiduke.strftime("%Y年度")
  return hiduke


def amount_format(amount):
  """料金のフォーマット。カンマと円をつける"""
  if amount is None:
    amount = 0

  if not type(amount) == int:
    raise Exception("金額のフォーマットが正しくありません。")

  amount = "{:,}".format(amount) + "円"
  return amount


def seikyu_amount_format(amount):
  """料金のフォーマット。カンマで￥表記"""
  if amount is None:
    amount = 0

  if not type(amount) == int:
    raise Exception("金額のフォーマットが正しくありません。")

  amount = '￥' + "{:,}".format(amount)
  return amount


def number_of_people(count):
  """人数に単位をつける"""
  if not count:
    count = 0
  return f'{count}人'


def action_of_histrory(action):
  """行動履歴を残すためのメソッド
    Args:
      action(str型):それぞれのメソッドの行動内容を文字列で入力
    Returns:
      なし
    Examples:
      各メソッドのreturnの前にそのメソッドの目的毎の引数を入れて使用。
      ただし、セッションを使用する為ログイン失敗等には使用できない。
  """
  with BaseModel().start_transaction(False) as tx:
    sql = "SELECT nextval('history_id_seq') as history_id"
    history_id = tx.find_one(sql)["history_id"]

    sql = """
            INSERT INTO
              action_history(
                history_id,
                college_id,
                action,
                created_id,
                updated_id,
                created_at,
                updated_at,
                deleted
              )
              VALUES(
                %s,%s,%s,%s,%s,%s,%s,%s
              )
            """
    insert_history_index = [
      history_id,
      session['college_id'],
      action,
      session['user_id'],
      session['user_id'],
      datetime.datetime.now(),
      datetime.datetime.now(),
      '0'
    ]
    tx.save(sql, insert_history_index)


def password_histrory(mail, password):
  """パスワードの履歴を残すためのメソッド
    Args:
      mail(str型):フォームで受け取ったmailの値
      password(str型):フォームで受け取ったpasswordの値(ハッシュ化する事)
    Returns:
      なし
    Examples:
      セッションでIDを使用する為、必ずsession['user_id']が定義された後に使用する事。
  """
  with BaseModel().start_transaction(False) as tx:
    sql = "SELECT nextval('password_history_seq') as history_id"
    history_id = tx.find_one(sql)["history_id"]

    sql = """
            INSERT INTO
              password_history(
                history_id,
                email,
                password,
                created_id,
                updated_id,
                created_at,
                updated_at,
                deleted
              )
              VALUES(
                %s,%s,%s,%s,%s,%s,%s,%s
              )
            """
    insert_history_index = [
      history_id,
      mail,
      password,
      session['user_id'],
      session['user_id'],
      datetime.datetime.now(),
      datetime.datetime.now(),
      '0'
    ]
    tx.save(sql, insert_history_index)


def password_yet_check(mail, password):
  """パスワード変更時に、過去に使用したかどうか確認する為のメソッド
    Args:
      mail(str型):フォームで受け取ったmailの値
      password(str型):フォームで受け取ったpasswordの値(ハッシュ化する事)
    Returns:
      過去に使用したことがなければTrue、使用していればFalseを返す。
    Examples:
      セッションでIDを使用する為、必ずsession['user_id']が定義された後に使用する事。
  """
  with BaseModel().start_transaction(False) as tx:
    sql = "SELECT password FROM password_history WHERE email=%s"
    password_historys = tx.find_all(sql, [mail])

  check = True
  for history in password_historys:
    if check_password_hash(history['password'], password) is True:
      check = False
      break

  return check


def password_check(password):
  """パスワードの正規表現メソッド
    Args:
      password(str型):フォームで受け取ったpasswordの値(ハッシュ化する前)
    Returns:
      過去に使用したことがなければTrue、使用していればFalseを返す。
    Examples:
      セッションでIDを使用する為、必ずsession['user_id']が定義された後に使用する事。
  """
  if len(password) >= 8 and re.search('[A-Z]', password) and re.search('[a-z]', password) and re.search('[0-9]', password) and re.search(r'[!@#$%&?+*\/\[\]()-]', password):
    return True
  return False
