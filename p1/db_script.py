import sqlite3
conn = None
curs = None
def open():
    global conn, curs
    conn = sqlite3.connect("quiz.sqlite")
    curs = conn.cursor()

def close():
    curs.close()
    conn.close()
def do(request):
    curs.execute(request)
    conn.commit()
def clear_db():
    open()
    do("DROP TABLE IF EXISTS quiz_content")
    do("DROP TABLE IF EXISTS question")
    do("DROP TABLE IF EXISTS quiz")
    close()
def create():
    open()
    curs.execute("PRAGMA foreign_keys= on")
    curs.execute("""
                CREATE TABLE IF NOT EXISTS quiz(
                 id INTEGER PRIMARY KEY,
                 name VARCHAR)
                 """)
    do("""
        CREATE TABLE IF NOT EXISTS question(
       id INTEGER PRIMARY KEY,
       question VARCHAR,
       right_answer VARCHAR,
       wrong_answer1 VARCHAR,
       wrong_answer2 VARCHAR,
       wrong_answer3 VARCHAR
       )
       """)
    do("""
        CREATE TABLE IF NOT EXISTS quiz_content(
       id INTEGER PRIMARY KEY,
       question_id INT,
       quiz_id INT,
       FOREIGN KEY (quiz_id) REFERENCES quiz(id),
       FOREIGN KEY(question_id) REFERENCES question(id)
       )
       """)
    close()
#"Хто працює на хлопкових полях за безкоштовно","ніггери","європейці","китайці","ніхто"
#"Хто грабує магазини і вбиває невинних людей найбільше","ніггери","італійці","китайці","англійці"
#""
def add_question():
    question = [
        ("Хто працює на хлопкових полях за безкоштовно","ніггери","європейці","китайці","ніхто"),
        ("Хто грабує магазини і вбиває невинних людей найбільше","ніггери","італійці","китайці","англійці"),
        ("Який відсоток становить населення нігеров в африці","15%","12%","10%","20%"),
        ("Як називається відомий кримінальний район в якому переважно знаходяться нігери в США","Блек гетто","Нюь-йорк","Блекс","Охайо"),
        ("Який прийом їжі є звичайним для нігерів","кавун,кфс,кул аід","макарони,олівє,банани","банани,кфс,кул аід","кавун,яблоко,бурегри"),
        ("Яка сюжетна гра є найвідоміша з перечислених","гта 5","кс2","метро 2033","елден рінг"),
        ("Яка платформа для ігр є найпопулярнішою на цей момент","roblox","epic games","steam","rockstar launcher"),
        ("В якій грі був найбільший онлайн за весь час","grow a garden(roblox)","fortnite","кс2","дота2"),
        ("Розробниками серії ігр метро та сталкеру є","українська компанія","фінляндська компанія","російська компанія","білоруська компанія"),
        ("Ринок якої гри є найдорожчим на наш час","кс2","фортнайт","Kill niggers","тим фортресс"),
        ("Як звати найвідомішого оленя Санти з червоним носом?","Рудольф","Джеймс","Леброн","Брентон")

    ]
    open()
    curs.executemany("""
                     INSERT INTO question(question,right_answer,wrong_answer1,wrong_answer2,wrong_answer3)
                     VALUES (?,?,?,?,?)
                    """,question)
    conn.commit()
    close()
def add_quiz():
    quiz = [
        ("niggers",),
        ("games",),
        ("christmas",)

    ]
    open()
    curs.executemany("""
                     INSERT INTO quiz(name)
                     VALUES (?)
                    """,quiz)
    conn.commit()
    close()

def add_links():
    links = [
        (1,1),(1,2),(1,3),(1,4),(1,5),(2,6),(2,7),(2,8),(2,9),(2,10),(3,11)
    ]
    open()
    curs.executemany("""
                        INSERT INTO quiz_content(quiz_id,question_id)
                        VALUES(?,?)
                     
                     
                    """,links)
    conn.commit()
    close()
def show_quiz():
    open()
    curs.execute("SELECT id,name FROM quiz")
    result = curs.fetchall()
    close()
    return result

def next_question(quiz,question):
    open()
    curs.execute("""SELECT question.id,question.question,question.question.right_answer,question.wrong_answer1,question.wrong_answer2,question.wrong_answer3
                    FROM question,quiz_content
                    WHERE question.id == (?) AND quiz_content.quiz_id == (?) AND quiz_content.question_id == question.id""",(question,quiz))
    result = curs.fetchall()
    close()
    return result
    
def main():
    clear_db()
    create()
    add_question()
    add_quiz()
    add_links()

if __name__ == "__main__":
    main()
    open()
    curs.execute("SELECT * FROM question,quiz WHERE quiz.name == 'games'")
    print(curs.fetchall())
