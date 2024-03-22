# Portifólio_PySpark
# Seja muito bem vindo! Esse diretório é totalmente focado em desenvolvimento de processos com PySpark

## Meu Primeiro ETL com PySpark:

## DADOS FICTICÍOS!

Foi desenvolvido um processo do qual soluciona a dor de um cliente, o mesmo precisava gerar uma base de vendas unificada com informações dos vendedores. O processo faz um JOIN entre o arquivo de CSV (Vendas) e uma tabela com dados dos vendedores no MySql, para realizar esse cruzamento as duas fontes de dados tem uma coluna chamada ID_DO_VENDEDOR do qual será utilizada como chave, vou explicar o passo a passo logo a baixo:

1 Step - Foi necessário baixar o Apache Spark e instalar, logo após foi incluído o caminho nas variáveis de ambiente do sistema, também foi baixado o conector JDBC para poder conectar ao banco de dados MYSQL, esse conector foi salvo na pasta JARS do Spark para execução.

2 Step - Utilizei o VScode para desenvolver o código, foi necessário instalar a biblioteca PySpark, em seguida foi necessário alterar o caminho de execução do VScode, desse ponto estava tudo pronto para iniciar o desenvolvimento do código.

3 Step - Iniciando o desenvolvimento do código, importei as bibliotecas necessárias para desenvolver o processo e iniciei o Spark pelo comando padrão, coloquei o conector JDBC para executar junto para conseguir fazer conexões no banco de dados.

4 Step - Crio Variáveis que armazenam informações para conexão no banco de dados, verifico se o arquivo existe na pasta, caso existir ele abre o arquivo e salva os dados em uma variável DF, caso não existir ele encerra o PySpark e sai do processo para não deixar nada aberto como conexão para não prejudicar outro processo que for executado após.

5 Step - Foi necessário renomear as colunas do arquivo pois estava com espaço e caracteres especiais, também foi alterado o tipo de dado do campo DATA_DA_VENDA que estava como string e foi convertido para o tipo date.

6 Step - Faço a conexão com o banco de dados e capturo informações da tabela de vendedores.

7 Step - Realizo o JOIN entre as tabelas com o campo ID_DO_VENDEDOR como parâmetro.

8 Step - Subo essa base unificada para uma tabela no banco de dados para ser consumida por qualquer equipe que tenha acesso.

## PROPOSTA DESSE PROCESSO: 
Solucionar a dor do cliente pois ele precisava de uma base unificada com dados de quem fez aquela venda entre outras informações.
- Pensando em agilidade no desenvolvimento de relatórios, não será necessário importar duas tabelas de dados para o POWE BI e nem utilizar mais relacionamento para trazer informações dessa base, será necessário apenas relacionamento com Dimensão, com isso o relatório fica mais leve e mais rápido.