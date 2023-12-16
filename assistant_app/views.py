from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from datetime import datetime

nltk.download('punkt')
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

def home(request):
    return render(request, 'assistant_app/index.html')

def process_query(query):
    words = word_tokenize(query)
    filtered_query = [word.lower() for word in words if word.isalnum() and word.lower() not in stop_words]
    return filtered_query

@csrf_exempt  # Añade esta anotación para deshabilitar CSRF
def get_response(request):
    if request.method == 'POST':
        data = request.POST.get('query', '')
        processed_query = process_query(data)

        # Lógica mejorada para reconocer preguntas y entrenar al asistente
        if "hora" in processed_query and "es" in processed_query:
            current_time = datetime.now().strftime("%H:%M:%S")
            response = f"La hora actual es: {current_time}"
        elif any(word in ["nombre", "llamas"] for word in processed_query):
            response = "Mi nombre es Cody. ¿En qué puedo ayudarte?"
        else:
            response = f"No entendí completamente la pregunta: {' '.join(processed_query)}"

        return JsonResponse({'response': response})
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'})