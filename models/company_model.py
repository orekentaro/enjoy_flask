from models.base_model import BaseModel
from flask import render_template, request, flash, redirect, session, url_for, jsonify
import datetime
from common.library import company_insert, company_list

class CompanyModel(BaseModel):
  def clients_list(self):
    companys = company_list('clients')
    return render_template('company/company_list.html', company='取引先', companys=companys, clients=True)


  def create_clients(self):
    return render_template('company/company_edit.html', clients=True)

  def create_clients_complete(self):
    name = ''
    company_insert('clients')
    
    flash(f"登録が完了しました。", "alert-success")
    return redirect(url_for('company_route.clients_list'))

  def supplier_list(self):
    companys = company_list('supplier')
    return render_template('company/company_list.html', company='仕入れ先', companys=companys, supplier=True)

  def create_supplier(self):
    return render_template('company/company_edit.html', supplier=True)

  def create_supplier_complete(self):
    name = ''
    company_insert('supplier')
    
    flash(f"登録が完了しました。", "alert-success")
    return redirect(url_for('company_route.supplier_list'))

  def own_company_list(self):
    companys = company_list('own_company')
    return render_template('company/company_list.html', company='自社', companys=companys, own_company=True)

  def create_own_company(self):
    return render_template('company/company_edit.html', own_company=True)

  def create_own_company_complete(self):
    name = ''
    company_insert('own_company')
    
    flash(f"登録が完了しました。", "alert-success")
    return redirect(url_for('company_route.own_company_list'))