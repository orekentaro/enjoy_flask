from models.base_model import BaseModel
from flask import request, session
import datetime

def company_list(company):
  """
    自社、取引先、仕入れ先の一覧を表示するmethod
    引数company(string)に”own_company”, ”clients”, ”supplier”
    のうちいずれか一つを入れる。
  """
  with BaseModel().start_transaction() as tx:
    sql = f"""
      SELECT
        {company}_id,
        name,
        zip,
        address,
        phone,
        email
      FROM
        {company}
      WHERE
        status='0'
      """
    companys = tx.find_all(sql)
    return companys



def company_insert(company):
  """
    自社、取引先、仕入れ先の追加をするmethod
    引数company(string)に”own_company”, ”clients”, ”supplier”
    のうちいずれか一つを入れる。
  """
  name = request.form['name']
  zip = request.form['zip']
  address = request.form['address']
  phone = request.form['phone']
  email = request.form['email']
  with BaseModel().start_transaction(False) as tx:
    sql = f"SELECT nextval('{company}_seq') as {company}_seq"
    seq = tx.find_one(sql)[f"{company}_seq"]
    sql = f"""
      INSERT INTO
        {company}(
          {company}_id,
          name,
          zip,
          address,
          phone,
          email,
          status,
          created_id,
          updated_id,
          created_at,
          updated_at
        )
        VALUES(
          %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s
        )
        """
    insert_index = [
      seq,
      name,
      zip,
      address,
      phone,
      email,
      '0',
      session['user_id'],
      session['user_id'],
      datetime.datetime.now(),
      datetime.datetime.now()
    ]

    tx.save(sql, insert_index)
