from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def start():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    promotion_list = ['Человечество вырастает из детства.',
                      'Человечеству мала одна планета.',
                      'Мы сделаем обитаемыми безжизненные пока планеты.',
                      'И начнем с Марса!',
                      'Присоединяйся!']
    return '</br>'.join(promotion_list)


@app.route('/image_mars')
def image_mars():
    return """
    <!doctype html>
        <html lang="en">
          <head>
            <meta charset="utf-8">
            <title>Привет, Марс!</title>
          </head>
          <body>
            <h1>Жди нас, Марс!</h1>
            <p><img src="/static/img/mars.jpeg"></p>
            <p>Вот она какая, красная планета</p>
          </body>
        </html>
    """


@app.route('/promotion_image')
def promotion_image():
    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                       <link rel="stylesheet"
                       href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                       integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                       crossorigin="anonymous">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                        <title>Колонизация</title>
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                        <p><img src="/static/img/mars.jpeg"></p>
                        <div class="alert alert-secondary">Человечество вырастает из детства.</div>
                        <div class="alert alert-success">Человечеству мала одна планета.</div>
                        <div class="alert alert-secondary">Мы сделаем обитаемыми безжизненные пока планеты.</div>
                        <div class="alert alert-warning">И начнём с Марса!</div>
                        <div class="alert alert-danger">Присоединяйся!</div>
                      </body>
                    </html>'''


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def astronaut_selection():
    if request.method == 'GET':
        return f'''<!doctype html>
                                <html lang="en">
                                  <head>
                                    <meta charset="utf-8">
                                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                    <link rel="stylesheet"
                                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                    crossorigin="anonymous">
                                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                                    <title>Отбор астронавтов</title>
                                  </head>
                                  <body>
                                    <h1>Форма для регистрации в суперсекретной системе</h1>
                                    <div>
                                        <form class="login_form" method="post">
                                            <input type="surname" class="form-control" placeholder="Введите фамилию" name="surname">
                                            <input type="name" class="form-control" placeholder="Введите имя" name="name">
                                            <br>
                                            <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                            
                                            <div class="form-group">
                                                <label for="classSelect">Какое у вас образование?</label>
                                                <select class="form-control" name="education">
                                                  <option>Начальное</option>
                                                  <option>Среднее неполное</option>
                                                  <option>Среднее специальное</option>
                                                  <option>Высшее</option>
                                                  <option>Несколько высших</option>
                                                </select>
                                            </div>
                                            <div class="form-group form-check">
                                                <input type="checkbox" class="form-check-input" id="profession1" name="profession1">
                                                <label class="form-check-label" for="profession1">Инженер-исследователь</label></br>
                                                
                                                <input type="checkbox" class="form-check-input" id="profession2" name="profession2">
                                                <label class="form-check-label" for="profession2">Инженер-строитель</label></br>
                                                
                                                <input type="checkbox" class="form-check-input" id="profession3" name="profession3">
                                                <label class="form-check-label" for="profession3">Пилот</label></br>
                                                
                                                <input type="checkbox" class="form-check-input" id="profession4" name="profession4">
                                                <label class="form-check-label" for="profession4">Метеоролог</label></br>
                                                
                                                <input type="checkbox" class="form-check-input" id="profession5" name="profession5">
                                                <label class="form-check-label" for="profession5">Инженер по жизнеобеспечению</label></br>
                                                
                                                <input type="checkbox" class="form-check-input" id="profession6" name="profession6">
                                                <label class="form-check-label" for="profession6">Инженер по радиационной защите</label></br>
                                                
                                                <input type="checkbox" class="form-check-input" id="profession7" name="profession7">
                                                <label class="form-check-label" for="profession7">Врач</label></br>
                                                
                                                <input type="checkbox" class="form-check-input" id="profession8" name="profession8">
                                                <label class="form-check-label" for="profession8">Экзобиолог</label></br>
                                            </div>
                                            <div class="form-group">
                                                <label for="form-check">Укажите пол</label>
                                                <div class="form-check">
                                                  <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                                  <label class="form-check-label" for="male">
                                                    Мужской
                                                  </label>
                                                </div>
                                                <div class="form-check">
                                                  <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                                  <label class="form-check-label" for="female">
                                                    Женский
                                                  </label>
                                                </div>
                                            </div>
                                            <div class="form-group">
                                                <label for="about">Почему вы хотите принять участие в миссии?</label>
                                                <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                            </div>
                                            <div class="form-group">
                                                <label for="photo">Приложите фотографию</label>
                                                <input type="file" class="form-control-file" id="photo" name="file">
                                            </div>
                                            <div class="form-group form-check">
                                                <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                                <label class="form-check-label" for="acceptRules">Готовы остаться на марсе?</label>
                                            </div>
                                            <button type="submit" class="btn btn-primary">Записаться</button>
                                        </form>
                                    </div>
                                  </body>
                                </html>'''
    elif request.method == 'POST':
        print(request.form['surname'])
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['education'])
        for i in range(1, 9):
            print(request.form[f'profession{i}'])
        print(request.form['sex'])
        print(request.form['about'])
        print(request.form['accept'])
        return "Форма отправлена"


@app.route('/choice/<planet_name>')
def choice(planet_name):
    return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                           <link rel="stylesheet"
                           href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                           integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                           crossorigin="anonymous">
                            <title>Варианты выбора</title>
                          </head>
                          <body>
                            <h1>Мое предложение: {planet_name}</h1>
                            <p>Эта планета близка к Земле;</p>
                            <div class="alert alert-success">На ней много необходимых ресурсов;</div>
                            <div class="alert alert-secondary">На ней есть вода и атмосфера;</div>
                            <div class="alert alert-warning">На ней есть небольшое магнитное поле;</div>
                            <div class="alert alert-danger">Наконец, она просто красива!</div>
                          </body>
                        </html>'''



if __name__ == '__main__':
    app.run(port=8001, host='127.0.0.1')