import os

from celery import Celery, group, chain

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'reproduce.rep194.settings')

app = Celery('proj')

# Using a string here means the worker doesn't have to serialize
# the configuration object.
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

def print_cordcounter():
    from django_celery_results.models import ChordCounter
    print(f"ChordCounter.count(): {ChordCounter.objects.count()}")

@app.task(name="task_0")
def task_0():
    print_cordcounter()
    return "Task 0"

@app.task(name="task_1")
def task_1():
    print_cordcounter()
    return "Task 1"

@app.task(name="task_2.1")
def task_2_1():
    print_cordcounter()
    return "Task 2.1"

@app.task(name="task_2.2")
def task_2_2():
    print_cordcounter()
    return "Task 2.2"

@app.task(name="task_2", bind=True)
def task_2(self):
    print_cordcounter()
    return self.replace(group(task_2_1.si(), task_2_2.si()))

@app.task(name="task_3")
def task_3():
    print_cordcounter()
    return "Task 3"

@app.task(name="task_4")
def task_4():
    print_cordcounter()
    return "Task 4"

@app.task(name="task_5")
def task_5():
    print_cordcounter()
    return "Task 5"

@app.task(name="task_6")
def task_6():
    print_cordcounter()
    return "Task 6"

@app.task(name="task_7")
def task_7():
    print_cordcounter()
    return "Task 7"

def run():
    import django
    django.setup()
    group(
        task_0.si(),
        chain(
            task_1.si(),
            group(
                task_2.si(),
                chain(
                    task_3.si(),
                    task_4.si(),
                    task_5.si(),
                    task_6.si(),
                )
            ),
            task_7.si()
        )
    ).delay()
