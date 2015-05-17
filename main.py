#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route("/",methods=['GET' , 'POST'])
def main():

    if request.method == 'POST':
        p_time2=request.form['date']

        proc = subprocess.Popen(["echo '0616' | sudo -S date --set '%s' " % p_time2, ""], stdout=subprocess.PIPE, shell=True)
        proc.communicate()

    ip = request.remote_addr

    proc = subprocess.Popen(['date','+ %Y/%m/%d-%H:%M'], stdout=subprocess.PIPE)
    (time1, err) = proc.communicate()

    proc = subprocess.Popen(['./get_data','-u'], stdout=subprocess.PIPE)
    (user, err) = proc.communicate()

    proc = subprocess.Popen(['./get_data','-p'], stdout=subprocess.PIPE)
    (pw, err) = proc.communicate()

    proc = subprocess.Popen(['./get_data','-l'], stdout=subprocess.PIPE)
    (des_ip, err) = proc.communicate()

    proc = subprocess.Popen(['arp'], stdout=subprocess.PIPE)
    (message, err) = proc.communicate()
    message=message.split("\n")

    templateData = {
        'ip': ip,
        'time1': time1,
        'user': user,
        'pw' : pw,
        'message': message,
        'des_ip': des_ip
    }

    return render_template('index.html',**templateData)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
