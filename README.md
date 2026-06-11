# 🌿 420 Kush Community Bot

Un bot de Discord con sistema de verificación por reacciones en embeds. Los usuarios pueden verificarse haciendo clic en un emoji ✅ y reciben un rol automáticamente.

## 📋 Características

- ✅ Sistema de verificación por reacciones
- 🎨 Embed personalizado y atractivo
- 🔄 Asignación instantánea de rol
- 🛡️ Desverificación si se quita la reacción

## 🚀 Instalación

### 1. Requisitos previos
- Python 3.8 o superior
- Una cuenta de Discord
- Un servidor de Discord (si no tienes uno, créalo)
- Token del bot de Discord

### 2. Crear el bot en Discord Developer Portal

1. Ve a [Discord Developer Portal](https://discord.com/developers/applications)
2. Haz clic en "New Application"
3. Dale un nombre (ej: "420 Kush Community Bot")
4. Ve a la pestaña "Bot" y haz clic en "Add Bot"
5. Bajo "TOKEN", haz clic en "Copy" para copiar tu token
6. Guarda el token en un lugar seguro (lo necesitarás después)

### 3. Configurar permisos del bot

1. En Developer Portal, ve a "OAuth2" → "URL Generator"
2. Selecciona estos scopes:
   - `bot`
3. Selecciona estos permisos:
   - `Send Messages`
   - `Manage Roles`
   - `Add Reactions`
   - `Read Message History`
4. Copia la URL generada y ábrela en tu navegador para invitar el bot a tu servidor

### 4. Crear rol de verificación

1. En tu servidor de Discord, ve a "Configuración del servidor" → "Roles"
2. Crea un nuevo rol llamado "Verificado"
3. Dale los permisos que quieras que tengan los usuarios verificados
4. Copia el ID del rol (en Developer Mode: Clica derecho → Copiar ID de usuario)

### 5. Crear canal de verificación

1. En tu servidor, crea un nuevo canal de texto llamado "verificacion"
2. Copia el ID del canal (Clica derecho → Copiar ID de canal)
3. Asegúrate de que el bot tenga permisos para enviar mensajes y reacciones en ese canal

### 6. Configurar variables de entorno

1. Clona o descarga este repositorio
2. Copia el archivo `.env.example` y renómbralo a `.env`
3. Rellena los valores:

```env
DISCORD_TOKEN=tu_token_del_bot_aqui
GUILD_ID=id_de_tu_servidor
VERIFICATION_CHANNEL_ID=id_del_canal_verificacion
VERIFIED_ROLE_ID=id_del_rol_verificado
```

### 7. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 8. Ejecutar el bot

```bash
python bot.py
```

Deberías ver en la consola:
```
[nombre_del_bot] se ha conectado a Discord!
------
```

## 📝 Cómo usar

1. Una vez que el bot esté corriendo, ve al canal de verificación
2. Ejecuta el comando:
   ```
   !verificar
   ```
3. El bot enviará un embed con la opción de verificación
4. Los usuarios pueden hacer clic en ✅ para verificarse
5. Automáticamente recibirán el rol "Verificado"

## 🔧 Configuración personalizada

### Cambiar el emoji
En `bot.py`, busca esta línea:
```python
VERIFICATION_EMOJI = "✅"
```
Y cámbialo por otro emoji que prefieras (ej: "👍", "🟢", etc.)

### Personalizar el embed
En la función `send_verification`, puedes cambiar:
- El título
- La descripción
- Los campos
- El color
- El ícono

## 📚 Estructura del proyecto

```
420-Kush-Community/
├── bot.py              # Archivo principal del bot
├── requirements.txt    # Dependencias necesarias
├── .env.example        # Ejemplo de variables de entorno
├── .env                # Variables de entorno (no compartir)
├── .gitignore          # Archivos a ignorar
└── README.md           # Este archivo
```

## ⚠️ Notas importantes

- **NUNCA** compartas tu token de Discord públicamente
- El archivo `.env` está en `.gitignore` para mantener tu token seguro
- Asegúrate de que el bot tenga permisos suficientes en el servidor
- El ID del rol debe ser válido, de lo contrario el bot no podrá asignar roles

## 🐛 Solución de problemas

### El bot no responde
- Verifica que el token sea correcto
- Asegúrate de que el bot está en el servidor
- Comprueba que tiene los permisos necesarios

### No puedo copiar IDs
- Activa "Modo de desarrollador" en Discord:
  - Configuración de Usuario → Avanzado → Modo de desarrollador (ON)

### El rol no se asigna
- Verifica que el ID del rol sea correcto
- Asegúrate de que el bot tiene permiso "Manage Roles"
- Comprueba que el rol está por debajo del rol del bot en la jerarquía

### El embed no aparece
- Verifica que estés en el canal correcto
- Comprueba que el bot tiene permisos para enviar mensajes
- Asegúrate de que no hay errores en la consola

## 📞 Soporte

Si tienes problemas, verifica:
1. La consola del bot para mensajes de error
2. Los permisos del bot en el servidor
3. Las variables de entorno en `.env`
4. Que todos los IDs sean válidos

## 📄 Licencia

Este proyecto está disponible bajo la licencia MIT.

---

**¡Disfruta de tu bot! 🚀🌿**
