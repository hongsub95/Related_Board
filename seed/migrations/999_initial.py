from django.db import migrations

from boards.initial_board_data import gen_board

class Migration(migrations.Migration):
    initial = True
    dependencies = [
    
    ]
    operations = [
        migrations.RunPython(gen_board)
        
    ]