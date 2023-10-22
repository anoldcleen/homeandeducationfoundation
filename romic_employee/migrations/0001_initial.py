# Generated by Django 3.2.12 on 2023-09-27 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectname', models.CharField(blank=True, default='', max_length=100)),
                ('mission', models.TextField(blank=True, default='')),
                ('vision', models.TextField(blank=True, default='')),
                ('objective1', models.TextField(blank=True, default='')),
                ('objective2', models.TextField(blank=True, default='')),
                ('objective3', models.TextField(blank=True, default='')),
                ('objective4', models.TextField(blank=True, default='')),
                ('objective5', models.TextField(blank=True, default='')),
                ('objective6', models.TextField(blank=True, default='')),
                ('objective7', models.TextField(blank=True, default='')),
                ('objective8', models.TextField(blank=True, default='')),
                ('objective9', models.TextField(blank=True, default='')),
                ('objective10', models.TextField(blank=True, default='')),
                ('testimonial1', models.CharField(blank=True, default='', max_length=100)),
                ('testimonialrole1', models.CharField(blank=True, default='', max_length=100)),
                ('testimonialdecription1', models.TextField(blank=True, default='')),
                ('testimonial2', models.CharField(blank=True, default='', max_length=100)),
                ('testimonialrole2', models.CharField(blank=True, default='', max_length=100)),
                ('testimonialdecription2', models.TextField(blank=True, default='')),
                ('testimonial3', models.CharField(blank=True, default='', max_length=100)),
                ('testimonialrole3', models.CharField(blank=True, default='', max_length=100)),
                ('testimonialdecription3', models.TextField(blank=True, default='')),
                ('testimonial4', models.CharField(blank=True, default='', max_length=100)),
                ('testimonialrole4', models.CharField(blank=True, default='', max_length=100)),
                ('testimonialdecription4', models.TextField(blank=True, default='')),
                ('testimonial5', models.CharField(blank=True, default='', max_length=100)),
                ('testimonialrole5', models.CharField(blank=True, default='', max_length=100)),
                ('testimonialdecription5', models.TextField(blank=True, default='')),
                ('location1', models.CharField(blank=True, default='', max_length=100)),
                ('location2', models.CharField(blank=True, default='', max_length=100)),
                ('contact1', models.CharField(blank=True, default='', max_length=100)),
                ('contact2', models.CharField(blank=True, default='', max_length=100)),
            ],
            options={
                'db_table': 'about',
            },
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activitytitle', models.CharField(default='', max_length=50)),
                ('activitydescription', models.TextField(default='')),
                ('activity_main_img1', models.ImageField(default='', upload_to='images/')),
                ('activity_main_img2', models.ImageField(default='', upload_to='images/')),
                ('activity_main_img3', models.ImageField(default='', upload_to='images/')),
                ('activity_main_img4', models.ImageField(default='', upload_to='images/')),
                ('activity_main_img5', models.ImageField(default='', upload_to='images/')),
                ('activity_main_img6', models.ImageField(default='', upload_to='images/')),
            ],
            options={
                'db_table': 'activity',
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('btitle', models.CharField(default='', max_length=100)),
                ('bauthor', models.CharField(default='', max_length=100)),
                ('bdescription', models.TextField(default='')),
                ('byoutubelink', models.TextField(default='')),
            ],
            options={
                'db_table': 'blog',
            },
        ),
        migrations.CreateModel(
            name='Cause',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('causetitle', models.CharField(default='', max_length=50)),
                ('causedescription', models.TextField(default='')),
                ('cause_main_img1', models.ImageField(default='', upload_to='images/')),
                ('cause_main_img2', models.ImageField(default='', upload_to='images/')),
                ('cause_main_img3', models.ImageField(default='', upload_to='images/')),
                ('cause_main_img4', models.ImageField(default='', upload_to='images/')),
                ('cause_main_img5', models.ImageField(default='', upload_to='images/')),
                ('cause_main_img6', models.ImageField(default='', upload_to='images/')),
            ],
            options={
                'db_table': 'cause',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentname', models.CharField(default='', max_length=100)),
                ('commentemail', models.EmailField(default='', max_length=254)),
                ('commentsubject', models.TextField(default='')),
                ('commentmessage', models.TextField(default='')),
            ],
            options={
                'db_table': 'contact',
            },
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dname', models.CharField(default='', max_length=100)),
                ('damount', models.CharField(default='', max_length=100)),
                ('dtype', models.CharField(default='', max_length=15)),
                ('dcause', models.CharField(default='', max_length=15)),
            ],
            options={
                'db_table': 'donation',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ename', models.CharField(default='', max_length=100)),
                ('eemail', models.EmailField(default='', max_length=254)),
                ('econtact', models.CharField(default='', max_length=15)),
                ('edescription', models.TextField(default='')),
            ],
            options={
                'db_table': 'employee',
            },
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partnername', models.CharField(blank=True, default='', max_length=100)),
                ('partnerdescription', models.TextField(blank=True, default='')),
                ('partner_main_img', models.ImageField(default='', upload_to='images/')),
            ],
            options={
                'db_table': 'partner',
            },
        ),
        migrations.CreateModel(
            name='Respond',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respondmessage', models.TextField(default='')),
            ],
            options={
                'db_table': 'response',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servicetitle', models.CharField(blank=True, default='', max_length=50)),
                ('servicedescription', models.TextField(blank=True, default='')),
                ('service_main_img', models.ImageField(blank=True, upload_to='images/')),
                ('servicetitle2', models.CharField(blank=True, default='', max_length=50)),
                ('servicedescription2', models.TextField(blank=True, default='')),
                ('service_main_img2', models.ImageField(blank=True, upload_to='images/')),
                ('servicetitle3', models.CharField(blank=True, default='', max_length=50)),
                ('servicedescription3', models.TextField(blank=True, default='')),
                ('service_main_img3', models.ImageField(blank=True, upload_to='images/')),
            ],
            options={
                'db_table': 'service',
            },
        ),
    ]
