from models.base_model import BaseModel
from flask import render_template, request, flash, redirect, session, url_for, jsonify
import datetime

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
    return render_template('company/company_list.html', company='取引先', companys=companys)


  def create_clients(self):
    return render_template('company/company_edit.html', clients=True)

  def create_clients_complete(self):
    name = request.form['name']
    zip = request.form['zip']
    address = request.form['address']
    phone = request.form['phone']
    email = request.form['email']
    with self.start_transaction(False) as tx:
      sql = "SELECT nextval('clients_seq') as clients_seq"
      clients_seq = tx.find_one(sql)["clients_seq"]

      sql = """
        INSERT INTO
          clients(
            clients_id,
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
        clients_seq,
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
    
    flash(f"{name}を登録しました", "alert-success")
    return redirect(url_for('company_route.clients_list'))