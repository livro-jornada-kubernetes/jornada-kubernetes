# Escaneamento de vulnerabilidades com Trivy


## Exemplos de utilização em pipelines
### github actions:
- [doc oficial](https://github.com/aquasecurity/trivy-action?tab=readme-ov-file#trivy-action) 
- [github actions yaml](../examples/github/trivy.yaml)

### gitlab:
- [doc oficial](https://docs.gitlab.com/ee/user/application_security/container_scanning/)
- [gitlab yaml](../examples/gitlab/gitlab.yaml)

### Kubernetes
- [doc oficial](https://aquasecurity.github.io/trivy-operator/latest/getting-started/installation/helm/)
- [Instalando com helm](../examples/Kubernetes/README.md)




## Como instalar o trivy 
- [Doc oficial](https://trivy.dev/v0.27.1/getting-started/installation/)

## Comandos Trivy disponiveis (Binário) 

### scaneando uma imagem: 

```bash
trivy image [YOUR_IMAGE_NAME]

``` 
- Exemplo de saída: 

```bash
$ trivy image myimage:1.0.0
2022-04-21T18:56:44.099+0300    INFO    Detected OS: alpine
2022-04-21T18:56:44.099+0300    INFO    Detecting Alpine vulnerabilities...
2022-04-21T18:56:44.101+0300    INFO    Number of language-specific files: 0

myimage:1.0.0 (alpine 3.15.0)
=============================
Total: 6 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 0, CRITICAL: 2)

+--------------+------------------+----------+-------------------+---------------+---------------------------------------+
|   LIBRARY    | VULNERABILITY ID | SEVERITY | INSTALLED VERSION | FIXED VERSION |                 TITLE                 |
+--------------+------------------+----------+-------------------+---------------+---------------------------------------+
| busybox      | CVE-2022-28391   | CRITICAL | 1.34.1-r3         | 1.34.1-r5     | CVE-2022-28391 affecting              |
|              |                  |          |                   |               | package busybox 1.35.0                |
|              |                  |          |                   |               | -->avd.aquasec.com/nvd/cve-2022-28391 |
+--------------+------------------|          |-------------------+---------------+---------------------------------------+
| ssl_client   | CVE-2022-28391   |          | 1.34.1-r3         | 1.34.1-r5     | CVE-2022-28391 affecting              |
|              |                  |          |                   |               | package busybox 1.35.0                |
|              |                  |          |                   |               | -->avd.aquasec.com/nvd/cve-2022-28391 |
+--------------+------------------+----------+-------------------+---------------+---------------------------------------+

app/deploy.sh (secrets)
=======================
Total: 1 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 0, CRITICAL: 1)

+----------+-------------------+----------+---------+--------------------------------+
| CATEGORY |    DESCRIPTION    | SEVERITY | LINE NO |             MATCH              |
+----------+-------------------+----------+---------+--------------------------------+
|   AWS    | AWS Access Key ID | CRITICAL |   10    | export AWS_ACCESS_KEY_ID=***** |
+----------+-------------------+----------+---------+--------------------------------+

```

### Scan de misconfigurations:

```bash
trivy config [YOUR_IAC_DIR]

```

- Exemplo de saída: 

```bash 
$ ls build/
Dockerfile
$ trivy config ./build
2021-07-09T10:06:29.188+0300    INFO    Need to update the built-in policies
2021-07-09T10:06:29.188+0300    INFO    Downloading the built-in policies...
2021-07-09T10:06:30.520+0300    INFO    Detected config files: 1

Dockerfile (dockerfile)
=======================
Tests: 23 (SUCCESSES: 22, FAILURES: 1, EXCEPTIONS: 0)
Failures: 1 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 1, CRITICAL: 0)

+---------------------------+------------+----------------------+----------+------------------------------------------+
|           TYPE            | MISCONF ID |        CHECK         | SEVERITY |                 MESSAGE                  |
+---------------------------+------------+----------------------+----------+------------------------------------------+
| Dockerfile Security Check |   DS002    | Image user is 'root' |   HIGH   | Last USER command in                     |
|                           |            |                      |          | Dockerfile should not be 'root'          |
|                           |            |                      |          | -->avd.aquasec.com/appshield/ds002       |
+---------------------------+------------+----------------------+----------+------------------------------------------+

```

#### Scan um filesystem tanto local ou o root

```bash
trivy fs /path/to/project

trivy rootfs /path/to/rootfs

```

### scan vulnerabilidades SBOM 

```bash
trivy sbom [flags] SBOM_PATH
```

- Exemplo:
```bash
   # Scan CycloneDX e mostre o resultado em forma de tabela
  $ trivy sbom /path/to/report.cdx

  # Scan CycloneDX-type attestation e mostre o resultado em forma de tabela
  $ trivy sbom /path/to/report.cdx.intoto.jsonl
``` 
- [Doc oficial](https://github.com/aquasecurity/trivy/blob/main/docs/docs/references/configuration/cli/trivy_sbom.md)

### Scan de um repositorio

```bash
trivy repository [flags] (REPO_PATH | REPO_URL)
```

- Exemplos: 
```bash
  # Scan your remote git repository
  $ trivy repo https://github.com/knqyf263/trivy-ci-test
  # Scan your local git repository
  $ trivy repo /path/to/your/repository 
```
- [Doc oficial](https://github.com/aquasecurity/trivy/blob/main/docs/docs/references/configuration/cli/trivy_repository.md)


### Mais subcomandos: 

* [trivy clean](https://github.com/aquasecurity/trivy/blob/main/docs/docs/references/configuration/cli/trivy_clean.md)	 - Remove o cache
* [trivy convert](https://github.com/aquasecurity/trivy/blob/main/docs/docs/references/configuration/cli/trivy_convert.md)	 - Converte Trivy JSON reporte para um diferente formato
* [trivy kubernetes](https://github.com/aquasecurity/trivy/blob/main/docs/docs/references/configuration/cli/trivy_kubernetes.md)	 - [EXPERIMENTAL] Scan kubernetes cluster
* [trivy module](https://github.com/aquasecurity/trivy/blob/main/docs/docs/references/configuration/cli/trivy_module.md)	 - Gerencia modules
* [trivy plugin](https://github.com/aquasecurity/trivy/blob/main/docs/docs/references/configuration/cli/trivy_plugin.md)	 - Gerencia os plugins
* [trivy registry](https://github.com/aquasecurity/trivy/blob/main/docs/docs/references/configuration/cli/trivy_registry.md)	 - Gerencia os registrys de autenticação
* [trivy server](https://github.com/aquasecurity/trivy/blob/main/docs/docs/references/configuration/cli/trivy_server.md)	 - Server mode
* [trivy version](https://github.com/aquasecurity/trivy/blob/main/docs/docs/references/configuration/cli/trivy_server.md)	 - Print the version
