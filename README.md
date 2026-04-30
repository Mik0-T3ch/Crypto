<h1 align="center">🔐 VaultAPI</h1>
<h3 align="center">🛡️ Motor de Seguridad Modular</h3>

<p align="center">
API backend en Python para cifrado, hashing y validación de datos.<br>
Diseñada como un motor reutilizable de seguridad para aplicaciones, bots, herramientas OSINT y servicios backend.
</p>

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,fastapi,docker,linux,git,github&perline=6" />
</p>

<hr>

<h2>📊 Estadísticas del Proyecto</h2>

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api/pin/?username=Mik0-T3ch&repo=VaultAPI&theme=tokyonight" />
</p>

<hr>

<h2>📌 Descripción</h2>

<p>
<strong>VaultAPI</strong> es una API enfocada en centralizar operaciones críticas de seguridad como cifrado,
hashing de contraseñas y validación de datos.
</p>

<p>
El objetivo principal es desacoplar la lógica de seguridad del resto de la aplicación,
permitiendo reutilizar un núcleo robusto y consistente en múltiples proyectos.
</p>

<ul>
  <li>Aplicaciones web</li>
  <li>Microservicios</li>
  <li>Bots</li>
  <li>Herramientas OSINT</li>
  <li>Sistemas internos</li>
</ul>

<hr>

<h2>🚀 Características</h2>

<ul>
  <li>🔐 Cifrado con AES-GCM (autenticado y moderno)</li>
  <li>🔑 Hashing seguro con bcrypt</li>
  <li>🧠 Arquitectura modular desacoplada</li>
  <li>🚫 Bloqueo de algoritmos inseguros en producción</li>
  <li>🔐 Sistema de autenticación basado en API Keys</li>
  <li>🧪 Tests automatizados con pytest</li>
  <li>📊 Logging básico para auditoría</li>
  <li>📦 Diseño listo para integración en otros sistemas</li>
</ul>

<hr>

<h2>🧱 Arquitectura del Proyecto</h2>

<pre>
VaultAPI/
│
├── api/                # Capa de entrada (HTTP)
│   ├── routes/         # Endpoints
│   ├── schemas/        # Validación de datos
│   └── dependencies/   # Seguridad y middlewares
│
├── core/               # Motor interno
│   ├── crypto/         # AES-GCM
│   ├── hashing/        # bcrypt
│   ├── encoding/       # utilidades base64
│   ├── educational/    # algoritmos inseguros
│   ├── security/       # API Keys / Key Manager
│   ├── logging/        # sistema de logs
│   └── registry.py     # control de algoritmos
│
├── tests/              # pruebas automatizadas
└── main.py             # entrada principal
</pre>

<hr>

<h2>🔐 Seguridad</h2>

<h3>AES-GCM</h3>
<ul>
  <li>Cifrado autenticado (confidencialidad + integridad)</li>
  <li>Protección contra manipulación de datos</li>
  <li>Nonce aleatorio por operación</li>
  <li>Uso de claves externas seguras</li>
</ul>

<h3>bcrypt</h3>
<ul>
  <li>Hashing no reversible</li>
  <li>Salt automático incluido</li>
  <li>Resistente a ataques de fuerza bruta</li>
</ul>

<h3>Gestión de claves</h3>
<ul>
  <li>Uso de variables de entorno</li>
  <li>Separación entre código y secretos</li>
  <li>Evita exposición accidental de credenciales</li>
</ul>

<hr>

<h2>⚠️ Algoritmos inseguros</h2>

<p>
Los siguientes algoritmos están incluidos únicamente con fines educativos:
</p>

<pre>
Caesar Cipher
ROT13
</pre>

<p>
No están disponibles en producción y son bloqueados por el sistema.
</p>

<hr>

<h2>🔑 Configuración</h2>

<h3>1. Generar clave AES</h3>

<pre>
python -c "import os,base64; print(base64.b64encode(os.urandom(32)).decode())"
</pre>

<h3>2. Configurar variables de entorno</h3>

<pre>
setx VAULT_MASTER_KEY "TU_KEY"
setx VAULT_API_KEYS "key1,key2,key3"
</pre>

<hr>

<h2>▶️ Ejecución</h2>

<pre>
uvicorn main:app --reload
</pre>

<hr>

<h2>📡 Endpoints</h2>

<h3>🔐 Cifrado</h3>
<pre>
POST /api/v1/crypto/encrypt
</pre>

<h3>🔓 Descifrado</h3>
<pre>
POST /api/v1/crypto/decrypt
</pre>

<h3>🔑 Hash de contraseña</h3>
<pre>
POST /api/v1/password/hash
</pre>

<h3>✅ Verificación de contraseña</h3>
<pre>
POST /api/v1/password/verify
</pre>

<hr>

<h2>🧪 Testing</h2>

<pre>
pytest
</pre>

<hr>

<h2>📊 Logging</h2>

<p>El sistema incluye logging básico para auditoría de eventos:</p>

<pre>
Encrypt endpoint called
Decryption request executed
</pre>

<hr>

<h2>🔄 Flujo del sistema</h2>

<pre>
Cliente → API → Registry → Algoritmo → Resultado
</pre>

<hr>

<h2>🚀 Futuro</h2>

<ul>
  <li>🔁 Rotación de claves automática</li>
  <li>🔐 Soporte para Argon2</li>
  <li>🚫 Rate limiting</li>
  <li>🧠 Sistema de roles y permisos</li>
  <li>📊 Auditoría avanzada</li>
</ul>
