<h1 align="center">🔐 VaultAPI</h1>
<h3 align="center">🛡️ Motor de Seguridad Modular</h3>

<p align="center">
API backend en Python para cifrado, hashing y validación de datos.<br>
Diseñada como un núcleo reutilizable de seguridad para aplicaciones, bots y servicios backend.
</p>

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,fastapi,linux,git,github&perline=6" />
</p>

<hr>

<h2>📌 Descripción</h2>

<p>
<strong>VaultAPI</strong> es una API enfocada en centralizar operaciones críticas de seguridad como cifrado,
hashing de contraseñas y validación de datos.
</p>

<p>
Su objetivo es desacoplar la lógica criptográfica del resto del sistema, permitiendo reutilizar un núcleo seguro
y consistente en múltiples proyectos.
</p>

<ul>
  <li>Aplicaciones web</li>
  <li>Microservicios</li>
  <li>Bots</li>
  <li>Sistemas internos</li>
</ul>

<hr>

<h2>🚀 Características</h2>

<ul>
  <li>🔐 Cifrado moderno con AES-GCM</li>
  <li>🔑 Hashing seguro con bcrypt</li>
  <li>🧠 Arquitectura modular desacoplada</li>
  <li>🚫 Bloqueo de algoritmos inseguros</li>
  <li>🔐 Autenticación mediante API Key</li>
  <li>🧪 Tests automatizados con pytest</li>
  <li>📦 Diseño listo para integración</li>
</ul>

<hr>

<h2>🧱 Arquitectura</h2>

<pre>
VaultAPI/
│
├── api/                # Capa HTTP
│   ├── routes/         # Endpoints
│   ├── schemas.py      # Validación de datos
│   └── dependencies/   # Seguridad
│
├── core/               # Lógica interna
│   ├── crypto/         # AES-GCM
│   ├── hashing/        # bcrypt
│   ├── encoding/       # base64
│   ├── educational/    # cifrados inseguros
│   ├── security/       # API keys / keys
│   └── registry.py     # control de algoritmos
│
├── tests/              # pruebas
└── requirements.txt
</pre>

<hr>

<h2>⚙️ Instalación</h2>

<pre>
git clone https://github.com/Mik0-T3ch/VaultAPI.git
cd VaultAPI

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
</pre>

<hr>

<h2>🔐 Configuración</h2>

<h3>Generar MASTER_KEY</h3>

<pre>
python -c "import os,base64; print(base64.urlsafe_b64encode(os.urandom(32)).decode())"
</pre>

<h3>Crear archivo .env</h3>

<pre>
API_KEY=tu_api_key
MASTER_KEY=tu_master_key
</pre>

<hr>

<h2>▶️ Ejecución</h2>

<pre>
uvicorn api.main:app --reload
</pre>

<hr>

<h2>📡 Uso de la API</h2>

<h3>🔐 Encrypt</h3>

<pre>
curl -X POST http://127.0.0.1:8000/crypto/encrypt ^
-H "Content-Type: application/json" ^
-H "x-api-key: TU_API_KEY" ^
-d "{\"text\":\"hola\",\"method\":\"aes\"}"
</pre>

<h3>🔓 Decrypt</h3>

<pre>
curl -X POST http://127.0.0.1:8000/crypto/decrypt ^
-H "Content-Type: application/json" ^
-H "x-api-key: TU_API_KEY" ^
-d "{\"text\":\"TOKEN\",\"method\":\"aes\"}"
</pre>

<h3>🔑 Password Hash</h3>

<pre>
POST /password/hash
</pre>

<h3>✅ Password Verify</h3>

<pre>
POST /password/verify
</pre>

<hr>

<h2>🧪 Testing</h2>

<pre>
pytest
</pre>

<hr>

<h2>🔐 Seguridad</h2>

<ul>
  <li>AES-GCM con nonce aleatorio por operación</li>
  <li>Integridad y confidencialidad garantizadas</li>
  <li>bcrypt con salt automático</li>
  <li>Separación de claves mediante variables de entorno</li>
</ul>

<hr>

<h2>⚠️ Algoritmos educativos</h2>

<p>
Los algoritmos como Caesar y ROT13 están incluidos únicamente con fines educativos
y no pueden utilizarse en los endpoints seguros.
</p>

<hr>

<h2>🔄 Flujo del sistema</h2>

<pre>
Cliente → API → Registry → Algoritmo → Resultado
</pre>

<hr>

<h2>🚀 Futuro</h2>

<ul>
  <li>Rate limiting</li>
  <li>Logging estructurado</li>
  <li>Versionado de API</li>
  <li>Rotación de claves</li>
  <li>Soporte para Argon2</li>
</ul>
