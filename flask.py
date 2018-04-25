from flask import Flask
from flask import render_template
import numpy as np

app = Flask(__name__)
@app.route('/')
def inspiration_quote():
    with open("inspiration.txt",encoding="utf8") as txtfile:
      txt_list = txtfile.readlines() 
      para_order = np.random.randint(0, len(txt_list)) 
    para = txt_list[para_order].replace('\n','') 
    return render_template('inspiration_quote.html', quote = para)
