from os import supports_bytes_environ
from models.base_model import BaseModel
from flask import render_template, request, flash, redirect, session, url_for, jsonify
import datetime


class ProductModel(BaseModel):
  def product_list(self):
    with self.start_transaction() as tx:
      sql="""
        SELECT
          product_id,
          pr.name,
          cost_price,
          selling_price,
          su.name as supplier
        FROM
          product pr
        LEFT JOIN
          supplier as su
        ON
          pr.supplier_id = su.supplier_id
      """
      products = tx.find_all(sql)

    return render_template('product/product_list.html', products=products)

  def create_product(self):
    with self.start_transaction() as tx:
      sql="""
        SELECT
          supplier_id,
          name
        FROM
          supplier
      """
      suppliers = tx.find_all(sql)
    return render_template('product/product_edit.html', add=True, suppliers=suppliers)

  def create_product_complete(self):
    name = request.form['name']
    cost_price = request.form['cost_price']
    selling_price = request.form['selling_price']
    supplier_id = request.form['supplier']

    with BaseModel().start_transaction(False) as tx:
      sql = "SELECT nextval('product_seq') as product_seq"
      seq = tx.find_one(sql)["product_seq"]

      sql = """
            INSERT INTO
              product(
                product_id,
                name,
                cost_price,
                selling_price,
                supplier_id,
                status,
                created_id,
                updated_id,
                created_at,
                updated_at
              )
              VALUES(
                %s,%s,%s,%s,%s,%s,%s,%s,%s,%s
              )
            """
      insert_index = [
        seq,
        name,
        cost_price,
        selling_price,
        supplier_id,
        '0',
        session['user_id'],
        session['user_id'],
        datetime.datetime.now(),
        datetime.datetime.now()
      ]
      tx.save(sql, insert_index)
    flash(f"登録が完了しました。", "alert-success")
    return redirect(url_for('product_route.product_list'))