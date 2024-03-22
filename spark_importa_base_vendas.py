from pyspark import serializers
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
import os

# Inicia Sessão Pyspark
spark = SparkSession.builder \
        .master("local[1]")  \
        .appName("test")     \
        .config("spark.driver.extraClassPath", "C:\\Spark\\spark-3.5.1-bin-hadoop3\\jars\\mysql-connector-j-8.3.0.jar") \
        .config("spark.executor.extraClassPath", "C:\\Spark\\spark-3.5.1-bin-hadoop3\\jars\\mysql-connector-j-8.3.0.jar") \
        .getOrCreate()
spark

# Variaveis para conexão ao banco Mysql
mysql_user = "root"
mysql_password = "May1509$"
mysql_database = "teste_spark"
mysql_table = "venda_gold_flight_group"

# Variavel url para conexão ao banco Mysql
mysql_url = "jdbc:mysql://localhost:3306/{0}?user={1}&password={2}".format(mysql_database, mysql_user, mysql_password)

# Para ler o Mysql apontado a tabela de vendedores
options = {
    "url": mysql_url,
    "driver": "com.mysql.cj.jdbc.Driver",
    "dbtable": 'vendedores_gold_flight_group',
    "user": mysql_user,
    "password": mysql_password
}

# Localiza e abre arquivo que será usado no processo
if os.path.exists('C:\\Arquivos\\Base_de_vendas.csv'):
    df = spark.read.format('csv').load('C:\\Arquivos\\Base_de_vendas.csv', sep=';', encoding='iso-8859-1', header=True)

    # Renomeia nome das colunas 
    df = df.withColumnRenamed('Nome do Passageiro','nome_do_passageiro'
                                                ).withColumnRenamed('Origem','origem'
                                                                    ).withColumnRenamed('Destino','destino'
                                                                                        ).withColumnRenamed('Data da Viagem','data_da_viagem'
                                                                                                            ).withColumnRenamed('Classe','classe'
                                                                                                                                ).withColumnRenamed('Preço (R$)','preco'
                                                                                                                                                    ).withColumnRenamed('ID do Vendedor','id_do_vendedor'
                                                                                                                                                                        ).withColumnRenamed('id','id_da_venda')

    # Convete valor texto para data
    df = df.withColumn("data_da_viagem", to_date("data_da_viagem","dd/MM/yyyy"))

    # Obtem os dados da tabela de vendedores
    df2 = spark.read.format('jdbc').options(**options).load()
    df2.show()

    # Cruza as bases para obter dados dos vendedores
    df_join = df.join(df2,'id_do_vendedor', 'inner')
    df_join.show()


    # Sobe os dados para o banco Mysql
    df_join.write.jdbc(url=mysql_url, table=mysql_table, mode="append")

    spark.stop()
else:
    print('Arquivo não localizado')
    spark.stop()
    exit