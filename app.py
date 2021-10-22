import logging
from json import dumps

from flask import Flask, request, Response

app = Flask(__name__)
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

endpoints = {}


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def catch_all(path):
    company_id = '1'
    if 'companyId' in request.headers:
        company_id = request.headers['companyId']

    app.logger.info(request.method + " " + path + " Company " + str(company_id))

    if company_id not in endpoints:
        app.logger.info('Wrong companyId: ' + company_id)
        return 'Wrong companyId'

    if path not in endpoints[company_id]:
        app.logger.info('Wrong path: ' + path)
        return 'Wrong path'

    headers = endpoints[company_id][path]["headers"]
    body = dumps(endpoints[company_id][path]["body"], indent=2, default=str)
    status = endpoints[company_id][path]["status"]

    response = Response(body)
    response.headers = headers
    response.status = status

    return response


@app.route('/setup', methods=['POST'])
def setup():
    global endpoints
    endpoints = request.get_json()
    app.logger.info('Endpoints updated for companies: ' + ", ".join(endpoints.keys()))
    return 'Endpoints updated'
