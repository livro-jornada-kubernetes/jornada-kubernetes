# Daemonsets 

Este material complementa a seção sobre Daemonsets, fornecendo exemplos e explicações sobre manifestos e demonstrações de recursos importantes.

## Manifesto YAML

A seguir um exemplo de um manifesto básico de um Daemonset: 

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: node-name-printer
spec:
  selector:
    matchLabels:
      app: node-name-printer
  template:
    metadata:
      labels:
        app: node-name-printer
    spec:
      containers:
      - name: node-name-printer
        image: busybox:1.36.1 
        command: ["sh", "-c", "while true; do echo Node Name: $(hostname); sleep 5; done"]
```
No exemplo, é criado um DaemonSet chamado `node-name-printer` que define um pod contendo um container que utiliza uma imagem `busybox:1.36.1` e que apenas imprime o nome do host a cada 5 segundos. Ao aplicar o manifesto, o comportamento esperado é que sejam criados um pod para cada nó worker.

## Listando um DaemonSet e seus pods

Para listar DaemonSets, utilizamos o comando: 

``` kubectl get daemonset ``` 

na figura também mostramos a listagem dos pods correspondente ao DaemonSet:

DS1


## Detalhando um DaemonSet

Para consultarmos maiores detalhes sobre um DaemonSet, utilizamos o comando: 

``` kubectl describe daemonset node-name-printer```

a resposta esperada do comando será parecida com:

DS2




## Estratégias de atualizações

As estratégias de atualização de StatefulSets são um pouco diferente dos Deployments. Temos 2 opções de estratégias para os StatefulSets:

- **OnDelete**: Mesmo conceito usado pelo Statefulset, porém não é o padrão para DaemonSet. Usar essa estratégia significa que as atualizações não serão automáticas. É necessário deletar manualmente um pod, para quando ele seja recriado com a configuração nova.

- **Rolling Update**: exatamente como nos Deployments e StatefulSets, o rolling update faz a substituição um a um dos antigos pods pelos novos. É a estratégia padrão pro DaemonSet.


## Deletando um DaemonSet

Para deletar um DaemonSet, utilizamos o comando: 

``` kubectl delete daemonset node-name-printer``` 

DS3


Perceba que todos os pods foram removidos junto com seu DaemonSet