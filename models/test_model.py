from flask import render_template

class TestModel():
  def test(self):
    return render_template('test/test.html', name1="山田", name2="村上", name3="上田")

  def number(self, name):
    return name