.. _tututorial-para-instalar-la-última-versión-de-nes:

Tutorial para instalar la última versión de NES
=============================================
En esta guía, demostraremos cómo instalar y configurar NES en un entorno virtual de Python. Luego configuraremos PostgreSQL y Apache.

.. _información-técnica-importante:

Información técnica importante
-------------------------------
* Esta guía describe una instalación mediante el uso de paquetes disponibles a través de Debian 9 (nombre en clave: Stretch), pero se puede adaptar fácilmente a otros sistemas operativos Unix.
* Se recomienda usar virtualenv para instalar NES. Esto se debe a que cuando usa virtualenv, crea un entorno aislado con sus propios directorios de instalación.
* La última versión de NES solo funciona con Python 3.
* Para propósitos de demostración, usaremos el directorio `/usr/local` para implementar NES. Este directorio parece ser el lugar correcto según la `Fundación Linux <https://refspecs.linuxfoundation.org/FHS_3.0/fhs/ch04s09.html>`_.

.. _configuración-inicial-nes:

Configuración inicial
-------------
1. Antes de seguir los pasos de este tutorial, asegúrese de que todos sus repositorios estén actualizados::

    apt-get update

2. Instale algunos paquetes::

    apt-get install python3-pip git virtualenv graphviz libpq-dev python3-dev

    apt-get install python3-psycopg2

3. Cree el virtualenv (verifique la versión correcta de Python que está usando)::

    cd /usr/local

    virtualenv nes-system -p /usr/bin/python3.7

   Para ver la versión de python que posee escriba lo siguiente::

    python3 --version

   Si no tiene los permisos para crear el virtualenv en el directorio /usr/local puede realizar lo siguiente::

    sudo virtualenv nes-system -p /usr/bin/python3.7
    sudo chown -R tu_usuario:tu_usuario nes-system

4. Ejecute lo siguiente para activar este nuevo entorno virtual::

    source nes-system/bin/activate

5. Los siguientes pasos se ejecutarán dentro de virtualenv::

    cd nes-system

6. Clona la NES. Consulte la última versión de TAG `aquí <https://github.com/neuromat/nes/releases>`_ (si desea realizar la clonación dentro de un IDE recuerde hacerlo dentro del directorio nes-system)::

    git clone -b TAG-X.X https://github.com/neuromat/nes.git

   Ejemplo de como clonar la versión de TAG 1.72.4::

    git clone -b TAG-1.72.4 https://github.com/neuromat/nes.git

7. Diríjase al archivo qdc y modifique el archivo requirements.txt::

    cd nes/patientregistrationsystem/qdc/

    nano requirements.txt

   Edite las líneas 9 y 10, es decir las que dicen psycopg2==2.7.5 y psycopg2-binary>=2.7.7, cambiando de esto::

    psycopg2==2.7.5
    psycopg2-binary>=2.7.7

   A esto::

    psycopg2
    psycopg2-binary

   Modifique la línea python-dateutil==2.5.2 por python-dateutil>=2.5.2, una vez editado debería quedar como sigue::

    python-dateutil>=2.5.2

   Por último agregue la siguiente línea al final del archivo::

    pyparsing<3,>=2.4.2
    gitdb2==2.0.6

   Una vez terminados todos estos cambios, el archivo debería quedar de la siguiente forma::

    pip>=18.1
    setuptools>=40.6.3

    Django==1.11.23
    django-jenkins==0.19.0
    django-modeltranslation==0.12.2
    django-simple-history==1.9.0
    jsonrpc-requests==0.2
    psycopg2
    psycopg2-binary
    pyflakes==0.9.2
    pylint==1.5.4
    pep8==1.7.0
    python-dateutil>=2.5.2
    django-maintenance-mode>=0.15.0
    # Changes for installation with python 3.7.3
    # Obs.: error -> ERROR: botocore 1.14.7 has requirement docutils<0.16,>=0.10, but you'll have docutils 0.16 which is incompatible.
    # But installed
    # Refers to installation of goodtables==2.2.1 below
    numpy>=1.11.0
    scipy>=0.17.1
    h5py>=2.6.0
    matplotlib>=1.5.3

    pydot==1.2.3
    django-solo==1.1.2
    coreapi==2.3.1
    GitPython==2.1.8
    reportlab==3.4.0
    xhtml2pdf==0.2.2
    networkx==2.2

    -e "git+https://github.com/davedash/django-fixture-magic.git#egg=django-fixture-magic"

    mne==0.17.2
    -e "git+https://github.com/AllenInstitute/nwb-api.git#egg=nwb&subdirectory=ainwb"

    # For testing
    goodtables==2.2.1
    Faker==0.8.17
    pyparsing<3,>=2.4.2
    gitdb2==2.0.6

8. Instale los paquetes de Python adicionales::

    cd nes/patientregistrationsystem/qdc/

    pip3 install -r requirements.txt

.. _implementación-de-NES-con-apache-postgresql-y-mod-wsgi:

Implementación de NES con Apache, PostgreSQL y mod_wsgi
--------------------------------------------------
1. Instale los paquetes::

    apt-get install apache2 libapache2-mod-wsgi-py3 postgresql

2. Cree un usuario y una base de datos (utilizará este usuario/contraseña/base de datos en el siguiente paso)::

    su - postgres

    createuser nes --pwprompt --encrypted

    createdb nes --owner=nes

    exit

3. Utilice esta `plantilla <https://github.com/neuromat/nes/blob/master/patientregistrationsystem/qdc/qdc/settings_local_template.py>`_ para crear un archivo llamado settings_local.py y configure la base de datos::

    cd /usr/local/nes-system/nes/patientregistrationsystem/qdc

    nano qdc/settings_local.py

Edite la base de datos para utilizar el usuario / contraseña / base de datos creada en el paso anterior::

    # Database
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'nes',
            'USER': 'nes',
            'PASSWORD': 'tu_contraseña',
            'HOST': 'localhost',
        }
    }

4. Edite la línea ``SECRET_KEY`` modificando lo que se encuentra entre comillas por una clave secreta generada, si no sabes como generarla puedes hacerlo `aquí <https://djecrety.ir/>`_ ::

    SECRET_KEY = ‘tu_clave_secreta_generada’

5. Cree las tablas::

    python3 manage.py migrate

6. Cree el superusuario::

    python3 manage.py createsuperuser

7. Copie el archivo wsgi_default.py en el archivo wsgi.py y edite wsgi.py::

    cd qdc

    cp wsgi_default.py wsgi.py

    nano wsgi.py

El archivo debe contener::

    # -*- coding: utf-8 -*-

    """
    WSGI config for qdc project.
    It exposes the WSGI callable as a module-level variable named ``application``.
    For more information on this file, see
    https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
    """
    import os
    import sys
    import site

    # Add the site-packages of the chosen virtualenv to work with
    site.addsitedir('/usr/local/nes-system/lib/python3.5/site-packages')

    # Add the paths according to your installation
    paths = ['/usr/local', '/usr/local/nes-system', '/usr/local/nes-system/nes', '/usr/local/nes-system/nes/patientregistrationsystem', '/usr/local/nes-system/nes/patientregistrationsystem/qdc',]

    for path in paths:
        if path not in sys.path:
            sys.path.append(path)

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "qdc.settings")

    # Activate virtual env
    activate_env=os.path.expanduser("/usr/local/nes-system/bin/activate_this.py")

    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()

8. Cree un host virtual::

    nano /etc/apache2/sites-available/nes.conf

Luego, inserte el siguiente contenido recordando que las rutas y el nombre del servidor proporcionado deben cambiarse de acuerdo con su instalación::

    <VirtualHost *:80>
    	ServerName nes.example.com
    	WSGIProcessGroup nes
    
    	DocumentRoot /usr/local/nes-system/nes/patientregistrationsystem/qdc
    
    	<Directory />
    		Options FollowSymLinks
    		AllowOverride None
    	</Directory>
    
    	Alias /media/ /usr/local/nes-system/nes/patientregistrationsystem/qdc/media/ 
    
    	<Directory "/usr/local/nes-system/nes/patientregistrationsystem/qdc">
    		Require all granted
    	</Directory>
    
    	WSGIScriptAlias / /usr/local/nes-system/nes/patientregistrationsystem/qdc/qdc/wsgi.py application-group=%{GLOBAL}
    	WSGIDaemonProcess nes lang='en_US.UTF-8' locale='en_US.UTF-8'

    	Alias /img/ /usr/local/nes-system/nes/patientregistrationsystem/qdc/img/ 
    
    	ErrorLog ${APACHE_LOG_DIR}/nes_ssl_error.log
    	LogLevel warn
    	CustomLog ${APACHE_LOG_DIR}/nes_ssl_access.log combined
    </VirtualHost>

.. Nota::
            Tenga en cuenta el atributo "grupo de aplicaciones=%{GLOBAL}", que normalmente no es necesario. Es importante configurarlo debido a la librería mne, como se explica `aquí <https://serverfault.com/questions/514242/non-responsive-apache-mod-wsgi-after-installing-scipy/697251#697251?newreg=0819baeba10e4e92a0f459d4042ea98d>`_.

           Tenga en cuenta las líneas con las directivas WSGIProcessGroup y WSGIDaemonProcess. Son importantes para configurar la configuración regional utilizada por las librerías externas, como pydot. Sin estas directivas, los caracteres especiales utilizados por, por ejemplo, pydot, no se pueden aceptar y se podría lanzar una excepción. Los consejos se obtuvieron de `aquí <http://blog.dscpl.com.au/2014/09/setting-lang-and-lcall-when-using.html>`_ y `aquí <http://modwsgi.readthedocs.io/en/develop/configuration-directives/WSGIDaemonProcess.html>`_ se explican las configuraciones de wsgi_mod. Para configurar correctamente la directiva WSGIDaemonProcess, verifique la codificación ejecutando el comando “echo $LANG” en la terminal. A veces, el servidor utiliza por ejemplo "pt_BR.UTF-8".

9. Cargue los datos iniciales (mire el `script-for-creating-initial-data <https://nes.readthedocs.io/en/latest/installation/scriptinitialdata.html#script-for-creating-initial-data>`_ para ver más detalles)::

    cd /usr/local/nes-system/nes/patientregistrationsystem/qdc

    chmod +x add_initial_data.py

    python3 manage.py shell < add_initial_data.py

    python3 manage.py loaddata load_initial_data.json

10. Gestión de archivos estáticos::

    mkdir static

    nano qdc/settings_local.py

11. Edite la línea ``STATIC_ROOT line``::

     STATIC_ROOT = '/usr/local/nes-system/nes/patientregistrationsystem/qdc/static'

12. 12. Recopile los archivos estáticos en ``STATIC_ROOT``::

     python3 manage.py collecstatic

13. Cree el directorio media::

     mkdir media


14. Habilite el host virtual::

     a2ensite nes

     systemctl reload apache2
