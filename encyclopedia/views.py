from django.shortcuts import render
import markdown
from . import util
from django.http import HttpResponse


def convert_to_html(md_title):
    content = util.get_entry(md_title)
    if content == None:
        return None
    else:
        return markdown.Markdown().convert(content)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    content = convert_to_html(title)
    if content == None:
        return render(request, "encyclopedia/error.html")

    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": content
        })

def create(request):
    if(request.method == "POST"):
        entry_title = request.POST["title"]
        entry_content = request.POST["content"]
        util.save_entry(entry_title, entry_content)

    return render(request, "encyclopedia/create.html")


def random(request):
    return render(request, "encyclopedia/random.html")