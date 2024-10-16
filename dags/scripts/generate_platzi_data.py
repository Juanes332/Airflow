import pandas as pd


def _generate_platzi_data(**kwargs):
    data = pd.DataFrame({"student": ["Maria Cruz", "Daniel Crema",
                                     "Elon Musk", "Karol Castrejon", "Freddy Vega"],
                        "timestamp": [kwargs['logical_date'],
                                      kwargs['logical_date'], kwargs['logical_date'], kwargs['logical_date'],
                                      kwargs['logical_date']]})
    data.to_csv(f"/tmp/platzi_data_{kwargs['ds_nodash']}.csv",
                header=True)
