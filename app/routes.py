from flask import render_template
from app import app
from app.models import Result

from pandasdmx import Request


@app.route('/')
@app.route('/index')
def index():
    ecb = Request('ECB')

    interest_rate_date = fetch_interest_rate(ecb)
    inflation_rate_data = fetch_inflation_rate(ecb)
    exchange_rate_data = fetch_exchange_rate(ecb)

    result = Result(interest_rate_date, inflation_rate_data, exchange_rate_data)

    return render_template('index.html', result=result)


def fetch_interest_rate(ecb):
    return ecb.data('FM/B.U2.EUR.4F.KR.MRR_FR.LEV').write()


def fetch_inflation_rate(ecb):
    return ecb.data('ICP/M.U2.N.000000.4.ANR').write()


def fetch_exchange_rate(ecb):
    return ecb.data('EXR/M.USD.EUR.SP00.E').write()
