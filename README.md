# 🔐 VaultAPI — Motor de Seguridad Modular

## 📌 Descripción

**VaultAPI** es una API backend desarrollada en Python que centraliza operaciones de seguridad como cifrado, hashing y validación de datos.

Su objetivo es proporcionar un **motor reutilizable de seguridad** que pueda integrarse en aplicaciones web, bots, herramientas OSINT o cualquier sistema que necesite protección de datos.

---

## 🚀 Características

* 🔐 Cifrado de datos con AES-GCM (seguro y autenticado)
* 🔑 Hashing de contraseñas con bcrypt
* 🧠 Arquitectura modular (fácil de escalar)
* 🚫 Bloqueo de algoritmos inseguros
* 🔐 Autenticación mediante API Key
* 🧪 Tests automatizados con pytest
* 📊 Logging básico integrado

---

## 🧱 Arquitectura del Proyecto

```
VaultAPI/
│
├── api/                # Capa de entrada (endpoints, validación)
│   ├── routes/
│   ├── schemas/
│   └── dependencies/
│
├── core/               # Lógica interna (motor de seguridad)
│   ├── crypto/         # Cifrado (AES-GCM)
│   ├── hashing/        # Hashing de contraseñas (bcrypt)
│   ├── encoding/       # Utilidades (base64)
│   ├── educational/    # Algoritmos inseguros (solo aprendizaje)
│   ├── security/       # API keys, key manager
│   ├── logging/        # Sistema de logs
│   └── registry.py     # Control de algoritmos
│
├── tests/              # Tests automatizados
└── main.py             # Punto de entrada
```

---

## 🔐 Seguridad

VaultAPI está diseñado siguiendo buenas prácticas modernas:

### AES-GCM

* Cifrado autenticado (confidencialidad + integridad)
* Nonce aleatorio por operación
* Uso de clave segura externa

### bcrypt

* Hashing no reversible
* Uso de salt automático
* Protección contra ataques de fuerza bruta

### Key Management

* Claves manejadas mediante variables de entorno
* No se almacenan en el código

---

## ⚠️ Algoritmos inseguros

Los siguientes algoritmos están presentes **solo con fines educativos**:

* Caesar Cipher
* ROT13

```text
NO están disponibles en producción
```

---

## 🔑 Configuración

### 1. Clave maestra (AES)

Generar:

```bash
python -c "import os,base64; print(base64.b64encode(os.urandom(32)).decode())"
```

Configurar en entorno:

```bash
setx VAULT_MASTER_KEY "TU_KEY"
```

---

### 2. API Keys

```bash
setx VAULT_API_KEYS "key1,key2,key3"
```

---

## ▶️ Uso

### Iniciar servidor

```bash
uvicorn main:app --reload
```

---

## 📡 Endpoints

### 🔐 Cifrar

```
POST /api/v1/crypto/encrypt
```

**Body:**

```json
{
  "data": "hola mundo"
}
```

---

### 🔓 Descifrar

```
POST /api/v1/crypto/decrypt
```

**Body:**

```json
{
  "data": "token_encriptado"
}
```

---

### 🔑 Hash de contraseña

```
POST /api/v1/password/hash
```

---

### ✅ Verificar contraseña

```
POST /api/v1/password/verify
```

---

## 🧪 Tests

Ejecutar:

```bash
pytest
```

---

## 📊 Logging

VaultAPI incluye logging básico para auditoría de acciones:

```text
Encrypt endpoint called
Decryption request executed
```

---

## 🎯 Flujo del sistema

```
Cliente → API → Registry → Algoritmo → Resultado
```

---

## 📦 Tecnologías utilizadas

* Python 3.13
* FastAPI
* cryptography
* bcrypt
* pytest
  
---

## 🚀 Mejoras futuras

* 🔁 Rotación de claves
* 🔐 Soporte para Argon2
* 🚫 Rate limiting
* 🧠 Sistema de políticas (roles/permisos)
* 📊 Auditoría avanzada

---
