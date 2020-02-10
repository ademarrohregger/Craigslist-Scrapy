import subprocess
import json

from flask import Flask
from flask import render_template


app = Flask(__name__)

with open('results.json') as f:
    data = json.load(f)


@app.route('/scrap')
def scrap():
    """
    Run spider in another process and store items in file. Simply issue command:

    > scrapy crawl dmoz -o "output.json"

    wait for  this command to finish, and read output.json to client.
    """
    spider_name = "craigspider"
    subprocess.check_output(
        ['rm', 'results.json'])
    subprocess.check_output(
        ['scrapy', 'crawl', spider_name, "-o", "results.json"])
    with open("results.json") as items_file:
        return items_file.read()


@app.route("/view")
def view():
    message = {"data": data}
    return render_template('index.html', message=message)


@app.route("/results")
def results():
    return {"data": data}


if __name__ == '__main__':
    app.run(debug=True)
