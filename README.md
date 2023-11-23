# PublicSuscribeIngSoftware
Prototipo de Public Suscribe
En el prototipo de publicación-suscripción implementado:

[**Video**](https://www.youtube.com/watch?v=-bhRRn1NyUM&ab_channel=Yefersonvalencia)

**Objetivo:**
- Crear un sistema de mensajería utilizando el patrón de publicación-suscripción.
- Utilizar el broker de mensajería Mosquitto para facilitar la comunicación entre los nodos.

**Características:**
1. **Número de Nodos:**
   - Se implementaron tres publicadores y tres suscriptores.

2. **Distribución:**
   - El prototipo fue diseñado para ejecutarse localmente.

3. **Lenguaje de Implementación:**
   - Se utilizó Python como lenguaje de implementación para ambos, publicadores y suscriptores.

4. **Broker:**
   - Se eligió Mosquitto como broker de mensajería.

5. **Publicadores:**
   - Los publicadores fueron programados para enviar mensajes a un tema específico en el broker Mosquitto.

6. **Suscriptores:**
   - Los suscriptores se suscribieron al mismo tema que los publicadores y estaban diseñados para recibir y procesar los mensajes.

7. **Interacción:**
   - Los publicadores enviaron mensajes al tema definido en el broker.
   - Los suscriptores, al estar suscritos al mismo tema, recibieron y procesaron los mensajes publicados.

