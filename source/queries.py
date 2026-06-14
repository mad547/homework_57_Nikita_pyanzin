from django.utils import timezone
from datetime import timedelta
from django.db.models import Q, Count, F
from tracker_app.models import Issue

month_ago = timezone.now() - timedelta(days=30)
closed_last_month = Issue.objects.filter(
    status__name='Выполнено',
    updated_at__gte=month_ago
)
print('1. Закрытые за последний месяц:')
for issue in closed_last_month:
    print(f'   {issue.summary} | {issue.status.name} | {issue.updated_at}')

issues_by_status_and_type = Issue.objects.filter(
    Q(status__name='Новая') | Q(status__name='В процессе')б
    Q(issue_type__name='Задача') | Q(issue_type__name='Ошибка')
).distinct()
print('\n2. Задачи с нужными статусами и типами:')
for issue in issues_by_status_and_type:
    print(f'   {issue.summary} | {issue.status.name}')

not_done_bug = Issue.objects.filter(
    Q(summary__icontains='bug') | Q(issue_type__name='Ошибка')
).exclude(
    status__name='Выполнено'
).distinct()
print('\n3. Не закрытые задачи с bug или типом Ошибка:')
for issue in not_done_bug:
    print(f'   {issue.summary}')


issues_values = Issue.objects.values(
    'id', 'summary', 'issue_type__name', 'status__name'
)
print('\nТолько нужные поля:')
for issue in issues_values:
    print(f'   {issue}')


same = Issue.objects.filter(description=F('summary'))
    print('\n Краткое = полному:')
    for issue in same:
        print(f'   {issue.summary}')


count_by_type = Issue.objects.values(
    'issue_type__name'
).annotate(
    count=Count('id')
).order_by('issue_type__name')
print('\nКоличество задач по типам:')
for item in count_by_type:
    print(f'   {item["issue_type__name"]} | {item["count"]}')