#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import subprocess
import os.path

app = Flask(__name__)

@app.route("/",methods=['GET' , 'POST'])
def main():

    if request.method == 'POST':
        t_ssid=request.form['t_ssid']
        t_pw=request.form['t_pw']
        t_pw_again=request.form['t_pw_again']

        save_path = './'
        completeName = os.path.join(save_path, "wifi_config")
        file = open(completeName, "w")
        file.write(t_ssid + "\t" + t_pw + "\t" + t_pw_again)
        file.close()
        proc = subprocess.Popen(["./wifi_ap_reconfig", ""], stdout=subprocess.PIPE, shell=True)
        proc.communicate()

    ip = request.remote_addr

    proc = subprocess.Popen(['date','+ %Y/%m/%d-%H:%M'], stdout=subprocess.PIPE)
    (time1, err) = proc.communicate()

    proc = subprocess.Popen(['./get_wifi','-ethip_get'], stdout=subprocess.PIPE)
    (eth_ip, err) = proc.communicate()


    proc = subprocess.Popen(['./get_wifi','-ssid_get'], stdout=subprocess.PIPE)
    (t_ssid, err) = proc.communicate()

    proc = subprocess.Popen(['./get_wifi','-pw_get'], stdout=subprocess.PIPE)
    (t_pw, err) = proc.communicate()

    templateData = {
        'ip': ip,
        'time1': time1,
        't_ssid': t_ssid,
        't_pw' : t_pw,
	'eth_ip' : eth_ip,
    }

    return render_template('index.html',**templateData)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True, threaded=True)
