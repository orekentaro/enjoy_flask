from models.base_model import BaseModel
from flask import render_template, request, flash, redirect, session, url_for, jsonify


class CompanyModel(BaseModel):
  def clients_list(self):
    with self.start_transaction() as tx:
      sql = """
            SELECT
              clients_id,
              name,
              zip,
              address,
              phone,
              email
            FROM
              clients
            WHERE
              status='0'
            """
      companys = tx.find_all(sql)

      print(companys)
    return render_template('company/company_list.html', company='取引先', companys=companys)