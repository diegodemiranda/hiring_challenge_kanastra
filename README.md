# Hiring Challlenge Kanastra

BANCO DE DADOS 
Usei índices apropriados para campos que são comumente usados em operações de consulta.
Otimizei consultas frequentes para garantir que elas sejam rápidas, especialmente se 
o volume de dados aumentar.
Considerei a normalização dos dados, se necessário, para evitar a duplicação 
de informações e garantir a integridade dos dados.
Esta tabela armazenará as informações básicas do devedor. As restrições UNIQUE 
garantem que o número do documento do governo e o endereço de e-mail sejam únicos, 
evitando duplicações.

Utilizei um volume persistente, pratica comum em ambientes Docker para 
garantir que os dados gerados pelo contêiner sejam preservados mesmo que o contêiner 
seja destruído ou reiniciado. Isso é importante para manter a integridade e 
persistência dos dados do banco de dados, garantindo que os dados sobrevivam 
aos ciclos de vida do contêiner.  Isso também facilita o backup e a migração de 
dados entre diferentes ambientes.

Usei um arquivo .sql, para automatizar e repetir facilmente tarefas de banco de dados, 
como as instruções para criação da estrutura de tabelas do banco de dados, incluir consultas 
SQL em um arquivo ou inserir dados nessas tabelas. Especialmente, quando precisar executar
as mesmas operações em diferentes ambientes ou em momentos diferentes. 
Isso é útil para configuração, migração de dados, atualizações e outras tarefas de 
gerenciamento de banco de dados.


Modelo de Charge
Neste modelo completo de Charge, adicionamos dois campos de data/hora: created_at e updated_at. O created_at registra o momento em que a carga foi criada pela primeira vez, enquanto o updated_at registra o momento em que a carga foi atualizada pela última vez. Ambos são inicializados automaticamente com o valor atual do tempo na criação de uma nova carga e atualizados automaticamente sempre que a carga é modificada.

Comando para rodar o container Docker:
docker run -e FRONTEND_URL=http://localhost:3000 -e DB_USER=kanastra -e DB_PASSWORD=kanastra_challenge -e DB_NAME=db_kanastra -e SERVER_HOST=0.0.0.0 -e SERVER_PORT=8000 -p 8000:8000 -p 5432:5432 kanastra_billing_system

Comando para iniciar a aplicação manualmente se for preciso:
docker exec -it kanastra_billing_system uvicorn main:app --host 0.0.0.0 --port 8000

Sim, a estrutura do seu projeto parece estar correta para a construção da imagem Docker. Aqui está uma breve descrição de cada arquivo e diretório:

- `backend/`: Este diretório deve conter o código do backend da sua aplicação, incluindo o arquivo `main.py`.
- `frontend/`: Este diretório deve conter o código do frontend da sua aplicação.
- `.env`: Este arquivo deve conter as variáveis de ambiente necessárias para a sua aplicação.
- `docker-compose.yml`: Este arquivo é usado para definir e executar aplicações Docker multi-contêiner. Se você estiver usando vários serviços (como um serviço de aplicação e um serviço de banco de dados), você pode definir todos eles neste arquivo.
- `Dockerfile`: Este arquivo é usado para construir a imagem Docker da sua aplicação. Ele contém as instruções para construir a imagem.
- `README.md`: Este arquivo geralmente contém informações sobre o projeto, como instruções de instalação e uso.
- `requirements.txt`: Este arquivo deve listar todas as dependências Python necessárias para a sua aplicação.

Certifique-se de que o `Dockerfile` e o `docker-compose.yml` (se presente) estão configurados corretamente para construir a imagem e executar os contêineres. Além disso, certifique-se de que todas as dependências necessárias estão listadas no `requirements.txt` e que todas as variáveis de ambiente necessárias estão definidas no arquivo `.env`.

Esses campos adicionais podem ser úteis para rastrear o histórico e a atividade das cargas no seu sistema. Certifique-se de que a tabela correspondente no banco de dados tenha suporte para armazenar valores de data/hora. Com este modelo completo, você tem uma representação abrangente das cargas no seu sistema, pronta para ser usada na sua aplicação FastAPI.