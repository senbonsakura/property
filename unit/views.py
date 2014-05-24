from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from unit.models import Project, Unit
from django.views import generic
from unit.forms import ProjectForm, UnitForm
from django.template import RequestContext


def project_list(request, page=0, maxlist=10):
    projects = Project.objects.all()[int(page) * int(maxlist):int(page) * int(maxlist) + int(maxlist)]
    # tlng = len(Project.objects.all())
    units = Unit.objects.filter()
    context = {'project_list': projects}

    return render(request, 'unit/project_list.html', context)


def project(request, id):
    project = Project.objects.get(id=id)
    context = {'project': project}
    return render(request, 'unit/project.html', context)


def index(request):
    projects = Project.objects.all()
    context = {'project_list': projects}
    return render(request, 'unit/index.html', context)


def delete_project(request, id):
    server = get_object_or_404(Project, id=id)
    if request.method == 'POST':
        server.delete()
        return redirect('project_list')
    return render(request, 'unit/confirm_delete.html', {'object': server})


def add_project(request):
    # Get the context from the request.
    context = RequestContext(request)

    # A HTTP POST?
    if request.method == 'POST':
        form = ProjectForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new projecto to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return redirect('project_list')
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = ProjectForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    # return render_to_response('unit/add_project.html', {'form': form}, context)
    #return render_to_response('unit/add_project.html', {'form': form}, context)

    return render(request, 'unit/add_project.html', {'form': form})


def edit_project(request, id):
    project = get_object_or_404(Project, id=id)
    form = ProjectForm(request.POST or None, instance=project)
    if form.is_valid():
        form.save()
        return redirect('project_list')
    return render(request, 'unit/add_project.html', {'form': form})


def add_unit(request, id):
    # Get the context from the request.
    context = RequestContext(request)
    project = get_object_or_404(Project, id=id)
    # A HTTP POST?
    if request.method == 'POST':
        initial = {'project': project}
        form = UnitForm(request.POST or None, initial=initial)
        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new projecto to the database.

            unit = form.save(commit=False)
            unit.project = project
            unit.save()
            return redirect('add_unit')
        else:
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = UnitForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    # return render_to_response('unit/add_project.html', {'form': form}, context)
    #return render_to_response('unit/add_project.html', {'form': form}, context)

    return render(request, 'unit/add_unit.html', {'form': form})
