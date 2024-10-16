from typing import Any
from airflow.models.baseoperator import BaseOperator
from airflow.utils.context import Context


class CustomOperator(BaseOperator):

    def __init__(self, name: str, **kwargs: Any):
        super().__init__(**kwargs)
        self.name = name

    def execute(self, context: Context):
        print(f'Hola {self.name}')
