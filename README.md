<body>
<div class="container">

<h1>🔐 VaultAPI — Motor de Seguridad Modular</h1>

<h2>📌 Descripción</h2>
<p><strong>VaultAPI</strong> es una API backend desarrollada en Python que centraliza operaciones de seguridad como cifrado, hashing y validación de datos.</p>
<p>Su objetivo es proporcionar un <strong>motor reutilizable de seguridad</strong> que pueda integrarse en aplicaciones web, bots, herramientas OSINT o cualquier sistema que necesite protección de datos.</p>

<hr>

<h2>🚀 Características</h2>
<ul>
  <li>🔐 Cifrado de datos con AES-GCM (seguro y autenticado)</li>
  <li>🔑 Hashing de contraseñas con bcrypt</li>
  <li>🧠 Arquitectura modular (fácil de escalar)</li>
  <li>🚫 Bloqueo de algoritmos inseguros</li>
  <li>🔐 Autenticación mediante API Key</li>
  <li>🧪 Tests automatizados con pytest</li>
  <li>📊 Logging básico integrado</li>
</ul>

<hr>

<h2>🧱 Arquitectura del Proyecto</h2>
<pre>
VaultAPI/
│
├── api/
│   ├── routes/
│   ├── schemas/
│   └── dependencies/
│
├── core/
│   ├── crypto/
│   ├── hashing/
│   ├── encoding/
│   ├── educational/
│   ├── security/
│   ├── logging/
│   └── registry.py
│
├── tests/
└── main.py
</pre>

<hr>

<h2>🔐 Seguridad</h2>

<h3>AES-GCM</h3>
<ul>
  <li>Cifrado autenticado (confidencialidad + integridad)</li>
  <li>Nonce aleatorio por operación</li>
  <li>Uso de clave segura externa</li>
</ul>

<h3>bcrypt</h3>
<ul>
  <li>Hashing no reversible</li>
  <li>Uso de salt automático</li>
  <li>Protección contra ataques de fuerza bruta</li>
</ul>

<h3>Key Management</h3>
<ul>
  <li>Claves manejadas mediante variables de entorno</li>
  <li>No se almacenan en el código</li>
</ul>

<hr>

<h2>⚠️ Algoritmos inseguros</h2>
<p>Los siguientes algoritmos están presentes <strong>solo con fines educativos</strong>:</p>
<ul>
  <li>Caesar Cipher</li>
  <li>ROT13</li>
</ul>

<div class="warning">
  <strong>NO están disponibles en producción</strong>
</div>

<hr>

<h2>🔑 Configuración</h2>

<h3>1. Clave maestra (AES)</h3>
<pre>python -c "import os,base64; print(base64.b64encode(os.urandom(32)).decode())"</pre>

<p>Configurar en entorno:</p>
<pre>setx VAULT_MASTER_KEY "TU_KEY"</pre>

<h3>2. API Keys</h3>
<pre>setx VAULT_API_KEYS "key1,key2,key3"</pre>

<hr>

<h2>▶️ Uso</h2>

<h3>Iniciar servidor</h3>
<pre>uvicorn main:app --reload</pre>

<hr>

<h2>📡 Endpoints</h2>

<h3>🔐 Cifrar</h3>
<pre>POST /api/v1/crypto/encrypt</pre>
<pre>{
  "data": "hola mundo"
}</pre>

<h3>🔓 Descifrar</h3>
<pre>POST /api/v1/crypto/decrypt</pre>
<pre>{
  "data": "token_encriptado"
}</pre>

<h3>🔑 Hash de contraseña</h3>
<pre>POST /api/v1/password/hash</pre>

<h3>✅ Verificar contraseña</h3>
<pre>POST /api/v1/password/verify</pre>

<hr>

<h2>🧪 Tests</h2>
<pre>pytest</pre>

<hr>

<h2>📊 Logging</h2>
<p>VaultAPI incluye logging básico para auditoría de acciones:</p>
<pre>
Encrypt endpoint called
Decryption request executed
</pre>

<hr>

<h2>🎯 Flujo del sistema</h2>
<pre>Cliente → API → Registry → Algoritmo → Resultado</pre>

<hr>

<h2>📦 Tecnologías utilizadas</h2>
<ul>
  <li>Python 3.13</li>
  <li>FastAPI</li>
  <li>cryptography</li>
  <li>bcrypt</li>
  <li>pytest</li>
</ul>

<hr>

<h2>🚀 Mejoras futuras</h2>
<ul>
  <li>🔁 Rotación de claves</li>
  <li>🔐 Soporte para Argon2</li>
  <li>🚫 Rate limiting</li>
  <li>🧠 Sistema de políticas (roles/permisos)</li>
  <li>📊 Auditoría avanzada</li>
</ul>

</div>
</body>
</html>
