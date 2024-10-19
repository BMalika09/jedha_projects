# Get Around Pricing API 🚗

This project provides a machine learning-based API to predict the price of car rentals based on various features of the vehicle. The API is built using FastAPI and is deployed on Heroku. It uses a trained model to predict car rental prices based on inputs such as mileage, engine power, car type, and other vehicle characteristics.


Project Structure

    api.py: The FastAPI application with the /predict endpoint for making predictions.
    reg.pkl: The machine learning model file (trained on historical data).
    preprocessor.pkl: The preprocessor file used to transform input data.
    requirements.txt: List of dependencies required to run the application.


## How to Use
Local Use

Once the API is running locally:

    Go to http://127.0.0.1:8000/docs to test the /predict endpoint interactively.

    Make POST requests to http://127.0.0.1:8000/predict with the following payload structure:

```
{
  "car": "Audi",
  "mileage": 50000,
  "engine_power": 150,
  "fuel": "diesel",
  "paint_color": "black",
  "car_type": "sedan",
  "private_parking_available": true,
  "has_gps": false,
  "has_air_conditioning": true,
  "automatic_car": true,
  "has_getaround_connect": false,
  "has_speed_regulator": true,
  "winter_tires": false
}
```

## Deployed API (Online)

The API is also deployed on Heroku. You can use the following URL to access it:

API Base URL: https://get-around-pricing-c6d2cc25341d.herokuapp.com/

Interactive Documentation: https://get-around-pricing-c6d2cc25341d.herokuapp.com/docs

You can make POST requests to the /predict endpoint using tools like curl, Postman, or directly via the API documentation at /docs.

# Thank you ! 🚀