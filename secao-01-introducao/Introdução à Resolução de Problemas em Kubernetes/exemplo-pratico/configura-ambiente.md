## Criação do cluster local utilizando o kind

1 - Instalar o [kind](https://kind.sigs.k8s.io/docs/user/quick-start/#installation) na máquina local.

2 - Para iniciar o cluster, execute o comando:   `kind create cluster --config cluster.yaml`

## Instalação do chart do banco de dados postgres

Pré-requisito: 

É necessário ter o [helm charts](https://helm.sh/docs/intro/install/) instalado na máquina.

1 - Adiciona o repositorio do chart: 

`helm repo add bitnami https://charts.bitnami.com/bitnami`

2 - Instala o chart passando a configuração definida no arquivo `values.postgres.yaml`: 

`helm install my-release oci://registry-1.docker.io/bitnamicharts/postgresql -f 1.18/exemplos/values.postgres.yaml`

3 - Aguardar alguns minutos até o pod do postgre esteja pronto:

`kubectl get pods`

## Habilitar conexão com a aplicação

Habilite a conexão direta com o pod através da porta 30007, para validar o funcionamento da aplicação:

`kubectl port-forward service/app-flask-pg-svc 30007:8080`

## Abrir a aplicação no navegador

Em seguida, acesse a URL: [](http://localhost:30007)

Se estiver tudo funcionando corretamente, deve ser apresentada uma mensagem parecida com:

`Hello from Flask! PostgreSQL version: <versão do postgres> `


## Desinstalação do chart do postgres

Para desinstalar o postgres, execute o comando:

`helm uninstall my-release`

Deverá aparecer uma resposta parecida com:

`release "<nome-da-release>" uninstalled`