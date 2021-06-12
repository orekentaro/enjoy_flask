from models.base_model import BaseModel
from flask import render_template, request, flash, redirect, session, url_for, jsonify


class ProductModel(BaseModel):
  def product_list(self):
    with self.start_transaction() as tx:
      sql="""
        SELECT
          product_id,
          pr.name,
          cost_price,
          selling_price,
          su.name
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
    return render_template('product/product_edit.html', add=True)