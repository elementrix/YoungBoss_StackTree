from django.shortcuts import render

# Create your views here.
def main(request):

    return render(request, 'main.html')

def result(request):
    return render(request, 'result.html')

<<<<<<< HEAD

def position_detail(request):
    
    return render(request, 'position_detail.html')
=======
    return render(request, 'result.html')

def mypage(request):

    return render(request, 'mypage.html')
>>>>>>> 6229d492e89ae84a77142cbb9326f1b36f2ddf48
