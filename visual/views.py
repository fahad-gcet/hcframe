from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import FileUploadForm
from .models import FileUpload


def file_input(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = FileUpload(file=request.FILES['file'])
            file.save()

    else:
        form = FileUploadForm

    context = {
        'form': form
    }

    return render(request, 'visual/upload.html', context)
