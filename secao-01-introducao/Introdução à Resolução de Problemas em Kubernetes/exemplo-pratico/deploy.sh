#!/bin/bash

## efetua o build da imagem usada para a aplicação app.py
docker build -t jornadak8s:exemplo .

## carrega a imagem criada no passo anterior para dentro do cluster kind
kind load docker-image jornadak8s:exemplo

## deleta o deployment da aplicação app-flask-pg (demora alguns segundos para o pod ser deletado)
kubectl delete -f app-deployment.yaml --force --grace-period=0
sleep 30

## cria o deployment da aplicação app-flask-pg
kubectl apply -f app-deployment.yaml

## cria o service da aplicação app-flask-pg
# kubectl apply -f app-svc.yaml

