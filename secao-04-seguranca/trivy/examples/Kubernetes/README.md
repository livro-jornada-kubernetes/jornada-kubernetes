# Instalando trivy operator usando helm 

### Adicione o repo do Agua chart

- Comandos helm: 
```bash
   helm repo add aqua https://aquasecurity.github.io/helm-charts/    
   helm repo update
```
### Instalando o trivy a partir do repositorio 

```bash
  helm install trivy-operator aqua/trivy-operator \
     --namespace trivy-system \
     --create-namespace \
     --version 0.24.0
```

### Lembre-se que é possivel passar configurações personalizadas usando o --set


```bash
  helm install trivy-operator aqua/trivy-operator \
     --namespace trivy-system \
     --create-namespace \
     --version 0.24.0
     --set="trivy.ignoreUnfixed=true"

```
- Existem muitas configs que podem ser personalizadas, para ver todas as disponiveis segue o [link](https://raw.githubusercontent.com/aquasecurity/trivy-operator/v0.22.0/deploy/helm/values.yaml)

### Para mais informações de como testar o operator e todas suas funcionalidades basta acessar o seguinte link: 

[Doc oficial](https://aquasecurity.github.io/trivy-operator/v0.3.0/operator/quick-start/)