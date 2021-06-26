from models.base_model import BaseModel
from flask import render_template, request, flash, redirect, session, url_for, jsonify
import datetime

class QuotationModel(BaseModel):
  def quotation_list(self):
    with BaseModel().start_transaction() as tx:
      sql = f"""
        SELECT
          quotation_id,
          clients_id,
          created_at
        FROM
          quotation
        WHERE
          status='0'
        """
      quotations = tx.find_all(sql)
    
    return render_template('quotation/quotation_list.html', quotations=quotations)