# Flask Microframework: https://flask.palletsprojects.com/en/1.1.x/
# Библиотека requests: http://docs.python-requests.org/
# Передача параметров через командную ?key1=val1&key2=val2...:
from flask import Flask, request, escape, render_template, jsonify
from flask_cors import CORS
app = Flask(__name__, template_folder='./templates')



# Задачи из бакэнда (Flask) для отображения во фронте (Vue)
groceryList = [
    {
        'id': 0,
        'text': 'Backend text',
    },
    {
        'id': 1,
        'text': 'Backend text2',
    }
]

# Просто тест работы бакэнда
@app.route('/echo/')
def echo():
    thing = escape(request.args.get('thing'))
    place = escape(request.args.get('place'))
    return render_template('template1.html', thing=thing, place=place)



# API-точка входа
@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'groceryList': groceryList})


CORS(app)


# Vue:
#https://ru.vuejs.org/v2/guide/#Разбиение-приложения-на-компоненты # Маленький туториал
# To-do на Vue: https://scrimba.com/p/pXKqta/cgnEeh4

# Есть ещё FlaskAPI, что вообще-то лучше и использовать
# https://www.flaskapi.org/
from flask_api import FlaskAPI

app_api = FlaskAPI(__name__, template_folder='./templates')

@app_api.route('/example/')
def example():
    return {'groceryList': groceryList}



# Вообще как подружить Flask и Vue лучше почитать эту статью: https://tproger.ru/translations/developing-app-with-flask-and-vue-js/

if __name__ == "__main__":
    app.run(port=9999, debug=True)

    #app_api.run(port=9999, debug=True)




# Как развернуть приложение Flask на сервере через nginx + uWSGI


# Последние ссылки:
# https://ru.vuejs.org/v2/guide/#Разбиение-приложения-на-компоненты
# https://scrimba.com/p/pXKqta/cgnEeh4
# http://127.0.0.1:9999/echo/?thing=test&place=Canada
# http://127.0.0.1:9999/example/
# https://tproger.ru/translations/developing-app-with-flask-and-vue-js/