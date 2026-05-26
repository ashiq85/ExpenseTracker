from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.db.models import Sum, Q
from django.utils import timezone
import datetime
from .models import Expense
from .forms import ExpenseForm, ExpenseFilterForm

class ExpenseListView(ListView):
    model = Expense
    template_name = 'expenses/expense_list.html'
    context_object_name = 'expenses'

    def get_queryset(self):
        queryset = super().get_queryset().order_by('-date', '-id')
        category = self.request.GET.get('category')
        date_from = self.request.GET.get('date_from')
        date_to = self.request.GET.get('date_to')
        search = self.request.GET.get('search')

        if category:
            queryset = queryset.filter(category=category)
        if date_from:
            queryset = queryset.filter(date__gte=date_from)
        if date_to:
            queryset = queryset.filter(date__lte=date_to)
        if search:
            queryset = queryset.filter(Q(title__icontains=search) | Q(note__icontains=search))
            
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = ExpenseFilterForm(self.request.GET)
        return context

class ExpenseCreateView(CreateView):
    model = Expense
    form_class = ExpenseForm
    template_name = 'expenses/expense_form.html'
    success_url = reverse_lazy('expense-list')

class ExpenseUpdateView(UpdateView):
    model = Expense
    form_class = ExpenseForm
    template_name = 'expenses/expense_form.html'
    success_url = reverse_lazy('expense-list')

class ExpenseDeleteView(DeleteView):
    model = Expense
    template_name = 'expenses/expense_confirm_delete.html'
    success_url = reverse_lazy('expense-list')

class ExpenseSummaryView(TemplateView):
    template_name = 'expenses/expense_summary.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Determine the month for summary, default to current month
        month_str = self.request.GET.get('month')
        if month_str:
            try:
                year, month = map(int, month_str.split('-'))
                target_date = datetime.date(year, month, 1)
            except ValueError:
                target_date = timezone.now().date()
        else:
            target_date = timezone.now().date()
            
        start_date = target_date.replace(day=1)
        
        # Calculate end of month
        if target_date.month == 12:
            end_date = target_date.replace(year=target_date.year + 1, month=1, day=1) - datetime.timedelta(days=1)
        else:
            end_date = target_date.replace(month=target_date.month + 1, day=1) - datetime.timedelta(days=1)
            
        expenses_this_month = Expense.objects.filter(date__range=[start_date, end_date])
        total_amount = expenses_this_month.aggregate(Sum('amount'))['amount__sum'] or 0
        
        category_breakdown = expenses_this_month.values('category').annotate(total=Sum('amount')).order_by('-total')
        
        # For Chart.js
        labels = [item['category'].title() for item in category_breakdown]
        data = [float(item['total']) for item in category_breakdown]
        
        context.update({
            'total_amount': total_amount,
            'category_breakdown': category_breakdown,
            'current_month_display': start_date.strftime('%B %Y'),
            'current_month_value': start_date.strftime('%Y-%m'),
            'chart_labels': labels,
            'chart_data': data,
        })
        return context
