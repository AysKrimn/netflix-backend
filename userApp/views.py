from django.shortcuts import render

# Create your views here.
def user_login(request):
    return render(request, 'login.html')



def user_main_browse_page(request):
    return render(request, 'browse-movies.html')