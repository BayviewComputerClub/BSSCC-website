from django.db import migrations

def make_models(apps, schema_editor):
    ExecRole = apps.get_model('website', 'ExecRole')
    pres = ExecRole(name='President', color='#FD0061').save()
    vp = ExecRole(name='Vice President', color='#A652BB').save()
    genExec = ExecRole(name='General Executive', color='#00D166').save()
    compExec = ExecRole(name='Competitive Executive', color='#0099E1').save()
    catBoyEnMing = ExecRole(name='Cat Boy En Ming', color='#FF1694').save()

    Exec = apps.get_model('website', 'Exec')
    bsscc = Exec(name='Bayview Computer Club Executive Team').save()

class Migration(migrations.Migration):
    dependencies = [
        ('website', '0002_auto_20211008_1422'),
    ]
    operations = [
        migrations.RunPython(make_models),
    ]
