# Parcial Docker y FastAPI 🚀

## 📌 Descripción general

Este proyecto corresponde al desarrollo de una **API REST** construida con **FastAPI**, empaquetada y desplegada mediante **Docker**, como solución a la parte práctica del parcial.

La API permite realizar **predicciones utilizando un modelo de Machine Learning**, exponiendo un endpoint accesible vía HTTP y ejecutándose dentro de un contenedor Docker.

---

## 🧱 Tecnologías utilizadas

- Python 3.10
- FastAPI
- Uvicorn
- Docker
- Pickle (modelo entrenado)
- Ubuntu (entorno de ejecución)

---
▶️ Ejecución del contenedor

Para levantar la API desde la imagen creada:

docker run -d -p 8000:8000 --name api-fastapi-container api-fastapi

Esto:

Ejecuta el contenedor en segundo plano

Expone la API en el puerto 8000

Permite el acceso desde el navegador o herramientas como Postman

