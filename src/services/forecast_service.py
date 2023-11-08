from statsmodels.tsa.holtwinters import ExponentialSmoothing
import okama as ok
import pandas as pd
import numpy as np
import datetime


async def get_forecast(
        ticket: str = 'MSFT.US',
        n_days: int = 30) -> str:
    result = super_forecast(ticket, int(n_days))
    return str(result)


def super_forecast(
        ticket: str = 'MSFT.US',
        n_days: int = 30,
        last_period: int = 120) -> pd.DataFrame:
    if n_days > 31:
        print('Не рекомендуем строить прогноз более, чем на 1 месяц')

    hist = ok.Asset(ticket).close_daily

    data = pd.DataFrame({
        'ds': pd.to_datetime(hist.index.astype(str)),
        'y': hist.values.astype(float)
    })

    date_range = pd.date_range(
        datetime.date.today() - pd.Timedelta(days=1),
        datetime.date.today() + pd.Timedelta(days=n_days))

    data = pd.concat([data, pd.DataFrame({'ds': date_range, 'y': np.nan})])
    train, test = data[~data.y.isna()], data[data.y.isna()].drop(columns=['y'])
    train = train[train.ds >= train.ds.max() - datetime.timedelta(days=last_period)]

    model = ExponentialSmoothing(train['y']).fit()
    preds = model.predict(start=test.index[0], end=test.index[-1])

    test['y'] = preds.reset_index(drop=True)
    data = pd.concat([data.dropna(), test])
    tiemdelta = datetime.date.today() + datetime.timedelta(days=n_days)
    return data[data['ds'] == str(tiemdelta)]['y'].values[0]
