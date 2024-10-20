from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
import os
from datetime import datetime, timedelta
import subprocess

def htop(request):
    # Get system username
    username = os.getlogin()
    
    # Get server time in IST
    ist_time = datetime.now() + timedelta(hours=5, minutes=30)
    
    # Get top output
    try:
        top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode('utf-8')
    except Exception as e:
        top_output = str(e)

    response = {
        'Name': 'Manoj K',  # Replace with your full name
        'Username': username,
        'Server Time (IST)': ist_time.strftime('%Y-%m-%d %H:%M:%S'),
        'Top Output': top_output
    }
    return JsonResponse(response)
