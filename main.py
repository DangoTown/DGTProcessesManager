# coding: utf-8

import json
from flask import *
import user
import process
import _thread as thread

pc = process.ProcessesController()
print("ProcessController got")

app = Flask("main")
print("Flask object registed")
app.add_template_global(len)
app.config['SECRET_KEY'] = 'secretkey'


@app.route("/")
def login():
    return render_template("login.html")


@app.route("/login", methods=['POST'])
def loginapi():
    if user.login((request.form).get("u"), (request.form).get("p")):
        return redirect("/internal")
    else:
        return "<script>alert('Account or password does not exist');history.go(-1);</script>"


@app.route("/internal")
def internal():
    return render_template("list.html", processes=[i[0] for i in pc.get_processes()])


@app.route("/internal/<int:process_id>")
def process_info(process_id: int):
    return render_template("process_info.html", process=pc.get_processes()[process_id], pid=process_id, process_name=pc.get_processes()[process_id][0])


@app.route("/internal/create")
def create_process():
    return render_template("create.html")


@app.route("/internal/terminal_page/<int:pid>")
def terminal_page(pid):
    return render_template("terminal.html", pid=pid)


@app.route("/internal/debug/crash")
def close_app():
    exit(0)


@app.route("/internal/terminal_ajax/<int:pid>/flush")
def get_term_flush(pid: int):
    return pc.read_flush(pid).decode()


@app.route("/internal/terminal_ajax/<int:pid>/read")
def get_term_stdout(pid: int):
    return pc.read_stdout(pid).decode()


@app.route("/internal/terminal_ajax/<int:process_id>/write", methods=['POST'])
def terminal_input(process_id: int):
    input_data = (request.form).get("s")
    pc.put_stdin(int(process_id), input_data.encode())
    return "ok"


with open("./processes.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    for k in data:
        v = data[k]
        pc.create_process(k, v, shell=True)


app.run(threaded=True)
