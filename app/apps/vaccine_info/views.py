from django.views.generic import FormView, ListView, DeleteView
from apps.core.permissions import AdminMixin
from .forms import VaccineInfoForm
from apps.core.models import VaccineInfo
from django.shortcuts import reverse, render
from django.contrib import messages


class VaccineInfoCreateFormView(AdminMixin, FormView):
    template_name = 'vaccine_info/vaccine_info_form.html'
    form_class = VaccineInfoForm

    def get_success_url(self) -> str:
        return reverse('add-vaccine-info')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Successfully added vaccine information")
        return super(VaccineInfoCreateFormView, self).form_valid(form)

    def form_invalid(self, form):
        return render(self.request, self.template_name, context={'form': form})


class VaccineInfoListView(ListView):
    template_name = 'vaccine_info/vaccine_info_list.html'
    paginate_by = 20
    context_object_name = 'vaccine_infos'

    def get_queryset(self):
        filter_by = self.request.GET.get('filter_by', None)
        search_word = self.request.GET.get('search_word', None)
        print(filter_by)
        print(search_word)
        queryset = VaccineInfo.objects.all()
        if filter_by is None or search_word is None:
            return queryset
        if filter_by == 'author_name':
            return queryset.filter(author__icontains=search_word)
        if filter_by == 'institution':
            return queryset.filter(institution__icontains=search_word)
        if filter_by == 'research_title':
            return queryset.filter(research_title__icontains=search_word)
        if filter_by == 'keyword':
            return queryset.filter(keywords__keyword__icontains=search_word)
        return queryset


class VaccineInfoDeleteView(AdminMixin, DeleteView):
    model = VaccineInfo
    success_url = '/'
    template_name = 'vaccine_info/delete-confirm.html'

    def get_success_url(self) -> str:
        messages.success(self.request, "Successfully deleted Vaccine Information")
        return super().get_success_url()