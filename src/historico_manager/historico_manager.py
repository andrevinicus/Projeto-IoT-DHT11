import pandas as pd
import io
from flask import Response
import psycopg2
import logging

class HistoricoManager:
    def __init__(self, parametros_conexao):
        self.parametros_conexao = parametros_conexao
        self.logger = logging.getLogger(__name__)

    def obter_dados_periodo(self, startdate, enddate, period):
            try:
                with psycopg2.connect(**self.parametros_conexao) as connection, connection.cursor() as cursor:
                    if period == 'day':
                        # Consulta para um dia específico
                        query = "SELECT temperature, humidity, data_hora FROM public.sensor_data WHERE DATE(data_hora) = %s ORDER BY data_hora"
                        cursor.execute(query, (startdate,))
                    elif period == 'month':
                        # Consulta para um mês específico
                        query = "SELECT temperature, humidity, data_hora FROM public.sensor_data WHERE EXTRACT(MONTH FROM data_hora) = %s ORDER BY data_hora"
                        cursor.execute(query, (startdate,))
                    elif period == 'year':
                        # Consulta para um ano específico
                        query = "SELECT temperature, humidity, data_hora FROM public.sensor_data WHERE EXTRACT(YEAR FROM data_hora) = %s ORDER BY data_hora"
                        cursor.execute(query, (startdate,))
                    elif period == 'custom':
                        # Consulta para um intervalo personalizado
                        query = "SELECT temperature, humidity, data_hora FROM public.sensor_data WHERE data_hora >= %s AND data_hora <= %s ORDER BY data_hora"
                        cursor.execute(query, (startdate, enddate))
                    else:
                        return None

                    resultados = cursor.fetchall()

                    if not resultados:
                        return None

                    df = pd.DataFrame(resultados, columns=['temperature', 'humidity', 'data_hora'])
                    return df

            except (Exception, psycopg2.Error) as erro:
                self.logger.error(f"Erro ao obter dados do banco de dados: {erro}")
                return None

    def download_csv_period(self, startdate, enddate):
        df = self.obter_dados_periodo(startdate, enddate)
        csv_data = self.gerar_csv(df)

        if csv_data:
            filename = f'historico_dados_{startdate}_to_{enddate}.csv'
            return Response(
                csv_data,
                headers={
                    'Content-Disposition': f'attachment; filename={filename}',
                    'Content-Type': 'text/csv',
                }
            )

        return None

    def gerar_csv(self, df):
        if df is None:
            return None

        csv_buffer = io.StringIO()
        df.to_csv(csv_buffer, index=False)
        return csv_buffer.getvalue()
