import pickle

model = pickle.load(open('functions/weather_model.pkl', 'rb'))

def predict_weather(input_list):
    try:
        result_list = model.predict(input_list).tolist()

    except Exception as e:
        print(e)
        return "Failed to Infer with this Input "
    finally:
        print(f"predict weather: {result_list}")
    return result_list