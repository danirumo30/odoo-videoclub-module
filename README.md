# 🎬 Módulo Videoclub para Odoo

Este proyecto es un módulo personalizado desarrollado para **Odoo**, como parte del proyecto final del módulo de SGE. Su propósito es la gestión de un videoclub, incluyendo películas, actores, directores, artistas y categorías. 

La infraestructura está contenida en **Docker** con **Docker Compose**, facilitando el despliegue y pruebas del entorno completo.

---

## 🧩 Características del módulo

- Gestión de películas con información detallada.
- Registro y consulta de actores, directores y artistas.
- Clasificación de películas por categoría.
- Seguridad integrada mediante grupos y permisos Odoo.
- Informes PDF personalizables de películas, actores y directores.
- Traducción parcial al inglés (`i18n/en.po`).
- Interfaz de usuario integrada en la vista principal de Odoo.

---

## ⚙️ Requisitos

- Docker
- Docker Compose
- Git
- Odoo 16 (configurado en el contenedor)
- PostgreSQL (también configurado en el contenedor)

---

## 🚀 Instalación y ejecución

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/tu_usuario/odoo-videoclub-module.git
   cd odoo-videoclub-module
   ```

2. **Establecer permisos**
   ```bash
   chmod +x set_permissions.sh
   ./set_permissions.sh
   ```

3. **Levantar los contenedores**
   ```bash
   docker-compose up -d
   ```

4. **Acceder a Odoo**
   - URL: [http://localhost:8069](http://localhost:8069)
   - Iniciar sesión como **superusuario**
   - Activar el **modo desarrollador (debug)**
   - Ir a **Apps → Actualizar lista**
   - Buscar y **instalar el módulo `Videoclub`**

---

## 🧱 Estructura del proyecto

```
odoo-videoclub-module-main/
│
├── docker-compose.yml
├── set_permissions.sh
├── README.md
├── LICENSE
│
├── odoo/
│   ├── config/
│   └── addons/
│       └── drm_videoclub/
│           ├── models/
│           ├── views/
│           ├── reports/
│           ├── security/
│           ├── static/
│           ├── demo/
│           └── __manifest__.py
│
└── pgadmin4/ (config opcional para pgAdmin)
```

---

## 📸 Capturas de ejemplo

A continuación, puedes añadir capturas de pantalla del módulo en funcionamiento. Recomendamos incluir:

1. **Vista de películas**
2. **Formulario de actor/director**
3. **Informe PDF generado**
4. **Menú principal del videoclub**

> 📁 Crea una carpeta `/screenshots` y guarda tus imágenes ahí. Luego, enlázalas así:

```markdown
![Películas](screenshots/peliculas.png)
![Formulario Actor](screenshots/actor_form.png)
```

---

## 🧪 Extensiones recomendadas (VSCode)

- `jigar-patel.OdooSnippets`
- `ms-python.python`
- `ms-azuretools.vscode-Docker`
- `ckolkman.vscode-postgres`

---

## 🔐 Seguridad

El módulo define sus propios modelos de seguridad:

- `security.xml`: Grupos de acceso y reglas básicas.
- `ir.model.access.csv`: Permisos por modelo.

---

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo [LICENSE](./LICENSE) para más información.

---

## 👤 Autor

**Daniel Rubio Mora**

Proyecto final del módulo **Servicios en Red (SGE)**.
