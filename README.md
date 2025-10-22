# Microservicio factorial
Esto es un microservicio que recibe un número por url y devuelve:
- número: el número que se recibió
- factorial: el factorial del número que se recibió
- paridad: si el número que se pasó en la url es par o impar

## Endpoint
`/factorial/<n>`

Ejemplo:
`/factorial/5`
Retorna:
`{ "numero": 5, "factorial": "120", "paridad": "impar" }`

## Tecnología
Se hace uso de flask dentro de python.

## Para ejecutar (windows):
1. `python -m venv venv`
2. `venv\Scripts\Activate.ps1`
3. `pip install -r requirements.txt`
4. `python app.py`
5. Abrir `http://127.0.0.1:5000/factorial/2` por ejemplo, cambiando el 2 por el número que se quiera

## Análisis para persistir historial de cálculos

### Llamada síncrona HTTP al servicio de historial
Después de calcular el factorial, el microservicio haría una solicitu POST al otro servicio encargado de almacenar el historial de cálculos en una base de datos externa. En la petición post se le enviaría el json que se le muestra al usuario, y puede ser también un campo donde diga la fecha y hora de la petición. 




