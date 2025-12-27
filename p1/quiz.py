from flask import Flask,session,redirect,url_for,render_template,request
from db_script import *
def start_quiz(quiz=1):
    session["quiz"] = quiz
    session["next_question"] = next_question(quiz,0)
    session["result"] = 0
    session["total"] = 0
def quiz_form():
    quiz_list = show_quiz()
    return render_template("index.html",quiz_list= quiz_list)
def index():
    if request.method == "GET":
        start_quiz
        return quiz_form()
    else:
        quiz_id = request.form.get("quiz")
        start_quiz(quiz_id)
        return redirect(url_for("test"))

def test():
    if not("quiz" in session) or int(session["quiz"]) <0:
        return redirect(url_for("index"))
    else:
        if request.method == "POST":
            pass
        session["next_question"] = next_question(session["quiz"],session["total"])
        if session["next_question"] is None or len(session["next_question"]== 0):
            return redirect(url_for("result"))
        else:
            session["total"] += 1
            return render_template("test.html",question = session["next_question"][1],
                                   answer_list = session["next_question"][2:],
                                   question_id = session["next_question"][0])
def result():
    return 0

app = Flask(__name__,template_folder= "template",static_folder= "static")
app.add_url_rule("/","index",index)
app.add_url_rule("/test","test",test)
app.add_url_rule("/result","result",result)
app.secret_key = "niggers" 

if __name__ == "__main__":
    app.run()