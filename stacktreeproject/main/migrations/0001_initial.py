# Generated by Django 4.0.4 on 2022-08-19 06:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('company_id', models.AutoField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=45)),
                ('company_address', models.TextField()),
                ('Company_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Framework',
            fields=[
                ('framework_id', models.AutoField(primary_key=True, serialize=False)),
                ('framework_name', models.CharField(max_length=45)),
                ('framework_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Framework_for_tree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField()),
                ('essential', models.BooleanField(default=True)),
                ('choice', models.IntegerField(null=True)),
                ('framework_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.framework')),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('Language_id', models.AutoField(primary_key=True, serialize=False)),
                ('Language_name', models.CharField(max_length=45)),
                ('Language_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Language_for_tree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField()),
                ('essential', models.BooleanField(default=True)),
                ('choice', models.IntegerField(null=True)),
                ('language_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.language')),
            ],
        ),
        migrations.CreateModel(
            name='Language_syntax',
            fields=[
                ('language_syntax_id', models.AutoField(primary_key=True, serialize=False)),
                ('l_syntax_title', models.CharField(max_length=45)),
                ('l_syntax_difficulty', models.IntegerField()),
                ('l_syntax_teer', models.CharField(max_length=45)),
                ('l_syntax_order', models.IntegerField()),
                ('language_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.language')),
            ],
        ),
        migrations.CreateModel(
            name='Tree',
            fields=[
                ('Tree_id', models.AutoField(primary_key=True, serialize=False)),
                ('Tree_name', models.CharField(max_length=45)),
                ('framework', models.ManyToManyField(blank=True, through='main.Framework_for_tree', to='main.framework')),
                ('language', models.ManyToManyField(blank=True, through='main.Language_for_tree', to='main.language')),
            ],
        ),
        migrations.CreateModel(
            name='Syntax_to_master_framework',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('framework_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.framework')),
                ('language_syntax_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.language_syntax')),
            ],
        ),
        migrations.CreateModel(
            name='Language_to_master_framework',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Framework_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.framework')),
                ('Language_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.language')),
            ],
        ),
        migrations.AddField(
            model_name='language_for_tree',
            name='tree_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.tree'),
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('Job_id', models.AutoField(primary_key=True, serialize=False)),
                ('Job_name', models.CharField(max_length=45)),
                ('Company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.company')),
                ('Tree_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.tree')),
            ],
        ),
        migrations.CreateModel(
            name='Framework_syntax',
            fields=[
                ('framework_syntax_id', models.AutoField(primary_key=True, serialize=False)),
                ('f_syntax_title', models.CharField(max_length=45)),
                ('f_syntax_difficulty', models.IntegerField()),
                ('f_syntax_teer', models.CharField(max_length=45)),
                ('f_syntax_order', models.IntegerField()),
                ('framework_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.framework')),
            ],
        ),
        migrations.AddField(
            model_name='framework_for_tree',
            name='tree_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.tree'),
        ),
        migrations.AddField(
            model_name='framework',
            name='language',
            field=models.ManyToManyField(blank=True, through='main.Language_to_master_framework', to='main.language'),
        ),
        migrations.AddField(
            model_name='framework',
            name='syntax',
            field=models.ManyToManyField(blank=True, through='main.Syntax_to_master_framework', to='main.language_syntax'),
        ),
    ]
