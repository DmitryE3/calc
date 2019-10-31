from flask import Flask, request, render_template, abort
import random
app = Flask(__name__)


@app.route('/', methods=['POST'])
def my_form_post():
    try:
        text = int(request.form['text'])
    except:
        abort(404)
    return graph(text)


@app.route("/")
def graph(num=10):
    chartID = 'chart_ID'
    chart = {"renderTo": chartID, "type": 'areaspline', "height": 450}
    title = {"text": 'test test test'}
    xAxis = {"categories": [i for i in range(10)]}
    yAxis = {"labels": {"format": '{value} thing'}, "title": {"text": 'Temperature'}}
    series = [{"name": 'City', "data": [random.randint(0, 10) for i in range(num)]}]
    return render_template("chart3.html", chartID=chartID, chart=chart, title=title, xAxis=xAxis, yAxis=yAxis,
                           series=series)


if __name__ == "__main__":
    app.run()
