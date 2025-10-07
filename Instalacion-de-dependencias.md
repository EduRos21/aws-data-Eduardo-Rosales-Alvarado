# Instalación de dependencias

## Instalación de Python
Python viene preinstalado en la mayoría de las versiones de Ubuntu por lo que solo hace falta checar si ya viene en la versión manejada con: 

```bash
python3 –version
```

---

## Instalación de Docker y Docker Compose

### 1. Actualizar el Sistema e Instalar Requisitos Previos

```bash
sudo apt update
sudo apt install ca-certificates curl gnupg
```
### 2. Añadir la Clave GPG y el Repositorio de Docker

### 2.1 Crea el directorio de keyrings (si no existe) sudo install -m 0755 -d /etc/apt/keyrings

```bash
sudo install -m 0755 -d /etc/apt/keyrings
```
### 2.2 Descarga la clave GPG y añádela al keyring

```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
```

### 2.3 Añade el repositorio a las fuentes de APT

```bash
echo \
"deb [arch=\"$(dpkg --print-architecture)\" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
\"$(. /etc/os-release && echo \"$VERSION_CODENAME\")\" stable" | \
sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```
### 3. Instalar Docker Engine

### 3.1 Actualiza el índice de paquetes

```bash
sudo apt update
```

### 3.2 Instala Docker Engine, CLI, y Compose

```bash
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

### 4. Verificar la Instalación

```bash
sudo docker run hello-world
docker –versión
```
---

## Instalación de virtual env

### 1. Se instala a través de pip por lo que hace falta primero instalar pip en Ubuntu
```bash
sudo apt install python3-pip
```

### 2. Se revisa si se consiguió instalar

```bash
pip3 –version
```

### 3. Ahora se procede a instalar virtual env

```bash
sudo apt install python3-virtualenv
```

### 4. Se comprueba la instalación

```bash
virtualenv –version
```

---

## Instalación de Jupyter

### 1. Crear y Activar el Entorno Virtual

### 1.1 Crea una carpeta para tu proyecto y entra en ella

```bash
mkdir jupyter_projects
cd jupyter_projects
```

### 1.2 Crea el entorno virtual

```bash
virtualenv jupyter_env_homework
```

### 1.3 Activa el entorno virtual

```bash
source jupyter_env_homework/bin/actívate
```

### 2. Instalar Jupyter

```bash
pip install jupyter
```

### 3. Comprobar que esté instalado

```bash
jupyter --version
```

---
## Referencias

#### Docker
- [Docker](https://docs.docker.com/engine/install/ubuntu/)
- [Gemini] (como instalar docker en ubuntu)

#### Virtual env
- [Virtualenv](https://pypi.org/project/virtualenv/)
- [Gemini] (instalar junyper en ubuntu usando virtual env)

### Jupyter
- [Jupyter](https://jupyter.org/install)




